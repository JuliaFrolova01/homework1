from src.masks.account import get_mask_account


def test_get_mask_account1():
    assert get_mask_account('73654108430135874305') == '**4305'
