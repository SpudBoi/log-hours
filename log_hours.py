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

    #closing the window
    window.destroy()

################################################################################
#creating window, setting size, setting background
window = tkinter.Tk()
window.title("Extension Reassignment")
window.geometry('400x300')
window.configure(bg = "white")
window.resizable(False,False)


#creation and placement of text inputs

#username
enter_username = tkinter.Entry(window)
enter_username.place(height=20,width=150,x=10,y=125)
tkinter.Label(window,font = "verdana 10", text = "Username", bg = "white").place(x=10,y=100)

#password
enter_pass = tkinter.Entry(window, show="*")
enter_pass.place(height=20,width=150,x=10,y=175)
tkinter.Label(window, font = "verdana 10", text = "Password", bg = "white").place(x=10,y=150)

#custom button
hurts = tkinter.PhotoImage(file = "log_hours/hurts.png")
tkinter.Button(window, command = input_info, image = hurts, bg = "white").place(height=45, width = 100, x=75, y = 250)

#add in the pictures for the title and greeting anime girl
icon = tkinter.PhotoImage(file = "log_hours/network_chan.png")
tkinter.Label(window, image = icon, bg="white").place(x=175,y=5)

title = tkinter.PhotoImage(file = "log_hours/title.png")
tkinter.Label(window, image = title, bg = "white").place(x=5,y=5)

window.mainloop()
################################################################################


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

# //*[@id="win0divDAY_OF_WK_DISPLAY$0"] //*[@id="win0divPUNCH_DATE_DISPLAY$0"] //*[@id="PUNCH_TIME_1$0"] //*[@id="PUNCH_TIME_2$0"] //*[@id="TRC$0"]
# //*[@id="win0divDAY_OF_WK_DISPLAY$1"] //*[@id="win0divPUNCH_DATE_DISPLAY$1"] //*[@id="PUNCH_TIME_1$1"] //*[@id="PUNCH_TIME_2$1"] //*[@id="TRC$1"]
frame = driver.find_element_by_xpath("//*[@id='main_target_win0']")
driver.switch_to.frame(frame)
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
driver.find_element_by_xpath(xpath1).send_keys("8:30AM")

driver.find_element_by_xpath(xpath2).click()
driver.find_element_by_xpath(xpath2).clear()
driver.find_element_by_xpath(xpath2).send_keys("12:00PM")

driver.find_element_by_xpath(xpath3).click()
driver.find_element_by_xpath(xpath3).clear()
driver.find_element_by_xpath(xpath3).send_keys("12:30PM")

driver.find_element_by_xpath(xpath4).click()
driver.find_element_by_xpath(xpath4).clear()
driver.find_element_by_xpath(xpath4).send_keys("5:00PM")

xpath5 = "//select[@id='TRC$" + str(index) + "']/option[text()='STE - Regular Pay - Student FICA Ex']"
driver.find_element_by_xpath(xpath5).click()

driver.find_element_by_xpath("//*[@id='TL_LINK_WRK_SUBMIT_PB$418$']").click()
