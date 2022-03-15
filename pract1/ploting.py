import sys
import pandas as pd
import altair as alt

def main(args):
    data = pd.DataFrame({'x': ['A','B','C','D','E'],
                         'y': [5,3,6,7,2]})
    chart = alt.Chart(data).mark_bar().encode(
        x='x',
        y='y'
    ).properties(title = "Lolazo")


    chart.save("grafico.png")


    return 0

if __name__=="__main__":
    print("Starting ploting")
    main(sys.argv)

