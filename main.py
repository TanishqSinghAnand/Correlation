import pandas as pd
import csv
import plotly.express as px
import numpy as np


def getDataSources(data_path):
    Students = []
    Days = []
    with open(data_path) as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            Students.append(float(row["Marks In Percentage"]))
            Days.append(float(row["Days Present"]))
    return {"x": Students, "y": Days}


def findCoralation(data_source):
    correlation = np.corrcoef(data_source["x"], data_source["y"])
    print("correlation between x and y = ", correlation[0, 1])


def setup():
    data_path = "data.csv"
    data_source = getDataSources(data_path)
    findCoralation(data_source)


setup()
