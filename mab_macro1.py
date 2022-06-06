import pyautogui, time
def mouse_justclick():
    pyautogui.mouseDown()
    pyautogui.mouseUp() 
    time.sleep(0.5)  

def mouse_click(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.mouseDown()
    pyautogui.mouseUp() 
    time.sleep(0.5)

def mouse_doubleclick(x,y):
    pyautogui.moveTo(x, y)
    pyautogui.doubleClick()
    time.sleep(0.5)

def productRegistration():
    # 아이템 등록 클릭
    pyautogui.moveTo(1334,315)
    mouse_justclick()

    # 리무버 인식 후 클릭
    loc = pyautogui.locateOnScreen('item01.png',confidence = 0.7)
    if loc == None: # 없으면?
        return #어떡하지?
    center = pyautogui.center(loc)
    pyautogui.moveTo(center)
    mouse_justclick()

    # 아이템 등록창 클릭
    mouse_click(849, 420)

    # 등록최저가 더보기 클릭
    loc = pyautogui.locateOnScreen('item06.png', confidence = 0.7)
    center = pyautogui.center(loc)
    pyautogui.moveTo(center)
    pyautogui.moveRel(178, 3)
    mouse_justclick()

    # 최저가 서치 후 클릭
    loc = pyautogui.locateOnScreen('item04.png', confidence = 0.7)
    if loc == None:  #최저가가 없으면?
        return #어떡하냐
    center = pyautogui.center(loc)
    pyautogui.moveTo(center)
    mouse_justclick()

    # 상대좌표로 x 클릭
    pyautogui.moveRel(206,-67)
    mouse_justclick()
    
    # 등록버튼 클릭
    mouse_click(922,776)

    # 알림창 닫기 클릭
    mouse_click(1047, 587)

    return

def receivePayment():
    loc = pyautogui.locateOnScreen('item02.png', confidence = 0.7)
    if loc != None: #판매성공시
        
        #대금수령 클릭
        center = pyautogui.center(loc)
        pyautogui.moveTo(center)
        mouse_justclick()

        # 영수증 닫기 클릭
        mouse_click(1042, 642)

        # 재귀호출로 대금수령 전부 클릭
        receivePayment()
        time.sleep(1)

    else: return
    
def cancelProduct():
    # 내 경매 현황 클릭
    mouse_click(610,351)

    #전체보기로 변경
    mouse_click(679, 414)

    # 가장 위에 있는 상품 더블클릭
    mouse_doubleclick(856,390)

    # 판매취소 클릭
    mouse_click(969, 689)

    # 확인 클릭
    mouse_click(1003, 591)

    # 닫기 클릭
    mouse_click(1046, 593)

    # 내 경매 현황 클릭
    mouse_click(610,351)
    
    #판매성공 보기로 변경
    mouse_click(690, 462)

timeCounter = 0
while True: #무한반복

    # 30초에 한 번씩 새로고침
    
    mouse_click(1279,276)
    
    loc = pyautogui.locateOnScreen('item02.png', confidence = 0.7)
    if loc != None: #판매성공시
        
        #대금수령 
        receivePayment()

        # 상품등록
        productRegistration()

        # 판매량 카운트
        timeCounter = 0
    
    else: # 30분동안 판매없으면 취소 후 재등록

        timeCounter += 1
        if timeCounter >= 60: 
            cancelProduct()
            productRegistration()

    time.sleep(30)


