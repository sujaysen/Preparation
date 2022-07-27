from collections import Counter
from itertools import product
import json

#Assuming these are the list of user id's we got from json
counter = Counter(['sujay','user_1','user_1','user_1','user_1','user_2','user_2','user_2','user_3','user_3','user_4','sujay','sujay','sujay' ])


#Get top 3 using most_common
top_3 = counter.most_common(3)

for key, value in top_3:
    print('{}: {}'.format(key,value))
