import sys
import pandas as pd

def main(args):
    # lee el csv
    db = pd.read_csv('raw_data.csv')

    # elimina columnas innecesarias
    filtered_db = db.drop(columns=['ZIP CODE', 
                            'LOCATION',
                            'ON STREET NAME',
                            'CROSS STREET NAME',
                            'OFF STREET NAME',
                            'VEHICLE TYPE CODE 1',
                            'VEHICLE TYPE CODE 2',
                            'VEHICLE TYPE CODE 3',
                            'VEHICLE TYPE CODE 4',
                            'VEHICLE TYPE CODE 5'])

    # comprueba si hay IDs repetidos
    if(filtered_db['COLLISION_ID'].duplicated()[::-1].idxmax() != 29704):
         print("There are repeated values")

    # valores de BOROUGH (barrios)
    print(filtered_db.groupby(['BOROUGH']).count())

    # máximo y mínimo de heridos
    print("Max injured: {} ".format(filtered_db['NUMBER OF PERSONS INJURED'].max()))
    print("Min injured: {} ".format(filtered_db['NUMBER OF PERSONS INJURED'].min()))

    # máximo y mínimo de muertos
    print("Max killed: {} ".format(filtered_db['NUMBER OF PERSONS KILLED'].max()))
    print("Min killed: {} ".format(filtered_db['NUMBER OF PERSONS KILLED'].min()))

    # valores de CONTRIBUTING FACTOR
    print(filtered_db.groupby(['CONTRIBUTING FACTOR VEHICLE 1']).count())
    print(filtered_db.groupby(['CONTRIBUTING FACTOR VEHICLE 2']).count())
    print(filtered_db.groupby(['CONTRIBUTING FACTOR VEHICLE 3']).count())
    print(filtered_db.groupby(['CONTRIBUTING FACTOR VEHICLE 4']).count())
    print(filtered_db.groupby(['CONTRIBUTING FACTOR VEHICLE 5']).count())

    # print(filtered_db.count())
    # print(db.dtypes)
    # print(db.keys())
    # print(db.index)
    # print(db.size)
    
    #filtered_db.to_csv("cleaned_data.csv")

    return 0

if __name__=="__main__":
    print("Starting preprocessing")
    main(sys.argv)
