import os

print("1 = Shutdown")
print("2 = Restart")

stdwn = int(input("Choose if you want Turn off your Computer : "))

if(stdwn == 1):
    os.system("shutdown /s /t 1")
elif(stdwn == 2):
    os.system("shutdown /r /t 1")
else:
    print("Invalid Number!")