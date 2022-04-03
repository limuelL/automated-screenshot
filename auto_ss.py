from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EXPCON
from selenium.common.exceptions import TimeoutException
import time

EDGE_DRIVER_PATH = "C:/Users/monto/Downloads/edgedriver_win32 (1)/msedgedriver.exe" #your msedgeriver path
MS_EDGE_PATH = "C:/Program Files/Microsoft/Edge/Application/msedge.exe" #your browser path
set_width = 580
set_height = 860

element = 'CSS selector'

edge_options = Options()
edge_options.add_argument("--headless")
edge_options.add_argument(f"--window-size={set_width}, {set_height}")
edge_options.binary_location = MS_EDGE_PATH
driver = webdriver.ChromiumEdge(executable_path=EDGE_DRIVER_PATH, options=edge_options)

urls = ['List of urls']
count = 1

for links in urls:
    try:
        driver.get(links)

        WebDriverWait(driver, 50).until(EXPCON.presence_of_element_located((By.CSS_SELECTOR, element)))
        time.sleep(.2)
        driver.get_screenshot_as_file(f"capture.{count}.png")
        count += 1

    except TimeoutException:
        print('Timeout exception : exceeds Web Driver wait limit!')
    finally:
        driver.close()
