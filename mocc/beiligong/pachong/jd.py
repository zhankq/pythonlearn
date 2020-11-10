import requests
url="https://item.jd.com/2967929.html"
r=requests.get(url)
print(r.status_code)

print(r.text)
