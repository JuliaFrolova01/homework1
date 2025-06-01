def get_mask_card_number(card_number: str) -> str:
    """Принимает номер карты и создает маску"""
    return card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]


print(get_mask_card_number("7000792289606361"))
