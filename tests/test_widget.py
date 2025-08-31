import pytest
from src.widget import mask_account_card


@pytest.fixture()
def number():
    return "Visa Platinum 7000792289606361"


def test_mask_account_card(number):
    assert mask_account_card(number) == "Visa Platinum 7000 79** **** 6361"