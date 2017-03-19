import re
import plotly

plotly.tools.set_credentials_file(username='MaclighterX8', api_key='0AQhRtD0rdU0xrD2iqPJ')


def string_to_array(line):
    split = re.split("\s", line)  # split line on whitespaces
    split = filter(None, split)  # remove whitespaces
    return list(split)


# DATA HELPERS

# line filtering regex
float_re = "[+-]?([0-9]*[,])?[0-9]+"
line_re = " " + float_re + "\s+" + float_re + "\s+" + float_re + "\s+[0-9]+"
r = re.compile(line_re)


# data lines parsing
def parse_line(line):
    values_str = string_to_array(line)
    values = []
    for item in values_str:
        if item != values_str[-1]:  # convert every number (but last one) to float
            val = item.replace(",", ".")
            values.append(float(val))
        else:  # convert last number to int
            values.append(int(item))
    return values


# UNITS HELPERS

# regex parse
line_fu = "Fixed unit" + "[0-9]*" + "\s+"
fu = re.compile(line_fu)


# units lines parsing
def parse_unit_line(line):
    values_str = string_to_array(line)
    values = []
    for index, item in enumerate(values_str):
        if index == 2:  # convert unit number to int
            values.append(int(item))
        else:
            values.append(item)
    return values
