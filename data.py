import pandas as pd

def get_data(): 
    # Read Excel file
    df_1 = pd.read_excel('data/schule_ohne_rassismus_2006_bis_2023.xlsx')

    # Compose the column FullAddress
    df_1['FullAddress'] = df_1['Adresse'].astype(str) + ' ' + df_1['Berlin'].astype(str) + ' Berlin' 

    # Read CSV file with lat and long
    df_2 = pd.read_csv('schule_ohne_rassismus_adresse.csv')

    # Merge dataframes on 'FullAddress'
    df_3 = pd.merge(df_1, df_2, on="FullAddress")

    # Drop rows with NaN values
    df_3.dropna(inplace=True)

    return df_3
