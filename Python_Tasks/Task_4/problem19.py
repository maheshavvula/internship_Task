#Collections.Counter()
#https://www.hackerrank.com/challenges/collections-counter/problem

 Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

if __name__ == '__main__':
    # Step 1: Read input
    n = int(input())                          # number of shoes
    shoe_sizes = list(map(int, input().split()))
    x = int(input())                          # number of customers

    # Step 2: Count available shoes
    inventory = Counter(shoe_sizes)

    # Step 3: Process each customer
    earnings = 0
    for _ in range(x):
        size, price = map(int, input().split())
        if inventory[size] > 0:               # shoe available
            earnings += price
            inventory[size] -= 1              # reduce stock

    # Step 4: Print total earnings
    print(earnings)
