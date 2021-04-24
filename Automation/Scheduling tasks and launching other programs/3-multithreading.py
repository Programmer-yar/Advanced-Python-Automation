import threading, time
start_time = time.time()
print("Start of program")

def take_nap():
    time.sleep(5)
    print("Oh! wow The sun is up")

def nums(num1, num2, num3):
    #try removing sleep time of 1 sec
    time.sleep(1)
    print("the first number is:", num1)
    time.sleep(2)
    print("the second number is:", num2)
    time.sleep(1)
    print("the third number is:", num3)

thread_object_1 = threading.Thread(target=take_nap)
thread_object_1.start()

#passing arguments to functions in threading
thread_object_2 = threading.Thread(target=nums, args=[1, 2], kwargs={'num3':3})
thread_object_2.start()

print("this is the end of program", time.time()-start_time)
    
