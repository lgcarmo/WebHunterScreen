import argparse
import concurrent.futures
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import sqlite3
import os
import time


fd = os.open('/dev/null', os.O_WRONLY)
os.dup2(fd, 2)

parser = argparse.ArgumentParser(description='Requests.')
parser.add_argument('-f', dest='hunt_file', help='-f INPUT_FILE', required=False)
parser.add_argument('-p', dest='hunt_projet', help='-p NAME_PROJECT', required=True)
parser.add_argument('--sqlite', dest='hunt_sqlite', help='--sqlite import SQLITE BY TurboSearch(https://github.com/helviojunior/turbosearch)', required=False)
parser.add_argument('-t', dest='num_threads', type=int, default=4, help='Number of threads to use (default: 4)')
parser.add_argument('--headless', dest='headless', action='store_true', help='Run browser in headless mode')
parser.add_argument('--delay', dest='delay', type=int, default=2, help='Delay in seconds before screenshot (default: 2)')


args = parser.parse_args()

def header():
    print('''
 __          __  _     _    _             _            _____                          
 \\ \\        / / | |   | |  | |           | |          / ____|                         
  \\ \\  /\\  / /__| |__ | |__| |_   _ _ __ | |_ ___ _ _| (___   ___ _ __ ___  ___ _ __  
   \\ \\/  \\/ / _ \\ '_ \\|  __  | | | | '_ \\| __/ _ \\ '__\\___ \\ / __| '__/ _ \\/ _ \\ '_ \\ 
    \\  /\\  /  __/ |_) | |  | | |_| | | | | ||  __/ |  ____) | (__| | |  __/  __/ | | |
     \\/  \\/ \\___|_.__/|_|  |_|\\__,_|_| |_|\\__\\___|_| |_____/ \\___|_|  \\___|\\___|_| |_|
                                                                                                      
    ''')

def help_menu():
    print('''
    Usage: webhunterscreen.py [-h] [-f HUNT_FILE] -p HUNT_PROJET
                              [--sqlite HUNT_SQLITE] [-t NUM_THREADS] [--headless]

    Requests.
    
    options:
      -h, --help                show this help message and exit
      -f File                   -f INPUT_FILE
      -p Folder Name            -p NAME_PROJECT
      --sqlite Sqlite.db        --sqlite import SQLITE BY TurboSearch(https://github.com/helviojunior/turbosearch)
      -t Threads Number         Number of threads to use (default: 4)
      --headless                Run browser in headless mode (no GUI)
      --delay SECONDS           Delay in seconds before screenshot (default: 2)

    ''')

def import_dbstats():
    try:
        urls = []
        conn = sqlite3.connect(args.hunt_sqlite)
        cursor = conn.execute("SELECT uri FROM stats;")
        for row in cursor:
            if row[0] not in urls:
                urls.append(row[0])
        conn.close()
        return urls
    except:
        print('Database does not exist')
from selenium.webdriver.chrome.service import Service  # adicione esse import no topo

def webhunterscreen(url):
    chrome_options = Options()
    if args.headless:
        chrome_options.add_argument("--headless")
    chrome_options.add_argument("--silent")
    chrome_options.add_argument("--log-level=OFF")
    chrome_options.add_argument("--window-size=1920x1080")

    try:
        url_name = str(url).split("//")[1].replace("/", "%2F")
    except IndexError:
        url_name = url.replace("/", "%2F")

    print(f"[+] Acessando: {url}")
    try:
        service = Service(ChromeDriverManager().install())  # forma correta com Selenium 4+
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.get(url)
        time.sleep(args.delay)
        screenshot_path = f"{args.hunt_projet}/{url_name}.png"
        driver.save_screenshot(screenshot_path)
        print(f"[✓] Screenshot salvo: {screenshot_path}")
        driver.quit()
    except Exception as e:
        print(f"[!] Falha ao capturar {url}: {e}")



def process_url(url):
    try:
        url = url.strip()
        if not url.startswith("http"):
            url = "http://" + url
        webhunterscreen(url)
    except Exception as e:
        print(f"[!] Erro ao processar {url}: {e}")


def main():
    os.system(f'rm -Rf {args.hunt_projet}')
    if args.hunt_projet is not None:
        os.mkdir(args.hunt_projet)
        print('[+] Create Path Project')
    else:
        print('-p NameOfProject')
        help_menu()
        return

    if args.hunt_sqlite is not None:
        header()
        try:
            print('[+] Start ScreenShot Sqlite')
            with concurrent.futures.ThreadPoolExecutor(max_workers=args.num_threads) as executor:
                executor.map(process_url, import_dbstats())
        except:
            pass
    elif args.hunt_file is not None:
        header()
        print('[+] Start ScreenShot Project File')
        with open(args.hunt_file, 'r') as file:
            urls = file.readlines()
            with concurrent.futures.ThreadPoolExecutor(max_workers=args.num_threads) as executor:
                executor.map(process_url, urls)

    print('[+] Finished')

main()
