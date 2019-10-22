from faker import Faker
import pandas as pd
import numpy as np
from collections import OrderedDict
fake = Faker()
rand = fake.random

def transactions(users, products, multiplier=1.0, base=0):
    """
    Generate transactions for users with products returning a 
    pandas DataFrame with transactions
    Keyword args:
        users -- user pandas dataframe
        products -- products for customers to purchase
        multiplier -- factor of products that each customer will buy
        base -- minumum number of products a customer will buy if they
                exist in the dataset


    """
    nusers = len(users)
    distoverusers = (np.clip(
            np.random.exponential(10, nusers+1) - 5, 0, 10000000)*multiplier).round().astype(np.int32)

    # Few customers make the majority of the purchases
    trans = []
    for i, user in (users.iterrows()):
        # User probably frequents 3 stores or less
        for n in range(distoverusers[i]):
            item = rand.randint(products.index.start, products.index.stop-1)
            itemv = products.loc[item]
            stores = [fake.random_number(3, True) for _ in range(3)]
            price = itemv['basePrice']*(1-_getpurchasediscount(1)[0])
            transaction = {
                    'price': price,
                    'customer': i,
                    'product': item,
                    'datetime': _random_trans_time(),
                    'points': int(price * rand.random() * 0.5),
                    'store': fake.random_element(stores)
            }
            trans.append(transaction)

    res = pd.DataFrame(trans)
    res['price'] = res['price'].round(2)
    return res

def _getpurchasediscount(n):
    """
    Return a discount for a product that favours low discounts but
    sometimes produces discounts up to 50% of the total price
    """
    return np.clip(np.random.exponential(0.5, n) - 1, 0, 0.5)

def _random_trans_time():
    """
    Imposes a distribution over the dates of the year favouring the 10th month
    """
    base = fake.date_time_between('-5y')
    while True:
        try:
            new = base.replace(hour=int(np.clip(rand.gauss(18, 8), 9, 23)),
                    month=int(1 + (fake.random.gauss(10, 8) % 12)))
            return new
        except ValueError:
            pass

    

