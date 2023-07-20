import re
fname = input("input data file name: ")
if len(fname)<1: 
    fname = 'regex_sum_1849801.txt'
str=[]
new_list = list()
fh = open(fname)
for line in fh:
    line = line.rstrip()
    str = re.findall('[0-9]+', line)
    for i in str:
        if i:
            i = int(i)
            new_list.append(i)
print(sum(new_list))
    