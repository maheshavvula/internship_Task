#Word Order

#https://www.hackerrank.com/challenges/word-order/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

if __name__ == '__main__':
    n = int(input())
    word_count = OrderedDict()   # preserves insertion order

    for _ in range(n):
        word = input().strip()
        word_count[word] = word_count.get(word, 0) + 1

    # First line: number of distinct words
    print(len(word_count))

    # Second line: occurrences in order of appearance
    print(" ".join(str(count) for count in word_count.values()))
