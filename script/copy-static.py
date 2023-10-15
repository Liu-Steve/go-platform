import os

ui_path = os.path.dirname(os.path.dirname(__file__))
os.chdir(os.path.join(ui_path, 'ui'))
print("Working dir:", os.getcwd())

# 打包
print("打包中......")
os.system("cnpm i")
os.system("npm run build")

# 拷贝
print("拷贝中......")
static_dir = "../server/go-server/src/main/resources/static"
os.system(f"rm -r {static_dir}/*")
os.system(f"cp -r ../ui/dist/* {static_dir}")

print('Done.')
