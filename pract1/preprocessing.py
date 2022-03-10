import sys
import pandas as pd

def main(args):
    
    # lee el csv
    db = pd.read_csv(args[1])

    # convierte CRASH DATE object a formato pandas datetime
    db['CRASH DATE'] = pd.to_datetime(db['CRASH DATE'])

    # filtra los meses de abril de 2019, 2020 y 2021
    filtered_db = db.loc[(db['CRASH DATE'].dt.year >= 2019)
                         & (db['CRASH DATE'].dt.month == 4)]

    # ordena por dia y mes (useless)
    # filtered_db.sort_values(by='CRASH DATE', inplace=True)

    # print(db.dtypes)
    # print(db.keys())
    # print(db.index)
    # print(db.size)
    

    filtered_db.to_csv("raw_data.csv")
    return 0

if __name__=="__main__":
    print("Starting preprocessing")
    main(sys.argv)
