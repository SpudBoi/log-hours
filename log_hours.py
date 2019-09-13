from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import tkinter
from playsound import playsound
from datetime import date
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

#global variables to hold information
password = ""
username = ""

#fetching and formatting date
today = date.today()
date = today.strftime("%#m/%#d")

#this function assigns the global variables to the info collected by
#network chan
def input_info():
    #playsound('reassign_extension/disgust.wav')

    #retrieving and assigning information
    global password
    password = enter_pass.get()
    global username
    username = enter_username.get()
    global choice
    choice = v.get()

    #closing the window
    window.destroy()
    execute_logging()


def execute_logging():
    #create web driver and navigate to call manager
    driver = webdriver.Chrome()
    driver.get("https://my.pugetsound.edu/psp/PA91PRD/EMPLOYEE/EMPL/h/?tab=UP_SIGNIN_TAB")
    driver.implicitly_wait(10)

    #enter username
    web_username = driver.find_element_by_name("userid")
    web_username.click()
    web_username.send_keys(username)

    #enter password and login
    web_password = driver.find_element_by_name("pwd")
    web_password.click()
    web_password.send_keys(password)
    web_password.send_keys(Keys.RETURN)

    time.sleep(5)
    driver.find_element_by_xpath("//*[@id='win1divPTGP_STEPS_L1_row$2']").click()
    time.sleep(2)
    driver.find_element_by_xpath("//*[@id='win1divPTGP_STEPS_L2_row$12']").click()

    week_days = ["Mon", "Tue", "Wed", "Thu", "Fri"]

    frame = driver.find_element_by_xpath("//*[@id='main_target_win0']")
    driver.switch_to.frame(frame)

    if choice == 0:
        driver.find_element_by_xpath("//*[@id='LAST_NAME$1']").click()
    elif choice == 1:
        driver.find_element_by_xpath("//*[@id='LAST_NAME$0']").click()

    time.sleep(1)
    index = -1
    for i in range(0,17):
        xpath = "//*[@id='PUNCH_DATE_DISPLAY$" + str(i) + "']"
        if driver.find_element_by_xpath(xpath).text == date:
            index = i
            break

    xpath1 = "//*[@id='PUNCH_TIME_1$" + str(index) + "']"
    xpath2 = "//*[@id='PUNCH_TIME_2$" + str(index) + "']"
    xpath3 = "//*[@id='PUNCH_TIME_3$" + str(index) + "']"
    xpath4 = "//*[@id='PUNCH_TIME_4$" + str(index) + "']"

    driver.find_element_by_xpath(xpath1).click()
    driver.find_element_by_xpath(xpath1).clear()
    if choice == 0:
        driver.find_element_by_xpath(xpath1).send_keys("11:00AM")
    else:
        driver.find_element_by_xpath(xpath1).send_keys("7:00PM")

    # driver.find_element_by_xpath(xpath2).click()
    # driver.find_element_by_xpath(xpath2).clear()
    # driver.find_element_by_xpath(xpath2).send_keys("12:00PM")
    #
    # driver.find_element_by_xpath(xpath3).click()
    # driver.find_element_by_xpath(xpath3).clear()
    # driver.find_element_by_xpath(xpath3).send_keys("12:30PM")

    driver.find_element_by_xpath(xpath4).click()
    driver.find_element_by_xpath(xpath4).clear()
    if choice == 0:
        driver.find_element_by_xpath(xpath4).send_keys("2:00PM")
    else:
        driver.find_element_by_xpath(xpath4).send_keys("9:00PM")

    xpath5 = "//select[@id='TRC$" + str(index) + "']/option[text()='STE - Regular Pay - Student FICA Ex']"
    driver.find_element_by_xpath(xpath5).click()

    driver.find_element_by_xpath("//*[@id='TL_LINK_WRK_SUBMIT_PB$418$']").click()
    time.sleep(10)
    driver.quit()

################################################################################
#creating initial window
window = tkinter.Tk()
window.resizable(False,False)

#configuring main window
window.title("University of Puget Sound")
window.geometry('500x295')
window.configure(bg = "white")

banner = tkinter.PhotoImage(file = "C:\\Users\\nettechs\\Desktop\\Code\\log_hours\\ups_banner.png")
tkinter.Label(window, image = banner, bg = "white").place(x=-5,y=-5)

tkinter.Label(window,font = "verdana 12", text = "Log Work Hours", bg = "white").place(x=225,y=50)

#username
enter_username = tkinter.Entry(window, borderwidth = 3, font = "verdana 10")
enter_username.place(height=25,width=150,x=225,y=105)
tkinter.Label(window,font = "verdana 8", text = "Username:", bg = "white").place(x=225,y=85)

#password
enter_pass = tkinter.Entry(window, show="\u2022", borderwidth = 3)
enter_pass.place(height=25,width=150,x=225,y=155)
tkinter.Label(window, font = "verdana 8", text = "Password:", bg = "white").place(x=225,y=135)

#custom button
login = tkinter.PhotoImage(file = "C:\\Users\\nettechs\\Desktop\\Code\\log_hours\\signin.png")
tkinter.Button(window, image = login, bg = "white", command = input_info, borderwidth = 0, cursor = "hand2").place(height=24, width = 90, x=220, y = 240)

v = tkinter.IntVar()
tkinter.Radiobutton(window, text = "Network Technician", variable = v, value = 0, bg = "white",font = "verdana 8").place(x = 220, y = 185)
tkinter.Radiobutton(window, text = "Math Tutor", variable = v, value = 1, bg = "white",font = "verdana 8").place(x = 220, y = 205)

#initiate gui
window.mainloop()
################################################################################
