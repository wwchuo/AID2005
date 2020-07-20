"""
http 请求响应演示
"""

from  socket import *

# 创建tcp套接字
s = socket()
s.bind(("0.0.0.0",8888))
s.listen(5)

c,addr = s.accept()
print("Connect from",addr) # 浏览器连接
data = c.recv(4096) # 接收的是http请求
print(data.decode())

# 响应格式
# html = """HTTP/1.1 200 OK
# Content-Type:text/html
#
# hello worldhttp://127.0.0.1:8888/
# """

html = """HTTP/1.1 404 Not Found
Content-Type:text/html

Sorry...
"""

c.send(html.encode()) # 发送响应给客户端

c.close()
s.close()