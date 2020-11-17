import re
pat = re.compile(r'[1-9]\d{5}')

#sub = re.sub(r'[1-9]\d{5}',':zipcode','BIT100081 tsu100084')
#print(sub)
# ===============================================================
# sub = pat.sub(':zipcode','BIT100081 tsu100084')
# print(sub)

#finditer
#for m in re.finditer(r'[1-9]\d{5}','Bit100081 TSU100084'):
#    if m:
#        print(m.group(0))
# ===============================================================
# for m in pat.finditer('Bit100081 TSU100084'):
#     if m:
#         print(m.group(0))



#split使用
#s = re.split(r'[1-9]\d{5}','Bit100081 TSU100084')
#s = re.split(r'[1-9]\d{5}','Bit100081 TSU100084',maxsplit=1)
#print(s)
# =====================================================================
# s = pat.split('Bit100081 TSU100084',maxsplit=1)
# s = pat.split(r'Bit100081 TSU100084')
# print(s)


#findall使用
#ls = re.findall(r'[1-9]\d{5}','Bit100081 TSU100084')
#print(ls)
# =========================================================
# ls = pat.findall("Bit100081 TSU100084")
# print(ls)


#search 使用 返回match对象
#match= re.search(r'[1-9]\d{5}\|4','Bit 100080|41')
#match= re.search(r'[1-9]\d{5}','Bit 100081')
#if match:
#    print(match.group(0))
# ======================================================
# match = pat.search('Bit 100080|41')
# if match:
#     print(match.group(0))

# match= re.search(r'[1-9]\d{5}','Bit 100081')
# if match:
   # print(match.group(0))
   # print(match.start())
   # print(match.string)
match= re.search(r'a[a-z]*n','Bit adfadnadfn')  #贪婪匹配
match= re.search(r'a[a-z]*?n','Bit adfadnadfn')#非贪婪匹配
if match:
   print(match.group(0))