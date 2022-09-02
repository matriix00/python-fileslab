def create_user(user):
    try:
        fileobject=open("users.txt","a")
    except Exception as e :
        print(e)
        return False
    else:
        fileobject.write(user+"\n")
        return True