def clean_int(s: str) -> int:
    """
    Convert strings like " '1,234,567 " or "1 234 567" to int 1234567.
    Keeps a leading '-' if present.
    """

    cleaned = s.strip().replace(",", "").replace("'", "").replace(" ", "")

    return int(cleaned)


def parse_currency_row(row: dict) -> dict:
    """
       Takes a CSV DictReader row and returns a cleaned version.
       Expected keys: date, merchant, amount, currency
       """

    out = dict(row)  # copy
    out["date"] = row["date"].strip()
    out["merchant"] = row["merchant"].strip()
    out["currency"] = row["currency"].strip().upper()

    amt = row["amount"]
    cleaned_amt = amt.strip().replace("€", "").replace(",", "").replace(" ", "")
    out["amount"] = float(cleaned_amt)

    return out

