import pandas as pd
import csv
import plotly.express as px

with open("datas.csv") as f:
    df = csv.DictReader(f)
    fig = px.scatter(df, x="Coffee in ml", y="sleep in hours")
    fig.show()
