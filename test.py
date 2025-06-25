import pytest
from main import count_vowels

def test_count_vowels():
    # Проверка строки, содержащей только гласные
    assert count_vowels('аеёиоуыэюяАЕЁИОУЫЭЮЯ') == 20
    # Проверка строки без гласных
    assert count_vowels('бвгджзйклмнпрстфхцчшщ') == 0
    # Проверка смешанной строки с прописными и строчными буквами
    assert count_vowels('Привет, как дела?') == 5
    assert count_vowels('Съешь ещё этих мЯгких французскИх булок, да выпей чаю.') == 17
