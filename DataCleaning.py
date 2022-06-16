import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

df = pd.read_csv('assignment_seven.csv')

description = df.describe(include='all')

processedDataFrame = df[['transaction_id','transaction_date','record_id','products']]

processedDataFrame.replace('', np.nan, inplace=True)

processedDataFrame.dropna(inplace=True)

pdfdescription = processedDataFrame.describe(include='all')

# print(pdfdescription,'\n\n')

# dup_check_record_id = processedDataFrame.pivot_table(index='transaction_id', aggfunc='size')
# dup_check_record_id = dup_check_record_id.sort_values(ascending=False)
# print(dup_check_record_id)

itemPopularity = processedDataFrame.pivot_table(index='products', aggfunc='size')
itemPopularity = itemPopularity.sort_values(ascending=False)
itemPopularity = itemPopularity.head()

print(itemPopularity)

def create_csv():
    while True:
        print('Do you want to make a csv? \n')
        check = input('Y/N?  ')
        check.lower()
        if check == 'y' or 'yes':
            processedDataFrame.to_csv('output.csv',index=False)
            break
        elif check == 'n' or 'no':
            break
        else:
            print('Please answer yes or no \n')
    
create_csv()

itemPopularity.plot(kind='bar')
plt.show()
