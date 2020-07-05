import flask
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017")
database = client.database

app = flask.Flask(__name__)

@app.route("/users", methods=["GET"])
def get_users():
	#return flask.jsonify([ 'user_{}'.format(i) for i in range(10) ])
	return 'get all users'

@app.route("/users", methods=["POST"])
def post_users():

	payload = flask.request.json or flask.request.form

	email = payload.get('email')
	password = payload.get('password')

	query = {
		"email": email
	}

	user_exists = database.users.find_one(query)
	
	if not user_exists:
		
		user = {
			"email": email,
			"password": password
		}

		result = database.users.insert_one(user)

		user['_id'] = str(result.inserted_id)

		del user['password']

		return flask.jsonify(user)

	else:
		#status_code = 400	
		error = {
			"message":"user already exists"
		}
		return flask.jsonify(error)#, status_code

@app.route("/users/<uid>", methods=["GET"])
def get_user_by_id(uid):
	return 'get user by id {}'.format(uid)

@app.route("/users/<uid>", methods=["PUT"])
def put_users(uid):
	return 'put user by id {}'.format(uid)

@app.route("/users/<uid>", methods=["PATCH"])
def patcj_users(uid):
	return 'patch user by id {}'.format(uid)

@app.route("/users/<uid>", methods=["DELETE"])
def delete_users(uid):
	return 'delete user by id {}'.format(uid)

if __name__ == '__main__':
	app.run(debug=True)