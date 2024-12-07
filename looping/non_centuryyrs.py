

#print all non century years from 1800 to 2024

for year in range(1800,2025,1):
    if year%100!=0:
        print(year)