import pandas as pd

PRODUCT_FILE = "data/DatafinitiElectronicsProductsPricingData.csv"

def fetch_products():
    """
    fetch_products gets the list of electronics products from a list
    and formats them in a useful way and returns them as a pandas DataFrame
        
    """
    df = pd.read_csv(PRODUCT_FILE)
    df = df[['prices.amountMax', 'brand', 'categories', 'manufacturer', 'name']].dropna()
    df.rename({'prices.amountMax': 'basePrice'}, axis=1, inplace=True)
    df = df.drop_duplicates('name')
    
    cats = df['categories'].unique()
    popcats = {}
    for cat in cats:
        s = cat.split(",")
        for v in s:
            if v in popcats:
                popcats[v] += 1
            else:
                popcats[v] = 0
    popcats = list(popcats.items())
    popcats.sort(key=lambda x: x[1], reverse=True)
    popcats = popcats[5:50]
    popcats = [x for (x, _) in popcats]

    def _mostlikelycat(row):
        splitcats = row['categories'].split(",")
        for cat in popcats:
            if cat in splitcats:
                return cat
        return None
            

    newcat = df.apply(_mostlikelycat, axis=1)
    df['categories'] = newcat
    return df.reset_index(drop=True)



