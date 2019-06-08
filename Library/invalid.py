def invalid_number(number):
    if not number:
        raise ValueError
    res = int(number)
    if res < 0:
        raise ValueError
    return res


def invalid_text(text: str):
    if "," in text:
        raise ValueError
    return text.strip()
