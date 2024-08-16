from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import allure


@given(u'Tambahkan produk ke keranjang dan tekan tombol checkout')
def step_impl(context):
    context.driver=webdriver.Firefox()
    context.driver.get('https://www.saucedemo.com/')
    context.driver.find_element(By.ID,'user-name').send_keys('standard_user')
    context.driver.find_element(By.ID,'password').send_keys('secret_sauce')
    context.driver.find_element(By.ID,'login-button').click()
    assert context.driver.find_element(By.XPATH,"//span[text()='Products']").is_enabled()
    context.driver.find_element(By.XPATH,"//button[@id='add-to-cart-sauce-labs-backpack']").click()
    context.driver.find_element(By.XPATH,"//a[@data-test='shopping-cart-link']/span[@data-test='shopping-cart-badge']").click()
    context.driver.find_element(By.ID,'checkout').click()

@when(u'Isi seluruh form informasi')
def step_impl(context):
    context.driver.find_element(By.ID,'first-name').send_keys('udin')
    context.driver.find_element(By.ID,'last-name').send_keys('udin')
    context.driver.find_element(By.ID,'postal-code').send_keys('11111')
    context.driver.find_element(By.ID,'continue').click()


@when(u'Tekan tombol Finish')
def step_impl(context):
    context.driver.find_element(By.ID,'finish').click()


@then(u'Menampilkan pesan THANK YOU FOR YOUR ORDER')
def step_impl(context):
    assert context.driver.find_element(By.XPATH,"//h2[contains(text(), 'Thank you for your order!')]").is_enabled()
    context.driver.quit()


@when(u'Isi seluruh form informasi kecuali kolom firts name')
def step_impl(context):
    context.driver.find_element(By.ID,'first-name').send_keys('')
    context.driver.find_element(By.ID,'last-name').send_keys('udin')
    context.driver.find_element(By.ID,'postal-code').send_keys('11111')
    

@when(u'Tekan tombol Continue')
def step_impl(context):
    context.driver.find_element(By.ID,'continue').click()

@then(u'Menampilkan allert Error: First Name is required')
def step_impl(context):
    assert context.driver.find_element(By.XPATH,"//h3[contains(text(), 'Error: First Name is required')]").is_enabled()
    context.driver.quit()