import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os.path

def get_match_ids():
    match_id = re.compile('^.*https:\/\/www.tsn.ca\/fifa-world-cup\/game\/(\d*).*$')
    match_ids = []
    for i in range(1, 4):
        file_name = "week_" + str(i) + "_tsn_world_cup.html"
        with open(file_name, "r") as file:
            for line in file:
                temp = match_id.match(line)
                if temp:
                    temp_id = int(temp.group(1))
                    if temp_id not in match_ids:
                        match_ids.append(temp_id)
    return match_ids
def download_pages(match_ids):
    num_downloaded = 0
    options = Options()
    options.add_argument("headless")
    browser = webdriver.Chrome('./chromedriver', chrome_options=options)
    for item in match_ids:
        if not os.path.exists('game_files/' + str(item)):
            url = "https://www.tsn.ca/fifa-world-cup/game/" + str(item)
            browser.get(url)
            start = browser.page_source.find('<div class="soccer-game-summary game-page">')
            end = browser.page_source.find('<div class="game-page-box-stats">')
            text = browser.page_source[start:end]
            text = text.replace("\n", "")
            text = text.replace("<li", "\n<li")
            text = text.replace("</li>", "</li>\n")
            match = 'game_files/' + str(item)
            success = open(match, 'w').write(text)
            if success:
                print("File " + match + " created")
                num_downloaded += 1
            else:
                print("Failed to create a file for match id: " + str(item))
        else:
            print("File " + str(item) + " already exists")
    return num_downloaded
def fetch_match_data():
    # pre-process entire page down to relevant table
    ot_event = re.compile('^<li.*><div class="logo logo-flags flags-(\w*)-.*>\s*<div class="soccer-summary__minutes">\s*(\d*)(<span>\+(\d*)<\/span>)?.*<i class="soccer-summary-icon__(\w*)">.*<div class="soccer-summary-player">([\w\s]*)<\/div>.*$')
    

if __name__ == "__main__":
    match_ids_list = get_match_ids()
    num_downloaded = download_pages(match_ids_list)
    print("Done downloading, downloaded a total of: " + str(num_downloaded))
    fetch_match_data()
    # match_data = []
    # for item in match_ids_list:
    #     match_data.append(download_pages(item))
    # df = pd.DataFrame()
    # print(df)
