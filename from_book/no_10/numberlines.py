import fileinput                                   #  1 #  1 #  1
                                                   #  2 #  2 #  2
for line in fileinput.input(inplace=True):         #  3 #  3 #  3
    line = line.rstrip()                           #  4 #  4 #  4
    num = fileinput.lineno()                       #  5 #  5 #  5
                                                   #  6 #  6 #  6
    print('{:<50} # {:2d}'.format(line,num))       #  7 #  7 #  7
