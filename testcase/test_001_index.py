#!/usr/bin/python3
# _*_coding:utf-8 _*_
# 创建时间: 2019/4/28 14:12
# 创建人员: 廖志妹

from time import sleep
from selenium import webdriver
from config.proxy import url1
import pytest
import allure
from selenium.webdriver.common.action_chains import ActionChains
from Cookie.get_cookie import getCookies



class Test_index():
    def setup(self):
        #不显示自动化提示
        option = webdriver.ChromeOptions()
        option.add_argument('disable-infobars')
        #禁止加载图片
        # prefs = {"profile.managed_default_content_settings.images": 2}
        # option.add_experimental_option("prefs", prefs)
        option.add_argument('--ignore-certificate-errors')
        self.driver = webdriver.Chrome(options=option)
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
        sleep(5)

    def teardown(self):
        self.driver.quit()


    @pytest.mark.flaky(rerun = 2)
    # @pytest.mark.skip(reason="skip")
    @allure.step('页面检查')
    def test_index_scan(self):
        driver = self.driver
        driver.implicitly_wait(10)
        #等待首页按钮出现
        driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/ul/li[1]/a').click()
        assert "TONGYUAN-专注数字货币的交易平台" in driver.title
        # 点击交易产品
        driver.find_element_by_link_text("交易产品").click()
        assert "TONGYUAN交易产品-专注数字货币的交易平台" in driver.title
        # 点击交易平台
        driver.find_element_by_link_text("交易平台").click()
        assert "TONGYUAN交易平台-专注数字货币的交易平台" in driver.title
        # 点击PC版
        driver.find_element_by_xpath("/html/body/div[5]/div/div[2]/a[1]").click()
        sleep(5)
        # 点击IOS版
        driver.find_element_by_xpath("/html/body/div[5]/div/div[2]/a[2]").click()
        sleep(5)
        driver.back()
        # 点击android版
        driver.find_element_by_xpath("/html/body/div[5]/div/div[2]/a[3]").click()
        sleep(5)
        # 点击帮助中心
        driver.get(url1)
        driver.find_element_by_link_text("帮助中心").click()
        assert u"TONGYUAN帮助中心-专注数字货币的交易平台" in driver.title
        sleep(5)
        # 点击公告资讯
        driver.find_element_by_link_text("公告资讯").click()
        assert u"TONGYUAN-专注数字货币的交易平台" in driver.title


    @pytest.mark.flaky(rerun = 2)
    # @pytest.mark.skip(reason="skip")
    @allure.step('帮助中心')
    def test_index_help(self):
        driver = self.driver
        driver.implicitly_wait(10)
        driver.find_element_by_link_text("帮助中心").click()
        assert u"专注数字货币的交易平台" in driver.title
        sleep(5)
        driver.find_element_by_xpath("/html/body/div[4]/div[2]/div[1]/ul/li[1]/a").click()
        assert u"1.如何注册" in driver.page_source
        sleep(5)
        driver.find_element_by_xpath("/html/body/div[4]/div[2]/div[1]/ul/li[2]").click()
        assert u"1.注册失败" in driver.page_source
        sleep(5)
        driver.find_element_by_xpath("/html/body/div[4]/div[2]/div[1]/ul/li[3]").click()
        assert u"1.比特币（BTC）" in driver.page_source
        sleep(5)
        driver.find_element_by_xpath("/html/body/div[4]/div[2]/div[1]/ul/li[4]").click()
        assert u"1.币种交易" in driver.page_source
        sleep(5)
        driver.find_element_by_xpath("/html/body/div[4]/div[2]/div[1]/ul/li[5]").click()
        assert u"1.账户登录" in driver.page_source
        sleep(5)
        driver.find_element_by_xpath("/html/body/div[4]/div[2]/div[1]/ul/li[6]").click()
        assert u"安卓教程" in driver.page_source


    @pytest.mark.flaky(rerun = 2)
    # @pytest.mark.skip(reason="skip")
    @allure.step('公告资讯')
    def test_index_notice(self):
        driver = self.driver
        driver.implicitly_wait(10)
        # js = "window.scrollTo(0,500)"
        # driver.execute_script(js)
        driver.find_element_by_link_text("公告资讯").click()
        assert "专注数字货币的交易平台" in driver.title
        sleep(5)
        driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/ul/li[1]/div[1]/p[3]/a').click()
        sleep(5)
        msg = driver.find_element_by_class_name('cont-box').text
        assert len(msg)!=0
        sleep(5)
        driver.back()
        sleep(5)
        driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/ul/li[1]/div[1]/p[3]/a').click()
        msg = driver.find_element_by_class_name('cont-box').text
        assert len(msg)!=0
        sleep(5)

    # @pytest.mark.flaky(rerun=2)
    # @pytest.mark.skip(reason="skip")
    @allure.step('页面底部')
    def test_index_bottom(self):
        driver = self.driver
        driver.implicitly_wait(10)
        js = "window.scrollTo(0,window.scrollTo(0, document.body.scrollHeight))"
        driver.execute_script(js)
        driver.find_element_by_link_text("免责声明").click()
        assert "专注数字货币的交易平台" in driver.title
        assert u"1. 密码保护" in driver.page_source
        sleep(5)
        driver.back()
        sleep(5)
        driver.find_element_by_link_text("私隐条款").click()
        assert "专注数字货币的交易平台" in driver.title
        assert  u"TONGYUAN私隐政策" in driver.page_source
        sleep(5)
        driver.back()
        sleep(5)
        driver.find_element_by_link_text("关于我们").click()
        assert "专注数字货币的交易平台" in driver.title
        assert u"什么是TongYuan" in driver.page_source






if __name__ == "__main__":
    pytest.main()