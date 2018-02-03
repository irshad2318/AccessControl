import os 
from sys import argv

def main():
    """Lenel Access Controll System unofficail Attendance System"""

    print("EMPID : " '{}'  " No Of Days : " '{}'.format(empid, top))
    cnt = input("enter")
    if cnt == 'q':
        exit(0)
    if cnt == '1':
          
        dst = input("Enter FROM date  : ")
        dend = input("Enter TO date  :  ")
        files = input(" Enter file Name :Note must be in same folder  :")
        with open(files, 'r') as f:
                s = f.read().splitlines()
                s = list(s)
        print(s[0])

        att(dst, dend, s)
        exit(0)
    else:
        sms_update(query)
if __name__ == "__main__":
    main()
