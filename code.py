import csv
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics 

df=pd.read_csv("height-weight.csv")

heightList=df["Height(Inches)"].to_list()

mean=statistics.mean(heightList)
median=statistics.median(heightList)
mode=statistics.mode(heightList)
standarddeviation=statistics.stdev(heightList)

first_Standard_deviation_start,first_Standard_deviation_end=mean-standarddeviation,mean+standarddeviation
second_Standard_deviation_start,second_Standard_deviation_end=mean-(2*standarddeviation),mean+(2*standarddeviation)
third_Standard_deviation_start,third_Standard_deviation_end=mean-(3*standarddeviation),mean+(3*standarddeviation)

list_of_data_within_firstStandard_deviation=[result for result in heightList if result>first_Standard_deviation_start and result<first_Standard_deviation_end]
list_of_data_within_secondStandard_deviation=[result for result in heightList if result>second_Standard_deviation_start and result<second_Standard_deviation_end]
list_of_data_within_thirdStandard_deviation=[result for result in heightList if result>third_Standard_deviation_start and result<third_Standard_deviation_end]

# print("{}% of data lies in first standard deviation ".format(len(list_of_data_within_firstStandard_deviation)*100.0/len(heightList)))
# print("{}% of data lies in second standard deviation ".format(len(list_of_data_within_secondStandard_deviation)*100.0/len(heightList)))
# print("{}% of data lies in third standard deviation ".format(len(list_of_data_within_thirdStandard_deviation)*100.0/len(heightList)))

# print("mean,mode,median of height{},{},{}".format(mean,mode,median))

fig=ff.create_distplot([heightList],["height graph"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.16],mode="lines",name="mean"))

fig.add_trace(go.Scatter(x=[first_Standard_deviation_start,first_Standard_deviation_start],y=[0,0.16],mode="lines",name="firstStandarddeviation"))
fig.add_trace(go.Scatter(x=[second_Standard_deviation_start,second_Standard_deviation_start],y=[0,0.16],mode="lines",name="secondStandarddeviation"))
fig.add_trace(go.Scatter(x=[third_Standard_deviation_start,third_Standard_deviation_start],y=[0,0.16],mode="lines",name="thirdStandarddeviation"))

fig.add_trace(go.Scatter(x=[first_Standard_deviation_end,first_Standard_deviation_end],y=[0,0.16],mode="lines",name="firstStandarddeviation"))
fig.add_trace(go.Scatter(x=[second_Standard_deviation_end,second_Standard_deviation_end],y=[0,0.16],mode="lines",name="secondStandarddeviation"))
fig.add_trace(go.Scatter(x=[third_Standard_deviation_end,third_Standard_deviation_end],y=[0,0.16],mode="lines",name="thirdStandarddeviation"))

fig.show()


