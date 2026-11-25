
arr1 = [10, 5, 3]
arr2 = [3, 5 ,9]

for value1 in arr1:
    value1_1 = int(value1)

    result = value1_1 * 10

    print(result)


pick = input("분류: ").strip().split(",")

arr3 = []

if pick == "note":
    arr3.append(12000)
elif pick == "cup":
    arr3.append(6000)
else:
    arr3.append(3000)

print(arr3)