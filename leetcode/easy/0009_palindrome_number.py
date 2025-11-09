import sys


def is_palindrome(n: int) -> bool:
    if x // 10 == 0:
        return True
    # Check for negative numbers and trailing zeros
    if n < 0 or (n % 10 == 0 and n != 0):
        return False

    str_x = str(n)
    while len(str_x) > 1:
        if str_x[0] != str_x[-1]:
            return False
        str_x = str_x[1:-1]
    return True


if __name__ == "__main__":
    if len(sys.argv) > 1:
        x = int(sys.argv[1])
    else:
        x = 121
    print(f"Input: {x}")
    print(is_palindrome(x))
    # Output: True
    # Explanation: 121 is a palindrome number.
