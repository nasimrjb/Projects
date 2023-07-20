name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
lst = list()
mailn = list()
dictt = dict()
handle = open(name)
for line in handle:
    if not line.startswith("From:"):
        continue
    line = line.split()
    lst.append(line[1])
# print(lst)
for v in lst:
    dictt[v] = dictt.get(v, 0) + 1

print(dictt)

bc = None
bw = None

for x, y in dictt.items():
    if bc is None or y > bc:
        bc = y
        bw = x

print(bw, bc)
