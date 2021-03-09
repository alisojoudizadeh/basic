from datetime import datetime
import random
import time

odds=[1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,47,49,51,53,55,57,59]

for i in range(10):
    rdn=random.randrange(0,5)
    right_this_min=datetime.today().minute
    if right_this_min in odds:
        print("the min is {} => odd min".format(right_this_min))
    else:
        print("the min is {} => not odd min".format(right_this_min))
    print(rdn)
    time.sleep(rdn)