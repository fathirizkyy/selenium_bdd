from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import allure

@when(u'Menggunakan username locked_out_user dan password valid')
def step_impl(context):
    context.driver.find_element(By.ID,'user-name').send_keys('locked_out_user')
    context.driver.find_element(By.ID,'password').send_keys('secret_sauce')


@then(u'Muncul pesan error Epic sadface: Sorry, this user has been locked out')
def step_impl(context):
    element=context.driver.find_element(By.XPATH,"//h3[@data-test='error' and text()='Epic sadface: Sorry, this user has been locked out.']")
    assert 'Epic sadface: Sorry, this user has been locked out.' in element.text
    context.driver.quit()