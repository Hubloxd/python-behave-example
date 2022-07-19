from behave import when, then, given
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


@given(u'na stronie blackjacka')
def step_imp(context):
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    context.driver.get("http://localhost:8000/blackjack/")
    sleep(1)
    print(context.driver.current_url)
    assert context.driver.current_url == "http://localhost:8000/blackjack/"


@when(u'wciśnięty przycisk play')
def step_impl(context):
    context.driver.find_element(By.XPATH, value='//*[@id="playc-start"]').click()
    sleep(1)


@then(u'zostają poprawnie rozdane karty')
def step_impl(context):
    # fetch player data, split it and strip to find the hand value
    p_hand = int(context.driver.find_element(By.XPATH, value='//*[@id="play-data"]').text.split('-')[-1].strip())
    assert 21 > p_hand > 0


@then(u'webdriver się wyłącza')
def step_impl(context):
    context.driver.close()


if __name__ == '__main__':
    # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # driver.get("http://localhost:8000/blackjack/")
    # sleep(1)
    # driver.find_element(By.XPATH, value='//*[@id="playc-start"]').click()
    # p_hand = int(driver.find_element(By.XPATH, value='//*[@id="play-data"]').text.split('-')[-1].strip())
    # print(p_hand)
    pass
