import re
import missingno as msno
import pandas as pd


def gather_data():
    date = re.compile('^\D*(\d*)\s*(.*),\s*.*<br>$')
    date_range = re.compile('^\D*(\d*)-(\d*) (.*),\s*.*<br>$')
    data = {"jan": [], "feb": [], "mar": [], "apr": [],
            "may": [], "jun": [], "jul": [], "aug": [],
            "sep": [], "oct": [], "nov": [], "dec": []}
    with open("Public Holidays by Country - Diversity Resources.html", "r") as file:
        for line in file:
            temp = date.match(line)
            if temp:
                month = temp.group(2)
                day = temp.group(1)
                type = parseMonth(month)
                if type != None: data[type].append(int(day))
            temp = date_range.match(line)
            if temp:
                month = temp.group(3)
                lower_day = int(temp.group(1))
                upper_day = int(temp.group(2))
                type = parseMonth(month)
                for i in range(lower_day, upper_day + 1):
                    if type != None: data[type].append(i)

    return data

def parseMonth(month):
    month = month.lower()
    months = ["january", "february", "march", "april",
              "may", "june", "july", "august", "september",
              "october", "november", "december"]

    for item in months:
        if month == item or month == item[0:3]:
            return item[0:3]

    return None

def processData(data):
    newData = {"jan": {}, "feb": {}, "mar": {}, "apr": {},
               "may": {}, "jun": {}, "jul": {}, "aug": {},
               "sep": {}, "oct": {}, "nov": {}, "dec": {}}
    for item in data:
        for day in data[item]:
            if day in newData[item]:
                newData[item][day] += 1
            else:
                newData[item].update({day: 1})
    return newData



if __name__ == "__main__":
    df = pd.DataFrame(processData(gather_data()))
    print(df)
    msno.matrix(df, inline=True, sparkline=False, filter="top", n=12, labels=True)