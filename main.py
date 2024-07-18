import selenium
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from time import sleep
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys

spotify_playlist_url = input("Enter the Spotify playlist URL: ")

driver = webdriver.Firefox()
def download_songs():
    driver.get('https://spotifymp3.com/')
    sleep(5)
    link_insert = driver.find_element(By.ID,'input')
    link_insert.send_keys(spotify_playlist_url)

    download_button = driver.find_element(By.ID, 'submit')
    download_button.click()

    sleep(10)

    all_buttons = driver.find_elements(By.CSS_SELECTOR, 'input.get-download-submit')
    number_of_repetitions = int(len(all_buttons))
    number = 0
    
    while number < number_of_repetitions:
        
        driver.get('https://spotifymp3.com/')
        sleep(5)
        link_insert = driver.find_element(By.ID,'input')
        link_insert.send_keys(spotify_playlist_url)

        download_button = driver.find_element(By.ID, 'submit')
        download_button.click()
        
        sleep(10)
        
        song_download_buttons = driver.find_elements(By.CSS_SELECTOR, 'input.get-download-submit')
        button = song_download_buttons[number]
        sleep(2)
        button.click()
        sleep(15)
        try: 
            mp3_download_button = driver.find_element(By.CLASS_NAME, 'download-btn')
        except:
            print(f"Failed to download song {number+1}")
        try:
            mp3_download_button.click()
        except:
            print(f"Failed to download song {number+1}")
        sleep(10)
        number += 1

    sleep(10)

download_songs()  
driver.quit()
    