from pathlib import Path

from summarize_text import summarize_transactions, summarize_transactions_json
from summarizer import load_transactions, summarize

PRINT_JSON = False

if __name__ == "__main__":
    base_dir = Path(__file__).resolve().parent
    csv_path = base_dir / "data" / "demo_transactions.csv"

    rows = load_transactions(csv_path)
    report = summarize(rows)

    print(summarize_transactions(report))

    if PRINT_JSON:
        print(summarize_transactions_json(report))