# 北邮校园网登陆
服务器安装在机房，没有进行虚拟化，没有安装 VMware vSphere，因此只能通过 shell 登陆校园网。

### 支持登陆和注销
```
Usage: campus_network.py [options]

Options:
  -h, --help            show this help message and exit
  -u USERNAME, --username=USERNAME
                        Your username.
  -p PASSWD, --password=PASSWD
                        Your passwd.
  -i, --login           The flag indicating: login.
  -o, --logout          The flag indicating: logout.
``` 
### 注意事项
1. 源代码在 Python 2.7 环境下编写，使用 2to3 完成 Python 2 to 3 code translation，
   ```
   2to3 -w campus_network.py
   ```
   生成的备份文件 `campus_network.py.bak` 为 Python 2.7 下仍可运行的版本。2to3 生成的 modified `campus_network.py` 需要在 line 35 下加入一行 `data = data.encode("utf8")` 将 str 编码为字节流。否则会报错
   > TypeError: POST data should be bytes, an iterable of bytes, or a file object. It cannot be of type str.