import pandas as pd
import csv
import plotly.express as px
import numpy as np


def getDataSources(data_path):
    Coffee = []
    Sleep = []
    with open(data_path) as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            Coffee.append(float(row["Coffee in ml"]))
            Sleep.append(float(row["sleep in hours"]))
    return {"x": Coffee, "y": Sleep}


def findCoralation(data_source):
    correlation = np.corrcoef(data_source["x"], data_source["y"])
    print("correlation between x and y = ", correlation[0, 1])


def setup():
    data_path = "datas.csv"
    data_source = getDataSources(data_path)
    findCoralation(data_source)


setup()
