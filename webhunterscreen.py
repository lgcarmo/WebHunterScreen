import argparse
import concurrent.futures
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import sqlite3
import os

fd = os.open('/dev/null', os.O_WRONLY)
os.dup2(fd, 2)

parser = argparse.ArgumentParser(description='Requests.')
parser.add_argument('-f', dest='hunt_file', help='-f INPUT_FILE', required=False)
parser.add_argument('-p', dest='hunt_projet', help='-p NAME_PROJECT', required=True)
parser.add_argument('--sqlite', dest='hunt_sqlite', help='--sqlite import SQLITE BY TurboSearch(https://github.com/helviojunior/turbosearch)', required=False)
parser.add_argument('-t', dest='num_threads', type=int, default=4, help='Number of threads to use (default: 4)')

args = parser.parse_args()

def header():
        print('''
 __          __  _     _    _             _            _____                          
 \ \        / / | |   | |  | |           | |          / ____|                         
  \ \  /\  / /__| |__ | |__| |_   _ _ __ | |_ ___ _ _| (___   ___ _ __ ___  ___ _ __  
   \ \/  \/ / _ \ '_ \|  __  | | | | '_ \| __/ _ \ '__\___ \ / __| '__/ _ \/ _ \ '_ \ 
    \  /\  /  __/ |_) | |  | | |_| | | | | ||  __/ |  ____) | (__| | |  __/  __/ | | |
     \/  \/ \___|_.__/|_|  |_|\__,_|_| |_|\__\___|_| |_____/ \___|_|  \___|\___|_| |_|
                                                                                                                                                                      
    ''')

def help_menu():

    print('''
    Usage: webhunterscreen.py [-h] [-f HUNT_FILE] -p HUNT_PROJET
                          [--sqlite HUNT_SQLITE] [-t NUM_THREADS]

    Requests.
    
    options:
      -h, --help                show this help message and exit
      -f File                   -f INPUT_FILE
      -p Folde Name             -p NAME_PROJECT
      --sqlite Sqlite.db        --sqlite import SQLITE BY TurboSearch(https://github.com/helviojunior/turbosearch)
      -t Threads Number to use  Number of threads to use (default: 4)

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

def webhunterscreen(url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--silent")
    chrome_options.add_argument("--log-level=OFF")
    chrome_options.add_argument("--window-size=1920x1080")

    url_name = str(url).split("//")[1].replace("/", "%2F")

    print(url)
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    driver.get(url)
    driver.save_screenshot("{}/{}.png".format(args.hunt_projet, url_name))
    driver.quit()

def process_url(url):
    try:
        webhunterscreen(url)
    except:
        pass

def main():

    os.system(f'rm -Rf {args.hunt_projet}')
    if args.hunt_projet is not None:
        os.mkdir(args.hunt_projet)
        print('[+] Create Path Project')
    else:

        print('-p NameOfPoject')
        help_menu()

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
            with concurrent.futures.ThreadPoolExecutor(max_workers=args.num_threads) as executor:
                executor.map(process_url, file.readlines())

    print('[+] Finished')


main()
