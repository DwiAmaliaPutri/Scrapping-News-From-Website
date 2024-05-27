from selenium import webdriver
import sys, getopt
import argparse
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
full_text = []

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--infile', default='', help='input filename')
    parser.add_argument('-o', '--outfile', default='', help='output filename')
    return parser.parse_args()

def main():
    args = parse_args()
    outfile = args.outfile
    infile =args.infile
    
    with open(infile) as f:
        content = f.read().splitlines()
    f.close()
    
    f = open(outfile, "w", encoding='utf-8')
    for u in content[0:2]:
        driver.get(u)
        elems = driver.find_element(By.TAG_NAME,'body').text
        filtered_text = [line for line in elems.split('\n') if len(line.split()) >= 5]
        full_text.append(filtered_text)
    
    f.write(str(full_text))
    print(full_text) 
    driver.close()
    f.close()

main()