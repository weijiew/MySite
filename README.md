# 起源

在创建文章的时候我发现比较麻烦，首先创建一个文件夹，这个文件夹名字对应了 url 。然后再创建一个 md 文件。

除此之外每一个 md 文件的头部还需要写关于文章的基本信息。类似于如下这种信息，每次都要写一遍非常繁琐，而且 gatsby 没有类似于 hexo new 文章的命令。于是我尝试用 python 写了一个脚本。 

```
---
title: 快速创建文章
date: "2020-06-01"
draft: false
tags:
- summary
---
```


# 内容

首先根据我的文件结构，需要首先设置目录名，如果你的方式不一样的话需要灵活改变，仅供参考。

```python
# 设置目录名
def getFolderName():
    today = datetime.date.today()
    path = input("请输入路径名：")
    filename = str(today) + "---" + path
    return filename
```

然后根据路径名创建文件夹

```python
# 创建目录并设置目录名
def createFloder(filename):
    # 创建文件夹
    p = Path(filename)
    # 如果文件夹已经存在就抛出异常
    try:
        p.mkdir()
    except Exception as e:
        print(e)
```

创建文件夹再创建 md 文件，这个我采取了默认的名称。也就是 index.md 然后在将头部的内容写入文件中即可。

```python
# 设置输入内容
def getContent():
    date = datetime.date.today()
    content = "---\ntitle: " + "\n" + "date: "  +"\"" + str(date) + "\"" + "\n" + "draft: false\n" + "tags:\n" + "- " + "\n" + "---\n"
    return content
```

执行并写入：

```python
if __name__ == '__main__':
    folderName = getFolderName()
    createFloder(folderName)
    con = getContent()
    with open(folderName+"\\index.md", 'w') as f:
        f.write(str(con))
    print(con)
```

# 总结
我针对自己的路径进行了适当的修改。应该是可以写成插件的。

我的python 环境是 3.6 ，并且为了方便使用，我用 `pyinstaller -F CreateMd.py` 将代码打包了 exe 可执行文件。exe 文件执行起来有点慢，不如 py 文件迅速，有点疑惑。
