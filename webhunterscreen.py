import argparse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import sqlite3
import os # if you have not already done this

#supress chome erro 2>/dev/null
fd = os.open('/dev/null',os.O_WRONLY)
os.dup2(fd,2)



parser = argparse.ArgumentParser(description='Requests.')
parser.add_argument('-f', dest='hunt_file', help='-f INPUT_FILE', required=False)
parser.add_argument('-p', dest='hunt_projet', help='-p NAME_PROJECT', required=True)
parser.add_argument('--sqlite', dest='hunt_sqlite', help='--sqlite import SQLITE BY TurboSearch(https://github.com/helviojunior/turbosearch)', required=False)


args = parser.parse_args()



def import_dbstats():
    try:
        urls = []
        conn = sqlite3.connect(args.hunt_sqlite)

        cursor = conn.execute("SELECT uri FROM stats;")
        for row in cursor:
           #print(f'{row[1]}')
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
    #driver = webdriver.Chrome(driver, chrome_options=chrome_options)
    driver.get(url)
    driver.save_screenshot("{}/{}.png".format(args.hunt_projet,url_name))
    driver.quit()

def main():
    os.system(f'rm -Rf {args.hunt_projet}')
    if args.hunt_projet is not None:

        os.mkdir(args.hunt_projet)
        print('[+] Create Path Project')

    else:
        print('-p NameOfPoject')

    if args.hunt_sqlite is not None:
        try:
            print('[+] Start ScreenShot Sqlite')
            for uri in import_dbstats():
                try:
	                webhunterscreen(uri)
                except:
                    pass

        except:
            pass

    elif args.hunt_file is not None:
        print('[+] Start ScreenShot Project File')
        file = open(args.hunt_file,'r')
        for url in file:
            try:
                webhunterscreen(url)
            except:
                pass

    print('[+] Finished')



main()
