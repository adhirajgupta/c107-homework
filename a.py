import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import csv


df = pd.read_csv("students.csv")
mean = df.groupby("level")["attempt"].mean()
print(mean)

fig = px.scatter(mean,y = "attempt",size_max = 60)
fig.show()
