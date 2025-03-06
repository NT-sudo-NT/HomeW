from main import rev, is_palindrome, count_vowels, find_repeated_chars

def run_tests():

    print("Тесты для функции rev:")
    assert rev("hello") == "olleh", "Ошибка: 'hello' должно быть 'olleh'"
    assert rev("Python") == "nohtyP", "Ошибка: 'Python' должно быть 'nohtyP'"
    assert rev("") == "", "Ошибка: пустая строка должна оставаться пустой"
    print("Все тесты для rev пройдены.\n")

    print("Тесты для функции is_palindrome:")
    assert is_palindrome("A man a plan a canal Panama") == True, "Ошибка: это палиндром"
    assert is_palindrome("hello") == False, "Ошибка: это не палиндром"
    assert is_palindrome(" ") == True, "Ошибка: пробел считается палиндромом"
    assert is_palindrome("Was it a car or a cat I saw") == True, "Ошибка: это палиндром"
    print("Все тесты для is_palindrome пройдены.\n")

    print("Тесты для функции count_vowels:")
    assert count_vowels("hello") == 2, "Ошибка: 'hello' должно содержать 2 гласные"
    assert count_vowels("Python") == 1, "Ошибка: 'Python' должно содержать 1 гласную"
    assert count_vowels("AEIOU") == 5, "Ошибка: 'AEIOU' должно содержать 5 гласных"
    assert count_vowels("") == 0, "Ошибка: пустая строка должна содержать 0 гласных"
    print("Все тесты для count_vowels пройдены.\n")

    print("Тесты для функции find_repeated_chars:")
    assert find_repeated_chars("hello") == {'l': 2}, "Ошибка: 'hello' должно вернуть {'l': 2}"
    assert find_repeated_chars("Python") == {}, "Ошибка: 'Python' не должно содержать повторяющихся символов"
    assert find_repeated_chars("aabbcc") == {'a': 2, 'b': 2, 'c': 2}, "Ошибка: 'aabbcc' должно вернуть {'a': 2, 'b': 2, 'c': 2}"
    assert find_repeated_chars("") == {}, "Ошибка: пустая строка не должна содержать повторяющихся символов"
    print("Все тесты для find_repeated_chars пройдены.\n")

if __name__ == "__main__":
    run_tests()