#Nested Lists
#https://www.hackerrank.com/challenges/nested-list/problem

if __name__ == '__main__':
   
    students = []
    for _ in range(int(input())):
        name = input().strip()
        score = float(input())
        students.append([name, score])

    # Step 1: Extract all scores
    scores = sorted(set([s[1] for s in students]))

    # Step 2: Find second lowest score
    second_lowest = scores[1]

    # Step 3: Collect names with second lowest score
    names = [s[0] for s in students if s[1] == second_lowest]

    # Step 4: Print names alphabetically
    for name in sorted(names):
        print(name)
