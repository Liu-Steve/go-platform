import os
import socket

os.chdir(os.path.dirname(__file__))
print("Working dir:", os.getcwd())

# 获取局域网IP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("223.5.5.5", 80))
ip = s.getsockname()[0]
s.close()
print(f"当前局域网IPv4地址: {ip}")

os.system("docker stop katago")
os.system("docker rm katago")
os.system("docker rmi $(docker images | grep 'none' | awk '{print $3}')")
os.system(f"docker run -p 8083:8083 --env JASYPT_PASSWORD=$JASYPT_PASSWORD \
--env MYSQL_IP={ip} --name katago --restart=always -d liusteve/go-platform-katago:latest")

print('Done.')
