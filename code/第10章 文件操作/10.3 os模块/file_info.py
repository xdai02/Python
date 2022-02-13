import os

PATH = "第10章 文件操作" + os.sep + "10.3 os模块" + os.sep + "data.txt"

def main():
    # 路径存在
    if os.path.exists(PATH):
        print("绝对路径：%s" % os.path.abspath(PATH))
        print("文件名称：%s" % os.path.basename(PATH))
        print("文件大小：%s" % os.path.getsize(PATH))
        print("当前路径是否为文件：%s" % os.path.isfile(PATH))
        print("当前路径是否为目录：%s" % os.path.isdir(PATH))

if __name__ == "__main__":
    main()