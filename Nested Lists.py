def find_lowest(arr):
    for i in range(1, 2*n, 2):
        for j in range(1, 2*n-1, 2):
            if arr[j] > arr[j+2]:
                temp = arr[j]
                arr[j] = arr[j+2]
                arr[j+2] = temp

                t = arr[j-1]
                arr[j-1] = arr[j+1]
                arr[j+1] = t
                
    for i in range(1, 2*n-2, 2):
        if arr[i] < arr[i+2]:
            scnd = arr[i+2]
            break
    else:
        scnd = arr[0]
    return scnd

if __name__ == '__main__':
    li = []
    name = []
    n = int(input())
    for i in range(2*n):
        x = input()
        if i % 2 == 0:
            li.append(x)
        else:
            li.append(float(x))
    second_lowest = find_lowest(li)
    for a in range(1, 2*n, 2):
        if li[a] == second_lowest:
            name.append(li[a-1])
    name.sort()
    for z in name:
        print(z)
