from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import allure

@given(u'Melakukan Login')
def step_impl(context):
    context.driver=webdriver.Firefox()
    context.driver.get('https://www.saucedemo.com/')
    context.driver.find_element(By.ID,'user-name').send_keys('standard_user')
    context.driver.find_element(By.ID,'password').send_keys('secret_sauce')
    context.driver.find_element(By.ID,'login-button').click()
    assert context.driver.find_element(By.XPATH,"//span[text()='Products']").is_enabled()


@when(u'Memilih produk')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//div[text()='Sauce Labs Backpack']").is_enabled()


@when(u'Menekan tombol add to cart')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//button[@id='add-to-cart-sauce-labs-backpack']").click()


@then(u'Menampilkan angka di icon cart')
def step_impl(context):
    assert context.driver.find_element(By.XPATH,"//span[@data-test='shopping-cart-badge' and text()='1']").is_enabled()
    context.driver.quit()





@when(u'Memilih dan tekan tombol cart')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//button[@id='add-to-cart-sauce-labs-backpack']").click()


@when(u'Tekan tombol remove')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//button[@data-test='remove-sauce-labs-backpack' and text()='Remove']").click()

@then(u'Angka di icon cart berkurang')
def step_impl(context):
    assert context.driver.find_element(By.XPATH,"//a[@class='shopping_cart_link']").is_enabled()
    context.driver.quit()


@when(u'Tekan icon cart')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//a[@data-test='shopping-cart-link']").click()


@then(u'Menampilkan produk yang ditambah')
def step_impl(context):
    assert context.driver.find_element(By.XPATH,"//div[@class='inventory_item_name' and @data-test='inventory-item-name']").is_enabled()
    context.driver.quit()


@given(u'Masuk dan pilih produk')
def step_impl(context):
    context.driver=webdriver.Firefox()
    context.driver.get('https://www.saucedemo.com/')
    context.driver.find_element(By.ID,'user-name').send_keys('standard_user')
    context.driver.find_element(By.ID,'password').send_keys('secret_sauce')
    context.driver.find_element(By.ID,'login-button').click()
    assert context.driver.find_element(By.XPATH,"//span[text()='Products']").is_enabled()
    context.driver.find_element(By.XPATH,"//button[@id='add-to-cart-sauce-labs-backpack']").click()


@when(u'Tekan icon dan muncul produk yang ditambah')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//a[@data-test='shopping-cart-link']").click()
    assert context.driver.find_element(By.XPATH,"//div[@class='inventory_item_name' and @data-test='inventory-item-name']").is_enabled()
    


@when(u'Tekan tombol Continue shopping')
def step_impl(context):
    context.driver.find_element(By.NAME,"continue-shopping").click()


@then(u'Kembali ke daftar produk')
def step_impl(context):
    assert context.driver.find_element(By.XPATH,"//span[text()='Products']").is_enabled()
    context.driver.quit()