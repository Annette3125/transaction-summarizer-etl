# transaction-summarizer-etl
Mini ETL: parse transaction CSV, generate totals, top merchants, daily sums, and risk flags.

Loads a CSV file of transactions and prints:
- total spent
- total income
- totals by merchant
- totals by date
- high-amount flags

## Run
```
python run.py
```

### Tests
```
python summary_text.py
```


## CSV format

```csv
date,merchant,amount,currency
```
- negative amount = expense, positive = income



### Sample output

```
Total spent: 329.38
Total income: 1200.0
Top merchants: [('AMAZON', 274.99), ('MAXIMA', 35.5), ('NETFLIX', 9.99)]
Daily totals: {'2026-03-01': -21.3, '2026-03-02': 1135.01, '2026-03-03': -33.09, '2026-03-04': -210.0}
High flags: [{'date': '2026-03-04', 'merchant': 'AMAZON', 'amount': -210.0, 'currency': 'EUR'}]
```
