from handler import HTMLRenderer
import re
handler = HTMLRenderer()
s = handler.sub('emphasis')
print(s)
f = re.sub(r'\*(.+?)\*',s,"This *is& a test")
print(f)
