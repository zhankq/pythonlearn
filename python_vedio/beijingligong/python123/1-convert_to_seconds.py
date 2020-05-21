import sys
def convert_to_seconds(time_str):
    # write code here
    if 'd' in time_str or 'D' in time_str:
        

while True:
    line = sys.stdin.readline()
    line = line.strip()
    if line == '':
        break
    print(convert_to_seconds(line))
