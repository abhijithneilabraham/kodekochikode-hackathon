import csv
data = "hs.csv"
with open(data, 'r') as file:
    reader = csv.reader(file)
    hospital_list = list(reader)
for a in hospital_list:
    print("Name :",a[3],"\nAddress :",a[2])
    if a[1][0]=='N':
        print("\n")
        continue
    for i in range(0,15):
        if a[1][i]==',':
            break
    print("Latitude :",a[1][0:i])
    print("Longitude :",a[1][i+1:18])
    print("\n")
