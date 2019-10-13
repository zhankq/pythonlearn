def divide(x, y):
        try:
            result = x / y
        except ZeroDivisionError:
            print("division by zero!")
        else:
            print("result is", result)
        finally:
            print("executing finally clause")

divide(12,0)
'''
import sys
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except IOError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()
'''
'''
import sys
try:
    f = open('myfiler.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise


=======================================================================

while True:
        try:
            x = int(input("Please enter a number: "))
            print("aaaaaaaaaa")
            break
#        except ZeroDivisionError:
        except (ZeroDivisionError,ValueError):#用这种方式统一处理，但这样就没法定制化了
            print("Oops!  That was no valid number.  Try again   ")

'''
