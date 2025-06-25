def count_vowels(text):
    vowels = set('аеёиоуыэюяАЕЁИОУЫЭЮЯ')
    return sum(1 for char in text if char in vowels)
