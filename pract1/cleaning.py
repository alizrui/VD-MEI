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

    # maximo de heridos
    print(filtered_db['NUMBER OF PERSONS INJURED'].max())

    # maximo de muertos
    print(filtered_db['NUMBER OF PERSONS KILLED'].max())

    # print(filtered_db.count())


    #print(db.dtypes)
    #print(db.keys())
    # print(db.index)
    # print(db.size)
    
    # filtered_db.to_csv("cleaned_data.csv")



    return 0

if __name__=="__main__":
    print("Starting preprocessing")
    main(sys.argv)
