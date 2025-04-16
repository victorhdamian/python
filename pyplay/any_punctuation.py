import string

# returns true if there are any punctuation characters
def contains_punctuation(input_str):
    return any(
        char in string.punctuation
        for char in input_str
    )


test_cases = [
   (1, "Readability counts."),
   (2, "If the implementation is hard to explain, it's a bad idea."),
   (3, "There should be one-- and preferably only one --obvious way to do it."),
   (4, "Errors should never pass silently"),
   (5, "Simple is better than complex")
]

for test in test_cases:
    print(contains_punctuation(test[1]))

