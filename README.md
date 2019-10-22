# CCSampleGen
Simple dataset generator for electronics sales with customers designed
for use with Campaign Classic however can be useful elsewhere.

# Usage
First unzip data/data.zip into data/
then:

`python3 dataset.py [...] basepath user-number`

```bash
usage: Generate datasets which are compatible with Adobe Campaign Classic
       [-h] [--transaction-multiplier TRANSACTION_MULTIPLIER]
       [--min-transactions MIN_TRANSACTIONS]
       basepath user-number

positional arguments:
  basepath              where csv files should be exported
  user-number           total number of users

optional arguments:
  -h, --help            show this help message and exit
  --transaction-multiplier TRANSACTION_MULTIPLIER
                        multiplier for number of transactions
  --min-transactions MIN_TRANSACTIONS
                        minumum number of transactions per customer
```

# Notice
This repo uses Electronic Products and Pricing Data
https://www.kaggle.com/datafiniti/electronic-products-prices/download
https://creativecommons.org/licenses/by-nc-sa/4.0/

and therefore is limited by its license agreement, feel free to replace it.
