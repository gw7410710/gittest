# -*- coding: utf-8 -*-
from selenium import webdriver


driver=webdriver.Chrome()
driver.get('http://devops.sqtest.online:6007/')
driver.implicitly_wait(10)
#用户名
driver.find_element_by_xpath('//form/div[1]/div/input').send_keys('747370289@qq.com')
#密码
driver.find_element_by_xpath('//form/div[2]/div/input').send_keys('111111')
#点击登陆
driver.find_element_by_xpath('//button[@type="submit"]/span[1][@class="MuiButton-label"]').click()
#点击日程
driver.find_element_by_xpath('//nav/ul/li[11]').click()
#点击新建
driver.find_element_by_xpath('//div/ul/li/a/div[@class="slds-truncate"]').click()


#输入主题
driver.find_element_by_xpath('//form/div/div/div/div[@data-required="true"]/div/input[@class="form-control"]').send_keys('奔驰C260L')

#开始时间的下拉框
driver.find_element_by_xpath('//*[@name="start"]/div[1]/div/div[2]/div/div').click()
