def mpp(numbers):
    n = len(numbers)
    ind1 = -1
    for i in range(n):
        if ind1 == -1 or numbers[i] > numbers[ind1]:
            ind1 = i
    ind2 = -1
    for i in range(n):
        if i != ind1 and (ind2 == -1 or numbers[i] > numbers[ind2]):
            ind2 = i
    max_product = numbers[ind1] * numbers[ind2]
    return max_product


if __name__ == '__main__':
    #     _ = int(float(input('')))
    #     input_numbers = list(map(int, input().rsplit()))

    x = input("input numbers")
    input_numbers = list(map(int, x.rsplit()))

print(mpp(input_numbers))
