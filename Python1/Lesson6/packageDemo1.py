import pandas as pd
#创建Dataframe
data = {"Name": ["Alice", "Bob", "Katy", "Sam"],
        "Age" : [12, 11, 10, 12],
        "Gender" : ["Female", "Male", "Female", "Male"],
        "Score" : [1, 2, 3, 4]}
df = pd.DataFrame(data)
print(df)