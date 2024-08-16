from behave import *
from selenium import webdriver
from selenium.webdriver.support.ui import Select,WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import allure

def clean_price(price_text):
    # Menghapus simbol mata uang dan spasi, lalu mengubah menjadi float
    return float(price_text.replace('$', '').strip())

@given(u'Login dengan akun Valid')
def step_impl(context):
    context.driver=webdriver.Firefox()
    context.driver.get('https://www.saucedemo.com/')
    context.driver.find_element(By.ID,'user-name').send_keys('standard_user')
    context.driver.find_element(By.ID,'password').send_keys('secret_sauce')
    context.driver.find_element(By.ID,'login-button').click()


@when(u'Masuk kedalam akun')
def step_impl(context):
    assert context.driver.find_element(By.XPATH,"//span[text()='Products']").is_enabled()


@when(u'Tekan tombol dropdown')
def step_impl(context):
    assert context.driver.find_element(By.XPATH,"//span[text()='Products']").is_enabled()
    
    
    


@then(u'Pilih opsi Price low to high')
def step_impl(context):
    element_before=[clean_price(element.text) for element in context.driver.find_elements(By.XPATH,"//div[@class='inventory_item_price']")]
    pilih=Select(context.driver.find_element(By.XPATH, "//select[@class='product_sort_container']"))
    pilih.select_by_value('lohi')
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "//div[@class='inventory_item_price']"))
    )
    element_after = [clean_price(element.text) for element in context.driver.find_elements(By.XPATH, "//div[@class='inventory_item_price']")]
    sorted_elements = sorted(element_before)
    #print("Harga sebelum:", context.element_before)
    #print("Harga setelah:", element_after)
    #print("harga sorted:",sorted_elements)
    assert sorted_elements == element_after
    context.driver.quit()

@then(u'Pilih opsi Name A to Z')
def step_impl(context):
     element_before=[element.text for element in context.driver.find_elements(By.XPATH,"//div[@data-test='inventory-item-name']")]
     pilih=Select(context.driver.find_element(By.XPATH, "//select[@class='product_sort_container']"))
     pilih.select_by_value('az')
     WebDriverWait(context.driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "//div[@data-test='inventory-item-name']"))
    )
     element_after = [element.text for element in context.driver.find_elements(By.XPATH, "//div[@data-test='inventory-item-name']")]
     sorted_elements = sorted(element_before)
     assert sorted_elements == element_after
     context.driver.quit()