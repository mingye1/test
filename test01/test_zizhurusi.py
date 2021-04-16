import time
import unittest

# from django.views.generic.base import View
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import warnings

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
# from selenium.webdriver.common.touch_actions import TouchAction

from appium.webdriver.mobilecommand import MobileCommand

'''
自助入司

'''
class MyTests(unittest.TestCase):
    # 测试开始前执行的方法
    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)#通过warnings库来忽略掉相关告警。
        desired_caps = {'platformName': 'Android', # 平台名称
                        'platformVersion': '7.1.2',  # 系统版本号
                        # 'deviceName': '10.120.2.10:5556',  # 设备名称。如果是真机，在'设置->关于手机->设备名称'里查看
                        'deviceName': '红米手机',
                        'appPackage': 'cn.proatech.a',  # apk的包名
                        'appActivity': 'cn.proatech.a.LoginActivity',  # activity 名称
                        'noReset': True,  # 不需要每次都安装apk
                        # 'resetKeyboard':True,
                        # 'unicodeKeyboard':True,
                        'automationName':'Uiautomator2',#定位toast元素这里一定注意
                        'newCommandTimeout':'150000'  #超时设置，appium保持与设备连接

                        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)  # 连接Appium
        self.driver.implicitly_wait(30)


    def test_calculator(self):
        """投保"""

        driver=self.driver
        print(driver.contexts)
        try:

            el4 = driver.find_element_by_xpath(
                "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/com.tencent.tbs.core.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.widget.EditText")
            # el4.clear()
            el4.send_keys('1010000011')#输入账号
            el5 = driver.find_element_by_xpath(
                "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/com.tencent.tbs.core.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View[1]/android.widget.EditText")
            # el5.clear()
            el5.send_keys('123456')#输入密码
            el6 = driver.find_element_by_xpath(
                "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/com.tencent.tbs.core.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View/android.widget.Button[2]")
            el6.click()#点击登录
            time.sleep(6)
        except:
            print("已自动登录！")

        #点击更多按钮
        el7 = driver.find_element_by_xpath(#SIT
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/com.tencent.tbs.core.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View/android.view.View[1]/android.view.View[11]/android.view.View[1]/android.widget.Image")
        el7.click()
        time.sleep(2)
        #点击
        el8 = driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/com.tencent.tbs.core.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View/android.view.View[3]/android.view.View/android.view.View/android.view.View[1]/android.view.View[2]/android.view.View[1]")
        el8.click()
        time.sleep(2)
        #点击选择年龄按钮
        el9 = driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/com.tencent.tbs.core.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View[2]/android.view.View[1]/android.widget.Image")
        el9.click()
        #选择时间，点击确定
        el10 = driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/com.tencent.tbs.core.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View[3]/android.widget.Button[2]")
        el10.click()
        time.sleep(4)
        #切换至原生页面
        driver.execute(MobileCommand.SWITCH_TO_CONTEXT, {"name": "NATIVE_APP"})
        #选择性别：选择女
        el11 = driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/com.tencent.tbs.core.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[2]/android.view.View[3]/android.view.View[3]/android.view.View[1]")
        el11.click()
        time.sleep(4)
        #选择职级
        # print(driver.contexts)


        # el12 = driver.find_element_by_xpath(
        #     "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/com.tencent.tbs.core.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View[4]/android.view.View[1]/android.widget.Image")
        el12=driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/com.tencent.tbs.core.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View[4]/android.view.View[1]/android.widget.EditText')
        el12.click()
        time.sleep(2)
        el13 = driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/com.tencent.tbs.core.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View[5]/android.view.View[2]/android.view.View/android.view.View[1]")
        el13.click()
        time.sleep(2)
        el14 = driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/com.tencent.tbs.core.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View[5]/android.view.View[2]/android.view.View/android.view.View[2]")
        el14.click()
        time.sleep(2)
        el15 = driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/com.tencent.tbs.core.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View[5]/android.view.View[2]/android.view.View/android.view.View[3]")
        el15.click()
        time.sleep(2)
        #切换至H5页面
        # driver.execute(MobileCommand.SWITCH_TO_CONTEXT, {"name": "WEBVIEW_cn.proatech.a"})
        #是否有社保：选择“是”
        driver.implicitly_wait(10)
        el16 = driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/com.tencent.tbs.core.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View[5]/android.view.View[2]/android.view.View[1]")
        el16.click()
        driver.implicitly_wait(10)
        time.sleep(2)
        #页面滑动
        # TouchAction(driver).press(x=290, y=699).move_to(x=282, y=1201).release().perform()
        #
        # TouchAction(driver).press(x=305, y=1647).move_to(x=305, y=1170).release().perform()
        #
        # TouchAction(driver).press(x=285, y=1537).move_to(x=290, y=883).release().perform()
        #
        # TouchAction(driver).press(x=316, y=722).move_to(x=316, y=231).release().perform()
        #
        # TouchAction(driver).press(x=468, y=1808).move_to(x=491, y=248).release().perform()
        #将Vconsole移动到其他地方
        el1=driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/com.tencent.tbs.core.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View')
        TouchAction(driver).press(el1).move_to(x=100, y=200).release().perform()

        #点击“下一步”按钮
        # el17 = driver.find_element_by_xpath(
        #     "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/com.tencent.tbs.core.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View/android.view.View[3]/android.view.View/android.widget.Button")
        el17=driver.find_element_by_class_name('android.widget.Button')

        el17.click()
        time.sleep(4)


        '''
        寿险规划师报告书页面
        '''

        #点击“投保人自己提出”按钮
        el18 = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/com.tencent.tbs.core.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View/android.view.View[2]/android.view.View[10]/android.view.View/android.view.View[2]')
        el18.click()
        #点击“下一步”按钮
        el19 = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/com.tencent.tbs.core.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View/android.view.View[2]/android.view.View[12]/android.widget.Button')
        el19.click()
        time.sleep(20)
        driver.implicitly_wait(20)

        '''
        投保信息页面
        '''
        try:
            print(driver.contexts)
            el2=driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/com.tencent.tbs.core.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View[2]/android.view.View[2]')
            el2.click()
        except:
            pass

        #点击选择客户按钮
        el20 = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/com.tencent.tbs.core.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.widget.Image')
        el20.click()
        time.sleep(5)
        #点击搜索框
        el_1=driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/com.tencent.tbs.core.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View/android.view.View[2]/android.view.View[1]/android.view.View/android.view.View[2]/android.widget.EditText')
        # el_1=driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/com.tencent.tbs.core.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View/android.view.View[1]/android.widget.Image[2]')
        el_1.click()
        time.sleep(2)
        el_2=driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/com.tencent.tbs.core.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText')
        # el_2=driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/com.tencent.tbs.core.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View/android.view.View[1]/android.widget.EditText')
        el_2.click()
        el_2.send_keys('士兵')
        driver.press_keycode(84)
        driver.press_keycode(66)
        # el_1.click()
        time.sleep(2)
        #选择客户
        el_3=driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/com.tencent.tbs.core.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View[2]')
        # el_3 = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/com.tencent.tbs.core.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[2]')
        el_3.click()
        time.sleep(14)
        driver.execute(MobileCommand.SWITCH_TO_CONTEXT, {"name": "NATIVE_APP"})
        #选择个人税收居民身份声明
        el21=driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/com.tencent.tbs.core.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[14]/android.view.View[1]/android.view.View[1]/android.widget.Image')
        el21.click()
        time.sleep(4)
        # driver.switch_to_frame().accept()
        # driver.execute(MobileCommand.SWITCH_TO_CONTEXT, {"name": "WEBVIEW_cn.proatech.a"})
        driver.execute(MobileCommand.SWITCH_TO_CONTEXT, {"name": "NATIVE_APP"})
        print(driver.contexts)
        #仅为中国税收居民
        a=driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/com.tencent.tbs.core.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View/android.view.View[2]/android.view.View[1]/android.view.View[14]/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View/android.view.View[1]')
        # TouchAction(driver).press(a).move_to(x=500, y=1600).press().perform()
        print(driver.contexts)
        driver.execute(MobileCommand.SWITCH_TO_CONTEXT, {"name": "NATIVE_APP"})
        TouchAction(driver).press(x=545, y=1770).move_to(x=549, y=1962).release().perform()
        a_1=driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/com.tencent.tbs.core.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View/android.view.View[2]/android.view.View[1]/android.view.View[9]/android.view.View[2]/android.view.View/android.view.View[2]')
        TouchAction(driver).press(a).move_to(a_1).release().perform()
        # TouchAction(driver).press(x=545, y=1770).move_to(x=549, y=1662).release().perform()
        #
        # TouchAction(driver).press(x=526, y=1770).move_to(x=521, y=1874).release().perform()
        print(driver.page_source)
        time.sleep(5)

        #点击确定
        el22=driver.find_element_by_xpath('//android.widget.Button["确定"]')
        print(el22.is_displayed())
        el22.click()
        time.sleep(4)
        #
        # TouchAction(driver).press(x=180, y=1900).move_to(x=180, y=500).release().perform()
        #收起投保人信息
        driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/com.tencent.tbs.core.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.widget.Image').click()
        #是否需要纸质保单：选择是
        el23=driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/com.tencent.tbs.core.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View/android.view.View/android.view.View[4]/android.view.View[2]/android.view.View[2]/android.view.View[1]')
        el23.click()
        #收起被保人信息
        driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/com.tencent.tbs.core.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View[1]/android.widget.Image').click()
        #收起身故受益人
        driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/com.tencent.tbs.core.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View/android.view.View[2]/android.view.View[3]/android.widget.Image').click()
        #收起保单信息
        driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/com.tencent.tbs.core.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View/android.view.View[2]/android.view.View[4]/android.widget.Image').click()
        #收起险种信息
        driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/com.tencent.tbs.core.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View/android.view.View[2]/android.view.View[5]/android.widget.Image').click()


        time.sleep(4)

        print(driver.contexts)
        driver.execute(MobileCommand.SWITCH_TO_CONTEXT, {"name": "NATIVE_APP"})
        # driver.execute(MobileCommand.SWITCH_TO_CONTEXT, {"name": "WEBVIEW_cn.proatech.a"})

        #支付方式：点击“实时”
        el24=driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/com.tencent.tbs.core.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View/android.view.View[2]/android.view.View[6]/android.view.View[3]/android.view.View[2]/android.view.View[1]')
        # el24=driver.find_element_by_android_uiautomator('new UiSelector().text("实时")')
        el24.click()
        el28=driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/com.tencent.tbs.core.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View/android.view.View[2]/android.view.View[11]/android.view.View')
        TouchAction(driver).press(el28).move_to(x=900, y=200).release().perform()
        #付款账号
        #点击“请选择”
        el25=driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/com.tencent.tbs.core.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View/android.view.View[2]/android.view.View[6]/android.view.View[5]/android.widget.Image')
        # el25=driver.find_element_by_accessibility_id('839a0758-709c-44f2-9773-b07f6673dba2')
        el25.click()
        time.sleep(2)
        '''
        银行账号选择页面s
        '''
        #
        el27=driver.find_element_by_xpath('//*[@resource-id="page"]/android.view.View[2]/android.view.View[1]/android.widget.Image[1]')
        el27.click()
        time.sleep(4)


        #选择已阅读协议
        el26=driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/com.tencent.tbs.core.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View/android.view.View[2]/android.view.View[7]/android.widget.CheckBox')
        el26.click()
        #点击《条款》
        driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/com.tencent.tbs.core.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View/android.view.View[2]/android.view.View[7]/android.view.View[2]').click()
        time.sleep(2)
        driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/com.tencent.tbs.core.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View/android.view.View[2]/android.widget.ListView/android.view.View').click()
        time.sleep(2)
        driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/com.tencent.tbs.core.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View/android.view.View[1]/android.widget.Image').click()
        time.sleep(2)
        driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/com.tencent.tbs.core.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View/android.view.View[1]/android.widget.Image').click()
        time.sleep(2)
        #点击《投保人声明书》
        driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/com.tencent.tbs.core.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View/android.view.View[2]/android.view.View[7]/android.view.View[4]').click()
        driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/com.tencent.tbs.core.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View/android.view.View[1]/android.widget.Image').click()
        time.sleep(2)
        #点击《投保提示书》
        driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/com.tencent.tbs.core.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View/android.view.View[2]/android.view.View[7]/android.view.View[6]').click()
        time.sleep(2)

        driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/com.tencent.tbs.core.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View/android.view.View[1]/android.widget.Image').click()
        time.sleep(2)
        # 点击《投保须知》
        driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/com.tencent.tbs.core.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View/android.view.View[2]/android.view.View[7]/android.view.View[8]').click()
        time.sleep(2)
        driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/com.tencent.tbs.core.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View/android.view.View[2]/android.widget.ListView/android.view.View').click()
        time.sleep(2)
        driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/com.tencent.tbs.core.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View/android.view.View[1]/android.widget.Image').click()
        time.sleep(2)
        driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/com.tencent.tbs.core.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View/android.view.View[1]/android.widget.Image').click()
        time.sleep(2)

        # driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/com.tencent.tbs.core.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View/android.view.View[1]/android.widget.Image').click()
        # time.sleep(2)
        #点击下一步
        driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/com.tencent.tbs.core.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View/android.view.View[2]/android.widget.Button[2]').click()







    # 测试结束后执行的方法
    def tearDown(self):
        self.driver.quit()
        # pass