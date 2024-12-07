
# calculate order_summary

orders=["tea","coffee","tea","coffee","gheeroast","plainroast","porotta","tea"]

item_count={}

for item in orders:

    if item in item_count:
        item_count[item]+=1

    else:
       
        item_count[item]=1
