from datetime import datetime


def get_date(date: str) -> str:
    """Принимает дату и возвращает ее в правильном формате"""
    dt = datetime.fromisoformat(date)
    return dt.strftime("%d.%m.%Y")


print(get_date("2024-03-11T02:26:18.671407"))
