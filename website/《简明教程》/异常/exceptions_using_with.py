#我们将关闭文件的操作交由 with open 来自动完成
with open("poem.txt") as f:
    for line in f:
        print(line, end='')
