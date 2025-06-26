# palindrome_checker.py
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

if __name__ == "__main__":
    word = "Racecar"
    print(f"'{word}' is a palindrome? {is_palindrome(word)}")
