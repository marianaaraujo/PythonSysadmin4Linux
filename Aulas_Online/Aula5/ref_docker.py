import docker

docker_con = docker.DockerClient('192.168.0.200:2376')

print(docker_con)

container = docker_con.containers.run('debian:latest','/bin/bash',name='learn',detach=True,tty=True)

learn_container = docker_con.containers.get('learn')

print(learn_container.exec_run("ls -la"))