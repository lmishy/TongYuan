#!/usr/bin/python3
# _*_coding:utf-8 _*_
# 创建时间: 2019/4/30  15:40
# 创建人员: 廖志妹

from time import sleep
from selenium import webdriver
from config.proxy import url1
import pytest
import allure
import json



class Test_login():
    def setup(self):
        #不显示自动化提示
        option = webdriver.ChromeOptions()
        option.add_argument('disable-infobars')
        option.add_argument('--ignore-certificate-errors')
        option.add_argument('--ignore-ssl-errors')
        self.driver = webdriver.Chrome(options=option)
        #火狐浏览器
        # self.driver = webdriver.Firefox()
        driver = self.driver
        #最大化浏览器
        driver.maximize_window()
        #设置页面最大加载时间
        driver.set_page_load_timeout(20)
        try:
            driver.get(url=url1)
        except Exception:
            pass
        finally:
            driver.find_element_by_class_name("btn-login").click()
        sleep(5)

    def teardown(self):
        self.driver.quit()



    @pytest.mark.flaky(rerun = 2)
    @allure.step('登录功能检查')
    def test_login(self):
        driver =  self.driver
        driver.implicitly_wait(10)
        driver.find_element_by_xpath('/html/body/div[3]/form/div[1]/input').send_keys('600218')
        driver.find_element_by_xpath('/html/body/div[3]/form/div[2]/input').send_keys('j6d3f9')
        driver.find_element_by_class_name("login-submit").click()
        sleep(3)
        Text = driver.find_element_by_xpath('//*[@id="cancel-accountMT4"]').text
        assert len(Text)!=0





    @pytest.mark.flaky(rerun = 2)
    @allure.step('找回密码功能检查')
    def test_forget_pwd(self):
        driver = self.driver
        driver.implicitly_wait(10)
        driver.find_element_by_xpath('/html/body/div[3]/form/div[3]/a').click()
        Text = driver.find_element_by_xpath('/html/body/div[3]/form/h2').text
        assert u"重置密码" in Text
        driver.find_element_by_xpath('//*[@id="name"]').send_keys('600218')
        driver.find_element_by_id('email').send_keys('545056850@qq.com')
        driver.find_element_by_xpath('//*[@id="identify-code"]').click()
        smg = driver.find_element_by_class_name('popup-inner').text
        print(smg)
        assert u"验证码发送成功" in smg
        sleep(5)





if __name__ == "__main__":
    pytest.main()