from data_check import chk_pass, chk_valid_int, chk_valid_mail, chk_valid_mobile, chk_valid_pass,chk_valid_st
import uuid
from  users_file import create_user
def register():
    print("============== welcome to register page =================\n")
    fname=chk_valid_st("please enter your first name ")
    lname=chk_valid_st("please enter your last name ")
    email=chk_valid_mail("please enter your email ")
    password=chk_valid_pass("please enter your password ")
    confirm_pass=chk_pass("please retype password ",password)
    mobile=chk_valid_mobile("please enter your mobile phone ")
    userID=str(uuid.uuid4())

    return f"{userID}:{fname}:{lname}:{password}:{email}:{mobile}"


def user_details():
    user_data=register()
    # print (user_data)
    if create_user(user_data):
        print("user created ")
        return True
    else:
        print("error")
        return False
