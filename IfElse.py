def is_weird(num):
    if num % 2 != 0:
        return True
    if 2 <= num <= 5:
        return False
    if 6 <= num <= 20:
        return True
    return False


if __name__ == '__main__':
    n = int(input())
    if is_weird(n):
        print('Weird')
    else:
        print('Not Weird')
