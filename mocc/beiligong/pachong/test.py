import requests
#yf_access_token:{$aduser_id}:{$appid}
# authorizer_access_token = '38_T6qET7TcryuTXPAnwSu4vqvFQTJVpIh1P432J4C4npvBaViOflcy1wIrVw00X6aqbgummbv3-S8WvMI90mtjDIQoAdupW6yUZXNAVvQyBpJgGXscwvFLD8p8j9lIwI8FlltsiAotmAZetSF9ADFeAKDKNP'
# openid = "oY8Fbs63lL9jgv8IlRY6D1FtBKhY"
# url = "https://api.weixin.qq.com/cgi-bin/user/info?access_token="+authorizer_access_token+"&openid="+openid

#https://api.weixin.qq.com/cgi-bin/user/info?access_token=38_T6qET7TcryuTXPAnwSu4vqvFQTJVpIh1P432J4C4npvBaViOflcy1wIrVw00X6aqbgummbv3-S8WvMI90mtjDIQoAdupW6yUZXNAVvQyBpJgGXscwvFLD8p8j9lIwI8FlltsiAotmAZetSF9ADFeAKDKNP&openid=oY8Fbs63lL9jgv8IlRY6D1FtBKhY

#print(url)

#r = requests.get(url)
#print(r.text)

# r=requests.request('get',url)
# print(r.text)
#
# sr = {"access_token":authorizer_access_token,"openid":openid}
# f = requests.get("https://api.weixin.qq.com/cgi-bin/user/info",params=sr)
# print(f.status_code)
#r = requests.post("http://httpbin.org/post",data="ABC")

#r = requests.post("http://httpbin.org/post",data={"a":"aaa","b":"BBB"})
#print(r.text)

# r2 = requests.post("http://httpbin.org/post",params={"a":"aaa","b":"BBB"})

# for i in r2:
#     print(i)
# print(r2.origin)
pxs = {"https":"https://www.baidu.com"}


r = requests.get('http://adm.goluodi.com/welcome',proxies=pxs)
print(r.text)
