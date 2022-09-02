from login_page import login
from register_page import  user_details


print("=============   hello to our app =============")

def mainpage():
    choice=input("""
    l =>>>>> login 
    r =>>>>> register,if you don't have account 
    """)

    if choice in ['l','r']:
        if choice == 'l':
            login()
        else:            

            if user_details():
                login()
    else:
        print("enter valid choice")
        return mainpage()
mainpage()