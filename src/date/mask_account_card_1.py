def mask_account_card(card_number: str) -> str:
    """Принимает номер карты или счета и маскирует"""
    parts = card_number.split()
    if len(parts) != 2:
        return "Неверный формат"

    card_type, number = parts
    if "Счет" in card_type:
        masked_number = "**" + number[-4:]
    else:
        masked_number = number[:4] + " " + number[4:6] + "** **** " + number[-4:]
    return f"{card_type} {masked_number}"


print(mask_account_card("MasterCard 7158300734726758"))
