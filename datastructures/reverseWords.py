def reverseWords_new_array(s: str) -> str:
    words = s.split()
    res = []

    for i in range(len(words) - 1, -1, -1):
        res.append(words[i])
        if i != 0:
            res.append(" ")

    return "".join(res)


def reverseWords_swap_in_place( s: str) -> str:
    words = s.split()
    left, right = 0, len(words) - 1

    while left < right:
        words[left], words[right] = words[right], words[left]
        left += 1
        right -= 1

    return " ".join(words)


def reverseWordsPY(s: str) -> str:
    return " ".join(reversed(s.split()))


s = "life is an adventure"

print(reverseWords_new_array(s))
print(reverseWords_swap_in_place(s))
print(reverseWordsPY(s))