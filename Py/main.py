def rev(s):
    # Возвращает строку в обратном порядке.
    return s[::-1]

def is_palindrome(s):
    # Проверяет, является ли строка палиндромом.
    s = ''.join(s.lower().split())
    return s == rev(s)

def count_vowels(s):
    # Считает количество гласных букв в строке.
    return sum(1 for char in s.lower() if char in 'aeiou')

def find_repeated_chars(s):
    # Находит повторяющиеся символы в строке.
    s = s.lower()
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return {char: count for char, count in char_count.items() if count > 1}