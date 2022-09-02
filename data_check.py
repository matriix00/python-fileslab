
def chk_valid_st(msg):
    val=input(msg)
    if val.isdigit() or val.isspace() or not val:
        print("enter a valid string")
        return chk_valid_st(msg)
    else:
        return val

def chk_valid_int(msg):
    val=input(msg)
    if val.isdigit():
        return int(val)
    else:
        print("enter a valid number ")
        return chk_valid_int(msg)

from curses.ascii import isdigit, isspace
import mailbox
import re
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
def chk_valid_mail(msg):
    val=input(msg)
    if(re.fullmatch(regex, val)):
        return val
 
    else:
        print("enter valid email ")
        return chk_valid_mail(msg)

def chk_valid_pass(msg):
    val=input(msg)
    if val.isspace() or not val :
        print("enter valid password ")
        return chk_valid_pass
    else:
        return val

def chk_pass(msg,password):
    confirm=input(msg)
    if confirm.isspace() or not confirm :
        print("please enter valid password ")
        return chk_valid_pass(msg)
        
    else:
        if confirm != password :
            print("password does not match ")
            return chk_valid_pass(msg)
        else :
            return confirm
    
def chk_valid_mobile(msg):
    val=input(msg)
    sp=val[0:3]
    ll=['011','010','012','015']
    if val.isdigit():
        if (len(val) != 11) or (sp not in ll ):
            print("please enter valid phone number ")
            return chk_valid_mobile(msg)
        else:
            return val
    else:
        print("please enter valid digits")
        return chk_valid_mobile(msg)

def chk_valid_details(msg):
    val=input(msg)
    if not val :
        print("enter valid detail ")
        return chk_valid_details(msg)
    else:
        return val

import datetime


def chk_valid_date(msg):
    inputDate = input(msg)
    if inputDate.isspace() or not inputDate:
        print("please enter valid string ")
        return chk_valid_date(msg)
    else:    
        day, month, year = inputDate.split('/')
        isValidDate = True
        try:
            datetime.datetime(int(year), int(month), int(day))
        except ValueError:
            isValidDate = False

        if(isValidDate):
            return inputDate
        else:
            return chk_valid_date(msg)

            

    
