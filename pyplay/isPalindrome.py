def isPalindrome(s: str) -> bool:
    newStr = ""
    for c in s:
        if c.isalnum():
            newStr += c.lower()
    return newStr == newStr[::-1]

test_cases = [
   (1, "Was it a car or a cat I saw?"),
   (2, "tab a cat"),
   (3, "Able was I ere I saw Elba"),
   (4, "Ah, Satan sees Natasha"),
   (5, "Simple is better than complex")
]

for test in test_cases:
    print(isPalindrome(test[1]))