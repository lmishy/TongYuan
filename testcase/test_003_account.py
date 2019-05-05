#!/usr/bin/python3
# _*_coding:utf-8 _*_
# 创建时间: 2019/4/10 9:12
# 创建人员: 廖志妹

from time import sleep
from selenium import webdriver
from config.proxy import url1
import pytest
import allure




class Test_account():
    def setup(self):
        # 不显示自动化提示
        option = webdriver.ChromeOptions()
        option.add_argument('disable-infobars')
        option.add_argument('--ignore-certificate-errors')
        self.driver = webdriver.Chrome(options=option)
        driver = self.driver
        # 最大化浏览器
        driver.maximize_window()
        # 设置页面最大加载时间
        driver.set_page_load_timeout(20)
        try:
            driver.get(url=url1)
        except Exception:
            pass
        self.login()



    def teardown(self):
        self.driver.quit()


    def login(self):
        driver = self.driver
        driver.implicitly_wait(10)
        driver.find_element_by_class_name("btn-login").click()
        driver.find_element_by_xpath('/html/body/div[3]/form/div[1]/input').send_keys('600218')
        driver.find_element_by_xpath('/html/body/div[3]/form/div[2]/input').send_keys('j6d3f9')
        driver.find_element_by_class_name("login-submit").click()
        sleep(3)

    @pytest.mark.flaky(rerun = 2)
    @allure.step('最新通知')
    def test_notice(self):

        driver =  self.driver
        driver.implicitly_wait(10)
        driver.find_element_by_xpath('/html/body/div/aside/section/ul/li[2]/a/span').click()
        text = driver.find_element_by_xpath('/html/body/div/div[4]/section[1]/h1').text
        assert u"最新通知" in text



    @pytest.mark.flaky(rerun = 2)
    @allure.step('账户信息检查')
    def test_account(self):
        driver = self.driver
        driver.implicitly_wait(10)
        driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[3]/a/span').click()
        assert u"基本信息" in driver.find_element_by_xpath('/html/body/div[1]/div[4]/section[2]/div/section[1]/div/div[1]/h3').text
        text = driver.find_element_by_xpath('/html/body/div[1]/div[4]/section[2]/div/section[1]/div/div[2]/table/tbody/tr/td[1]').text
        assert len(text) != 0


    @pytest.mark.flaky(rerun = 2)
    @allure.step('资金管理检查')
    def test_fund_management(self):
        driver = self.driver
        driver.implicitly_wait(10)
        driver.find_element_by_xpath('/html/body/div/aside/section/ul/li[4]/a').click()
        #立即入金
        driver.find_element_by_xpath('/html/body/div/div[4]/section[2]/div[1]/div[1]/a/div/div/span').click()
        driver.find_element_by_xpath('/html/body/div/div[4]/section[2]/div[2]/div/main/div[2]/div/form/button').click()
        assert u"钱包地址" in driver.find_element_by_xpath('/html/body/div/div[4]/section[2]/div[2]/div/main/div[1]/div[2]/div[1]').text
        #出金申请
        driver.find_element_by_xpath('/html/body/div/div[4]/section[2]/div[1]/div[2]/a/div/div/span').click()
        driver.find_element_by_xpath('/html/body/div/div[4]/section[2]/div[2]/div/main/div[2]/div/form/button').click()
        assert u"出金申请" in driver.find_element_by_xpath('/html/body/div[1]/div[4]/section[2]/div[2]/div[1]/h3').text



    @pytest.mark.flaky(rerun = 2)
    @allure.step('交易管理检查')
    def test_fund_management(self):
        driver = self.driver
        driver.implicitly_wait(10)
        driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[5]/a/span').click()
        #持仓订单
        driver.find_element_by_xpath('/html/body/div[1]/div[4]/section[2]/div[1]/div[1]/a/div/div/span').click()
        assert u"持仓订单" in driver.find_element_by_xpath('/html/body/div[1]/div[4]/section[2]/div[2]/div[1]/h3').text
        #挂单订单
        driver.find_element_by_xpath('/html/body/div[1]/div[4]/section[2]/div[1]/div[2]/a/div').click()
        assert u"挂单订单" in driver.find_element_by_xpath('/html/body/div[1]/div[4]/section[2]/div[2]/div[1]/h3').text
        #交易历史
        driver.find_element_by_xpath('/html/body/div[1]/div[4]/section[2]/div[1]/div[3]/a/div').click()
        assert u"交易历史" in driver.find_element_by_xpath('/html/body/div[1]/div[4]/section[2]/div[2]/div[1]/h3').text



    @pytest.mark.flaky(rerun = 2)
    @allure.step('软件下载检查')
    def test_APP_management(self):
        driver = self.driver
        driver.implicitly_wait(10)
        driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[6]/a/span').click()
        assert u"软件下载" in driver.find_element_by_xpath('/html/body/div[1]/div[4]/section[2]/div/div/h3').text


if __name__ == "__main__":

    pytest.main()