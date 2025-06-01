def get_mask_account(account: str) -> str:
    """Принимает номер счета и возвращает маску"""
    return "**" + account[-4:]


print(get_mask_account("73654108430135874305"))
