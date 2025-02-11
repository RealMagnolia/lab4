import json 

with open("sample.json", "r") as file:
    data = json.load(file)

print("Interface status")
print("=" * 77)
print("DN", " " * 40, "Description ", "Speed", " " * 10, "MTU")
print("-" * 42, "-" * 13, "-" * 8, "\t", "-" * 4)
for imdata in data["imdata"]:
    for i in imdata:
        for j in imdata[i]: # every imdata[i] is dictionary
            print(imdata[i][j]["dn"],"\t", "\t"  , imdata[i][j]["speed"] ,"\t" , imdata[i][j]["mtu"])
