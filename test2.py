import pytest
from main import count_vowels


@pytest.mark.parametrize("input_text, expected",
    [
        ("аеёиоуыэюяАЕЁИОУЫЭЮЯ", 20),  # только гласные
        ("бвгджзйклмнпрстфхцчшщ", 0),  # нет гласных
        ("Привет, как дела?", 5),      # смешанная строка
        ("Съешь ещё этих мягких французских булок, да выпей чаю.", 17),  # сложная строка
        ("", 0),                       # пустая строка
        ("12345!@#", 0),               # только цифры и знаки
        ("АаЕе", 4),                   # смешанный регистр
    ]
)
def test_count_vowels(input_text, expected):
    assert count_vowels(input_text) == expected