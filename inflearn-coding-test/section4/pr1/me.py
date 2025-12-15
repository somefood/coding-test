import sys
sys.stdin = open("input.txt", "rt")

def is_palindrome(word: str):
    lower_word = word.lower()
    
    if lower_word[::] == lower_word[::-1]:
        return "YES"
    else:
        return "NO"

N = int(input())

for idx, _ in enumerate(range(N)):
    word = input().strip()
    print(f"#{idx + 1} {is_palindrome(word)}")
    