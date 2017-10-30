import time

MAX_NUMBER = 99999


def biggest_palindrome(n):
    palindrome = 0
    for i in range(n, 10000, -1):
        if i*i < palindrome:
            break

        for j in range(i, 10000, -1):
            check_number = j * i
            if check_number <= palindrome:
                break
            if str(check_number) == str(check_number)[::-1]:
                palindrome = check_number
                break

    return palindrome


start = time.time()
print(biggest_palindrome(MAX_NUMBER))
print(time.time() - start)
