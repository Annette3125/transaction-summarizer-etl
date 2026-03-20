import csv
from collections import defaultdict

from cleaning import parse_currency_row


def load_transactions(path):
    rows = []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for r in reader:
            rows.append(parse_currency_row(r))
    return rows


def summarize(rows, high_amount_threshold=200.0):
    total_spent = 0.0
    total_income = 0.0
    by_merchant = defaultdict(float)
    by_date = defaultdict(float)
    high_flags = []

    for r in rows:
        amt = r["amount"]
        merchant = r["merchant"]
        date = r["date"]

        # update totals
        if amt < 0:
            total_spent += -amt
        else:
            total_income += amt

        # update group-bys
        by_merchant[merchant] += amt
        by_date[date] += amt

        # Tadd high amount flags (abs(amt) >= threshold and amt < 0)
        if amt < 0 and abs(amt) >= high_amount_threshold:
            high_flags.append(r)

    return {
        "total_spent": round(total_spent, 2),
        "total_income": round(total_income, 2),
        "by_merchant": dict(by_merchant),
        "by_date": dict(by_date),
        "high_flags": high_flags,
    }


def top_n_merchants(by_merchant, n=3):
    spent_items = []
    for m, total in by_merchant.items():
        if total < 0:
            spent_items.append((m, -total))

    spent_items.sort(key=lambda x: x[1], reverse=True)  # most negative first
    return spent_items[:n]


