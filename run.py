from pathlib import Path

from summarize_text import summarize_transactions
from summarizer import load_transactions, summarize

if __name__ == "__main__":
    base_dir = Path(__file__).resolve().parent
    csv_path = base_dir / "data" / "demo_transactions.csv"

    rows = load_transactions(csv_path)
    report = summarize(rows)

    print(summarize_transactions(report))
