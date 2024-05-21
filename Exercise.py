import random

import requests

# #1
# try:
#     res = requests.get("https://api.github.com/users/avielb/repos", timeout=10)  # Increase timeout to 10 seconds
#     # Process the response
#     # print(res.json())
# except requests.exceptions.Timeout:
#     print("Request timed out. Please try again later.")
#
# repostiories = res.json()
#
# list_of_5_git = []
#
# for repo in repostiories:
#     if "github" in repo["git_url"].lower():
#         list_of_5_git.append(repo["git_url"].lower())
#         if len(list_of_5_git) == 5:
#             break;
# print(list_of_5_git)

#2
# list_of_names = ["roni", "gili", "dana", "shira", "loren"]
# i = 1
# while i <= 3:
#     name = random.choice(list_of_names)
#     try:
#         res = requests.get(f"https://api.agify.io/?name={name}", timeout=10)
#         print(res.json())
#         if res.json()["age"] < 120 and res.json()["age"] > 0:
#             age = res.json()["age"]
#             print(f"{age} is in between 0 to 120")
#     except requests.exceptions.Timeout:
#         print("Request timed out. Please try again later.")
#     i += 1

#3
# list_of_universities = []
# i = 0
# try:
#     res = requests.get("http://universities.hipolabs.com/search?country=Israel", timeout=10)
#     repositories = res.json()
#     for repo in repositories:
#         if "university" in repo["name"].lower():
#             list_of_universities.append(repo["name"])
#             i += 1
#             if len(list_of_universities) >= 5:
#                 break;
# except requests.exceptions.Timeout:
#     print("Request timed out. Please try again later.")
#
# print(list_of_universities)

#4
# from selenium import webdriver
# from time import sleep
# mydriver = webdriver.Chrome()
# mydriver.get("https://www.ycombinator.com/")
# title = mydriver.find_element("xpath", "/html/body/div[1]/div/div[2]/div[1]/div/div/div[1]/div[1]/div[2]")
# actual = title.text
# expected = "Ya Combinator?"

# try:
#     assert actual == expected
#     print("value is true")
# except AssertionError:
#     print("Assertion error occurred. Actual title:", actual)
# else:
#     print("No AssertionError occurred. Title matches the expected title.")
#
# print(title.text)
# sleep(400)


#5
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
timeout = 10

mydriver = webdriver.Chrome()
mydriver.get("https://hub.docker.com/")
title = WebDriverWait(mydriver, timeout).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id=\"mainContainer\"]/div/div/div[1]/div/div/h6'))
)
# title = mydriver.find_element("xpath", "//*[@id=\"mainContainer\"]/div/div/div[1]/div/div/h6")
actual = title.text
expected = "Docker Hub Container Image Library | App Containerization"

try:
    assert actual == expected
except AssertionError as e:
    print("an error has occured", e)

sleep(400)