s = "talk is cheap".title()

print(s)
'''
sq = ["1","2"]
sp='+'
print(sp.join(sq))


title="money python"

re = title.find('fy')

print(re)


print('s5'.center(5,'*'))


width = int(input('please enter width: ')) #35

price_width=10
item_width=width-price_width #25

header_fmt = '{{:{}}},{{:>{}}}'.format(item_width,price_width) #{:25},{:>10}

fmt='{{:{}}},{{:>{}.2f}}'.format(item_width,price_width) #{:25},{:>10.2f}
#print(fmt)

print('='*width)

print(header_fmt.format('Item',"Price"))





from math import pi
print("{pi!s} , {pi!r}, {pi!a},{pi}".format(pi=pi))



fullname = ["Alfred","smoketoomuch"]
s = "Mr {name[0]}".format(name=fullname)

print(s)





f = "{foo} {} {bar} {}".format(1,2,bar=4,foo=3)

print(f)



from math import e
print(f"contansts {e}.")

print("contansts {e}.".format(e='111'))



print("{name} is app {value:.2f}".format(name="PI",value=pi))

format = "hello,%s.%s enough for you "
values = ("world","hot")

print(format % values)

print("hello,%s.%s enough for you " % ("world","hot"))


from string import Template

tmpl = Template("Hello ,$who! $what enough for ya ?")
tmpl.substitute(who="Mars",what="Dusty")

"{},{} and {}".format("first","second","third")
"{0},{1} and {2}".format("first","second","third")
print("{1},{2} and {0}".format("first","second","third"))
'''






