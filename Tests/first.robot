*** Settings ***
Documentation    Light Test Suite For HungerStation app
Library    ../Keywords/CommonKeywords.py
Library    ../Keywords/HomeKeywords.py

Test Setup    Launch HungerStation Application
Test Teardown    Close HungerStation Application

*** Test Cases ***
Navigate To Home Screen Of HungerStation
    [Tags]    test
    Set Delivery Address    Riyadh Park
    Verify Home Screen Displayed Successfully

    Log    test
