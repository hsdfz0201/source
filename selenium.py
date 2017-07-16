from selenium import webdriver
from pyvirtualdisplay import Display
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
display = Display(visible=0, size=(1024, 768))
display.start()
browser = webdriver.Firefox() # Get local session of firefox
browser.get("http://www.yahoo.com") # Load page


browser.close()