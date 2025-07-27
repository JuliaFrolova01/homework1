from masks.card_number import get_mask_card_number


def mask_account_card(account_card: str) -> str:
    '''Принимает номер карты и возвращает маску'''
    if "Счет" in account_card:
        mask_account_card = f"{account_card[:4]} **{account_card[-5:-1]}"
        return mask_account_card
    else:
        tip_card = f"{account_card[:-16]}"

        num_card = str(get_mask_card_number())
        mask_account_card = tip_card + num_card
        return mask_account_card



if __name__ == "__main__":
    print(mask_account_card("Visa Platinum 7000792289606361"))