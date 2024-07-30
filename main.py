import requests
import warnings
import random
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from colorama import Fore, Style, init
from pystyle import Center, Colors, Colorate
import os
import time
import chromedriver_autoinstaller
from selenium.common.exceptions import WebDriverException

# Initialize colorama
init(autoreset=True)

warnings.filterwarnings("ignore", category=DeprecationWarning)

def save_settings(twitch_username, set_160p):
    with open('settings.txt', 'w') as file:
        file.write(f"Twitch Username: {twitch_username}\n")
        file.write(f"Set 160p: {set_160p}\n")

def load_settings():
    try:
        with open('settings.txt', 'r') as file:
            lines = file.readlines()
            if len(lines) >= 2:
                twitch_username = lines[0].split(': ')[1].strip()
                set_160p = lines[1].split(': ')[1].strip()
                return twitch_username, set_160p
    except:
        pass
    return None, None

def set_stream_quality(driver, quality):
    if quality == "yes":
        element_xpath = "//div[@data-a-target='player-overlay-click-handler']"
        element = driver.find_element(By.XPATH, element_xpath)
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
        settings_button = driver.find_element(By.XPATH, "//button[@aria-label='Settings']")
        settings_button.click()
        wait = WebDriverWait(driver, 10)
        quality_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Quality']")))
        quality_option.click()
        time.sleep(15)
        quality_levels = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'video-quality-option')]")))
        target_quality = "160p"
        for level in quality_levels:
            if target_quality in level.text:
                level.click()
                break

def print_announcement():
    try:
        announcement = "Welcome to the new version of our script! Visit guns.lol/f4g for more information."
        return announcement
    except:
        print("Could not retrieve announcement.\n")

def fade_print(text):
    # Function to print text with a cyan to dark blue fade gradient
    gradient = Colorate.Vertical(Colors.cyan_to_blue, text)
    print(gradient)

def main():
    fade_print(print_announcement())

    twitch_username, set_160p = load_settings()

    os.system(f"title Germanized - Twitch Viewer Bot")

    fade_print("""
░██████╗░███████╗██████╗░███╗░░░███╗██╗░░░██╗██╗███████╗░██╗░░░░░░░██╗
██╔════╝░██╔════╝██╔══██╗████╗░████║██║░░░██║██║██╔════╝░██║░░██╗░░██║
██║░░██╗░█████╗░░██████╔╝██╔████╔██║╚██╗░██╔╝██║█████╗░░░╚██╗████╗██╔╝
██║░░╚██╗██╔══╝░░██╔══██╗██║╚██╔╝██║░╚████╔╝░██║██╔══╝░░░░████╔═████║░
╚██████╔╝███████╗██║░░██║██║░╚═╝░██║░░╚██╔╝░░██║███████╗░░╚██╔╝░╚██╔╝░
░╚═════╝░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░░╚═╝░░░╚═╝╚══════╝░░░╚═╝░░░╚═╝░░
    """)

    announcement = print_announcement()
    fade_print("")
    fade_print("ANNOUNCEMENT")
    fade_print(f"{announcement}")
    fade_print("")
    fade_print("")

    proxy_servers = ['https://www.blockaway.net', 'https://www.croxyproxy.com', 'https://www.croxyproxy.rocks', 'https://www.croxy.network', 'https://www.croxy.org', 'https://www.youtubeunblocked.live', 'https://www.croxyproxy.net']
    def selectRandom(proxy_servers):
        return random.choice(proxy_servers)

    proxy_url = selectRandom(proxy_servers)

    fade_print("Proxy servers are randomly selected every time")
    if twitch_username is None or set_160p is None:
        
        twitch_username = input(Colorate.Vertical(Colors.green_to_blue, "Enter your channel name (e.g Germanized): "))
        set_160p = input(Colorate.Vertical(Colors.purple_to_red,"Do you want to set the stream quality to 160p? (yes/no): "))

        save_settings(twitch_username, set_160p)

    else:
        use_settings = input(Colorate.Vertical(Colors.green_to_blue, "Do you want to use your saved settings? (yes/no): "))
        if use_settings.lower() == "no":
            
            twitch_username = input(Colorate.Vertical(Colors.green_to_blue, "Enter your channel name (e.g Germanized): "))
            set_160p = input(Colorate.Vertical(Colors.purple_to_red,"Do you want to set the stream quality to 160p? (yes/no): "))

            save_settings(twitch_username, set_160p)
        
    proxy_count = int(input(Colorate.Vertical(Colors.cyan_to_blue, "How many proxy sites do you want to open? (Viewer to send)")))

    os.system("cls")
    fade_print("""
░██████╗░███████╗██████╗░███╗░░░███╗██╗░░░██╗██╗███████╗░██╗░░░░░░░██╗
██╔════╝░██╔════╝██╔══██╗████╗░████║██║░░░██║██║██╔════╝░██║░░██╗░░██║
██║░░██╗░█████╗░░██████╔╝██╔████╔██║╚██╗░██╔╝██║█████╗░░░╚██╗████╗██╔╝
██║░░╚██╗██╔══╝░░██╔══██╗██║╚██╔╝██║░╚████╔╝░██║██╔══╝░░░░████╔═████║░
╚██████╔╝███████╗██║░░██║██║░╚═╝░██║░░╚██╔╝░░██║███████╗░░╚██╔╝░╚██╔╝░
░╚═════╝░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░░╚═╝░░░╚═╝╚══════╝░░░╚═╝░░░╚═╝░░
    """)
    fade_print('')
    fade_print('')
    fade_print("Viewers Send. Please don't hurry. If the viewers do not arrive, turn it off and on and do the same operations")

    # Install ChromeDriver automatically
    chromedriver_autoinstaller.install()

    chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
    driver_path = 'chromedriver.exe'

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome_options.add_argument('--disable-logging')
    chrome_options.add_argument("--lang=en")
    chrome_options.add_argument('--log-level=3')
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_argument("--mute-audio")
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)

    driver.get(proxy_url)

    for i in range(proxy_count):
        random_proxy_url = selectRandom(proxy_servers)  # Select a random proxy server for this tab
        driver.execute_script("window.open('" + random_proxy_url + "')")
        driver.switch_to.window(driver.window_handles[-1])
        
        try:
            driver.get(random_proxy_url)
            text_box = driver.find_element(By.ID, 'url')
            text_box.send_keys(f'www.twitch.tv/{twitch_username}')
            text_box.send_keys(Keys.RETURN)
            if set_160p.lower() == 'yes':
                set_stream_quality(driver, '160p')
            time.sleep(5)
        except WebDriverException as e:
            print(f"Error loading URL {random_proxy_url}: {e}")
            continue

    print(f"Finished opening {proxy_count} proxies for {twitch_username}'s broadcast.\nIf you want to support us, you can donate to support me.\n")

if __name__ == "__main__":
    main()
