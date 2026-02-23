#Check if All Elements Are Palindrome

def is_palindrome(num):
    return str(num) == str(num)[::-1]

def palindrome_array(arr):
    for i in arr:
        if not is_palindrome(i):
            return False
    return True


arr = [111, 222, 333, 444, 555]
print(palindrome_array(arr))