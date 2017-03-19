import fileinput
import helpers
import plotly.plotly as py
import plotly.graph_objs as go

path = 'CMO_Lab_02_Best_Units_'

file = input("File? ")

labels = [0]

# get simulation units numbers
for line in fileinput.input(file):
    if helpers.fu.match(line) is not None:
        fixed_unit = helpers.parse_unit_line(line)[2]

        if fixed_unit not in labels:
            labels.append(fixed_unit)

labels.sort()


# count best units
total = 0
counters = [0] * len(labels)

for line in fileinput.input(file):

    if helpers.r.match(line) is not None:
        total += 1

        location = helpers.parse_line(line)
        best_unit = location[3]

        counters[labels.index(best_unit)] += 1

for index, item in enumerate(counters):
    print("{} : {}".format(labels[index], item))

print("total : {}".format(total))


data = [go.Bar(
    x=labels,
    y=counters
)]

py.iplot(data, filename=path+fileinput.filename())