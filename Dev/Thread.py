import threading
import time
import logging
num = 0

def work():
    global num 
    while(num < 10000):
        num += 1
    
    return
def listen(num):
    print("Num after: ", num)

    return
def Thread_start(num):
    t1 = threading.Thread(name = 'Worker',target = work)
    threads.append(t1)
    t2 = threading.Thread(name = 'listen',target = listen, args= (num,)) 
    threads.append(t2)





   

