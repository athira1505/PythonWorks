


users=["rahul","rohit","kohli","sanju","pandya","siraj"]

rahul_followers=["rohit","kohli","rishab","rahul"]

sanju_followers=["sanju","rohit","kohli"]



# follow-suggestions  ["sanju","pandya","siraj"]
rahul_followers_suggestion=set(users).difference(set(rahul_followers))
print(rahul_followers_suggestion)


# mutual_frnds sanju and rahul followers
mutual_frnds=set(rahul_followers).intersection(set(sanju_followers))
print(mutual_frnds)
