import pandas as pd
import plotly_express as px

df=pd.read_csv("cups of coffee vs hours of sleep.csv")
fig=px.scatter(df,x="Coffee in ml",y="sleep in hours",color="week",title="coffee vs sleep")
fig.show()