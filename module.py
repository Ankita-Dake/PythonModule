# get current time
import time

print(time.localtime(time.time()))

# get formatted time
import time

print(time.asctime(time.localtime(time.time())))

# sleep time
import time

for i in range(0, 5):
    print(i)
    time.sleep(1)

# DateTime module
import datetime
print(datetime.datetime.now())

# calender module
import  calendar
cal = calendar.month(2020, 6)
print(cal)

calendar.prcal(2020)


# platform module
import platform
sys = platform.system()
print(sys)


# math module

import  math
print('squaroot is', math.sqrt(64))
print('power is' , math.pow(3,2))
print('factorial is', math.factorial(3))
print(math.remainder(2,23))

# random module
import  random
print(random.random())
print(random.randint(2,56))