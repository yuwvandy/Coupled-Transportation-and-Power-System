""" SAMPLE
In this file you can find sample data which could be used
into the TrafficFlowMod class in model.py file
"""

# Graph represented by directed dictionary
# In order: first ("5", "7"), second ("5", "9"), third ("6", "7")...
graph = [
    ("1", ["2", "12"]),
    ("2", ["1", "3", "11"]),
    ("3", ["2", "4", "10"]),
    ("4", ["3", "5"]),
    ("5", ["4", "6", "8"]),
    ("6", ["5", "7"]),
    ("7", ["6", "8", "13"]),
    ("8", ["9", "7"]),
    ("9", ["4", "10", "8"]),
    ("10", ["3", "11", "9", "14"]),
    ("11", ["2", "12", "10", "15"]),
    ("12", ["1", "11", "16"]),
    ("13", ["7", "14"]),
    ("14", ["10", "15", "13"]),
    ("15", ["11", "16", "14"]),
    ("16", ["12", "15"]),
]

# Capacity of each link (Conjugated to Graph with order)
# Here all the 19 links have the same capacity
capacity = [3600]*12 + [1800]*2 + [5400]*2 + [3600]*4 + [1800]*10 + [3600]*2 + [1800]*2 \
            + [5400]*2 + [3600]*2 + [1800]*6

# Free travel time of each link (Conjugated to Graph with order)
free_time = [48.28]*10 + [56.33]*2 + [48.28]*2 + [56.33]*2 + [48.28]*2 + [56.33]*2 \
            + [48.28]*10 + [56.33]*2 + [48.28]*2 + [56.33]*4 + [48.28]*6

# Origin-destination pairs
origins = ["1", "13", "6", "16"]
destinations = ["13", "1", "16", "6"]
# Generated ordered OD pairs: 
# first ("5", "15"), second ("5", "17"), third ("6", "15")...


# Demand between each OD pair (Conjugated to the Cartesian 
# product of Origins and destinations with order)
demand = [3000, 2000, 1200, 600]
