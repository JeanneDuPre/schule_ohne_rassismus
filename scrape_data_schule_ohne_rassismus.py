import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

data = []

# Create a ChromeService object and specify the executable path
chrome_service = ChromeService(executable_path=r'C:\Program Files\chromedriver.exe')

with webdriver.Chrome(service=chrome_service) as driver:
    driver.get("https://www.schule-ohne-rassismus.org/netzwerk/courage-schulen/")

    max_clicks = 250 # TODO 1000 Clicks eintragen -> 200-> 2015 400 -> zu viel 
    click_count = 0
    while click_count < max_clicks:
        try:
            # Wait for the "Mehr laden" link to become clickable
            element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Mehr laden"))
            )
            
            # Scroll to the "Mehr laden" link using JavaScript
            driver.execute_script("arguments[0].scrollIntoView();", element)
            
            # Click the "Mehr laden" link
            element.click()
            time.sleep(5)  # Add a sleep to allow the content to load
            
            click_count += 1
        except Exception as e:
            if click_count >= max_clicks:
                break  # Exit the loop if the desired number of clicks is reached
            else:
                continue  # Continue the loop if there was an error but not enough clicks

    # Now that you have loaded all the content, you can scrape the data as before

    names = driver.find_elements(By.CSS_SELECTOR, '.card__entry.card__entry--title')
    seits = driver.find_elements(By.CSS_SELECTOR, '.card__entry.card__entry--date')
    adresses = driver.find_elements(By.CSS_SELECTOR, '.card__entry.card__entry--address')
    pates = driver.find_elements(By.CSS_SELECTOR, '.card__entry.card__entry--sponsor')
    bundeslands = driver.find_elements(By.CSS_SELECTOR, '.card__entry.card__entry--type-state')
    
    for i in range(len(names)):
        name = names[i].text
        seit = seits[i].text
        adresse = adresses[i].text
        pate = pates[i].text
        bundesland = bundeslands[i].text

        data.append({
            "seit": seit,
            "name": name,
            "adresse": adresse,
            "pate": pate,
            "bundesland": bundesland
        })

# Create a DataFrame from the collected data
df = pd.DataFrame(data)
df.to_csv('probe_250.csv', index=False)
