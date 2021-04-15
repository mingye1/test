# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver import TouchActions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from selenium.webdriver.chrome.options import Options


class ATRB03_plan_1(unittest.TestCase):
    def setUp(self):
        # AppDynamics will automatically override this web driver
        # as documented in https://docs.appdynamics.com/display/PRO44/Write+Your+First+Script
        # self.driver = webdriver.Chrome()

        # self.base_url = "https://www.google.com/"
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(options=chrome_options)

        mobileEmulation = {'deviceName': 'iPhone 6/7/8 Plus'}
        options = webdriver.ChromeOptions()
        options.add_experimental_option('w3c', False)
        options.add_experimental_option('mobileEmulation', mobileEmulation)
        self.driver = webdriver.Chrome(executable_path='e:\chromedriver.exe')
        # self.driver = webdriver.Chrome(executable_path='e:\chromedriver.exe')
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_app_dynamics_job(self):
        driver = self.driver
        driver.get(
            "https://sita.aixin-life.net/patvue/#/InsureProcess?planId=ATRB03_plan_1&sourceId=78&fpInfoId=557f6da8ce8148e7a4e777824c33f4b0&navKey=f97166cd")
        driver.maximize_window()

        # js = "$('input:eq(0)').removeAttr('readonly')"  # jQuery，移除属性
        # # js = "$('input:eq(0)').attr('readonly',false)"  # jQuery，设置为false
        # driver.execute_script(js)

        self.driver.implicitly_wait(30)
        time.sleep(8)
        driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div/p[2]").click()
        time.sleep(6)
        driver.find_element_by_xpath("//div[@id='app']/div[2]/div/div[2]/div").click()
        driver.find_element_by_xpath("//div[@id='app']/main/article/section[2]/div/div/p[2]").click()
        driver.find_element_by_xpath("//div[@id='app']/div/div/div[2]/div[2]").click()
        time.sleep(8)
        # 输入姓名
        driver.find_element_by_xpath("(//input[@type='text'])[2]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[2]").send_keys(u"测试101")
        # driver.find_element_by_xpath("//div[@id='app']/main/article/section/div[4]/div[2]/div/div[2]/div").click()
        # 输入身份证号
        driver.find_element_by_xpath("(//input[@type='text'])[3]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[3]").send_keys("610101200001019814")
        time.sleep(4)
        # 身份证有效期选择“长期”
        sfz = driver.find_element_by_name("long")
        # sfz.click()
        # sfz=driver.find_element_by_xpath("//input[@type='checkbox']")
        # print(sfz.is_displayed())
        webdriver.ActionChains(driver).move_to_element(sfz).click(sfz).perform()
        '''actionchains:只针对PC端鼠标模拟，对H5不生效, touchaction: 可以针对H5 ，点击滑动，拖拽，模拟手势等'''
        # action=TouchActions(driver)
        # action.tap(sfz)
        # action.perform()

        # sleep(5)
        # b=mobile_driver.find_element_by_class_name('btn')
        # ActionChains(mobile_driver).click(b).perform()
        # input_datetime = driver.find_element_by_name("long")
        # input_datetime.send_keys("2022-09-21")
        # input_datetime.click()
        # time.sleep(5)
        print(sfz.is_selected())

        # time.sleep(2)
        # # driver.find_element_by_xpath('/html/body/div/main/article/section[1]/div[4]/div[2]/div/div[3]/div[2]/div/div[3]/button[2]').click()
        #
        # time.sleep(2)
        # # webdriver.ActionChains(driver).move_to_element(sfz).click(sfz).perform()
        # #输入手机号
        # driver.find_element_by_xpath("//input[@type='tel']").clear()
        # driver.find_element_by_xpath("//input[@type='tel']").send_keys("18874637777")
        # #输入验证码
        # driver.find_element_by_xpath("(//input[@type='text'])[5]").clear()
        # driver.find_element_by_xpath("(//input[@type='text'])[5]").send_keys("180604")
        # #输入邮箱
        # driver.find_element_by_xpath("(//input[@type='text'])[6]").clear()
        # driver.find_element_by_xpath("(//input[@type='text'])[6]").send_keys("3263267632@126.com")
        # #选择职业
        #
        # # zy=driver.find_element_by_xpath("(//img[contains(@src,'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABIAAAAVCAYAAABLy77vAAAAAXNSR0IArs4c6QAAAWlJREFUOBFjZACC+fPnc/z+/bvj////nenp6c9BYqQCJpCGX79+VQANyWdkZLw5a9asov3797OQahDjvHnzRIGueQjUyAnTDDTwKhDnpKamHoCJEaIZQQpmz57tAHTRFCDWRtOwDMgvIca7YINAmkHeuXXrFsh79UADeWEGAvmfgewGVVXVSY6Ojn9g4ug03CCYxNy5c6X+/v3bAzQsEiYGogl5F8MgmGZSvYvTIJCBpHgXr0Ew1xHjXaIMghmIy7vA8FtOkkEgA1etWsX5/v37Q0CmCcwCEM2MzCHEBrnox48fG4DqDJDVEu2imTNnSgI19gBxFJoB8ByAN0+BYu327dt5QM0N6IkUyG8EJtKJsESKM4zwBSwzM3NJcnLyMxTXIXNAbGK8ga4HxId7jRRvYDMI7DVSvYHVIGqVR0xJSUmvmZiYOkG2QIuMEmBsGJBSqIH0gsOIhYWlE1hKCgJjows9NkCKiAEAFZTZ3i1eB1wAAAAASUVORK5CYII=')])[2]")
        # # zy=driver.find_element_by_xpath('/html/body/div/main/article/section[1]/div[4]/div[2]/div/div[7]/div/div[1]/img')
        # zy=driver.find_element_by_css_selector('div.form-selector:nth-child(7) > div:nth-child(1) > div:nth-child(1) > img:nth-child(3)')
        # webdriver.ActionChains(driver).move_to_element(zy).click(zy).perform()
        # time.sleep(8)
        # #
        # driver.find_element_by_xpath("/html/body/div/main/article/section[1]/div[4]/div[2]/div/div[7]/main/article/section[1]/p[1]").click()
        # time.sleep(2)
        # driver.find_element_by_xpath("/html/body/div/main/article/section[1]/div[4]/div[2]/div/div[7]/main/article/section[2]/div[2]/p").click()
        # time.sleep(2)
        # driver.find_element_by_xpath("/html/body/div/main/article/section[1]/div[4]/div[2]/div/div[7]/main/article/section[2]/div[2]/p[1]").click()
        # time.sleep(2)
        # #选择地址
        #
        # dz=driver.find_element_by_xpath("/html/body/div/main/article/section[1]/div[4]/div[2]/div/div[9]/div/div[1]/img")
        # webdriver.ActionChains(driver).move_to_element(dz).click(dz).perform()
        # time.sleep(2)
        # driver.find_element_by_xpath("//div[@id='app']/main/article/section/div[4]/div[2]/div/div[9]/main/article/section/p").click()
        # time.sleep(2)
        # driver.find_element_by_xpath("//div[@id='app']/main/article/section/div[4]/div[2]/div/div[9]/main/article/section[2]/div[2]/p").click()
        # time.sleep(2)
        # driver.find_element_by_xpath("//div[@id='app']/main/article/section/div[4]/div[2]/div/div[9]/main/article/section[2]/div[2]/p").click()
        # time.sleep(2)
        # #输入地址
        # driver.find_element_by_xpath("(//input[@type='text'])[9]").clear()
        # driver.find_element_by_xpath("(//input[@type='text'])[9]").send_keys(u"北京石景山区33号")
        # #选择本人已阅读
        # yd=driver.find_element_by_xpath("(//input[@type='checkbox'])[2]")
        # webdriver.ActionChains(driver).move_to_element(yd).click(yd).perform()
        #
        # #点击立即购买
        # driver.find_element_by_xpath("//div[@id='app']/main/article/section[2]/div/div/p[2]").click()
        # time.sleep(6)
        # #选择实时支付
        # driver.find_element_by_xpath("//div[@id='app']/main/article/div/section/div/span").click()
        # time.sleep(2)
        #
        # driver.find_element_by_xpath("//div[@id='app']/main/article/div/div[6]/div/div").click()
        # time.sleep(4)
        #
        # driver.find_element_by_xpath("//div[@id='app']/main/article/div/div/p").click()
        # time.sleep(4)
        # driver.find_element_by_xpath("//div[@id='app']/main/article/div/div[2]/div").click()
        # time.sleep(6)
        # # ERROR: Caught exception [ERROR: Unsupported command [doubleClick | //input[@type='tel'] | ]]
        # #输入银行卡号
        # driver.find_element_by_xpath("//input[@type='tel']").clear()
        # driver.find_element_by_xpath("//input[@type='tel']").send_keys("617420100037139511")
        # #点击选择银行
        # driver.find_element_by_xpath("//div[@id='app']/main/article/div/div[3]/div/div").click()
        # time.sleep(2)
        # # 选择农业银行
        # el3 = driver.find_element_by_xpath("//div[@id='app']/main/article/div/div[3]/div[2]/div/div[2]/div/div/div[2]")
        # # el1 = driver.find_element_by_xpath("//div[@id='app']/main/article/div/div[3]/div[2]/div/div[2]/div/div/div[1]")
        # # webdriver.ActionChains(driver).move_to_element(el).click(el).perform()
        # # ------------鼠标滑动操作------------
        #
        # action = webdriver.ActionChains(driver)
        # # 第一步：在滑块处按住鼠标左键
        # action.click_and_hold(el3)
        # # 第二步：相对鼠标当前位置进行移动
        # # action.move_by_offset(0, -45)
        # action.drag_and_drop_by_offset(el3, 0, -40)
        # # 第三步：释放鼠标
        # action.release()
        # # 执行动作
        # action.perform()
        # time.sleep(10)
        #
        # #点击确定按钮
        # driver.find_element_by_xpath("//div[@id='app']/main/article/div/div[3]/div[2]/div/div/button[2]").click()
        #
        # # driver.find_element_by_xpath("//div[@id='app']/main/article/div[2]/span[2]").click()
        # # driver.find_element_by_xpath("//div[@id='app']/main/article/div/div[3]/p").click()
        # # driver.find_element_by_xpath("//div[@id='app']/main/article/div/button").click()
        # # driver.find_element_by_xpath("//input[@type='tel']").click()
        # # driver.find_element_by_xpath("//input[@type='tel']").clear()
        # # driver.find_element_by_xpath("//input[@type='tel']").send_keys("180604")
        # # driver.find_element_by_xpath("//div[@id='app']/main/article/section/div/div/div[3]/button[2]").click()
        # time.sleep(2)
        # # 点击确定，添加银行卡成功
        # driver.find_element_by_xpath("//div[@id='app']/main/article/div[2]/span[2]").click()
        # time.sleep(5)
        # # 选择银行信息
        # driver.find_element_by_xpath(
        #     "//img[contains(@src,'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACQAAAAkCAYAAADhAJiYAAAAAXNSR0IArs4c6QAAA7NJREFUWAnNmD9MU0Ecx9vXMoGJjpDo4mANSRP+TCBjB6MEXVwcCWzGwURNXJgMmjgQRuPo4qJEjcNzQ5hoSZoQ6+CCCR0lESb6x+/nevd4tMW20vZxyb27d/e77/f7fnfv3u9ePNZhyufzl46Ojm5Vq9WMhl5RHonH4yPAqG1PBXlXbf7AwMDndDr9m752U7xdw2w2e1eED2Q/o5xsc1xJdusStzoxMfG+nTEtBW1vb09XKpWXEjNVB7ij+7xyURmvkPDUsHJaeVQ5SBK16Xne47GxsY2gsUnlVEESkMjlcq9UPgyNKwj0tQSuTU5O/gy1N1S3trauynZOtgvqTDkDCVsZHx9/pLLs2sJlU0HyysVyufxOhqwTUlEASwJ6cxpQzazxah9sXuWSevEeyU8kEvfkrf3a7fG1QRBi9FSbAriOmQR8HBwcvJ9Kpf4cD+u8VigULhweHr4V7qzF/S4PTtWL8sLQPA2ecWLU90JeuXNWMXCAARaY3MNhuRLcu3RCEGtGHW6alrVOnspDFWd81hIsMIWzbLEyljOADqaMt0mKv9HDNPE03RQTMKoi73gS8kGlmT6tpxvu7Qs8xKttBxVZM70SAwfYcKjKlhELcceMILvpmX1GxkvdWDMQ/SvBARc28tQUGqgbQWpgByYVeLVr1d5fLVcBJqfB49ukez4HMTY9qW66YdHf7QQXnBZ3Bi1eqVS6rQbzbdJcrnWbtBVeiDOJFk+ucq/5TqvPQSvw/+m3nHwXmbYMgi5bID6UUSXDjRYWtYllVJpXMCJFjnvE08JyglwIEYUmw40WpqwahYJmnGhhygJ3NTPqU5ubpSKC3FS5WKVPGk7QOO49BO3aLsLOqJLj3tVG6X21KkYJO/utyHKa+FuL2veSyeQnieB0wKdjrt+CQpwljk2ePTetI0Tb+IIW+okIrpcC4YLTcqyjhTVEfLJqG1MKnOZtveeF5TInEqchiBgVj2xIMTFRcWho6FqvYyKC/oODgx/iG5aYTR0kp/GA8ZCp6BBHqTRsTwdBX625e1f2PzjgAlXryHEfCyKmldIVDDRgVh57Tr0XCWw4wIbTxdPmPkwoo4SMv6jNhSTLcuUzDerKyQPP2Ad9Ynl94d8UfhAUBmvICTtXB0VEyX37mlMWt889rmXx6ckW8SBtnSTr9UUwwLJjfTjgqsdq8JAzAIhDnMrofzY4UZQcILV5Rf87JiyKuqbsfPywqhfGUYXTgaYyo0w83vBLT2/NL2Wf72Snv/T+AmOm8dKkuuGnAAAAAElFTkSuQmCC')]").click()
        #
        # time.sleep(6)
        # # 点击立即付款
        # driver.find_element_by_xpath("//div[@id='app']/main/article/div/button").click()
        # time.sleep(2)
        # # 清空并输入短信验证码
        # driver.find_element_by_xpath("//input[@type='tel']").click()
        # driver.find_element_by_xpath("//input[@type='tel']").clear()
        # driver.find_element_by_xpath("//input[@type='tel']").send_keys("180604")
        # # 点击确定按钮
        # driver.find_element_by_xpath("//div[@id='app']/main/article/section/div/div/div[3]/button[2]").click()
        # time.sleep(4)
        # a = driver.find_element_by_xpath('/html/body/div/main/article/div/div[2]/span').text
        # print("ATRB03爱安享2020投保成功，保单号为：" + a)
        time.sleep(10)
        # driver.quit()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        # To know more about the difference between verify and assert,
        # visit https://www.seleniumhq.org/docs/06_test_design_considerations.jsp#validating-results
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
