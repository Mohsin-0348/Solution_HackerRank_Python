def find_runnerup(arr):
    for i in range(len(arr)-1, 0, -1):
        if arr[i] > arr[i-1]:
            runner_up = arr[i-1]
            break
    else:
        runner_up = arr[-1]
    return runner_up

if __name__ == '__main__':
    n = int(input())
    num = list(map(int, input().split()))
    num = num[:n]
    for i in range(n):
        for j in range(n-1):
            if num[j] > num [j+1]:
                temp = num[j]
                num[j] = num[j+1]
                num[j+1] = temp

    print(find_runnerup(num))
