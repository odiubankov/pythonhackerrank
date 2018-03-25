if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    arr.sort(reverse=True)
    for i in arr:
        if i < arr[0]:
            print(i)
            break
