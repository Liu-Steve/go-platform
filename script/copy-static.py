import os

os.chdir(os.path.dirname(__file__))
print("Working dir:", os.getcwd())

static_dir = "../server/go-server/src/main/resources/static"
os.system(f"rm -r {static_dir}/*")
os.system(f"cp -r ../ui/dist/* {static_dir}")
