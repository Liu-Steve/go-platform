import os

os.chdir(os.path.dirname(__file__))
print("Working dir:", os.getcwd())

static_dir = "../server/go-server/src/main/resources/static"
os.system(f"rm -r {static_dir}/css")
os.system(f"rm -r {static_dir}/js")
os.system(f"rm -r {static_dir}/img")
os.system(f"cp ../ui/index.html {static_dir}/index.html")
os.system(f"cp -r ../ui/css {static_dir}/css")
os.system(f"cp -r ../ui/js {static_dir}/js")
os.system(f"cp -r ../ui/img {static_dir}/img")
