import itertools


def process_next_cmd():
    cmd = input().split()
    if cmd[0] == 'insert':
        listValues.insert(int(cmd[1]), int(cmd[2]))
    elif cmd[0] == 'print':
        print (listValues)
    elif cmd[0] == 'remove':
        listValues.remove(int(cmd[1]))
    elif cmd[0] == 'append':
        listValues.append(int(cmd[1]))
    elif cmd[0] == 'sort':
        listValues.sort()
    elif cmd[0] == 'pop':
        listValues.pop()
    elif cmd[0] == 'reverse':
        listValues.reverse()


if __name__ == '__main__':
    N = int(input())
    listValues = []
    for _ in itertools.repeat(None, N):
        process_next_cmd()
