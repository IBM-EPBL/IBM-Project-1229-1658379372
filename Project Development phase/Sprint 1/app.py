

from flask import Flask, render_template, request, redirect, session 

import ibm_db
import re



app = Flask(__name__)



  


app.secret_key = 'a'

conn=ibm_db.connect("DATABASE=bludb;HOSTNAME='';PORT='';SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID='';PWD='';",'','')




#HOME--PAGE
@app.route("/home")
def home():
    return render_template("homepage.html")

@app.route("/")
def add():
    return render_template("home.html")



#SIGN--UP--OR--REGISTER


@app.route("/signup")
def signup():
    return render_template("signup.html")



@app.route('/register', methods =['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST' :
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        

        

        sql = "SELECT * FROM REGISTER WHERE USERNAME =?"
        stmt = ibm_db.prepare(conn, sql)
        ibm_db.bind_param(stmt,1,username)
        ibm_db.execute(stmt)
        account = ibm_db.fetch_assoc(stmt)
        print(account)

        if account:
            msg = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address !'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'name must contain only characters and numbers !'
        else:
            sql1="INSERT INTO REGISTER(USERNAME,PASSWORD,EMAIL) VALUES(?,?,?)"
            stmt1 = ibm_db.prepare(conn, sql1)
            
            ibm_db.bind_param(stmt1,1,username)
            ibm_db.bind_param(stmt1,2,password)
            ibm_db.bind_param(stmt1,3,email)
            ibm_db.execute(stmt1)
            msg = 'You have successfully registered !'
            return render_template('signup.html', msg = msg)

           
        
        
 
        
 #LOGIN--PAGE
    
@app.route("/signin")
def signin():
    return render_template("login.html")
        
@app.route('/login',methods =['GET', 'POST'])
def login():
    global userid
    msg = ''
   
  
    if request.method == 'POST' :
        

        username = request.form['username']
        password = request.form['password']
        sql = "SELECT * FROM REGISTER WHERE USERNAME =? AND PASSWORD =?"
        stmt = ibm_db.prepare(conn, sql)
        ibm_db.bind_param(stmt,1,username)
        ibm_db.bind_param(stmt,2,password)
        ibm_db.execute(stmt)
        account = ibm_db.fetch_assoc(stmt)
        print(account)
        
        if account:
            session['loggedin'] = True
            session['id'] = account["ID"]
            userid=  account["ID"]
            session['username'] = account["USERNAME"]
            session['email']=account["EMAIL"]
           
            return redirect('/home')
        else:
            msg = 'Incorrect username / password !'
    return render_template('login.html', msg = msg)




@app.route('/logout')

def logout():
   session.pop('loggedin', None)
   session.pop('id', None)
   session.pop('username', None)
   session.pop('email',None)
   return render_template('home.html')

             

if __name__ == "__main__":
    app.run(debug=True)
