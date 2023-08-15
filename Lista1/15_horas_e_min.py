n = int(input())
hrs = 0
seg = n % 60
mts = n // 60
if mts > 59:
    hrs = mts // 60
    mts = mts % 60
print('{}:{}:{}'.format(hrs, mts, seg))
