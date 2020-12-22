from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

pelikoodi = ""
i = 0


pelikoodi = input("Syötä kahoot-pelin koodi: ")
botteja = input("Kuinka monta Bottia haluat: ")
nimet = input('Minkä nimisiä botteja haluat: ')

name = nimet

while i < int(botteja):
    selain = webdriver.Chrome()
    selain.get("https://kahoot.it/")
    kirjoitus = selain.find_element_by_id("game-input")
    kirjoitus.send_keys(pelikoodi)
    kirjoitus.send_keys(Keys.RETURN)
    time.sleep(1)
    nimi = selain.find_element_by_name("nickname") 
    nimi.send_keys(name + str(i))
    nimi.send_keys(Keys.RETURN)
    i = i + 1