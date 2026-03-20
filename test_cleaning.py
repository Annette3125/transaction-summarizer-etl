from cleaning import clean_int, parse_currency_row


def test_clean_int():
    assert clean_int(" '1,234,567 ") == 1234567
    assert clean_int("1 234 567") == 1234567
    assert clean_int("-2,000") == -2000
    assert clean_int("0") == 0

def test_parse_currency_row():
    row = {"date": " 2026-03-04 ", "merchant": " AMAZON ", "amount": " € 1,234.50 ", "currency": " eur "}
    out = parse_currency_row(row)
    assert out["date"] == "2026-03-04"
    assert out["merchant"] == "AMAZON"
    assert out["currency"] == "EUR"
    assert abs(out["amount"] - 1234.5) < 1e-9


if __name__ == "__main__":
    test_clean_int()
    test_parse_currency_row()
    print("All tests passed!")