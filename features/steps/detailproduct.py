from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import allure

@given(u'Masukan username dan password')
def step_impl(context):
    context.driver=webdriver.Firefox()
    context.driver.get('https://www.saucedemo.com/')
    context.driver.find_element(By.ID,'user-name').send_keys('standard_user')
    context.driver.find_element(By.ID,'password').send_keys('secret_sauce')
    


@when(u'Tekan tombol login')
def step_impl(context):
    context.driver.find_element(By.ID,'login-button').click()


@when(u'Masuk dan pilih cek detail produk')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//div[@data-test='inventory-item-name']").click()

@then(u'Menampilkan deskripsi produk')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//div[@class='inventory_details_desc large_size']").is_displayed()
    context.driver.quit()


@given(u'Masuk kedalam akun')
def step_impl(context):
    context.driver=webdriver.Firefox()
    context.driver.get('https://www.saucedemo.com/')
    context.driver.find_element(By.ID,'user-name').send_keys('standard_user')
    context.driver.find_element(By.ID,'password').send_keys('secret_sauce')
    context.driver.find_element(By.ID,'login-button').click()


@when(u'cek detail produk')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//div[@data-test='inventory-item-name']").click()


@when(u'Tekan tombol Back to Products')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//button[@data-test='back-to-products']").click()


@then(u'Kembali ke dalam daftar produk')
def step_impl(context):
    produk=context.driver.find_element(By.XPATH,"//*[@id='header_container']/div[2]/span")
    assert 'Products' in produk.text
    context.driver.quit()