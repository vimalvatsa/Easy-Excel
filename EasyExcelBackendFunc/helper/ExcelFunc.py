# creating a function that converts csv file to excel
import pandas as pd
import json

# Defining a fuction that takes csv file as input and converts it to excel


# def convert_to_excel(csv_file, name: str):
#     df = pd.read_csv(csv_file)
#     df.to_excel(name+'.xlsx', index=False)
#     return


def convert_to_excel(json_file, name: str):
    with open(json_file, 'r') as file:
        data = json.load(file)
    df = pd.DataFrame(data)
    df.to_excel(name + '.xlsx', index=False)
    return
