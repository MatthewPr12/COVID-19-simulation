from society import Society

data = dict()
data["young"] = 1
data["old"] = 0.75
data["female"] = 1
data["male"] = 0.8

data["T1"] = 10
data["T2"] = 4
data["T3"] = 4
data["T4"] = 7

data["u"] = 0.2
data["k"] = 0.33
data['init_infected'] = 0.001


soc = Society(1000, 1000, 1, data)
