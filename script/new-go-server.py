import os

os.chdir(os.path.dirname(__file__))
print("Working dir:", os.getcwd())

os.system("docker stop go-server")
os.system("docker rm go-server")
os.system("docker rmi $(docker images | grep 'none' | awk '{print $3}')")
os.system("docker run -p 8080:8084 --env JASYPT_PASSWORD=$JASYPT_PASSWORD \
--env MYSQL_IP=10.132.1.46 --name go-server -d liusteve/go-platform-server:latest")
