#Finding the Percentage
#https://www.hackerrank.com/challenges/finding-the-percentage/problem
if __name__ == '__main__':
    n = int(input())   # number of students
    student_marks = {}

    for _ in range(n):
        data = input().split()
        name = data[0]
        scores = list(map(float, data[1:]))
        student_marks[name] = scores

    query_name = input().strip()
    avg = sum(student_marks[query_name]) / len(student_marks[query_name])
    print(f"{avg:.2f}")
