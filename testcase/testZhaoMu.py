# coding='utf-8'
'''
招募

'''
import unittest

import ddt
import selenium
from selenium import webdriver
import time
import xlrd
# from venv.test_proa4 import open1_exel
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# 打开表格
from config import setting
from lib.readexcel import ReadExcel

testData = ReadExcel(setting.SOURCE_FILE, "Sheet1").read_data()
# workbook = xlrd.open_workbook('E:\python_pycharm\DemoAPI-master\database\Proa_customer.xlsx')

@ddt.ddt()
class zhaomu(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://uata.aixin-life.net/ax_client/index.html#/zl/webLogin')
        time.sleep(2)
        self.driver.maximize_window()  # 页面最大化


    @ddt.data(*testData)
    def test_LogIn(self, data):
        driver=self.driver
        #输入账号
        # driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/div/ion-view/ion-content/div[1]/form/div/div[2]/div[1]/div[1]/input').send_keys(int(wpsname.cell(1,0).value))
        driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/div/ion-view/ion-content/div[1]/form/div/div[2]/div[1]/div[1]/input').send_keys('1130100219')

        time.sleep(1)
        #输入密码
        # driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/div/ion-view/ion-content/div[1]/form/div/div[2]/div[1]/div[3]/input[1]').send_keys(int(wpspassword.cell(0,0).value))
        driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/div/ion-view/ion-content/div[1]/form/div/div[2]/div[1]/div[3]/input[1]').send_keys('123456')

        time.sleep(2)
        #点击登录
        driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/div/ion-view/ion-content/div[1]/form/div/div[2]/div[2]/button').click()
        time.sleep(5)
        driver.implicitly_wait(10)
        # 点击 招募管理
        driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/ion-content/div[1]/div/div/div[3]/p[1]/img').click()
        # /html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/ion-content/div[1]/div/div/div[2]
        time.sleep(4)
        driver.implicitly_wait(10)


        '''
            实现新增候选人
        '''

        # 点击右上角按钮
        driver.find_element_by_xpath('//*[@id="indexId"]/div[2]/ion-header-bar/div[3]/span/button').click()
        # /html/body/div[6]/div/ion-modal-view/ion-content/div/div[1]/span[2]
        driver.implicitly_wait(10)
        time.sleep(2)
        # 点击新增候选人
        driver.find_element_by_xpath('/html/body/div[6]/div/ion-modal-view/ion-content/div/div[1]').click()
        time.sleep(4)
        driver.implicitly_wait(10)
        # 输入姓名
        # driver.find_element_by_xpath("/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/ion-content/div[1]/div[1]/input").send_keys(wpsname.cell(1,1).value)
        driver.find_element_by_xpath(
            "/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/ion-content/div[1]/div[1]/input").send_keys(data['name'])
        #选择性别
        #选择男
        # driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/ion-content/div[1]/div[2]/div/span[1]').click()
        #选择女
        driver .find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/ion-content/div[1]/div[2]/div/span[2]').click()
        time.sleep(1)
        #输入手机号
        # driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/ion-content/div[1]/div[4]/input').send_keys(int(wpsname.cell(1,3).value))
        driver.find_element_by_xpath(
            '/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/ion-content/div[1]/div[4]/input'
        ).send_keys(int(data['tel']))

        time.sleep(4)
        #选择招募信息来源
        driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/ion-content/div[1]/div[6]/div/button').find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/ion-content/div[1]/div[6]/div/select/option[2]').click()

        driver.implicitly_wait(10)
        time.sleep(4)
        #点击提交
        driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/ion-content/div[1]/div[7]/div/div').click()
        time.sleep(6)



        #点击确定
        # driver.find_element_by_xpath('/html/body/div[7]/div/div[3]/button').click()
        # print(driver.find_element_by_css_selector("on-hold=\"errorAllFun()\""))
        print(driver.find_element_by_css_selector('img[class="disable-user-behavior"]'))


        try:
            # /html/body/div[7]/div/div[2]/span
            # while driver.find_element_by_xpath('/html/body/div[7]/div/div[2]/span[text()="该候选人已在库"]').is_displayed():
            while driver.find_element_by_css_selector('img[class="disable-user-behavior"]').is_displayed():
                # 点击确定

                driver.find_element_by_xpath('/html/body/div[7]/div/div[3]/button').click()
                time.sleep(2)
                print(222222222222222)
                driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/ion-content/div[1]/div[4]/input').clear()
                driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/ion-content/div[1]/div[4]/input').send_keys(int(data['tel']))
                time.sleep(4)
                # 点击提交
                driver.find_element_by_xpath(
                    '/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/ion-content/div[1]/div[7]/div/div').click()
                time.sleep(6)
                # 点击确定
                driver.find_element_by_xpath('/html/body/div[7]/div/div[3]/button').click()
                break
        except:
            # 点击确定
            # driver.find_element_by_xpath('/html/body/div[7]/div/div[3]/button').click()
            driver.find_element_by_xpath("//div[3]/button").click()
            print(11111111)
        time.sleep(4)

        # 打印时间
        print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
        '''
        TA
        '''
        # 点击TA
        # el1 = driver.find_element_by_css_selector('div[class*="my_tabox"]')
        el1 = driver.find_element_by_xpath("//div[13]").click()
        #move_to_element(element)                   鼠标悬浮在某元素上
        # perform()                                 执行所有存储在ActionChains中的动作
        webdriver.ActionChains(driver).move_to_element(el1).click(el1).perform()
        #/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/ion-view/ion-content/div[1]/div[2]/div[13]
        time.sleep(3)
        # 点击预约
        driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/ion-view/ion-content/div[1]/div[1]/div[2]/div[6]').click()
        time.sleep(1)
        driver.implicitly_wait(10)
        driver.find_element_by_xpath('//*[@id="opreationMenu0"]/div[1]/span').click()

        time.sleep(6)
        # 点击OT
        driver.implicitly_wait(10)
        driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/ion-content/div[1]/div[6]/div/div[1]/span[1]').click()
        time.sleep(2)
        # 点击成功
        driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/ion-content/div[1]/div[7]/div/span[1]').click()
        # 点击预约时间，选择时间
        # driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/ion-content/div[1]/div[7]/div[1]/div[1]/img').click()
        # element1=driver.find_element_by_css_selector('body > ion-nav-view > div > ion-nav-view > ion-nav-view > div > ion-view > ion-content > div.scroll > div:nth-child(7) > div:nth-child(1) > div:nth-child(1) > img')
        element1=driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/ion-content/div[1]/div[8]/div[1]/div[1]/img')
        webdriver.ActionChains(driver).move_to_element(element1).click(element1).perform()

        time.sleep(4)
        driver.find_element_by_xpath('/html/body/div[7]/div/div[2]/div/div[4]/div[2]/div').click()
        time.sleep(2)
        #输入详细地址
        driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/ion-content/div[1]/div[8]/div[1]/div[2]/input').clear()
        driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/ion-content/div[1]/div[8]/div[1]/div[2]/input').send_keys('北京市石景山区融科创意中心A座')
        time.sleep(1)
        # 选择面试官
        driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/ion-content/div[1]/div[8]/div[1]/div[3]/div[1]/button').click()

        time.sleep(4)
        driver.implicitly_wait(10)
        driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/ion-content/div[1]/div/div[3]/img').click()#选择面试官
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/div[2]/div[3]/button[1]').click()#点击提交按钮
        time.sleep(6)
        # # 将页面滑动至底部
        # # js="var q=document.documentElement.scrollTop=10000"
        # js = "var q=document.body.scrollTop=10000"
        # driver.execute_script(js)
        # WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/ion-content/div[1]/div[8]/div[2]')))


        # 点击下一步按钮
        # driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/ion-content/div[1]/div[8]/div[2]').click()
        selenium2=driver.find_element_by_css_selector('body > ion-nav-view > div > ion-nav-view > ion-nav-view > div > ion-view > ion-content > div.scroll > div.acs_tj > div.acs_detail_tj')
        webdriver.ActionChains(driver).move_to_element(selenium2).click(selenium2).perform()
        time.sleep(8)
        # 面试官已存在工作计划：  继续预约
        # '''
        try:
            # driver.find_element_by_xpath('/html/body/div[7]/div/div[3]/button[2]').is_displayed():
            print("1111111111")
            driver.find_element_by_xpath('/html/body/div[7]/div/div[3]/button[2]').click()
            time.sleep(8)
            print("222222222222")
            # 弹出预约成功，点击确定按钮。
            driver.find_element_by_xpath('/html/body/div[7]/div/div[3]/button').click()
        except:
            # 弹出预约成功，点击确定按钮。
            print('333333333333')
            driver.find_element_by_xpath('/html/body/div[7]/div/div[3]/button').click()
        # '''
        # driver.find_element_by_xpath('/html/body/div[7]/div/div[3]/button').click()
        time.sleep(2)
        # 返回我的候选人页面
        driver.find_element_by_xpath('//*[@id="indexId"]/div[1]/ion-header-bar/div[1]/span/button').click()
        time.sleep(6)

        '''
        OT
        '''

        # 点击我的面试，进入我的面试页面
        driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/ion-view/ion-content/div[1]/div[1]/div[2]').click()
        time.sleep(2)
        # 点击OT
        driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/ion-view/ion-content/div[1]/div[2]/div[1]/div[1]').click()
        time.sleep(2)
        # 点击待OT
        driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/ion-content/div[1]/ul/li[1]/img').click()
        time.sleep(2)

        #点击签到
        driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/ion-view/ion-content/div[1]/div[2]/div[1]/div[2]/div[6]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="staffIntSetting0"]/div[1]/span').click()
        time.sleep(6)
        # 候选人：XX 确定OT签到吗？    点击确定按钮
        driver.find_element_by_xpath('/html/body/div[7]/div/div[3]/button[2]').click()
        time.sleep(8)
        # 签到 成功  点击确定按钮
        driver.find_element_by_xpath('/html/body/div[7]/div/div[3]/button').click()
        time.sleep(2)
        # 点击返回
        driver.find_element_by_xpath('//*[@id="indexId"]/div[1]/ion-header-bar/div[1]/span/button').click()
        time.sleep(2)
        # 点击已签到
        driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/ion-content/div[1]/ul/li[2]/img').click()
        time.sleep(2)
        # 点击OT结果录入
        driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/ion-view/ion-content/div[1]/div[3]/div[2]/div[2]/div[5]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="opreationMenu0"]/div[1]/span').click()
        time.sleep(6)
        # 面试结果，点击通过
        driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/div[3]/ion-content/div[1]/dl/dl[1]/dd/ion-list/div/label[1]/div').click()
        time.sleep(1)
        # 评分级别 选择A+
        driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/div[3]/ion-content/div[1]/dl/dl[2]/dd/ion-list/div/label[1]/div').click()
        time.sleep(1)

        #选择OT形式
        '''下拉框选择'''
        driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/div[3]/ion-content/div[1]/dl/dl[3]/dt/select').find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/div[3]/ion-content/div[1]/dl/dl[3]/dt/select/option[2]').click()
        time.sleep(1)


        # 点击提交结果并预约
        driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/div[4]/button').click()
        time.sleep(2)
        # 提交成功，点击确定按钮
        driver.find_element_by_xpath('/html/body/div[7]/div/div[3]/button').click()
        time.sleep(3)
        # 在预约页面点击 ACS
        driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/ion-content/div[1]/div[6]/div/div[1]/span[2]').click()
        time.sleep(1)
        # 预约结果  点击成功
        driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/ion-content/div[1]/div[7]/div/span[1]').click()
        time.sleep(2)
        #选择会议
        driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/ion-content/div[1]/div[8]/div[1]/div[1]/button').click()

        time.sleep(2)
        driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/ion-content/div[1]/div[1]/div[2]/img').click()#选中会议
        time.sleep(1)
        #点击确定按钮
        selenium4=driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/ion-content/div[1]/div[2]/div/button[1]')
        webdriver.ActionChains(driver).move_to_element(selenium4).click(selenium4).perform()
        time.sleep(2)
        driver.implicitly_wait(10)
        #点击下一步按钮
        selenium5=driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/ion-content/div[1]/div[9]/div[2]')
        webdriver.ActionChains(driver).move_to_element(selenium5).click(selenium5).perform()



        time.sleep(2)
        driver.implicitly_wait(10)

        #预约成功点击确定按钮
        driver.find_element_by_xpath('/html/body/div[7]/div/div[3]/button').click()
        time.sleep(6)
        driver.implicitly_wait(10)

        #点击返回  返回到招募管理页面
        driver.find_element_by_xpath('//*[@id="indexId"]/div[2]/ion-header-bar/div[1]/span/button').click()

        time.sleep(3)

        '''
        ACS 会议
        '''

        #点击 ACS
        selenium3=driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/ion-view/ion-content/div[1]/div[2]/div[15]')
        webdriver.ActionChains(driver).move_to_element(selenium3).click(selenium3).perform()
        time.sleep(4)
        #点击签到
        driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/ion-view/ion-content/div[1]/div[1]/div[2]/div[6]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="opreationMenu0"]/div[1]').click()
        time.sleep(2)
        #选择ACS形式
        driver.find_element_by_xpath('/html/body/div[7]/div/ion-modal-view/ion-content/div[1]/div[1]/div/select').find_element_by_xpath('/html/body/div[7]/div/ion-modal-view/ion-content/div[1]/div[1]/div/select/option[2]').click()

        time.sleep(2)
        # 点击确定
        driver.find_element_by_xpath('/html/body/div[7]/div/ion-modal-view/ion-content/div[1]/div[2]/button[1]').click()
        time.sleep(2)
        # 签到成功，    点击确定
        driver.find_element_by_xpath('/html/body/div[8]/div/div[3]/button').click()

        time.sleep(2)
        #返回招募管理页面
        driver.find_element_by_xpath('//*[@id="indexId"]/div[2]/ion-header-bar/div[1]/span/button').click()
        time.sleep(4)

        '''
        ASC1
        '''
        #点击ASC1
        selenium5=driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/ion-view/ion-content/div[1]/div[2]/div[16]')

        webdriver.ActionChains(driver).move_to_element(selenium5).click(selenium5).perform()
        time.sleep(4)
        driver.implicitly_wait(10)
        # 点击预约
        driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/ion-view/ion-content/div[1]/div[1]/div[2]/div[6]').click()

        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="opreationMenu0"]/div[1]').click()
        time.sleep(6)
        #点击ASC1按钮
        driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/ion-content/div[1]/div[6]/div/div[1]/span[3]').click()
        time.sleep(1)
        #点击成功按钮
        driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/ion-content/div[1]/div[7]/div/span[1]').click()
        # 选择预约时间
        selenium6=driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/ion-content/div[1]/div[8]/div[1]/div[1]/img')
        webdriver.ActionChains(driver).move_to_element(selenium6).click(selenium6).perform()
        time.sleep(4)
        #选择时间，点击确定按钮

        driver.find_element_by_xpath('/html/body/div[8]/div/div[2]/div/div[4]/div[2]/div').click()
        # webdriver.ActionChains(driver).move_to_element(driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/ion-content/div[1]/div[8]/div[1]/div[1]/img')).click(driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/ion-content/div[1]/div[8]/div[1]/div[1]/img')).perform()
        time.sleep(3)
        # 输入详细地址

        driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/ion-content/div[1]/div[8]/div[1]/div[2]/input').send_keys('北京市石景山区融科创意中心A座')
        time.sleep(1)
        #选择面试官
        driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/ion-content/div[1]/div[8]/div[1]/div[3]/div[1]/button').click()
        time.sleep(4)
        #
        driver.find_element_by_xpath('//div[3]/img').click()
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/div[2]/div[3]/button[1]').click()
        time.sleep(6)
        # 点击下一步
        selenium7=driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/ion-content/div[1]/div[9]/div[2]')
        webdriver.ActionChains(driver).move_to_element(selenium7).click(selenium7).perform()
        time.sleep(6)

        try:
            if driver.find_element_by_xpath('/html/body/div[8]/div/div[3]/button[2]').is_displayed():
            # if driver.find_element_by_link_text('陈林无敌在如下时间已存在工作计划:').is_displayed():
                print("444444444444")
                driver.find_element_by_xpath('/html/body/div[8]/div/div[3]/button[2]').click()
                time.sleep(2)
                print("555555555555")
                # 弹出预约成功，点击确定按钮。
                driver.find_element_by_xpath('/html/body/div[8]/div/div[3]/button').click()
            # elif driver.find_element_by_xpath('/html/body/div[8]/div/div[3]/button[2]').is_displayed():
            #     driver.find_element_by_xpath('/html/body/div[8]/div/div[3]/button[2]').click()
            #     time.sleep(2)
            #     print("-------------------")
        except :
            # 弹出预约成功，点击确定按钮。
            print('66666666666')
            driver.find_element_by_xpath('/html/body/div[8]/div/div[3]/button').click()




        driver.implicitly_wait(10)
        # #  候选人：XX 确定进行ACS签到吗？              点击确定按钮
        # driver.find_element_by_xpath('/html/body/div[8]/div/div[3]/button[2]').click()
        # time.sleep(2)

        time.sleep(4)
        # # 预约成功   点击确定
        # driver.find_element_by_xpath('//html/body/div[8]/div/div[3]/button').click()

        # time.sleep(2)
        # 点击返回按钮，返回至招募管理页面

        driver.find_element_by_xpath('//*[@id="indexId"]/div[2]/ion-header-bar/div[1]/span/button').click()
        time.sleep(4)
        # 点击我的面试，跳转至我的面试页面
        driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/ion-view/ion-content/div[1]/div[1]/div[2]').click()
        time.sleep(4)
        # 点击  AS1
        driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/ion-view/ion-content/div[1]/div[2]/div[2]/div[1]').click()
        time.sleep(4)
        # 点击待AS1
        driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/ion-content/div[1]/ul/li[1]/img').click()
        time.sleep(3)
        # 签到
        driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/ion-view/ion-content/div[1]/div[2]/div[1]/div[2]/div[6]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="staffIntSetting0"]/div[1]/span').click()
        time.sleep(2)
        # 点击确定
        driver.find_element_by_xpath('/html/body/div[8]/div/div[3]/button[2]').click()
        driver.implicitly_wait(10)
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/div[8]/div/div[3]/button').click()
        # driver.find_element_by_css_selector('body > div.popup-container.popup-showing.active > div > div.popup-buttons > button').click()
        time.sleep(3)

        # 点击返回
        driver.find_element_by_xpath('//*[@id="indexId"]/div[2]/ion-header-bar/div[1]/span/button').click()
        time.sleep(2)
        # 点击已签到
        driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/ion-content/div[1]/ul/li[2]/img').click()
        time.sleep(4)
        # AS1 结果录入
        driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/ion-view/ion-content/div[1]/div[3]/div[2]/div[2]/div[5]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="opreationMenu0"]/div[1]').click()
        time.sleep(4)
        # 填写AS1评价
        # 点击通过
        driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/div[3]/ion-content/div[1]/dl/dl[1]/dd/ion-list/div/label[1]/div').click()
        time.sleep(1)
        #点击AS2
        driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/div[3]/ion-content/div[1]/dl/dl[1]/dd/div[2]/ion-list/div/label[2]/div').click()
        time.sleep(1)
        # 评分级别:选择A+
        driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/div[3]/ion-content/div[1]/dl/dl[2]/dd/ion-list/div/label[1]/div').click()
        time.sleep(1)

        #拟任职级，点击请选择。
        # driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/div[3]/ion-content/div[1]/dl/dl[3]/dt/select').find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/div[3]/ion-content/div[1]/dl/dl[3]/dt/select/option[2]').click()
        selenium9=driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/div[3]/ion-content/div[1]/dl/dl[3]/dt/select')
        Select(selenium9).select_by_visible_text('FP-理财规划师')



        time.sleep(1)
        #新人专案： 点击请选择

        selenium8=driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/div[3]/ion-content/div[1]/dl/dl[4]/dt/select')
        s=Select(selenium8)
        # s.select_by_index(3)#通过下标
        # s.select_by_value()#通过Value值
        s.select_by_visible_text('A版基本法')#通过文本

        # webdriver.ActionChains(driver).move_to_element(selenium8).click(selenium8).perform()
        time.sleep(2)
        #点击提交结果
        driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/div[4]/button').click()
        time.sleep(4)
        #点击确定,  跳转至预约页面
        driver.find_element_by_xpath('/html/body/div[8]/div/div[3]/button').click()
        time.sleep(8)
        #点击AS2
        driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/ion-content/div[1]/div[5]/div/div[2]/span[1]').click()
        time.sleep(1)
        #点击成功
        driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/ion-content/div[1]/div[6]/div/span[1]').click()
        time.sleep(1)
        #选择预约时间
        selenium9=driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/ion-content/div[1]/div[7]/div[1]/div[1]/img')
        webdriver.ActionChains(driver).move_to_element(selenium9).click(selenium9).perform()
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/div[8]/div/div[2]/div/div[4]/div[2]/div').click()
        # driver.find_element_by_link_text('确认').click()

        time.sleep(2)
        #输入详细地址
        driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/ion-content/div[1]/div[7]/div[1]/div[2]/input').send_keys('北京市石景山区融科创意中心A座')
        time.sleep(1)
        #选择面试官
        driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/ion-content/div[1]/div[7]/div[1]/div[3]/div[1]/button').click()
        time.sleep(4)
        driver.find_element_by_xpath('//div[3]/img').click()
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/div[2]/div[3]/button[1]').click()
        time.sleep(3)
        # 点击下一步
        selenium10=driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/ion-content/div[1]/div[8]/div[2]')
        webdriver.ActionChains(driver).move_to_element(selenium10).click(selenium10).perform()
        time.sleep(4)

        # if driver.find_element_by_xpath('/html/body/div[8]/div/div[3]/button[2]').is_displayed():
        #     driver.find_element_by_xpath('/html/body/div[8]/div/div[3]/button[2]').click()
        #     time.sleep(4)
        #     driver.find_element_by_xpath('/html/body/div[8]/div/div[3]/button').click()
        # else:
        #     driver.find_element_by_xpath('/html/body/div[8]/div/div[3]/button').click()

        try:
            if driver.find_element_by_xpath('/html/body/div[8]/div/div[3]/button[2]').is_displayed():
                driver.find_element_by_xpath('/html/body/div[8]/div/div[3]/button[2]').click()
                time.sleep(4)
                # 弹出预约成功，点击确定按钮。
                driver.find_element_by_xpath('/html/body/div[8]/div/div[3]/button').click()
        except:
            # 弹出预约成功，点击确定按钮。
            driver.find_element_by_xpath('/html/body/div[8]/div/div[3]/button').click()

        #点击确定
        # driver.find_element_by_xpath('/html/body/div[5]/div/div[3]/button').click()
        time.sleep(4)
        #点击返回  返回至招募管理页面
        driver.find_element_by_xpath('//*[@id="indexId"]/div[1]/ion-header-bar/div[1]/span/button').click()

        time.sleep(4)
        # 点击我的面试，跳转至我的面试页面
        driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/ion-view/ion-content/div[1]/div[1]/div[2]').click()
        time.sleep(1)
        # 点击AS2
        driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/ion-view/ion-content/div[1]/div[2]/div[3]/div[1]').click()
        time.sleep(2)
        # 点击待AS2
        driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/ion-content/div[1]/ul/li[1]/img').click()
        time.sleep(3)
        #签到
        driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/ion-view/ion-content/div[1]/div[2]/div[1]/div[2]/div[6]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="staffIntSetting0"]/div[1]/span').click()
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/div[8]/div/div[3]/button[2]').click()
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/div[8]/div/div[3]/button').click()
        time.sleep(2)

        # 返回  //*[@id="indexId"]/div[1]/ion-header-bar/div[1]/span/button
        driver.find_element_by_xpath('//*[@id="indexId"]/div[1]/ion-header-bar/div[1]/span/button').click()
        # //*[@id="indexId"]/div[2]/ion-header-bar/div[1]/span/button
        time.sleep(2)
        # 点击已签到
        driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/ion-content/div[1]/ul/li[2]/img').click()
        time.sleep(4)
        #AS2结果录入
        driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/ion-view/ion-content/div[1]/div[3]/div[2]/div[2]/div[5]').click()

        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="opreationMenu0"]/div[1]/span').click()
        time.sleep(3)
        # 填写AS2评价
        # 点击通过
        driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/div[3]/ion-content/div[1]/dl/dl[1]/dd/ion-list/div/label[1]/div').click()

        time.sleep(1)
        # 选择offer
        driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/div[3]/ion-content/div[1]/dl/dl[1]/dd/div[2]/ion-list/div/label[1]/div').click()
        time.sleep(1)
        # 选择FPTC班次
        s1=driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/div[3]/ion-content/div[1]/dl/dl[2]/dt/select')#定位下拉框
        s1.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/div[3]/ion-content/div[1]/dl/dl[2]/dt/select/option[2]').click()

        time.sleep(1)
        #评分级别
        driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/div[3]/ion-content/div[1]/dl/dl[3]/dd/ion-list/div/label[1]/div').click()
        time.sleep(1)
        #新人专案
        driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/div[3]/ion-content/div[1]/dl/dl[5]/dt/select')\
            .find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/div[3]/ion-content/div[1]/dl/dl[5]/dt/select/option[3]')\
            .click()


        time.sleep(1)
        #点击提交结果并预约
        driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/div[4]/button').click()
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div[8]/div/div[3]/button').click()
        time.sleep(6)
        # 预约页面
        # 点击offer
        driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/ion-content/div[1]/div[5]/div/div[2]/span[2]').click()
        time.sleep(1)
        #点击成功
        driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/ion-content/div[1]/div[6]/div/span[1]').click()
        time.sleep(1)





        #选择预约时间
        selenium11=driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/ion-content/div[1]/div[7]/div[1]/div[1]/img')
        webdriver.ActionChains(driver).move_to_element(selenium11).click(selenium11).perform()
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/div[8]/div/div[2]/div/div[4]/div[2]/div').click()#点击确定
        time.sleep(2)
        #输入详细地址
        driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/ion-content/div[1]/div[7]/div[1]/div[2]/input').clear()
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/ion-content/div[1]/div[7]/div[1]/div[2]/input').send_keys('北京市石景山区融科创意中心A座')
        time.sleep(1)
        #选择面试官
        driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/ion-content/div[1]/div[7]/div[1]/div[3]/div[1]/button').click()
        time.sleep(4)
        #
        driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/ion-content/div[1]/div/div[2]/img').click()
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/div[2]/div[3]/button[1]').click()
        time.sleep(3)
        # 点击下一步
        selenium12=driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/ion-content/div[1]/div[8]/div[2]')
        webdriver.ActionChains(driver).move_to_element(selenium12).click(selenium12).perform()
        time.sleep(5)
        try:
            if driver.find_element_by_xpath('/html/body/div[8]/div/div[3]/button[2]').is_displayed():
                print("77777")
                driver.find_element_by_xpath('/html/body/div[8]/div/div[3]/button[2]').click()
                time.sleep(2)
                print("8888")
                # 弹出预约成功，点击确定按钮。
                driver.find_element_by_xpath('/html/body/div[8]/div/div[3]/button').click()
        except:
            # 弹出预约成功，点击确定按钮。
            print('9999')
            driver.find_element_by_xpath('/html/body/div[8]/div/div[3]/button').click()


        time.sleep(2)
        #点击返回  返回至招募管理页面
        driver.find_element_by_xpath('//*[@id="indexId"]/div[2]/ion-header-bar/div[1]/span/button').click()

        time.sleep(4)
        # 点击我的面试，跳转至我的面试页面
        driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/ion-view/ion-content/div[1]/div[1]/div[2]').click()
        time.sleep(2)
        # 点击offer
        driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/ion-view/ion-content/div[1]/div[2]/div[4]/div[1]').click()

        time.sleep(4)
        # 点击待offer
        driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/ion-content/div[1]/ul/li[1]/img').click()

        time.sleep(3)
        #签到
        driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/ion-view/ion-content/div[1]/div[2]/div[1]/div[2]/div[6]').click()

        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="staffIntSetting0"]/div[1]/span').click()
        time.sleep(2)
        # 弹框  点击确定
        driver.find_element_by_xpath('/html/body/div[8]/div/div[3]/button[2]').click()
        time.sleep(2)
        # 预约成功   点击确定按钮
        driver.find_element_by_xpath('/html/body/div[8]/div/div[3]/button').click()
        time.sleep(3)
        #点击返回
        driver.find_element_by_xpath('//*[@id="indexId"]/div[2]/ion-header-bar/div[1]/span/button').click()
        time.sleep(2)
        #点击已签到
        driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/ion-content/div[1]/ul/li[2]/img').click()
        time.sleep(2)
        # 修改结果录入
        driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/ion-view/ion-content/div[1]/div[3]/div[2]/div[2]/div[5]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="opreationMenu0"]/div[1]/span').click()
        time.sleep(4)
        driver.implicitly_wait(10)

        '''
        填写offer评价
        '''
        #点击通过
        driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/div[3]/ion-content/div[1]/dl/dl[1]/dd/ion-list/div/label[1]/div').click()

        time.sleep(1)
        #选择FPTC班次
        # Select(driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/div[3]/ion-content/div[1]/dl/dl[2]/dt/select')).\
            # select_by_value('3012d90008cb451c900bedad2cc5037d')
        Select(driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/div[3]/ion-content/div[1]/dl/dl[2]/dt/select')).\
            select_by_index(1)
        # s.select_by_index(3)#通过下标
        # s.select_by_value()#通过Value值
        # s.select_by_visible_text('AMP')#通过文本
        time.sleep(1)
        #选择A+
        driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/div[3]/ion-content/div[1]/dl/dl[3]/dd/ion-list/div/label[1]/div').click()
        time.sleep(1)
        #新人专案
        Select(driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/div[3]/ion-content/div[1]/dl/dl[5]/dt/select')).select_by_index(2)
        time.sleep(1)
        #选择北斗计划标识
        Select(driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/div[3]/ion-content/div[1]/dl/dl[6]/dt/select')).select_by_index(2)
        time.sleep(1)
        #offer 是否签署
        Select(driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/div[3]/ion-content/div[1]/dl/div/div[1]/dl/dt/select')).select_by_index(2)
        time.sleep(1)


        # 点击提交结果并预约
        driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/div[4]/button').click()
        time.sleep(3)
        # 点击确定
        driver.find_element_by_xpath('/html/body/div[8]/div/div[3]/button').click()
        time.sleep(6)
        '''
        预约
        '''
        #点击wp
        driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/ion-content/div[1]/div[5]/div/div[2]/span[3]').click()
        time.sleep(1)
        #点击成功
        driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/ion-content/div[1]/div[6]/div/span[1]').click()
        time.sleep(1)
        #请选择预约的会议
        driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/ion-content/div[1]/div[7]/div[1]/div[1]/button').click()
        time.sleep(5)
        #选择会议
        driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/ion-content/div[1]/div[1]/div[2]/img').click()
        time.sleep(3)

        #点击“确定”

        selenium13=driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/ion-content/div[1]/div[2]/div/button[1]')
        webdriver.ActionChains(driver).move_to_element(selenium13).click(selenium13).perform()
        # /html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/ion-content/div[1]/div[2]/div/button[1]
        time.sleep(5)
        #点击下一步
        driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/ion-content/div[1]/div[8]/div[2]').click()
        time.sleep(2)
        #预约成功，点击确定
        driver.find_element_by_xpath('/html/body/div[8]/div/div[3]/button').click()
        time.sleep(4)

        '''
        WP签到
        '''
        #点击签到
        driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/ion-view/ion-content/div[1]/div[1]/div[2]/div[6]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="opreationMenu0"]/div[1]/span').click()
        time.sleep(4)
        #点击确定
        driver.find_element_by_xpath('/html/body/div[8]/div/ion-modal-view/ion-content/div[1]/div/button[1]').click()
        time.sleep(2)
        print('招募成功！')

        # driver.quit()
    def tearDown(self):
        self.driver.quit()
        pass

if __name__ == '__main__' :
    unittest.main()

