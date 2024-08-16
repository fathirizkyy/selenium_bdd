from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import allure


@then(u'Periksa jumlah produk')
def step_impl(context):
    angka=context.driver.find_element(By.XPATH,"//span[text()='1']")
    assert '1' in angka.text
    context.driver.quit()