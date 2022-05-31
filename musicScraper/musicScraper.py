### NOT WORKING, the specified site kicks you off, suspecting too bot like ###


# import module
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = 'https://www.genmp3.net/'
playlist_link = 'https://soundcloud.com/michael-huang-723382387/sets/all-likes'
download_dir = r"Z:\Music\soundcloudDownloads"
desired_caps = {'prefs': {'download': {'default_directory': download_dir}}}
chrome_driver_path = r"D:\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)
# driver = webdriver.Chrome(ChromeDriverManager(
# ).install(), desired_capabilities=desired_caps)

driver.get(link)

# Maximize the window and let code stall
# for 10s to properly maximise the window.
driver.maximize_window()
# input link and redirect to download link pg
time_to_sleep = 3
# try:
# time.sleep(time_to_sleep)
input_xpath = "/html/body/div[2]/form/div/input"
print(f"looking for {input_xpath}")

input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, input_xpath))
)
print(f"sending key to {input_xpath}")

input.send_keys(playlist_link)
button_xpath = "/html/body/div[2]/form/div/div/button"
print(f"looking for {button_xpath}")

goButton = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, button_xpath)))
print(f"clicking {button_xpath}")
# time.sleep(time_to_sleep)
goButton.click()



    # time.sleep(time_to_sleep+2)
link_xpath = "//a[contains(@id, 'mp3Down')]"
# link_xpath = "//span[contains(@role, 'status')]"
print(f"looking for {link_xpath}")
links = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, link_xpath)))
print(f"{link_xpath} found")
for link in links:
    link.click()
driver.quit()
# except Exception as e:
#     print(e)
#     driver.quit()
