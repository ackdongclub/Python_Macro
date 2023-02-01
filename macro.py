#import time #화면창 유지하는 시간 설정
from selenium import webdriver #원하는 브라우저 지정 후 url경로 타기
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from babel.numbers import *

from tkinter import * #팝업창을 띄워 줌
from tkinter.messagebox import * # alert창
from tkcalendar import * #python에서 만들어주는 달력

from datetime import datetime as dt #날짜 찾을 떄
import time 

root = Tk() #Tk로 root를 만들어 준다

#브라우저를 켤지 말지 선택
root.title("Choice browser On/Off")
root.geometry("200x150")

choice = Label(root, text='브라우저를 켤까요?')
choice.pack()
chk_yn = IntVar()
yes = Radiobutton(root, text='yes', variable=chk_yn, value=0)
no = Radiobutton(root, text='no', variable=chk_yn, value=1)
yes.pack()
no.pack()

options = webdriver.ChromeOptions()
options.add_argument('--headless') #headless
options.add_argument('--disable--gpu') #python gpu 비활성화
def choice_onoff():
    if chk_yn.get() == 0:
        driver = webdriver.Chrome('./chromedriver')
    elif chk_yn.get() == 1:
        driver = webdriver.Chrome('C:/Users/admin/Desktop/chrome/chromedriver', options=options) # 예약 신청 시 브라우저 보이지 않게 함 headless
    driver.get('https://yeyak.gys.or.kr/fmcs/27?referer=https%3A%2F%2Fgbc.gys.or.kr%2F&login_check=skip')
    
    choice.pack_forget()
    yes.pack_forget()
    no.pack_forget()
    next_btn.pack_forget()

    #사용자가 입력할 tk창-------------------------------------------------------------------------------------------------------------------------------------------------
    #LOGIN

    root.title("Login")
    root.geometry("200x150")

    #title
    login_label = Label(root, text='LOGIN')
    login_label.pack()

    #ID
    label1 = Label(root, text='ID')
    label1.pack()
    userId = Entry(root)
    userId.pack()

    #PASSWORD
    label2 = Label(root, text='PASSWORD')
    label2.pack()
    userPass = Entry(root, show='*')
    userPass.pack()

    #null 값 확인
    def chk_login():
        if userId.get() == "":
            showerror("null", "아이디를 입력하세요")
            root.mainloop()
        if userPass.get() == "":
            showerror("null", "비밀번호를 입력하세요")
            root.mainloop()
        #빈 값이 아니면 로그인
        driver.find_element(By.ID, 'userId').send_keys(userId.get()) #id가 userId인 것이 사용자 아이디를 넣는 input 값의 id
        driver.find_element(By.ID, 'userPassword').send_keys(userPass.get())
        #button은 고유 id값이 존재하지 않으므로 XPath로 가져와 click()
        driver.find_element(By.XPATH, '//*[@id="memberLoginForm"]/fieldset/div/p[3]/button').click()

    #로그인 됐는지 안됐는지 확인, 로그인 되면 데이터 입력 가능
    def login_chk():
        #로그아웃 버튼 생겼는지 확인
        login_chk = len(str(driver.find_element(By.XPATH, '/html/body/div[7]/div[1]/div[2]/ul/li[2]/a/img')))
        
        if login_chk > 0:
            #로그인창 숨기기
            login_label.pack_forget()
            label1.pack_forget()
            label2.pack_forget()
            userId.pack_forget()
            userPass.pack_forget()
            login_btn.pack_forget()

            root.title("Reservation")
            root.geometry("300x640")

            #데이터 선택 리스트
            label3 = Label(root, text='종목')
            label3.pack()
            kind = IntVar()
            kind1 = Radiobutton(root, text='테니스', variable=kind, value=0)
            kind2 = Radiobutton(root, text='풋살', variable=kind, value=1)
            kind1.pack()
            kind2.pack()

            # 테니스 >> 테니스 (2) 코트 모양으로 만들기
            label4 = Label(root, text='장소')
            label4.pack()
            place = Entry(root)
            place.pack()
            label5 = Label(root, text='테니스: 1~3코트, 풋살: 1~2코트')
            label5.pack()

            #정해진 입력 값에 맞춰 input 값을 받아서 해당 날짜를 클릭한다
            label6 = Label(root, text='날짜')
            label6.pack()
            #캘린더를 사용해 날짜 선택
            # today_time = datetime.date.today() 
            days = Calendar(root, selectmode='day')
            days.pack(pady = 20)
            # days.grid(row=1,column=3,sticky='nsew') grid 사용할 땐 sticky='nsew' 사용

            #참가인원 >> 숫자 값을 입력 받는다
            label9 = Label(root, text='참가인원')
            label9.pack()
            people = Entry(root)
            people.pack()

            #radio 버튼으로 시간을 선택하게 하여 해당 value로 if문을 돌린다
            label8 = Label(root, text='시간')
            label8.pack()

            reser_time = IntVar()
            radio1 = Radiobutton(root, text='06:00 ~ 08:00', variable=reser_time, value=0)
            radio2 = Radiobutton(root, text='08:00 ~ 10:00', variable=reser_time, value=1)
            radio3 = Radiobutton(root, text='10:00 ~ 12:00', variable=reser_time, value=2)
            radio4 = Radiobutton(root, text='12:00 ~ 14:00', variable=reser_time, value=3)
            radio5 = Radiobutton(root, text='14:00 ~ 16:00', variable=reser_time, value=4)
            radio6 = Radiobutton(root, text='16:00 ~ 18:00', variable=reser_time, value=5)
            radio7 = Radiobutton(root, text='18:00 ~ 20:00', variable=reser_time, value=6)
            radio8 = Radiobutton(root, text='20:00 ~ 22:00', variable=reser_time, value=7)
            radio1.pack()
            radio2.pack()
            radio3.pack()
            radio4.pack()
            radio5.pack()
            radio6.pack()
            radio7.pack()
            radio8.pack()   

            #위에서 받아온 테니스 장의 정보를 실제 option의 value값으로 만듦
            def tenni_place():
                if str(place.get()) == '1':
                    Select(driver.find_element(By.NAME, 'place_opt')).select_by_value('6')
                elif str(place.get()) == '2':
                    Select(driver.find_element(By.NAME, 'place_opt')).select_by_value('7')
                elif str(place.get()) == '3':
                    Select(driver.find_element(By.NAME, 'place_opt')).select_by_value('8')

            #위에서 받아온 풋살 장의 정보를 실제 option의 value값으로 만듦
            def foot_place():
                if str(place.get()) == '1':
                    Select(driver.find_element(By.NAME, 'place_opt')).select_by_value('4')
                elif str(place.get()) == '2':
                    Select(driver.find_element(By.NAME, 'place_opt')).select_by_value('5')

            #위에서 받아온 날짜와 동일한 id를 찾아 클릭한다
            def find_date():
                sel_days = days.selection_get()
                driver.find_element(By.ID, sel_days).click()

            def find_time():
                count = 0
                # 예약 가능한지 확인하기
                if reser_time.get() == 0:
                    rad1 = driver.find_element(By.XPATH, f'/html/body/div[1]/div[3]/div[2]/div[3]/div/form/div[7]/table[2]/tbody/tr[1]/td[3]')
                    if rad1.text == "":
                        driver.find_element(By.XPATH, f'/html/body/div[1]/div[3]/div[2]/div[3]/div/form/div[7]/table[2]/tbody/tr[1]/td[2]/input').click()
                    else:
                        try:
                            while True:
                                driver.refresh()
                                time.sleep(2)
                                count += 1
                                if count == 5:
                                    break                     

                                if driver.find_element(By.XPATH, f'/html/body/div[1]/div[3]/div[2]/div[3]/div/form/div[7]/table[2]/tbody/tr[1]/td[3]').text == "":
                                    break
                        finally:
                            print('error')
                elif reser_time.get() == 1:
                    rad2 = driver.find_element(By.XPATH, f'/html/body/div[1]/div[3]/div[2]/div[3]/div/form/div[7]/table[2]/tbody/tr[2]/td[3]')
                    if rad2.text == "":
                        driver.find_element(By.XPATH, f'/html/body/div[1]/div[3]/div[2]/div[3]/div/form/div[7]/table[2]/tbody/tr[2]/td[2]/input').click()
                    else:
                        try:
                            while True:
                                driver.refresh()
                                time.sleep(2)
                                count += 1
                                if count == 5:
                                    break
                                            
                                if driver.find_element(By.XPATH, f'/html/body/div[1]/div[3]/div[2]/div[3]/div/form/div[7]/table[2]/tbody/tr[2]/td[3]').text == "":
                                    break
                        finally:
                            print('error')
                elif reser_time.get() == 2:
                    rad3 = driver.find_element(By.XPATH, f'/html/body/div[1]/div[3]/div[2]/div[3]/div/form/div[7]/table[2]/tbody/tr[3]/td[3]')
                    if rad3.text == "":
                        driver.find_element(By.XPATH, f'/html/body/div[1]/div[3]/div[2]/div[3]/div/form/div[7]/table[2]/tbody/tr[3]/td[2]/input').click()
                    else:
                        try:
                            while True:
                                driver.refresh()
                                time.sleep(2)
                                count += 1
                                if count == 5:
                                    break

                                if driver.find_element(By.XPATH, f'/html/body/div[1]/div[3]/div[2]/div[3]/div/form/div[7]/table[2]/tbody/tr[3]/td[3]').text == "":
                                    break
                        finally:
                            print('error')
                elif reser_time.get() == 3:
                    rad4 = driver.find_element(By.XPATH, f'/html/body/div[1]/div[3]/div[2]/div[3]/div/form/div[7]/table[2]/tbody/tr[4]/td[3]')
                    if rad4.text == "":
                        driver.find_element(By.XPATH, f'/html/body/div[1]/div[3]/div[2]/div[3]/div/form/div[7]/table[2]/tbody/tr[4]/td[2]/input').click()
                    else:
                        try:
                            while True:
                                driver.refresh()
                                time.sleep(2)
                                count += 1
                                if count == 5:
                                    break

                                if driver.find_element(By.XPATH, f'/html/body/div[1]/div[3]/div[2]/div[3]/div/form/div[7]/table[2]/tbody/tr[4]/td[3]').text == "":
                                    break
                        finally:
                            print('error')
                elif reser_time.get() == 4:
                    rad5 = driver.find_element(By.XPATH, f'/html/body/div[1]/div[3]/div[2]/div[3]/div/form/div[7]/table[2]/tbody/tr[5]/td[3]')
                    if rad5.text == "":
                        driver.find_element(By.XPATH, f'/html/body/div[1]/div[3]/div[2]/div[3]/div/form/div[7]/table[2]/tbody/tr[5]/td[2]/input').click()
                    else:
                        try:
                            while True:
                                driver.refresh()
                                time.sleep(2)
                                count += 1
                                if count == 5:
                                    break

                                if driver.find_element(By.XPATH, f'/html/body/div[1]/div[3]/div[2]/div[3]/div/form/div[7]/table[2]/tbody/tr[4]/td[3]').text == "":
                                    break
                        finally:
                            print('error')
                elif reser_time.get() == 5:
                    rad6 = driver.find_element(By.XPATH, f'/html/body/div[1]/div[3]/div[2]/div[3]/div/form/div[7]/table[2]/tbody/tr[6]/td[3]')
                    if rad6.text == "":
                        driver.find_element(By.XPATH, f'/html/body/div[1]/div[3]/div[2]/div[3]/div/form/div[7]/table[2]/tbody/tr[6]/td[3]').click()
                    else:
                        try:
                            while True:
                                driver.refresh()
                                time.sleep(2)
                                count += 1
                                if count == 5:
                                    break

                                if driver.find_element(By.XPATH, f'/html/body/div[1]/div[3]/div[2]/div[3]/div/form/div[7]/table[2]/tbody/tr[6]/td[3]').text == "":
                                    break
                        finally:
                            print('error')
                elif reser_time.get() == 6:
                    rad7 = driver.find_element(By.XPATH, f'/html/body/div[1]/div[3]/div[2]/div[3]/div/form/div[7]/table[2]/tbody/tr[7]/td[3]')
                    if rad7.text == "":
                        driver.find_element(By.XPATH, f'/html/body/div[1]/div[3]/div[2]/div[3]/div/form/div[7]/table[2]/tbody/tr[7]/td[2]/input').click()
                    else:
                        try:
                            while True:
                                driver.refresh()
                                time.sleep(2)
                                count += 1
                                if count == 5:
                                    break

                                if driver.find_element(By.XPATH, f'/html/body/div[1]/div[3]/div[2]/div[3]/div/form/div[7]/table[2]/tbody/tr[7]/td[3]').text == "":
                                    break
                        finally:
                            print('error')
                elif reser_time.get() == 7:
                    rad8 = driver.find_element(By.XPATH, f'/html/body/div[1]/div[3]/div[2]/div[3]/div/form/div[7]/table[2]/tbody/tr[8]/td[3]')
                    if rad8.text == "":
                        driver.find_element(By.XPATH, f'/html/body/div[1]/div[3]/div[2]/div[3]/div/form/div[7]/table[2]/tbody/tr[8]/td[2]/input').click()
                    else:
                        try:
                            while True:
                                driver.refresh()
                                time.sleep(2)
                                count += 1
                                if count == 5:
                                    break

                                if driver.find_element(By.XPATH, f'/html/body/div[1]/div[3]/div[2]/div[3]/div/form/div[7]/table[2]/tbody/tr[8]/td[3]').text == "":
                                    break
                        finally:
                            print('error')
                            
                driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/div[3]/div/form/div[10]/span/a/img').click()
                driver.switch_to.window(driver.window_handles[-1]) # 최근에 뜬 창으로 권한을 이동시킨다
                time.sleep(1)
                driver.find_element(By.XPATH, '/html/body/div/form/table/tbody/tr[7]/td/input').send_keys(people.get())
                driver.find_element(By.NAME, 'apply_chk').click()  
                driver.find_element(By.NAME, 'apply_chk2').click()

                #테니스와 풋살의 대관신청 버튼위치가 달라서 조건 줌
                if kind.get() == 0:
                    driver.find_element(By.XPATH, '/html/body/div/form/table/tbody/tr[16]/td/center/a[1]/img').click()
                else:
                    driver.find_element(By.XPATH, '/html/body/div/form/table/tbody/tr[15]/td/center/a[1]/img').click() 

            def reservation_func():
                # 사용자가 원하는 달의 신청 일과 현재 시간과의 차이를 구해 해당 초만큼 지연, (서버시간 확인)
                time.sleep(5)
                #로그인이 돼있으면 로그아웃을 시키고 아니면 바로 로그인(자동로그아웃)
                if login_chk > 0:
                    driver.find_element(By.XPATH, '/html/body/div[7]/div[1]/div[2]/ul/li[2]/a/img').click() #로그아웃
                
                driver.get('https://yeyak.gys.or.kr/fmcs/27?referer=https%3A%2F%2Fgbc.gys.or.kr%2F&login_check=skip') #로그인창으로 이동
                
                # 처음 입력 받았던 회원데이터로 로그인
                driver.find_element(By.ID, 'userId').send_keys(userId.get()) 
                driver.find_element(By.ID, 'userPassword').send_keys(userPass.get())
                driver.find_element(By.XPATH, '//*[@id="memberLoginForm"]/fieldset/div/p[3]/button').click()
                
                #예약 실행
                if kind.get() == 0:
                    driver.get('https://gbc.gys.or.kr:446/rent/tennis_rent.php?part_opt=07') #테니스 입력 시
                    tenni_place() # 장소
                    find_date() # 날짜
                    find_time() # 시간

                elif kind.get() == 1:
                    driver.get('https://gbc.gys.or.kr:446/rent/footsal_rent.php?part_opt=06') #풋살 입력 시
                    foot_place() # 장소
                    find_date()  # 날짜
                    find_time() # 시간
                    
            # 예약 데이터 입력 버튼
            rsv_btn = Button(root, text='Reservation', command=reservation_func)
            rsv_btn.pack()
        else:
            showerror("error", "로그인 실패")
            root.mainloop()
        
    def login_func():
        chk_login()
        login_chk()

    #로그인 버튼
    login_btn = Button(root, text='LOGIN', command=login_func)
    login_btn.pack()          
    
#브라우저 선택 버튼
next_btn = Button(root, text='NEXT', command=choice_onoff)
next_btn.pack()

root.mainloop()

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
while True:
    pass