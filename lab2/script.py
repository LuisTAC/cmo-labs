import fileinput
import re
import plotly
import plotly.plotly as py
import plotly.graph_objs as go

path = 'CMO_Lab_02_'

plotly.tools.set_credentials_file(username='MaclighterX8', api_key='0AQhRtD0rdU0xrD2iqPJ')


def parse_line(line):
    split = re.split("\s", line)  # split line on whitespaces
    split = filter(None, split)  # remove whitespaces
    values_str = list(split)
    values = []
    for item in values_str:
        if item != values_str[-1]:  # convert every number (but last one) to float
            val = item.replace(",", ".")
            values.append(float(val))
        else:  # convert last number to int
            values.append(int(item))
    return values


# main

# line filtering regex
float_re = "[+-]?([0-9]*[,])?[0-9]+"
line_re = " " + float_re + "\s+" + float_re + "\s+" + float_re + "\s+[0-9]+"
r = re.compile(line_re)

total = 0
counters = [0] * 8
# ]..., -120[, [-120, -110[ [-110, -100[... [-70, -60[ [60, ...[
#  0  1   2   3   4   5   6   7

for line in fileinput.input(input("File?")):
    if r.match(line) is not None:
        total += 1

        values = parse_line(line)
        value = values[2]
        value = value - 120
        if -120 > value:
            counters[0] += 1
        elif -120 <= value < -110:
            counters[1] += 1
        elif -110 <= value < -100:
            counters[2] += 1
        elif -100 <= value < -90:
            counters[3] += 1
        elif -90 <= value < -80:
            counters[4] += 1
        elif -80 <= value < -70:
            counters[5] += 1
        elif -70 <= value < -60:
            counters[6] += 1
        else:
            counters[7] += 1

for index, item in enumerate(counters):
    print("<{} : {}".format(index * 10, item))

print("total : {}".format(total))

data = [go.Bar(
    x=['] *, -120[', '[-120, -110[', '[-110, -100[', '[-100, -90[', '[-90, -80[', '[-80, -70[', '[-70, -60[', '[-60, *['],
    y=counters
)]

py.iplot(data, filename=path+fileinput.filename())