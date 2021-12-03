x = 15
maxline = x // 2 + 1
control_line = x-maxline
for i in range(1,x+1):
    print('')
    if i<=maxline:
        print((maxline-i)*' ',end="")
        print((2*i-1)*'*',end="")
    else:
        print((i-maxline)*' ',end="")
        print((control_line*2-1)*'*',end='')
        control_line-=1
    #print('')
        

    
    #mid = (x-i) // 2
    #print(mid*' ',end="")
    
    #print((2*i-1)*'*',end="")
    #print(mid*' ',end="")
    #print("")
