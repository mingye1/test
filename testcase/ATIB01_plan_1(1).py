# -*- coding: utf-8 -*-
import ddt
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

from config import setting
from lib.readexcel import ReadExcel

'''
爱心守护计划
'''

testData = ReadExcel(setting.SOURCE_FILE_2, "Sheet1").read_data()
@ddt.ddt
class ATIB01_plan_1(unittest.TestCase):


    def setUp(self):
        # AppDynamics will automatically override this web driver
        # as documented in https://docs.appdynamics.com/display/PRO44/Write+Your+First+Script
        self.driver = webdriver.Chrome('E:\chromedriver.exe')
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    @ddt.data(*testData)
    def test_app_dynamics_job(self, data):

        driver = self.driver
        driver.maximize_window()
        time.sleep(2)
        # driver.get("https://sita.aixin-life.net/patvue/#/InsureProcess?planId=ATIB01_plan_1&sourceId=77&fpInfoId=557f6da8ce8148e7a4e777824c33f4b0&navKey=d9e2bae4")

        # driver.get("https://uata.aixin-life.net/patvue/#/InsureProcess?planId=ATIB01_plan_1&sourceId=10038&fpInfoId=84a88b84b13e49c6b264e1d544dbd3be&navKey=5b22388e")
        driver.get('https://stga.aixin-life.net/patvue/#/InsureProcess?planId=ATIB01_plan_1&sourceId=10038&fpInfoId=c2489ce16bd44579a14bc9968d486c2e&navKey=2a88495b')

        driver.find_element_by_xpath("//img[contains(@src,'https://axlis-test-1252661357.cos.ap-shanghai-fsi.myqcloud.com/PAT08/PD007/ATIB01/plan_1.jpg')]").click()
        time.sleep(4)
        driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div/p[2]").click()
        time.sleep(4)
        driver.find_element_by_xpath("//div[@id='app']/div[2]/div/div[2]/div").click()
        time.sleep(4)
        driver.find_element_by_xpath("//input[@type='text']").click()
        driver.find_element_by_xpath("//input[@type='text']").clear()
        # driver.find_element_by_xpath("//input[@type='text']").send_keys(u"测试005")
        driver.find_element_by_xpath("//input[@type='text']").send_keys(data['name'])
        driver.find_element_by_xpath("(//input[@type='text'])[2]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[2]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[2]").clear()
        # driver.find_element_by_xpath("(//input[@type='text'])[2]").send_keys("350101200001011552")
        driver.find_element_by_xpath("(//input[@type='text'])[2]").send_keys(str(data['ID']))
        driver.find_element_by_xpath("//input[@type='tel']").click()
        driver.find_element_by_xpath("//input[@type='tel']").clear()
        # driver.find_element_by_xpath("//input[@type='tel']").send_keys("18877214119")
        driver.find_element_by_xpath("//input[@type='tel']").send_keys(int(data['tel']))
        driver.find_element_by_xpath("(//input[@type='text'])[3]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[3]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[3]").send_keys("180604")
        driver.find_element_by_xpath("(//input[@type='text'])[4]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[4]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[4]").send_keys("7667626276@126.com")
        driver.find_element_by_xpath("//img[contains(@src,'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACQAAAAkCAYAAADhAJiYAAAAAXNSR0IArs4c6QAAA7NJREFUWAnNmD9MU0Ecx9vXMoGJjpDo4mANSRP+TCBjB6MEXVwcCWzGwURNXJgMmjgQRuPo4qJEjcNzQ5hoSZoQ6+CCCR0lESb6x+/nevd4tMW20vZxyb27d/e77/f7fnfv3u9ePNZhyufzl46Ojm5Vq9WMhl5RHonH4yPAqG1PBXlXbf7AwMDndDr9m752U7xdw2w2e1eED2Q/o5xsc1xJdusStzoxMfG+nTEtBW1vb09XKpWXEjNVB7ij+7xyURmvkPDUsHJaeVQ5SBK16Xne47GxsY2gsUnlVEESkMjlcq9UPgyNKwj0tQSuTU5O/gy1N1S3trauynZOtgvqTDkDCVsZHx9/pLLs2sJlU0HyysVyufxOhqwTUlEASwJ6cxpQzazxah9sXuWSevEeyU8kEvfkrf3a7fG1QRBi9FSbAriOmQR8HBwcvJ9Kpf4cD+u8VigULhweHr4V7qzF/S4PTtWL8sLQPA2ecWLU90JeuXNWMXCAARaY3MNhuRLcu3RCEGtGHW6alrVOnspDFWd81hIsMIWzbLEyljOADqaMt0mKv9HDNPE03RQTMKoi73gS8kGlmT6tpxvu7Qs8xKttBxVZM70SAwfYcKjKlhELcceMILvpmX1GxkvdWDMQ/SvBARc28tQUGqgbQWpgByYVeLVr1d5fLVcBJqfB49ukez4HMTY9qW66YdHf7QQXnBZ3Bi1eqVS6rQbzbdJcrnWbtBVeiDOJFk+ucq/5TqvPQSvw/+m3nHwXmbYMgi5bID6UUSXDjRYWtYllVJpXMCJFjnvE08JyglwIEYUmw40WpqwahYJmnGhhygJ3NTPqU5ubpSKC3FS5WKVPGk7QOO49BO3aLsLOqJLj3tVG6X21KkYJO/utyHKa+FuL2veSyeQnieB0wKdjrt+CQpwljk2ePTetI0Tb+IIW+okIrpcC4YLTcqyjhTVEfLJqG1MKnOZtveeF5TInEqchiBgVj2xIMTFRcWho6FqvYyKC/oODgx/iG5aYTR0kp/GA8ZCp6BBHqTRsTwdBX625e1f2PzjgAlXryHEfCyKmldIVDDRgVh57Tr0XCWw4wIbTxdPmPkwoo4SMv6jNhSTLcuUzDerKyQPP2Ad9Ynl94d8UfhAUBmvICTtXB0VEyX37mlMWt889rmXx6ckW8SBtnSTr9UUwwLJjfTjgqsdq8JAzAIhDnMrofzY4UZQcILV5Rf87JiyKuqbsfPywqhfGUYXTgaYyo0w83vBLT2/NL2Wf72Snv/T+AmOm8dKkuuGnAAAAAElFTkSuQmCC')]").click()
        driver.find_element_by_xpath("//img[contains(@src,'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACQAAAAkCAYAAADhAJiYAAAAAXNSR0IArs4c6QAAA7NJREFUWAnNmD9MU0Ecx9vXMoGJjpDo4mANSRP+TCBjB6MEXVwcCWzGwURNXJgMmjgQRuPo4qJEjcNzQ5hoSZoQ6+CCCR0lESb6x+/nevd4tMW20vZxyb27d/e77/f7fnfv3u9ePNZhyufzl46Ojm5Vq9WMhl5RHonH4yPAqG1PBXlXbf7AwMDndDr9m752U7xdw2w2e1eED2Q/o5xsc1xJdusStzoxMfG+nTEtBW1vb09XKpWXEjNVB7ij+7xyURmvkPDUsHJaeVQ5SBK16Xne47GxsY2gsUnlVEESkMjlcq9UPgyNKwj0tQSuTU5O/gy1N1S3trauynZOtgvqTDkDCVsZHx9/pLLs2sJlU0HyysVyufxOhqwTUlEASwJ6cxpQzazxah9sXuWSevEeyU8kEvfkrf3a7fG1QRBi9FSbAriOmQR8HBwcvJ9Kpf4cD+u8VigULhweHr4V7qzF/S4PTtWL8sLQPA2ecWLU90JeuXNWMXCAARaY3MNhuRLcu3RCEGtGHW6alrVOnspDFWd81hIsMIWzbLEyljOADqaMt0mKv9HDNPE03RQTMKoi73gS8kGlmT6tpxvu7Qs8xKttBxVZM70SAwfYcKjKlhELcceMILvpmX1GxkvdWDMQ/SvBARc28tQUGqgbQWpgByYVeLVr1d5fLVcBJqfB49ukez4HMTY9qW66YdHf7QQXnBZ3Bi1eqVS6rQbzbdJcrnWbtBVeiDOJFk+ucq/5TqvPQSvw/+m3nHwXmbYMgi5bID6UUSXDjRYWtYllVJpXMCJFjnvE08JyglwIEYUmw40WpqwahYJmnGhhygJ3NTPqU5ubpSKC3FS5WKVPGk7QOO49BO3aLsLOqJLj3tVG6X21KkYJO/utyHKa+FuL2veSyeQnieB0wKdjrt+CQpwljk2ePTetI0Tb+IIW+okIrpcC4YLTcqyjhTVEfLJqG1MKnOZtveeF5TInEqchiBgVj2xIMTFRcWho6FqvYyKC/oODgx/iG5aYTR0kp/GA8ZCp6BBHqTRsTwdBX625e1f2PzjgAlXryHEfCyKmldIVDDRgVh57Tr0XCWw4wIbTxdPmPkwoo4SMv6jNhSTLcuUzDerKyQPP2Ad9Ynl94d8UfhAUBmvICTtXB0VEyX37mlMWt889rmXx6ckW8SBtnSTr9UUwwLJjfTjgqsdq8JAzAIhDnMrofzY4UZQcILV5Rf87JiyKuqbsfPywqhfGUYXTgaYyo0w83vBLT2/NL2Wf72Snv/T+AmOm8dKkuuGnAAAAAElFTkSuQmCC')]").click()
        driver.find_element_by_xpath("//input[@type='checkbox']").click()
        driver.find_element_by_xpath("//div[@id='app']/main/article/div[8]/div").click()
        time.sleep(6)
        driver.find_element_by_xpath("//div[@id='app']/main/article/div/section/div/span").click()
        driver.find_element_by_xpath("//div[@id='app']/main/article/div/div[6]/div/div").click()
        time.sleep(6)
        # driver.find_element_by_xpath("//img[contains(@src,'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAD8AAAA/CAYAAAEgWCBJAAAAAXNSR0IArs4c6QAAAERlWElmTU0AKgAAAAgAAYdpAAQAAAABAAAAGgAAAAAAA6ABAAMAAAABAAEAAKACAAQAAAABAAAAP6ADAAQAAAABAAAAPwAAAACf5cgIAAADJElEQVRoBe1aPY/TQBDdsTmSo6IAISEUkoqOo6I4LqkRzf0CGgquQaLlD9DTgBAN4idQoStoYgIlIBoqpATprqbKx112GOdYy/bFsW/W9kDYa9bj3Zk3781ks3ZOqbP+jfstjPt4cWPZde4CCL3SYZdFiu6lF+dC5C6IQgteQJqWYC6Z0Hk5WivtAiglr0Fm/UuZyGuiEEReA5eBUlZ70mZvtNjbM3vG9UGmNImJajuRanScgCvbmPRbx0VKvQrXSgI6sPirgheZs0qgCEDeGpeAU2CxnU6C61NEPJ/XMGXOg4JpszdsWsUM9wDRfcAq+z/OrgmdAuIKlNHI/2GMo0GnF25A00F7l0ufXfu51k9CUJzjw9rB6QR0YQEKuFE7OBcw7seWPR6Ee+3AucpZ+fFlR1z94FkgLT64CY4q8aLU3C4y2oMXQclY48AzhKn2NswG7Vvzuf5cLczp6J7ytzyNcPn0VPV3tK8vsVHGQSsIv8/piegdN4h9t1tsNjbg7M3FKGUDbmKwRwfOls7G0cluox77UMGX3eIQYZjywU0Ei5ENTlqPF7gAMy4+G9z3/Kcn4OoFF1zUj92ptlnPPnZu67neoReUX+n3n/e28Tj+IuQnQeslotozCXsArxvd4QNj1zWye94uQbgR96dd61rcrutahDwdxEQ6Li2qCPl0ElK2Iy+lvDSuq7x0BaTwZSpv8bhfplAy5NMMSng8SYcsYv8d5ItkWsEaR74CUf+JkNExc9rv3FSe3kWNVwGgUWX2Wql7CvFKhAHqwFOwH9nZF6xXlOQU+k2J7KHy/beN7R/fQogF+UnQfoyon2VjrtcMFfdRszt8HlV+8qG9R8/W96kiLaK6WSVdAr1IpThnMCiZI8L+RXaUj5k700j/TbR0/cm3Cb32gREAvml2R6/CdcsXL41Q3s3wtwVqxB0TkZLYb/ZGd41d1yi127M+u2WLIkW+bB6seI48S7Y1cHKVX4Misii4yrNkK9dJ5LwhU3mh5/d0vWTIp7MQsh35uoUHUN8TmAA/E3ZNhshGE3KbBZ0tjbjt+/hl487wU018EzC/AYCLuSqEenMTAAAAAElFTkSuQmCC')]").click()
        driver.find_element_by_xpath('/html/body/div/main/article/div/div').click()
        time.sleep(6)
        #清空并输入银行卡号
        driver.find_element_by_xpath("//input[@type='tel']").click()
        driver.find_element_by_xpath("//input[@type='tel']").clear()
        driver.find_element_by_xpath("//input[@type='tel']").send_keys("617420100037139511")
        #/html/body/div/main/article/div[1]/div[3]/div[1]/div[1]/img
        driver.find_element_by_xpath("/html/body/div/main/article/div[1]/div[3]/div[1]/div[1]/img").click()
        time.sleep(1)
        #选择农业银行
        el2=driver.find_element_by_xpath("//div[@id='app']/main/article/div/div[3]/div[2]/div/div[2]/div/div/div[2]")
        el1=driver.find_element_by_xpath("//div[@id='app']/main/article/div/div[3]/div[2]/div/div[2]/div/div/div[1]")
        # webdriver.ActionChains(driver).move_to_element(el).click(el).perform()
        # ------------鼠标滑动操作------------

        action=webdriver.ActionChains(driver)
        # 第一步：在滑块处按住鼠标左键
        action.click_and_hold(el2)
        # 第二步：相对鼠标当前位置进行移动
        # action.move_by_offset(0, -45)
        action.drag_and_drop_by_offset(el2,0,-40)
        # 第三步：释放鼠标
        action.release()
        # 执行动作
        action.perform()
        time.sleep(10)

        #点击确定按钮
        driver.find_element_by_xpath("//div[@id='app']/main/article/div/div[3]/div[2]/div/div/button[2]").click()
        time.sleep(2)
        #点击确定，添加银行卡成功
        driver.find_element_by_xpath("//div[@id='app']/main/article/div[2]/span[2]").click()
        time.sleep(5)
        #选择银行信息
        driver.find_element_by_xpath("//img[contains(@src,'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACQAAAAkCAYAAADhAJiYAAAAAXNSR0IArs4c6QAAA7NJREFUWAnNmD9MU0Ecx9vXMoGJjpDo4mANSRP+TCBjB6MEXVwcCWzGwURNXJgMmjgQRuPo4qJEjcNzQ5hoSZoQ6+CCCR0lESb6x+/nevd4tMW20vZxyb27d/e77/f7fnfv3u9ePNZhyufzl46Ojm5Vq9WMhl5RHonH4yPAqG1PBXlXbf7AwMDndDr9m752U7xdw2w2e1eED2Q/o5xsc1xJdusStzoxMfG+nTEtBW1vb09XKpWXEjNVB7ij+7xyURmvkPDUsHJaeVQ5SBK16Xne47GxsY2gsUnlVEESkMjlcq9UPgyNKwj0tQSuTU5O/gy1N1S3trauynZOtgvqTDkDCVsZHx9/pLLs2sJlU0HyysVyufxOhqwTUlEASwJ6cxpQzazxah9sXuWSevEeyU8kEvfkrf3a7fG1QRBi9FSbAriOmQR8HBwcvJ9Kpf4cD+u8VigULhweHr4V7qzF/S4PTtWL8sLQPA2ecWLU90JeuXNWMXCAARaY3MNhuRLcu3RCEGtGHW6alrVOnspDFWd81hIsMIWzbLEyljOADqaMt0mKv9HDNPE03RQTMKoi73gS8kGlmT6tpxvu7Qs8xKttBxVZM70SAwfYcKjKlhELcceMILvpmX1GxkvdWDMQ/SvBARc28tQUGqgbQWpgByYVeLVr1d5fLVcBJqfB49ukez4HMTY9qW66YdHf7QQXnBZ3Bi1eqVS6rQbzbdJcrnWbtBVeiDOJFk+ucq/5TqvPQSvw/+m3nHwXmbYMgi5bID6UUSXDjRYWtYllVJpXMCJFjnvE08JyglwIEYUmw40WpqwahYJmnGhhygJ3NTPqU5ubpSKC3FS5WKVPGk7QOO49BO3aLsLOqJLj3tVG6X21KkYJO/utyHKa+FuL2veSyeQnieB0wKdjrt+CQpwljk2ePTetI0Tb+IIW+okIrpcC4YLTcqyjhTVEfLJqG1MKnOZtveeF5TInEqchiBgVj2xIMTFRcWho6FqvYyKC/oODgx/iG5aYTR0kp/GA8ZCp6BBHqTRsTwdBX625e1f2PzjgAlXryHEfCyKmldIVDDRgVh57Tr0XCWw4wIbTxdPmPkwoo4SMv6jNhSTLcuUzDerKyQPP2Ad9Ynl94d8UfhAUBmvICTtXB0VEyX37mlMWt889rmXx6ckW8SBtnSTr9UUwwLJjfTjgqsdq8JAzAIhDnMrofzY4UZQcILV5Rf87JiyKuqbsfPywqhfGUYXTgaYyo0w83vBLT2/NL2Wf72Snv/T+AmOm8dKkuuGnAAAAAElFTkSuQmCC')]").click()

        time.sleep(6)
        #点击立即付款
        driver.find_element_by_xpath("//div[@id='app']/main/article/div/button").click()
        time.sleep(2)
        #清空并输入短信验证码
        driver.find_element_by_xpath("//input[@type='tel']").click()
        driver.find_element_by_xpath("//input[@type='tel']").clear()
        driver.find_element_by_xpath("//input[@type='tel']").send_keys("180604")
        #点击确定按钮
        driver.find_element_by_xpath("//div[@id='app']/main/article/section/div/div/div[3]/button[2]").click()
        time.sleep(4)
        a=driver.find_element_by_xpath('/html/body/div/main/article/div/div[2]/span').text
        print("ATIB01爱心守护计划投保成功，保单号为："+a)
        time.sleep(10)
        driver.quit()
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
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
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        # To know more about the difference between verify and assert,
        # visit https://www.seleniumhq.org/docs/06_test_design_considerations.jsp#validating-results
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
