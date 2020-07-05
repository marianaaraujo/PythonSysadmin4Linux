from ldap3 import Server, Connection, MODIFY_REPLACE
from hashlib import md5
from binascii import b2a_base64

username = "admin"
password = "4linux"

server = Server("ldap://192.168.0.200:389")
ldap_con = Connection(
	server,
	"cn=%s,dc=dexter,dc=com,dc=br"%(username),
	password
)
#print(ldap_con.bind())
ldap_con.bind()

#md5json = md5("senhapadrao".encode("utf-8")).digest()
#user = {
#	"cn": "mariana",
#	"sn": "aruaujo",
#	"mail": "mariana.araujo.88@gmail.com",
#	"uidNumber": "123",
#	"gitNumber": "123",
#	"uid": "mariana.araujo.88@gmail.com",
#	"homeDirectory": "/home/mariana",
#	"UserPassword": "{MD5}" + b2a_base64(md5json).decode("utf-8")
#}
#objectClass = ["top","person","inetOrgPerson","posixaccount","organizationPerson"]
#dn = "uid=%s,dc=dexter,dc=com,dc=br"%(user["mail"])
#user_added = ldap_con.add(dn, objectClass, user)
#print(user_added)

#email = "mariana.araujo.88@gmail.com"
#dn = "uid=%s,dc=dexter,dc=com,dc=br"%(email)
#ldap_con.search(
#	dn,"(objectclass=person)",attributes=["sn", "userPassword"]
#)
#print(ldap_con.entries)

#email = "mariana.araujo.88@gmail.com"
#dn = "uid=%s,dc=dexter,dc=com,dc=br"%(email)
#changes = {
#	"cn": [(MODIFY_REPLACE, ["maria"])],
#	"sn": [(MODIFY_REPLACE, ["araújo"])]
#}
#ldap_con.modify(
#	dn,changes
#)
#print(ldap_con.result)

email = "mariana.araujo.88@gmail.com"
dn = "uid=%s,dc=dexter,dc=com,dc=br"%(email)
print(ldap_con.delete(dn))
