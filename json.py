print("am a citizen fun")
hands = [['J', 'Q', 'K'],
          ['2', '2', '2'],
            ['6', 'A', 'K'],
            ]
print(hands)


#converts into json strings
#dumps with the json
# import json 
# x = {
#     "kimondiu":"muhia",
#     "moses": "waweru",
#     "mutua":"musyoki"

# }
# print(json.dumps(x))
# y= js.dumps(x)
# print(js.dumps(y))

#data cleaning 
import pandas as pd

df = pd.read_csv('C:/Users/User/Desktop/Assa/dataset.csv')

x = df["Previous qualification"].median()

df["Previous qualification"].fillna(x, inplace = True)



#trying pandas in person

import pandas as pd

df = pd.read_csv('C:/Users/User/Desktop/Assa/dataset.csv')
print(df)


