from main import rev, is_palindrome, count_vowels, find_repeated_chars

import unittest

class TestingStringFunctions(unittest.TestCase):
    
    def test_rev(self):
        self.assertEqual(rev("Hello"), "olleH")
        self.assertEqual(rev("Python"), "nohtyP")
        self.assertEqual(rev(""), "") # Пустая строка.
        self.assertEqual(rev("12345"), "54321") # Числа.
        self.assertEqual(rev("A man"), "nam A") # Смешанные символы.
        self.assertEqual(rev("racecar"), "racecar") # Палиндром.
        self.assertEqual(rev("!@#$%^"), "^%$#@!") # Специальные символы.
        self.assertEqual(rev(" "), " ") # Пробел.
        self.assertEqual(rev("Hello World!"), "!dlroW olleH") # Фраза.
        self.assertEqual(rev("Python 3.9"), "9.3 nohtyP") # Числа и буквы.
        
    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))
        self.assertFalse(is_palindrome("Hello"))
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome(""))
        self.assertTrue(is_palindrome("No lemon, no melon"))
        self.assertFalse(is_palindrome("Python"))
        self.assertTrue(is_palindrome("Was it a car or a cat I saw"))
        self.assertFalse(is_palindrome("Hello World"))
        self.assertTrue(is_palindrome("Able was I ere I saw Elba"))
        self.assertFalse(is_palindrome("Not a palindrome"))
        
    def test_count_vowels(self):
        self.assertEqual(count_vowels("Hello"), 2)
        self.assertEqual(count_vowels("Python"), 1)
        self.assertEqual(count_vowels("aeiou"), 5)
        self.assertEqual(count_vowels(""), 0) # Пустая строка.
        self.assertEqual(count_vowels("This is a test"), 4)
        self.assertEqual(count_vowels("Rhythm"), 0)
        self.assertEqual(count_vowels("Beautiful"), 5)
        self.assertEqual(count_vowels(""), 0) # Пустая строка.
        self.assertEqual(count_vowels("AEIOU"), 5) # Все гласные в верхнем регистре.
        self.assertEqual(count_vowels("The quick brown fox jumps over the lazy dog"), 11) # Полный алфавит.
        
    def test_find_repeated_chars(self):
        self.assertEqual(find_repeated_chars("Hello"), { 'l': 2 })
        self.assertEqual(find_repeated_chars("Python"), {})
        self.assertEqual(find_repeated_chars("aabbcc"), { 'a': 2, 'b': 2, 'c': 2 })
        self.assertEqual(find_repeated_chars(""), {}) # Пустая строка
        self.assertEqual(find_repeated_chars("Mississippi"), { 'i': 4, 's': 4, 'p': 2 })
        self.assertEqual(find_repeated_chars("abcde"), {})
        self.assertEqual(find_repeated_chars("aaAA"), { 'a': 4 }) # Различные регистры.
        self.assertEqual(find_repeated_chars("11223344"), { '1': 2, '2': 2, '3': 2, '4': 2 }) # Числа.
        self.assertEqual(find_repeated_chars("!@#$%^&*()!@#"), { '!': 2, '@': 2, '#': 2 }) # Специальные символы.
        self.assertEqual(find_repeated_chars("abababab"), { 'a': 4, 'b': 4 }) # Повторяющиеся символы.
        
if __name__ == '__main__':
    unittest.main()