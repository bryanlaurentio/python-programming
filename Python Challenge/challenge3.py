import re;
import numpy as np
import pandas as pd
data = open('C:\\Users\\user\\Desktop\\Python Challenge\\challenge3.txt').read()

list_data = list(data)
#print(list(data))

#for i in range(len(list_data)):
#    if list_data[i].isupper():
#        list_data[i] = '1'; #capital nomor 1
#    else:
#        list_data[i] = '0'; #non capital nomor 0

#print(list_data)

result = re.findall("[A-Z]{3}[a-z][A-Z]{3}", data)
last_result = ''
for i in range(len(result)):
    last_result = result[i][3]

#print(result)
#last_result = re.findall('[^A-Z]', result)
last_result = pd.Series(last_result)
count = last_result.value_counts()
print(count)
