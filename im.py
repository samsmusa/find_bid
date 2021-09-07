import pandas as pd
import django


import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'find_bid.settings')

django.setup()

from user_login.models import Bids

tmp_data=pd.read_csv('bid11.csv',sep=',')
#ensure fields are named~ID,Product_ID,Name,Ratio,Description
#concatenate name and Product_id to make a new field a la Dr.Dee's answer
products = [
    Bids(
        title = tmp_data.iloc[row]['name'], 
        state = tmp_data.iloc[row]['region'],
        published = tmp_data.iloc[row]['Published'],
        end = tmp_data.iloc[row]['End'],

    )
    for row in tmp_data['ID']
]
print(products)
Bids.objects.bulk_create(products)