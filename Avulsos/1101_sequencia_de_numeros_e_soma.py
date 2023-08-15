while True:
    try:
        x, y = input().split()
        x = int(x)
        y = int(y)
        nums = []
        soma = 0
        if x <= 0 or 0 >= y:
            break
        if x > y:
            for i in range(y, x + 1):
                nums.append(i)
                soma = soma + i
        elif y > x:
            for i in range(x, y + 1):
                nums.append(i)
                soma = soma + i
        else:
            nums.append(0)
        for i in range(len(nums)):
            if i == len(nums) - 1:
                print(f'{nums[i]} Sum={soma}')
            else:
                print(nums[i], end=' ')
    except EOFError:
        break
