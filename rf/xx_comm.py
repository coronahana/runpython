import os
import random
import time
import string

def Get_A_Random_String():
    RandString = ''.join(random.sample(string.ascii_letters + string.digits, int))
    return RandString
def Get_A_Random_Name(tp='rb'):
    RandString = tp + '_' +str(random.randint(100, 999))+'_'+str(random.randint(1000, 9999))
    return RandString
def Get_A_Random_Int():
    RandINT = random.randint(100000, 999999)  # random integer in range [0,10]
    return RandINT
def Get_Login_User():
    return os.getlogin()

if __name__ == '__main__':
    print(string.ascii_letters)
    print (string.digits)
    # print(str(random.sample(string.ascii_letters + string.digits, int)))