import argparse
import sys

import pandas as pd
import os
import numpy as np

#- "--min-date": start of the date range. type:str, format:"YYYY-MM-DD", default:"2020-01-01"
#- "--max-date": end of the date range. type:str, format:"YYYY-MM-DD", default:"2020-06-30"
#- "--top": number of rows in the output. type:int, default:3

ap = argparse.ArgumentParser(description='Process some integers.')
ap.add_argument('--min', '--min-date', type=str, required=False,default="2020-01-01",
                    help='start of the date range. type:str, format:"YYYY-MM-DD"')
ap.add_argument('--max', '--max-date', type=str, required=False ,default="2020-06-30",
                    help='end of the date range. type:str, format:"YYYY-MM-DD"')
ap.add_argument('--t', '--top', type=int, required=False ,default="3",
                    help='number of rows in the output. type:int, default:3')
data = os.getcwd()+"\\data"

directory = os.fsencode(data)
dfs_dict = {}
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    key = filename.replace(".csv","")
    dfs_dict[key] = pd.read_csv(data+"\\"+filename)

product_table = dfs_dict['product']
sales_table = dfs_dict['sales']
store_table = dfs_dict['store']


args = vars(ap.parse_args())

sales_product = pd.merge(sales_table,product_table, left_on ='product', right_on ='id').drop('product', axis =1)
sales_store_product = pd.merge(sales_product,store_table, left_on='store', right_on='id').drop('store', axis = 1)
sales_store_product = sales_store_product.drop(['id_x','id_y'], axis = 1)

sales_store_product = sales_store_product.rename(columns={'name_x':'product'})
sales_store_product = sales_store_product.rename(columns={'name_y':'store'})
sales_store_product.head()

top_product = sales_store_product[(sales_store_product['date'] > args["min"]) & (sales_store_product['date'] < args["max"])]
top_product = top_product.groupby(by = ['product'])['quantity'].sum().sort_values(ascending = False) ## sum product sale
top_product.head()

top_store = sales_store_product[(sales_store_product['date'] > args["min"]) & (sales_store_product['date'] < args["max"])]
top_store = top_store.groupby(by = ['store'])['quantity'].sum().sort_values(ascending = False) ## sum store sale
top_store.head()

top_brand = sales_store_product[(sales_store_product['date'] > args["min"]) & (sales_store_product['date'] < args["max"])]
top_brand = top_brand.groupby(by = ['brand'])['quantity'].sum().sort_values(ascending = False) ## sum brand sale
top_brand.head()

top_city = sales_store_product[(sales_store_product['date'] > args["min"]) & (sales_store_product['date'] < args["max"])]
top_city = top_city.groupby(by = ['city'])['quantity'].sum().sort_values(ascending = False) ## sum city sale
top_city.head()


print("min date: {}".format(args["min"]))
print("max date: {}".format(args["max"]))
print("rows: {}".format(args["t"]))
print("-- top seller product -- \n" ,top_product.head(args["t"]))
print("-- top seller store -- \n" ,top_store.head(args["t"]))
print("-- top seller brand -- \n" ,top_brand.head(args["t"]))
print("-- top seller city -- \n" ,top_city.head(args["t"]))


