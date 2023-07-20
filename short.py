# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
sum=0
count=0
fh = open(fname)
# fh= fh.read()
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    t=line.find("0")
    sum = float(line[t:])+sum
    count = count + 1
print("Average spam confidence: ", sum/count)
print("Done")
#         sum = float(line[23:]) + sum
#         count = count + 1

# 