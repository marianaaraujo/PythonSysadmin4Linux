from pymongo import MongoClient

mongo_con = MongoClient()
db = mongo_con["flask_app"]


user = db.user.find_one(
	{
		"name":"usuario_name",
		"email": "usuario_email"
	}
)

print(user)
print(user["_id"].generation_time)
