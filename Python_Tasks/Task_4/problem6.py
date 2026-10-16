#Find the Runner-Up Score!
#https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())


   

    
    # Remove duplicate scores and sort them in descending order
    unique_scores = sorted(list(set(arr)), reverse=True)
    
    # The runner-up score will be at index 1
    print(unique_scores[1])
