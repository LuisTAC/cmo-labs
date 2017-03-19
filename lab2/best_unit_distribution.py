import fileinput
import helpers
import plotly.plotly as py
import plotly.graph_objs as go

path = 'CMO_Lab_02_Best_Units_'

file = input("File? ")

units = [(0, 'Indefinido')]

# get simulation units numbers
for line in fileinput.input(file):
    if helpers.fu.match(line) is not None:
        unit_line = helpers.parse_unit_line(line)
        fixed_unit = (unit_line[2], unit_line[3])

        if fixed_unit not in units:
            units.append(fixed_unit)

units.sort(key=lambda tup: tup[0])


# count best units
total = 0
counters = [0] * len(units)

for line in fileinput.input(file):

    if helpers.r.match(line) is not None:
        total += 1

        location = helpers.parse_line(line)
        best_unit = location[3]

        counters[helpers.get_index(units, 0, best_unit)] += 1

labels = []
for index, item in enumerate(units):
    label = str(item[0]) + " - " + str(item[1])
    labels.append(label)

for index, item in enumerate(counters):
    print("{} : {}".format(labels[index], item))

print("total : {}".format(total))

data = [go.Bar(
    x=labels,
    y=counters
)]

py.iplot(data, filename=path+fileinput.filename())