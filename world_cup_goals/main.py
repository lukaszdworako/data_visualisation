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
    options = Options()
    options.add_argument("headless")
    browser = webdriver.Chrome('./chromedriver', chrome_options=options)
    for item in match_ids:
        if not os.path.exists('game_files/' + str(item)):
            url = "https://www.tsn.ca/fifa-world-cup/game/" + str(item)
            browser.get(url)
            match = 'game_files/' + str(item)
            success = open(match, 'w').write(browser.page_source)
            if success:
                print("File " + match + " created")
            else:
                print("Failed to create a file for match id: " + item)
        else:
            print("File " + str(item) + " already exists")

# def fetch_match_data(match_id):
#     # pre-process entire page down to relevant table


if __name__ == "__main__":
    match_ids_list = get_match_ids()
    download_pages(match_ids_list)
    # match_data = []
    # for item in match_ids_list:
    #     match_data.append(download_pages(item))
    # df = pd.DataFrame()
    # print(df)
