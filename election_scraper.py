"""
election_scraper.py: třetí projekt do Engeto Online Python Akademie

author: Michal Janků
email: michal.janku@cdv.cz
discord: Michal J.#5035
"""

import sys
import csv
import requests
from bs4 import BeautifulSoup


def election_scraper(url: str, output_file: str):
    print("LET'S GO!")
    try:
        soup = process_response(url)
    except requests.exceptions.MissingSchema:
        # will report an error if the order of the arguments is wrong
        print("Wrong URL, please check the correct order of function arguments.")
        exit()
    else:
        list_of_codes = create_list_of_codes(soup)
        try:
            table_of_results = create_table(url, list_of_codes, soup)
        except AttributeError:
            # will report an error if the url is wrong
            print("Wrong URL, please check it and run the program again.")
            exit()
        else:
            table_to_csv(table_of_results, output_file)
            print(f"ELECTION RESULTS WAS SAVED TO FILE: {output_file}")
            print("EXITING election_scraper...")
            exit()


def create_table(url: str, list_of_codes: list, soup) -> list:
    # create a table and add rows to it
    code_url = find_first_code_url(soup)
    table = [create_columns(url, soup)]
    for code_number in list_of_codes:
        soup_l = location_url_response(get_location_url(url, code_number, code_url))
        row = [code_number] + create_row(soup_l)
        table.append(row)
    return table


def process_response(url: str) -> BeautifulSoup:
    """ send a request to the appropriate address 'url' and parse
    the returned response with the help of Beautifulsoup"""
    response = requests.get(url)
    print(f"DOWNLOADING DATA FROM THE SELECTED URL: {url}")
    return BeautifulSoup(response.text, "html.parser")


def create_list_of_codes(soup) -> list:
    # create list of codes
    code_list = []
    for code in soup.find_all(name="td", class_="cislo"):
        code_list.append(code.getText())
    return code_list


def find_first_code_url(soup) -> str:
    # return the url of the first code (location) in the table
    code_td = soup.find(name="td", class_="cislo")
    code_a = code_td.find(name="a")
    return code_a.get("href")


def get_location_url(url: str, code_number: str, code_url: str) -> str:
    # assemble the url of location
    return url[0:35] + code_url[:-18] + code_number + code_url[-12:]


def location_url_response(location_url: str) -> BeautifulSoup:
    """ send a request to the appropriate 'url' address of location
    and parse the returned response with the help of Beautifulsoup"""
    response_l = requests.get(location_url)
    return BeautifulSoup(response_l.text, "html.parser")


def create_columns(url: str, soup) -> list:
    # create column headers
    soup_l = location_url_response(url[0:35] + find_first_code_url(soup))
    columns = ["Code", "Location", "Registered", "Envelopes", "Valid"]
    for party in soup_l.find_all(name="td", class_="overflow_name"):
        # add parties from appropriate location
        columns.append(party.getText())
    return columns


def find_location(soup_l) -> str:
    # find and return name of location
    location_h3 = soup_l.find_all(name="h3")
    location_text = location_h3[2].getText().strip()
    return location_text[6:]


def find_registered(soup_l) -> str:
    # find and return the number of registered voters
    registered_td = soup_l.find(name="td", headers="sa2")
    return registered_td.getText()


def find_envelopes(soup_l) -> str:
    # find and return the number of issued envelopes
    envelopes_td = soup_l.find(name="td", headers="sa3")
    return envelopes_td.getText()


def find_valid(soup_l) -> str:
    # find and return the number of valid votes
    valid_td = soup_l.find(name="td", headers="sa6")
    return valid_td.getText()


def find_votes(soup_l) -> list:
    # find and return the number of votes for each party
    votes_list = []
    votes_t1 = soup_l.find_all(name="td", headers="t1sa2 t1sb3")
    for votes in votes_t1:
        votes_list.append(votes.getText())
    votes_t2 = soup_l.find_all(name="td", headers="t2sa2 t2sb3")
    for votes in votes_t2:
        votes_list.append(votes.getText())
    return votes_list


def create_row(soup_l) -> list:
    # create a table row and add individual items to it
    table_row = [find_location(soup_l), find_registered(soup_l), find_envelopes(soup_l),
                 find_valid(soup_l)] + find_votes(soup_l)
    return table_row


def table_to_csv(table_of_results: list, output_file: str):
    # save table to CSV file
    with open(output_file, "w", encoding="utf-8", newline="") as csv_file:
        csv_writer = csv.writer(csv_file, dialect="excel")
        csv_writer.writerows(table_of_results)


if len(sys.argv) != 3:
    print("Two artguments are not specified.", "Write: URL, 'file'.csv", sep="\n")
else:
    election_scraper(sys.argv[1], sys.argv[2])
