import jenkins

jenkins_con = jenkins.Jenkins(
	"http://192.168.0.200:8080",
	username = "4linux", password = "4linux123"
)

#print(jenkins_con.get_whoami())
#print(jenkins_con.get_version())

#jenkins_con.create_job("Python-Job, jenkins.EMPTY_CONFIG_XML")
#queue = jenkins_con.build_job("Python-Job")
#print(jenkins_con.get_queue_item(queue))

#print(jenkins_con.get_jobs())

#print(jenkins_con.get_job_config())

#print(jenkins_con.get_job_config("Python-Job"))

jenkins_con.recongfig_job("Python-Job", jenkins.EMPTY_CONFIG_XML)