
import pyautogui
import keyboard
import time

COUNTER = 0
DELAY_LIST = []
LOCATION_LIST = []


# 철봉제작
DELAY_LIST = [0.5, 0.5, 0.5, 6.0, 0.5, 0.5, 9.775, 0.45, 0.437, 0.452, 0.47, 0.589, 5.886, 0.5, 0.5, 0.5, 0.5, 0.5]
LOCATION_LIST = [(992, 754), (612, 507), (445, 762), (952, 819), (616, 509), (446, 761), (135, 473), (155, 469), (139, 480), (145, 482), (140, 483), (140, 483), (941, 814), (1647, 538), (1233, 410), (1641, 540), (1391, 371), (545, 761)]

# # 나무판제작0
# DELAY_LIST = [1.0, 0.5, 0.5, 0.5, 19]
# LOCATION_LIST = [(43, 496), (94, 739), (611, 465), (543, 743), (31, 494)]

#괴불리기
# DELAY_LIST = [1.0, 0.5, 0.5, 0.5, 0.5, 4.29]
# LOCATION_LIST = [(943, 689), (94, 492), (88, 362), (594, 452), (554, 738), (979, 693)]

#굵실5-질긴끈1 제작
# DELAY_LIST = [0.25, 0.5, 0.5, 0.5, 5.5,0.25, 0.5, 0.5, 0.5, 5.5,0.25, 0.5, 0.5, 0.5, 5.5,0.25, 0.5, 0.5, 0.5, 5.5,0.25, 0.5, 0.5, 0.5, 5.5,0.25, 0.5, 0.5, 0.5, 5.5]
# LOCATION_LIST = [(936, 554), (64, 412), (598, 471), (552, 739), (936, 554),(936, 554), (64, 412), (598, 471), (552, 739), (936, 554),(936, 554), (64, 412), (598, 471), (552, 739), (936, 554),(936, 554), (64, 412), (598, 471), (552, 739), (936, 554),(936, 554), (64, 412), (598, 471), (552, 739), (936, 554),(936, 554), (55, 572), (598, 471), (552, 739), (936, 554)]

timer_start = time.time()
while True:
    cur_MouseX, cur_MouseY = pyautogui.position()
    if keyboard.read_key() == "0": # 클릭 모드
        COUNTER += 1
        pyautogui.mouseDown()
        pyautogui.mouseUp()

        print(COUNTER, "번째 클릭의 좌표 : ", cur_MouseX, cur_MouseY)
        timer_end = time.time()
        DELAY = (timer_end - timer_start)*1000
        timer_start = timer_end
        print("구간시간 : ", int(DELAY) , "ms")

        DELAY_LIST.append(int(DELAY)/1000*1.0)
        LOCATION_LIST.append((cur_MouseX,cur_MouseY))

    if keyboard.read_key() == "f1": # 세부 모드
        print("현재 좌표 : ", cur_MouseX, cur_MouseY)
        timer_end = time.time()
        DELAY = (timer_end - timer_start)*1000
        timer_start = timer_end
        print("구간시간 : ", int(DELAY)/1000*1.0 , "s")
    if keyboard.read_key() == "=":
        print("현재 좌표 : ", cur_MouseX, cur_MouseY)

        break


  
DELAY_LIST[0] = 0.25
while True:
    if keyboard.read_key() == "=":
        SQNC = 0 
        while True:
            CUR_XPOS = LOCATION_LIST[SQNC][0]
            CUR_YPOS = LOCATION_LIST[SQNC][1]
            time.sleep(DELAY_LIST[SQNC])
            pyautogui.moveTo(CUR_XPOS ,CUR_YPOS)
            pyautogui.mouseDown()
            pyautogui.mouseUp()
            SQNC += 1
            if SQNC == len(DELAY_LIST):
                SQNC = 0

