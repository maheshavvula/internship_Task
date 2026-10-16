#11
#String Validators
#https://www.hackerrank.com/challenges/string-validators/problem

if __name__ == '__main__':
    s = input()
    
    print(any(c.isalnum() for c in s))   # Alphanumeric check
    print(any(c.isalpha() for c in s))   # Alphabet check
    print(any(c.isdigit() for c in s))   # Digit check
    print(any(c.islower() for c in s))   # Lowercase check
    print(any(c.isupper() for c in s))   # Uppercase check


