from data_check import chk_valid_int, chk_valid_mail, chk_valid_pass,chk_valid_st
from project_page import project
def login():
    print("============== welcome to login page =================\n")

    email=chk_valid_mail("enter your email ")
    password=chk_valid_pass("ente your password ")
    userID=search_user_by_email(email,password)
    if userID:
        project(userID)
        
def search_user_by_email(m,passwd):
    allusers=get_all_usersData()
    for user in allusers:
        user_detail = user.split(":")
        if (user_detail[4] == m) and (user_detail[3] ==passwd) :
            print("login successfully")
            
            return user_detail[0]
    else:
        print("invalid email or password")       

def get_all_usersData():
    try:
        fileobject=open("users.txt", "r")
    except Exception as e:
        print(e)
        return False
    else:
        users= fileobject.readlines()
        return users
