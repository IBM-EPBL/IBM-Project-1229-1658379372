import flask 
from flask import request, jsonify
app = flask.Flask(__name__) 

book_info = [
    {
        "bookid":1,
       "title":"Fehlervorhersage in Java-Code mittels Machine Learning",
       "bookimage":"https://cdn.asaha.com/assets/thumbs/d8c/d8c2039a12516bd126d6424d2adea61c-s.jpg",
       "bookurl":"http://dreamboxx.com/mark/data/PABAs/BA16_Bug_Detection_Meier_Mekesser.pdf",
       "pagepath":"/fehlervorhersage-in-java-code-mittels-machine-learning-e51290142.html",
       "Number of Pages":"117 Pages",
       "Author":"Ollie Schaich"
},
    {
        "bookid":2,
       "title":"Machine Learning - New Edition",
       "bookimage":"https://cdn.asaha.com/assets/thumbs/d8c/d8c2039a12516bd126d6424d2adea61c-s.jpg",
       "bookurl":"http://dreamboxx.com/mark/data/PABAs/BA16_Bug_Detection_Meier_Mekesser.pdf",
       "pagepath":"/fehlervorhersage-in-java-code-mittels-machine-learning-e51290142.html",
       "Number of Pages":"254 Pages",
       "Author":"Jhon"
}, ]

@app.route('/book', methods=['GET'])
def get_users():
    return jsonify(book_info)

@app.route("/book/<bookid>", methods=['GET'])
def get_user_by_bookid_in_path(bookid): 
    for user in book_info: 
        if user['bookid'] == int(bookid):
            return jsonify (user) 
    return {}

@app.route('/add_book', methods=['POST'])
def post_users():
    user = request.get_json() 
    user['bookid'] = len(book_info) + 1 
    book_info.append(user) 
    return jsonify(user)

@app.route('/update_book', methods=['PUT']) 
def put_users():
    user = request.get_json() 
    for i, u in enumerate(book_info): 
        if u['bookid'] == user['bookid']:
            book_info[i] = user 
    return {}

@app.route('/delete/', methods=['DELETE'])
def delete_users(bookid): 
    for user in book_info:
        if user['bookid'] == int(bookid):
            book_info.remove(user) 
    return {}

if __name__=="__main__":
    app.run()