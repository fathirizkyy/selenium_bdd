from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import allure

@given(u'Masuk ke login page')
def step_impl(context):
    context.driver=webdriver.Firefox()
    context.driver.get('https://www.saucedemo.com/')


@when(u'Memasukan username dan password valid')
def step_impl(context):
    context.driver.find_element(By.ID,'user-name').send_keys('standard_user')
    context.driver.find_element(By.ID,'password').send_keys('secret_sauce')


@when(u'Menekan tombol login')
def step_impl(context):
    context.driver.find_element(By.ID,'login-button').click()


@then(u'User berhasil masuk')
def step_impl(context):
    assert context.driver.find_element(By.XPATH,"//span[text()='Products']").is_enabled()
    context.driver.quit()


@when(u'Memasukan password invalid')
def step_impl(context):
    context.driver.find_element(By.ID,'user-name').send_keys('standard_user')
    context.driver.find_element(By.ID,'password').send_keys('123456')


@then(u'menampilkan pesan Epic sadface: Username and password do not match any user in this service')
def step_impl(context):
    assert context.driver.find_element(By.XPATH, "//h3[contains(text(), 'Epic sadface: Username and password do not match any user in this service')]").is_enabled()
    context.driver.quit()
    


@when(u'Memasukan username dan password invalid')
def step_impl(context):
    context.driver.find_element(By.ID,'user-name').send_keys('123456')
    context.driver.find_element(By.ID,'password').send_keys('123456')


@when(u'biarkan username dan password kosong')
def step_impl(context):
    context.driver.find_element(By.ID,'user-name').send_keys('')
    context.driver.find_element(By.ID,'password').send_keys('')


@then(u'Epic sadface: Username is required')
def step_impl(context):
    assert context.driver.find_element(By.XPATH, "//h3[contains(text(), 'Epic sadface: Username is required')]").is_enabled()
    context.driver.quit()