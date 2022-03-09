import sys
import pandas as pd

def main(args):
    # lee el csv
    db = pd.read_csv('Iznardo_raw_data.csv')

    print(db.head(10))
    #print(db.dtypes)
    #print(db.keys())
    # print(db.index)
    # print(db.size)
    

    return 0

if __name__=="__main__":
    print("Starting preprocessing")
    main(sys.argv)
