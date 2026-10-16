#Set .add()

#https://www.hackerrank.com/challenges/py-set-add/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    n = int(input())          # total number of stamps
    stamps = set()            # empty set

    for _ in range(n):
        country = input().strip()
        stamps.add(country)   # add each country to set

    print(len(stamps))        # print total distinct countries
