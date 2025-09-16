import pytest
from src.widget import mask_account_card


@pytest.mark.parametrize("number, card_number", [
    ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
    ("Счет 64686473678894779589", "Счет **79589"),
    ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658")
])
def test_mask_account_card(number, card_number):
    assert mask_account_card(number) == card_number
