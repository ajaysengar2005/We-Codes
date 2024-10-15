import time
t = time.strftime('%H: %M: %S')
print("Time Zone Of India")
print(t)
h = int(time.strftime('%H'))
print("\nPrint Greeting According to Time")
print("Time :",h)
if(h>=0 and h<12):
    print("Good Morning Sir")
elif(h>=12 and h<16):
    print("Good Afternoon Sir")
elif(h>=16 and h<19):
    print("Good Evening Sir")
else:
    print("Good Night Sir")
