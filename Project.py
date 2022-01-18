import statistics
import plotly.graph_objects as go
import plotly.figure_factory as ff
import pandas as pd
import random

df = pd.read_csv("ProjectData.csv")
dataList = df["reading_time"].tolist()

populationMean = statistics.mean(dataList)
print("Population Mean:", populationMean)


def random_mean(counter):
    dataSet = []

    for i in range(0,counter):
        randomIndex = random.randint(0, len(dataList))
        value = dataList[randomIndex]
        dataSet.append(value)

    randomMean = statistics.mean(dataSet)
    return randomMean


def fig_show(meanList):
    figData = meanList
    fig = ff.create_distplot([figData], ["Reading Time"], show_hist = False)

    samplingMean = statistics.mean(meanList)
    sd = statistics.stdev(meanList)
    
    sd1_str, sd1_end = samplingMean - sd, samplingMean + sd
    sd2_str, sd2_end = samplingMean - (2*sd), samplingMean + (2*sd)
    sd3_str, sd3_end = samplingMean - (3*sd), samplingMean + (3*sd)
    
    print("\nStandard Deviation 1:", sd1_str, ",", sd1_end)
    print("Standard Deviation 2:", sd2_str, ",", sd2_end)
    print("Standard Deviation 3:", sd3_str, ",", sd3_end)

    fig.add_trace(go.Scatter(x = [sd1_str, sd1_end], y = [0, 0.17], mode = "lines", name = "Standard Deviation 1 start"))
    fig.add_trace(go.Scatter(x = [sd1_str, sd1_end], y = [0, 0.17], mode = "lines", name = "Standard Deviation 1 end"))
    fig.add_trace(go.Scatter(x = [sd2_str, sd2_end], y = [0, 0.17], mode = "lines", name = "Standard Deviation 2 start"))
    fig.add_trace(go.Scatter(x = [sd2_str, sd2_end], y = [0, 0.17], mode = "lines", name = "Standard Deviation 2 end"))
    fig.add_trace(go.Scatter(x = [sd3_str, sd3_end], y = [0,0.17], mode = "lines", name = "Standard Deviation 3 start"))
    fig.add_trace(go.Scatter(x = [sd3_str, sd3_end], y = [0,0.17], mode = "lines", name = "Standard Deviation 3 end"))


    fig.add_trace(go.Scatter(x = [samplingMean, samplingMean], y = [0,0.8]))
    sampleMean = statistics.mean(dataList)
    fig.add_trace(go.Scatter(x = [sampleMean, sampleMean], y = [0,0.8]))
    
    z_score = (sampleMean - samplingMean)/sd
    print("\nZ Score:",z_score)

    fig.show()

meanList = []

for i in range(0, 100):
    meanSet = random_mean(30)
    meanList.append(meanSet)

fig_show(meanList)
