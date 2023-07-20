fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    x = line.rstrip()
    y = x.split()
    for w in y:
        if w in lst:
            continue
        else:
        lst.append(w)
print(list.sort())
