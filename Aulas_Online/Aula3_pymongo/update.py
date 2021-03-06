from pymongo import MongoClient

mongo_con = MongoClient()
db = mongo_con["flask_app"]


user = db.user.update_one(
	{
		"name":"usuario_name",
		"email": "usuario_email"
	},
	{
		"$set":{
			"email":"usuario@email.com.br"
		}
	}
)

print(user.matched_count, user.modified_count)