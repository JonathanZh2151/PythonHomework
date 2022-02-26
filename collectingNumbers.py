def collectRounds(n):
    r = 0
    curNum = 1
    while (curNum < len(n)):
        for i in range(len(n)):
            if (n[i] == curNum):
                curNum += 1
        r += 1
    return r

numNums = int(input())
nums = list(map(int, input().split()))

print(collectRounds(nums))
