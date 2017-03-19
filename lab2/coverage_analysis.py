import fileinput
import plotly.plotly as py
import plotly.graph_objs as go
import helpers

path = 'CMO_Lab_02_'

total = 0
counters = [0] * 8
# ]..., -120[, [-120, -110[ [-110, -100[... [-70, -60[ [60, ...[
#  0  1   2   3   4   5   6   7

for line in fileinput.input(input("File?")):
    if helpers.r.match(line) is not None:
        total += 1

        location = helpers.parse_line(line)
        coverage = location[2]
        coverage = coverage - 120
        if -120 > coverage:
            counters[0] += 1
        elif -120 <= coverage < -110:
            counters[1] += 1
        elif -110 <= coverage < -100:
            counters[2] += 1
        elif -100 <= coverage < -90:
            counters[3] += 1
        elif -90 <= coverage < -80:
            counters[4] += 1
        elif -80 <= coverage < -70:
            counters[5] += 1
        elif -70 <= coverage < -60:
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