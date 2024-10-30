def findLeaders_soln1(arr):
    leaders = []
    for i in range(len(arr)):
        j = i + 1
        while j < len(arr):
            if arr[i] < arr[j]:
                break
            j = j + 1
        if j == len(arr):
            leaders.append(arr[i])
    return leaders


def findLeaders_soln2(arr):
    leaders = []
    n = len(arr)
    maxFromRight = arr[n - 1]
    leaders.append(maxFromRight)
    for i in range(n - 2, -1, -1):
        if maxFromRight < arr[i]:
            maxFromRight = arr[i]
            leaders.append(maxFromRight)
    return leaders


print(findLeaders_soln2([16, 17, 4, 3, 5, 2]))
print(findLeaders_soln2([6, 5, 4, 3, 2, 1]))
print(findLeaders_soln2([1, 2, 3, 4, 5, 6]))
