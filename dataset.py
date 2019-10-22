import users
import products
import transactions
import argparse
from os.path import join

def generate_dataset(basepath, usern, trans_multi=1.0, minimum_trans=1):
    """
    Generate a dataset containing customers, products, and transactions
    Keyword arguments:
        basepath --directory to put the files in, do not end with /
        usern -- number of users (affects number of transactions)
        trans_multi -- multiplier of default transaction volumes
                     affects numbers of transactions, we simulate a customer 
                     purchase habit such as 90% of sales from 10% of customers
        minimum_trans -- minimum number of transactions per customer

    """
    # Discard customer/product 0 
    cust = users.make_users(usern+1)[1:]
    prod = products.fetch_products()[1:]
    tran = transactions.transactions(cust, prod, multiplier=trans_multi, base=minimum_trans)[1:]
    
    cust.to_csv(join(basepath, 'cust.csv'), float_format='%.2f')
    prod.to_csv(join(basepath, 'prod.csv'), float_format='%.2f')
    tran.to_csv(join(basepath, 'tran.csv'), float_format='%.2f')

if __name__ == '__main__':
    parser = argparse.ArgumentParser("Generate datasets which are compatible " +
        "with Adobe Campaign Classic")
    parser.add_argument('basepath', type=str, 
            help='where csv files should be exported')
    parser.add_argument('user_number', type=int, metavar='user-number',
            help='total number of users')
    parser.add_argument('--transaction-multiplier', type=float, 
            help='multiplier for number of transactions', default=1.0)
    parser.add_argument('--min-transactions', type=int, default=1, 
            help='minumum number of transactions per customer')
    arg = parser.parse_args()
    generate_dataset(arg.basepath, arg.user_number,
            arg.transaction_multiplier, arg.min_transactions)
