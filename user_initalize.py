import os
import sys


current_dir = os.path.curdir


# user watched file
# user rated file
# user analyze status, 

def check_user_exist(username:str)->bool:
    if os.path.exists(os.path.join(current_dir, "user_data", username)):
        return True
    else:
        return False

print(check_user_exist("joeldushouyu"))

