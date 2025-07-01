import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
from incubyte import load_web_page , validate_mail_id_format, account_creation


def test_case_1():
    assert load_web_page() 


def test_case_2():
    assert validate_mail_id_format() 

def test_case_3():
    assert account_creation()
    




