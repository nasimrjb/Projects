########## 1 ##########

# def multiples(a):
#     count = 0
#     for i in range(a):
#         if i % 3 == 0 or i % 5 == 0:
#             count += i
#     return count


# print(multiples(1000))

########## 2 ##########

# lst = [0]*400
# lst[0] = 1
# lst[1] = 2

# for i in range(0, 398):
#     lst[i+2] = lst[i+1]+lst[i]
# print(lst)
# sum = 0
# for j in lst:
#     if j < 4000000 and j % 2 == 0:
#         sum += j
# print(sum)

########## 3 ##########
# def largest_prime(n):
#     count = 0
#     for i in range(n, 0, -1):
#         if n % i == 0:
#             for j in range(i, 0, -1):
#                 if i % j == 0:
#                     count += 1
#             if count == 2:
#                 return i
#             count = 0


# print(largest_prime(600851475143))


########## 4 ##########
# lst = []
# for i in range(999):
#     for j in range(999):
#         m = i*j
#         n = str(m)
#         if n[::-1] == n:
#             lst.append(n)

# lst = [int(i) for i in lst]
# print(max(lst))

########## 5 ##########
count = 0
for i in range(300000000, 0, -1):
    for j in range(20, 0, -1):
        if i % j == 0:
            count += 1
    if count == 20:
        print(i)
    count = 0
########## 6 ##########
