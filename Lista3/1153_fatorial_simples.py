n = int(input())
fat = n
for i in range(n - 1, 0, -1):
    fat = fat * i
print(fat)
