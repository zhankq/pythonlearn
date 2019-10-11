#try:
#    print("A simple task")
#except:
#    print('What? Something went wrong?')
#else:
#    print('Ah ... It went as planned.')
'''
while True:
    try:
        x=int(input('Enter the first number:'))
        y=int(input('Enter the second number:'))
        value = x/y
        print('x/y is ',value)
    except:
        print('Invalid input. Please try again.')
    else:
        break
'''
'''
x=None
try:
    x=1/0
finally:
    print('Cleaning up...')
    del x
'''
warn("aaaaaaaa")
