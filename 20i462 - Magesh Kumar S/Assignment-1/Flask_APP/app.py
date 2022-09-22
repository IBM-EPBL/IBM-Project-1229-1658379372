import flask 
from flask import request, jsonify
app = flask.Flask(__name__) 
app.config["DEBUG"] = True

# Users dictionary 
users_dict = [{ 'id': 1, 'name': 'MageshKumar', 'age': 21 }, 
{ 'id': 2, 'name': 'Pragalathan', 'age': 21 },
{'id': 3, 'name': 'Sai Vignesh', 'age': 21}]

@app.route('/user', methods=['GET'])
def get_users():
    return jsonify(users_dict)
def get_user_by_id():
    # get parameter 'id' from request 
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error,No id field provided"
    for user in users_dict: 
        if user['id'] == id:
            return jsonify(user) 
    return {}

@app.route("/user/<id>", methods=['GET'])
def get_user_by_id_in_path(id): 
    for user in users_dict: 
        if user['id'] == int(id):
            return jsonify (user) 
    return {}

@app.route('/add_user', methods=['POST'])
def post_users():
    user = request.get_json() 
    user['id'] = len(users_dict) + 1 
    users_dict.append(user) 
    return jsonify(user)

@app.route('/update_user', methods=['PUT']) 
def put_users():
    user = request.get_json() 
    for i, u in enumerate(users_dict): 
        if u['id'] == user['id']:
            users_dict[i] = user 
    return {}


@app.route('/delete/', methods=['DELETE'])
def delete_users(id): 
    for user in users_dict:
        if user['id'] == int(id):
            users_dict.remove(user) 
    return {}

if __name__=="__main__":
    app.run()