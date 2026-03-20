def summarize_transactions(report: dict, top_n: int = 3) -> str:
    total_spent = report.get("total_spent", 0.0)
    total_income = report.get("total_income", 0.0)
    by_date = report.get("by_date", {})
    by_merchant = report.get("by_merchant", {})
    high_flags = report.get("high_flags", [])

    net = round(total_income - total_spent, 2)

    expense_days = [(d, amt) for d, amt in by_date.items() if amt < 0]
    expense_days.sort(key=lambda x: x[1])  # most negative first

    spent_items = []
    for m, total in by_merchant.items():
        if total < 0:
            spent_items.append((m, round(-total, 2)))
    spent_items.sort(key=lambda x: x[1], reverse=True)
    top_merchants = spent_items[:top_n]

    lines = []
    lines.append("Summary:")
    lines.append(f"- Total spent: {total_spent:.2f}")
    lines.append(f"- Total income: {total_income:.2f}")
    lines.append(f"- Net: {net:.2f}")


    if top_merchants:
        merch_str = ", ".join([f"{m} ({amt:.2f})" for m, amt in top_merchants])
        lines.append(f"- Top {len(top_merchants)} spending merchants: {merch_str}")

    if expense_days:
        worst_day, worst_amt = expense_days[0]
        lines.append(f"- Highest-spend day: {worst_day} ({abs(worst_amt):.2f})")

    if high_flags:
        lines.append(f"- High-amount flags: {len(high_flags)}")
        for r in high_flags[:3]:
            lines.append(
                f"  • {r.get('date')} {r.get('merchant')}: {abs(r.get('amount', 0.0)):.2f} {r.get('currency','')}".strip()
            )

    return "\n".join(lines)


def _test_summarize_transactions():
    report = {
        "total_spent": 329.38,
        "total_income": 1200.0,
        "by_merchant": {"AMAZON": -274.99, "SALARY": 1200.0},
        "by_date": {"2026-03-04": -210.0, "2026-03-02": 1135.01},
        "high_flags": [
            {
                "date": "2026-03-04",
                "merchant": "AMAZON",
                "amount": -210.0,
                "currency": "EUR",
            }
        ],
    }
    text = summarize_transactions(report)
    assert "Total spent: 329.38" in text
    assert "Total income: 1200.00" in text
    assert "Net: 870.62" in text
    assert "High-amount flags: 1" in text


if __name__ == "__main__":
    _test_summarize_transactions()
    print("All tests passed!")
