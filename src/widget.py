from src.masks.card_number import get_mask_card_number


def mask_account_card(card_number: str) -> str:
    '''Принимает номер карты и возвращает маску'''
    if "Счет" in card_number:
        mask_account_card = f"{card_number[:4]} **{card_number[-5:]}"
        return mask_account_card
    else:
        type_card = f"{card_number.split()[0]} {card_number.split()[1]} "

        card_num = get_mask_card_number(card_number.split()[-1])
        mask_account_card = type_card + card_num
        return mask_account_card



if __name__ == "__main__":
    print(mask_account_card("Счет 64686473678894779589"))
