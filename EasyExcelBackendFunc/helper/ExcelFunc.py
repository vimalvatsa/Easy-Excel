# creating a function that converts csv file to excel 
import pandas as pd


# Defining a fuction that takes csv file as input and converts it to excel

def convert_to_excel(csv_file, name:str):
    df = pd.read_csv(csv_file)
    df.to_excel(name+'.xlsx', index=False)
    return 