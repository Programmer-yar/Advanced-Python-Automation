import time

start = time.time()
time_dict = {}
lap_num = 0

flag = True
while flag:
    print("press enter to start a lap or type q to exit stopWatch")
    begin = input()
    if begin == '':
        lap_start = time.time()
        print("press s to stop lap")
        stop = input()
        if stop == 's':
            lap_stop = time.time()
            time_lapsed = lap_stop - lap_start
            lap_num += 1
            lap = f'lap_{lap_num}'
            time_dict[lap] = time_lapsed
        else:
            print("Incorrect Input press 's' only")

    elif begin == 'q':
        flag = False

if len(time_dict) > 0:
    for key, val in time_dict.items():
        print(key, "=>", val)

end = time.time()
print('Total time taken by program', end-start)




        
        
    
