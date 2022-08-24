import string
from xmlrpc.client import boolean
import lib
# import time
# import datetime

# def countSlot(total_seconds = 15):
#     totalSeconds = 15*60 #15minutos * 60 segundos/minuto
#     while(totalSeconds > 0):
#         timer = datetime.timedelta(seconds = total_seconds)
#         print(timer, end="\r")
#         time.sleep(1)
#         total_seconds -=1

# def countdown(h, m, s):
#     total_seconds = h * 3600 + m * 60 + s
#     while total_seconds > 0:
#         # Timer represents time left on countdown
#         timer = datetime.timedelta(seconds = total_seconds)
        
#         # Prints the time left on the timer
#         print(timer)
 
#         # Delays the program one second
#         time.sleep(1)
 
#         # Reduces total time by one second
#         total_seconds -= 1
 
#     print("Bzzzt! The countdown is at zero seconds!")
#     countdown(int(0),int(1),int(0))


bid = '10'
price1 = lib.binToString(0b10010110,10)
price2 = lib.binToString(0b10100000,10)
qntd = lib.binToString(0b100100010,10)
bid = bid + price1 + price2 + qntd
print(bid)
print(validaOrdem(bid))





