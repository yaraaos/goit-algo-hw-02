from collections import deque
import string

def is_palindrome(s):
    # Для зберігання символів
    d = deque()

    # Щоб ігнорувати пробіли та неалфавітно-цифрові символи
    for char in s.lower():
        if char in string.ascii_lowercase or char.isdigit():
            d.append(char)

    # Для порівняння символів з обох кінців
    while len(d) > 1:
        if d.popleft() != d.pop():
            return False
    
    return True

# Тестування функції
test_strings = ["око", "12321", "мадам", "потоп", "Ukraine", "Hello"]
for test in test_strings:
    print(f"'{test}' is a palindrome: {is_palindrome(test)}")
