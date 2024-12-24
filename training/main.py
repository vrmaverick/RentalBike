if __name__ == '__main__' :
    
    import tensorflow as tf
    import matplotlib.pyplot as plt
    import pandas as pd
    import numpy as np
    from train import model

    df = pd.read_csv("https://raw.githubusercontent.com/vrmaverick/RentalBike/main/datasets/BikeData.csv")
    print(df.describe)
    print(df.isna().sum())
    df_one_hot = pd.get_dummies(df,dtype=int) # Else it will give bool by defualt
    print(df_one_hot.head())

    X = df_one_hot.drop('Rented_Bike_Count',axis = 1)
    y = df_one_hot['Rented_Bike_Count']

    model(X,y)
