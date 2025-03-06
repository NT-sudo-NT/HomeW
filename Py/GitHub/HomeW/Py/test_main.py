from main import rev, is_palindrome, count_vowels, find_repeated_chars

def test_rev():
    assert rev("Hello") == "olleH"
    assert rev("Python") == "nohtyP"
    assert rev("") == ""  # Пустая строка.
    assert rev("12345") == "54321"  # Числа.
    assert rev("A man") == "nam A"  # Смешанные символы.
    assert rev("racecar") == "racecar"  # Палиндром.
    assert rev("!@#$%^") == "^%$#@!"  # Специальные символы.
    assert rev(" ") == " "  # Пробел.
    assert rev("Hello World!") == "!dlroW olleH"  # Фраза.
    assert rev("Python 3.9") == "9.3 nohtyP"  # Числа и буквы.

def test_is_palindrome():
    assert is_palindrome("A man a plan a canal Panama") == True
    assert is_palindrome("Hello") == False
    assert is_palindrome("racecar") == True
    assert is_palindrome("") == True
    assert is_palindrome("No lemon, no melon") == True
    assert is_palindrome("Python") == False
    assert is_palindrome("Was it a car or a cat I saw") == True
    assert is_palindrome("Hello World") == False
    assert is_palindrome("Able was I ere I saw Elba") == True
    assert is_palindrome("Not a palindrome") == False

def test_count_vowels():
    assert count_vowels("Hello") == 2
    assert count_vowels("Python") == 1
    assert count_vowels("aeiou") == 5
    assert count_vowels("") == 0  # Пустая строка.
    assert count_vowels("This is a test") == 4
    assert count_vowels("Rhythm") == 0
    assert count_vowels("Beautiful") == 5
    assert count_vowels("AEIOU") == 5  # Все гласные в верхнем регистре.
    assert count_vowels("The quick brown fox jumps over the lazy dog") == 11  # Полный алфавит.
    assert count_vowels("Cat! 123") == 1  # Только одна гласная "a"

def test_find_repeated_chars():
    assert find_repeated_chars("Hello") == {'l': 2}
    assert find_repeated_chars("Python") == {}
    assert find_repeated_chars("aabbcc") == {'a': 2, 'b': 2, 'c': 2}
    assert find_repeated_chars("") == {}  # Пустая строка
    assert find_repeated_chars("Mississippi") == {'i': 4, 's': 4, 'p': 2}
    assert find_repeated_chars("abcde") == {}
    assert find_repeated_chars("aaAA") == {'a': 4}  # Различные регистры.
    assert find_repeated_chars("11223344") == {'1': 2, '2': 2, '3': 2, '4': 2}  # Числа.
    assert find_repeated_chars("!@#$%^&*()!@#") == {'!': 2, '@': 2, '#': 2}  # Специальные символы.
    assert find_repeated_chars("abababab") == {'a': 4, 'b': 4}  # Повторяющиеся символы.