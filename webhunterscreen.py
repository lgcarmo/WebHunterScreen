import argparse
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

parser = argparse.ArgumentParser(description='Requests.')
parser.add_argument('-f', dest='hunt_file', help='-f INPUT_FILE', required=True)
parser.add_argument('-p', dest='hunt_projet', help='-p NAME_PROJECT', required=True)

args = parser.parse_args()

os.mkdir('output/'+args.hunt_projet)

file = open(args.hunt_file,'r')
for url in file:

	url_name = str(url).split("//")[1].replace("/", "%2F")
	chrome_options = Options()
	chrome_options.add_argument("--headless")
	chrome_options.add_argument("--silent")
	chrome_options.add_argument("--window-size=1920x1080")


	DRIVER = 'chromedriver'
	driver = webdriver.Chrome(DRIVER, chrome_options=chrome_options)
	driver.get(url)
	driver.save_screenshot("output/{}/{}.png".format(args.hunt_projet,url_name))
	driver.quit()