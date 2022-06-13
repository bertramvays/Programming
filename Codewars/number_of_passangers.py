"""
Return number of people who are still in the bus after the last bus station
(after the last array)
"""


def number(bus_stops):
    quantity_in, quantity_out = 0, 0  # determine first value of variables
    for passangers in bus_stops:  # iterrating the list of bus stops
        quantity_in += passangers[0]  # sum of in-passangers
        quantity_out += passangers[1]  # sum of out-passangers
    return quantity_in - quantity_out

