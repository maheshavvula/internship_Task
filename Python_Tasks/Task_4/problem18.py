#18
#Lists
#https://www.hackerrank.com/challenges/python-lists/problem
if __name__ == '__main__':
    N = int(input())   # number of commands
    lst = []           # initialize empty list

    for _ in range(N):
        command = input().split()
        op = command[0]

        if op == "insert":
            i, e = int(command[1]), int(command[2])
            lst.insert(i, e)
        elif op == "print":
            print(lst)
        elif op == "remove":
            e = int(command[1])
            lst.remove(e)
        elif op == "append":
            e = int(command[1])
            lst.append(e)
        elif op == "sort":
            lst.sort()
        elif op == "pop":
            lst.pop()
        elif op == "reverse":
            lst.reverse()

