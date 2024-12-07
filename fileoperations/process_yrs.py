

year_path="C:\\Users\\Athira\\OneDrive\\Desktop\\pythonworks\\dataset\\years.txt"
century_path="C:\\Users\\Athira\\OneDrive\\Desktop\\pythonworks\\dataset\\century_yr.txt"
leap_yr_path="C:\\Users\\Athira\\OneDrive\\Desktop\\pythonworks\\dataset\\leap_yr.txt"

f_read=open(year_path,"r")
f_century=open(century_path,"w")
f_leap=open(leap_yr_path,"w")

def is_century_yr(year):
    return True if year%100==0 else False

def is_leap_yr(year):
    if (year%100==0 and year%400==0) or (year%4==0 and year%100!=0):
        return True
    else:
        return False
    
for year in f_read:
    year=int(year)

    if is_century_yr(year):
        f_century.write(str(year)+"\n")

    elif is_leap_yr(year):
        f_leap.write(str(year)+"\n")

f_read.close()
f_century.close()
f_leap.close()