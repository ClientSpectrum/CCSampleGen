from faker import Faker
import pandas as pd
from collections import OrderedDict
fake = Faker()
rand = fake.random

def make_users(n):
    """
    Make n users for ACC
    """
    return pd.DataFrame([make_user() for _ in range(n)])

def make_user(extradomains=False):
    """
    Make a single user dictionary
    emails should be non routable, you can include
    .example tld examples via extradomains flags
    Keyword Args:
        extradomains -- set True if you want lots of example tld domains
    """
    add = fake.street_address().split(" ")
    address3 = " ".join(add[:3])
    app = None
    if len(add) >= 5:
        app = " ".join(add[3:5])

    first_name = fake.first_name()
    last_name = fake.last_name()
    tld = fake.random_element(["com", "org"])
    if extradomains:
        domain = fake.domain_name().split(".")[0] + '.example'
        email = f'{first_name.lower()}.{last_name.lower()}@{domain}'
    else:
        email = f'{first_name.lower()}.{last_name.lower()}@example.{tld}'

    return {
            "firstName": fake.first_name(),
            "lastName": fake.last_name(),
            "middleName": _rnull(fake.first_name, 0.6),
            "gender": _rnull(lambda: fake.random_int(1, 2), 0.3),
            "account": _acc_num(),
            "email": email,
            "company": _rnull(fake.company, 0.4),
            "fax": _rnull(_fnumber, 0.2),
            "language": fake.random_element(OrderedDict([
                ("EN", 0.8), ("FR", 0.2)])),
            "mobilePhone": _rnull(_fnumber, 0.5),
            "phone": _rnull(_fnumber, 0.8),
            "title": fake.random_element(OrderedDict([
                ("Mr", 0.4),
                ("Mrs", 0.05),
                ("Ms", 0.3),
                ("Miss", 0.05),
                ("Mx", 0.1),
                ("Dr", 0.1)])),
            "zipCode": fake.zipcode(),
            "stateCode": fake.state_abbr(),
            "countryCode": "US",
            "city": fake.city(),
            "address3": address3,
            "address1": app
            }

def _rnull(func, prob):
    """
    Masks data from the database
    """
    if rand.random() > prob:
        return None
    return func()


_acc_nums = set()
def _acc_num():
    v = None
    while v is None or v in _acc_nums:
        v = fake.random_number(12, True)
    _acc_nums.add(v)
    return v

def _fnumber():
    return fake.numerify("%%%-###-####")
                


