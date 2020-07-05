from pymongo import MongoClient

mongo_con = MongoClient()
db = mongo_con["flask_app"]


deleted = db.user.delete_one(
	{
		"name":"usuario_name"
	}
)

print(deleted.deleted_count)