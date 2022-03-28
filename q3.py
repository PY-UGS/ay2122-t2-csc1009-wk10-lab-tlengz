from statistics import mode


switch = {
    "CSC1006":"Maths 2",
    "CSC1007":"Operating system",
    "CSC1008":"Data structure and algo",
    "CSC1009":"Object oriented programming",
    "CSC1010":"Computer network",
}
module = "CSC1009"
print(switch.get(module))

for i in range(101, 66, -2):
    print(i)