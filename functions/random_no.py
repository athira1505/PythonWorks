# create a fn random_num(start,end,step)

# print numbers from start to end
# random_num(1,7,2)   :   #1,3,5
# dont use for loop


def random_num(start,end,step):

    while(start<=end):

        print(start)

        start=start+step

random_num(10,100,2)