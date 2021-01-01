import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import csv


df = pd.read_csv("students.csv")
student_df = df.loc[df["student_id"] == "TRL_987"]
print(student_df)

print(student_df.groupby("level")["attempt"].mean())

fig = px.scatter( x=df.groupby("level")["attempt"].mean(), y=["Level 1", "Level 2", "Level 3", "Level 4"],size_max = 60)


fig.show()
