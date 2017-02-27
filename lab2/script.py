import fileinput
import re
import plotly
import plotly.plotly as py
import plotly.graph_objs as go

import numpy as np

plotly.tools.set_credentials_file(username='MaclighterX8', api_key='0AQhRtD0rdU0xrD2iqPJ')


def parse_line(line):
    split = re.split("\s", line) # split line on whitespaces
    split = filter(None, split)# remove whitespaces
    values_str = list(split)
    values = []
    for item in values_str:
        if item!=values_str[-1]: # convert every number (but last one) to float
            val = item.replace(",",".")
            values.append(float(val))
        else:  # convert last number to int
            values.append(int(item))
    return values

#main

# line filtering regex
float_re= "[+-]?([0-9]*[,])?[0-9]+"
line_re = " " + float_re + "\s+" + float_re + "\s+" + float_re + "\s+[0-9]+"
r= re.compile(line_re)


total=0
counters = [0]*8
# <0 <10 <20 <30 <40 <50 <60 ...
#  0  1   2   3   4   5   6  7

for line in fileinput.input(input("File?")):
    if r.match(line) is not None :
        total += 1
        
        values=parse_line(line)
        value = values[2]
        if value < 0 :
            counters[0]+=1
        elif value < 10 :
            counters[1]+=1
        elif value < 20 :
            counters[2]+=1
        elif value < 30 :
            counters[3]+=1
        elif value < 40 :
            counters[4]+=1
        elif value < 50 :
            counters[5]+=1
        elif value < 60 :
            counters[6]+=1
        else:
            counters[7]+=1

for index, item in enumerate(counters):
    print("<{} : {}".format(index*10,item))

print("total : {}".format(total))


data = [go.Bar(
            x=['<0', '<10', '<20', '<30', '<40', '<50', '<60', '<70'],
            y=counters
    )]

py.iplot(data, filename='CMO Lab2 - ' + fileinput.filename())