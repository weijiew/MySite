import datetime
import os
from pathlib import Path

# 设置目录名
def getFolderName():
    today = datetime.date.today()
    path = input("请输入路径名：")
    filename = str(today) + "---" + path
    return filename


    
# 设置输入内容
def getContent():
    date = datetime.date.today()
    content = "---\ntitle: " + "\n" + "date: "  +"\"" + str(date) + "\"" + "\n" + "draft: false\n" + "tags:\n" + "- " + "\n" + "---\n"
    return content

# 创建目录并设置目录名
def createFloder(filename):
    # 创建文件夹
    p = Path(filename)
    # 如果文件夹已经存在就抛出异常
    try:
        p.mkdir()
    except Exception as e:
        print(e)
if __name__ == '__main__':
    folderName = getFolderName()
    createFloder(folderName)
    con = getContent()
    with open(folderName+"\\index.md", 'w') as f:
        f.write(str(con))
    print(con)
