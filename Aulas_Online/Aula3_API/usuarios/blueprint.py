from flask import Blueprint, Response, request
from config import mongo_db
from bson.json_util import dumps

usuarios_routes = Blueprint("usuarios",__name__,url_prefix="/usuarios")

@usuarios_routes.route("")
def getUsuarios():
	try: 
		users = mongo_db.user.find()
		return Response(dumps(users), status=200, content_type="application/json")
	except Exception as e:
		return "Erro: " +str(e)

@usuarios_routes.route("",methods=["POST"])
def postUsuarios():
	try: 
		user = request.get_json()
		mongo_db.user.insert_one(
			{"name": user["name"],
			 "email": user["email"],
			 "messages":[]
			}
		)
		response = {
			"message":"Usuario "+str(user["name"])+" criado com sucesso"
		}
		return Response(dumps(response), status=201, content_type="application/json")
	except Exception as e:
		return "Erro: " +str(e)

@usuarios_routes.route("",methods=["PATCH"])
def patchUsuarios():
	try: 
		user = request.get_json()
		updated = mongo_db.user.update_one(
				{"email":user["email"]},
				{"$set": user}
			)
		if updated.modified_count:
			response = {"message":"Usuario "+str(user["name"])+" atualizado com sucesso!"}
			return Response(dumps(response), status=200, content_type="application/json")
		elif updated.matched_count:
			response = {"message":"Usuario "+str(user["name"])+" encontrado mas não foi modificado!"}
			return Response(dumps(response), status=400, content_type="application/json")
		else:
			response = {"message":"Usuario "+str(user["name"])+" não foi encontrado"}
			return Response(dumps(response), status=404, content_type="application/json")
	except Exception as e:
		return "Erro: " +str(e)

@usuarios_routes.route("",methods=["DELETE"])
def deleteUsuarios():
	try: 
		user = request.get_json()
		deleted = mongo_db.user.delete_one(
				{"email":user["email"]}
			)
		if deleted.deleted_count:
			response = {"message":"Usuario "+str(user["email"])+" removido com sucesso!"}
			return Response(dumps(response), status=200, content_type="application/json")
		else:
			response = {"message":"Usuario "+str(user["email"])+" não foi encontrado"}
			return Response(dumps(response), status=404, content_type="application/json")
	except Exception as e:
		return "Erro: " +str(e)