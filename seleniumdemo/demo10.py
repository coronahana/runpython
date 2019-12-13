from selenium import webdriver
driver = webdriver.Chrome(r'E:\Python\webdriver\72\chromedriver.exe')
driver.get('http://temp.tesla.oa.com/ml/index.html#/my')
driver.implicitly_wait(3)
driver.find_element_by_name('btn_smartlogin').click()
# driver.switch_to.window('')
driver.find_element_by_class_name('cancel-guide').click()

#添加项目
driver.find_element_by_xpath('//*[@id="add_project_btn"]/span').click()
driver.find_element_by_xpath('//*[@id="modal-edit-project-name"]').send_keys("newproject")
driver.find_element_by_xpath('//*[@id="modal-project-desc"]').send_keys("newprojectsesc")
driver.find_element_by_xpath('//*[@id="save-project-btn"]').click()

driver.current_window_handle