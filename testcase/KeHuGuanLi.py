# -*- coding: utf-8 -*-

'''
H5端日程管理--新增客户
'''


import ddt
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

from config import setting
from lib.readexcel import ReadExcel

# testData = ReadExcel(setting.SOURCE_FILE_4, "Sheet1").read_data()
testData = ReadExcel(setting.SOURCE_FILE_4, "Sheet2").read_data()

@ddt.ddt
class KeHuGuanLi(unittest.TestCase):
    def setUp(self):
        # AppDynamics will automatically override this web driver
        # as documented in https://docs.appdynamics.com/display/PRO44/Write+Your+First+Script
        self.driver = webdriver.Chrome('E:\chromedriver.exe')
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    @ddt.data(*testData)
    def test_app_dynamics_job(self,data):
        driver = self.driver
        driver.get("https://sita.aixin-life.net/ax_client/index.html#/zl/webLogin")
        time.sleep(4)
        driver.find_element_by_xpath('/html/body/ion-nav-view/div/ion-nav-view/div/ion-view/ion-content/div[1]/form/div/div[2]/div[1]/div[1]/input').clear()
        driver.find_element_by_xpath(
            '/html/body/ion-nav-view/div/ion-nav-view/div/ion-view/ion-content/div[1]/form/div/div[2]/div[1]/div[1]/input').send_keys("1130100002")
        driver.find_element_by_xpath("//input[@type='password']").clear()
        driver.find_element_by_xpath("//input[@type='password']").send_keys("123456")
        driver.find_element_by_xpath("//button[@type='button']").click()
        time.sleep(4)
        #点击日程管理/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/ion-content/div[1]/div/div/div[4]/p[1]/img
        driver.find_element_by_xpath("/html/body/ion-nav-view/div/ion-nav-view/ion-nav-view/div/ion-view/ion-content/div[1]/div/div/div[4]/p[1]/img')]").click()
        time.sleep(4)
        #添加日程
        driver.find_element_by_xpath("//img[contains(@src,'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADwAAAA8CAYAAAA6/NlyAAAAAXNSR0IArs4c6QAAAnRJREFUaAXtm09rE0EYxt93dtvaKA3YFuppPajFiyfxULHYkx+gH8FbQfBLePBaqh/HS60B0YMXRQW1Ip56UVvzb3deZwNbttlAZyXzbAZmL9mZTOZ5f8+T7CYzhAl89A+SbdHyVIgWmfjJhXuHz5ElMFJM5H7c3/96JCTtXNeIpwut1TbffvsXVYdCCeU6g4Mf6wVs3jYpx8PB0Xp+jjqgwEoNR8mW4UzKi+W263MoMImKK0A6gtYAFavANtARgBswHSoZEoba3YAYNuFMoF90JvmJBZ5UAbgvAIMNh8uFhOGWgwVDwmDD4XLNJ6xT87MYdzQPjGMdKQVgsOFwuZAw3HKwYEgYbDhcDppwarYa4IRjgqfLpvLu1kXq/rlE6Xw0NmZqzQH3lnV2djqzSrsib5IrZ3vPaWm2/7LSizNqtU+K3Q3uvbr6gFK9Z2a4do6M10+bt9ZnitUj7u0nH0Xkhtc0lsXn0MokW9n+sHy9d8OEeUmZq9aed5X/Z8GK6dnoqtnvJDc54zta6yVSytlFi0Sum4/PTrleZrVrthG/lfusz9lmFZQzUfRLZfr1wub399DbRPdlskVaXpSB4og35u4edsp9Ls+h9+GJIOB7c/PAE11w1xmA3Xk7GzOHhGcjB3dVhITdeTsbM2MTlho/6xz5gwV2BFFn2gBcxy0fx4aEfUytTs0h4Tpu+Ti2+YRTm1WL6VnbPPD0WKxmCsBWNnk8KCTscXhWpUMTjlmllaoi1pU+hx1QYK3l9ziLaAX7z1KuDQWeb13+YFb+jwtoZh7ORWufijbiEQps9miHrKKHzPTFbI3/NICPeaPTRYAWGv8Abg2ACbuFkWQAAAAASUVORK5CYII=')]").click()
        time.sleep(4)
        #添加客户
        driver.find_element_by_xpath("//img[contains(@src,'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADMAAAA5CAYAAACbOhNMAAAAAXNSR0IArs4c6QAACLtJREFUaAXNWn2MXFUVv+fN7LzZYgGbBWtXd2fbLSStkRSRdndnt01MjEQh0mIUPxJM8DPRBGtpSkQbRW1BQf8TNMofyEf6ha0hxj8InZ1ui6mg6FIN23ZnpVBDP0Da7rydmXf8nTe9792Znfdmlu4Mc5PZc++595zz+7173333Y0nNc5rJLr2hpEq3EqsVzLxEkeomRVex4jcUqxNEdIJJHYmp2J5E+tjh+QxP8+GMs9cucTi/kZXaoJh7G/ZJlAOAnTYlH6T0v19r2C6k4SWR4bGBzpniiU0gcTd+l4XEqKsGiPP43Z+Idz9Agwen6xqENHjHZArZpemiW3wCfj9Q0zfRf9FLORlWqD+FXxeGXbci6oX+fTVtlPpPXKnbO0amDoTUR6rfERknk/oc3oFH8bNN70TqKBM9FYupXYmB3AtmnZmfOdh7famkNhDzZ5nVMrMO75eD3x32yOSTpr6R/JzJOKM9mzGkfgoQpu1p9MAP7HTfw0TPFRsJLG2Y18Wd7PGvoce2otglOkl4KJgj1BZ7eGp7WdPYXxNQXQsn2/t51+Xfmw3xFHfZC+lOWjX5pqmfS55fTF3pnONfg9Rtpp1l0RfsdO5xUxeVb5iMk+n7MFPpIHpkgXYIIg/Yw5Ob0SvorEtLIELOaGo7hu4m7Qk9dIE4NmCPHH9J66KkFVWp63h85XtAZI9JxCK6NzmSu3s+iEgc8SP+xK8fFw/Oi4v4WhclGyIzc/bcXSCyVDtC4N32cO4+XZ5PKX7Fv/YpcSW+LkfJumR4tOe97KqN2gnG5QQ+cnfocjOk+Jc42rfEFxy6HCbrksmzwkeRr9AOMI7vwdf6bV1uhhT/Ekf7lvh5fJh1OUxGksGMKfVf0cbo/r8l0rmdutxMKXEknh+D1Z0X8fiq6kwkmeLY71bDwJj/aRsCXPLMVQ2iVlni4LfNqOu6iMdQVWajybD6lG4OxzMJZT+jy62QEk/i6lhFA4/WmTKSDLnqpqAxZ5r9rgSxyrlyPM5ofSUerQ1kJBksWPp1UyLrWZ1vpayIa+CphSGUDB/+yAJ8lRdqI2L3VZ1vpTTjCh7BFRY/lIzjvPV+08hV6nWz3Kp8ddxqXCaOUDIxVbi6oqFlyZ6k5cmqimtx8aowEKFksAbHdypIJVddGZRal5sV12InLHooGZc7/mcaWawWm+VW5avjuiV+Kyx2KBn7avUq1kclbciEk5Z3IZlxBY+9OCHb8JoplAwtn3CwLvcXezgmGqzpodlKMy7RKx6ukJihZC62z/p2pD6OfU3CL7cg48VDXD8UqwCPrwwykWQwr8vpi5dkjnfOXliry62QEk/i6lgcUz4erTNlJJnk8OrnsAc86Ruw29AmyW9/qZmKeHQyOfhl4AlPkWSIdpTIUju0OZ7STYVMz5AuN1NKHImnY2AR/RTRVnxDw1MkGTEjij+CWcQ/PioSba+3rwgP11iN+Jc4urXEx8bjEV0Ok3XJ2ENH/wlGv/QdMA/lR397n19uQsbzjziBa/qFPTL1clCunQPp+klOZ/Kn3xZnH5TW5UM62oDDhz31refWwhntvRXb5F04yChjI5pKXn7FCrrupfP1PNXtGXFAK8fPWcr6tnYmgfB7Qo5ptW4+pHfsC78+EYlN1rcaISLxGyIjDXH2+7RFaqvkJeHp2Uzu406m9x68qA31cNly9l+x9/zAn/jVLXCi+f1k+vheXa4n5wxiOtPzEzjdUuGY6FCM6K5EevJQhb6Bwkw2tabE/BAOntdUNCf6cedw7nsVujqFOZMRf/nR3p/jaX6n2jf267vh8LFEbMmfou5ZvHud0mufwMnIF+Fn/Sw/in6G003/mLa6Pqw8ZzL5bN+1it1fAcS6CKd4WWk/XuFJTKm49uNTOGvpwmDsxvhMYZCuBZHwyymi/VZcfcMeyB0Ji1FL3zAZbFc78hdO3YuZbDOINH2NJqcyIHx/srPrh3TDXwu1wFfrGiLDh6/pyk87OzGuZ63NQG4fAj/p4hgI1yqfxkzUWR0krAzbaUyMf8DEso9dXDwpdUuNtpmkStxGIxNv1KirUNUlI1cZLrl7QaTXtIThn60O2mLekPGh/svzxcJncCS0HsBWYThVnCOU7el12L7IltqdjHfsoDUT/iZwZqx3lVvkbbANVspihItci61b6l1tRJJxDiz7kOsW9mOcL9JEYHBeWdbGZHryYa0Lkx45Li6ySvHL3FjxfJLiZ0zwYXb50Z6vIuaDIBW8V6TOWLH4Onvw2D/C7ELJ5A8tXc4zpQyerr9dxuXSERXruDk5NHE0zOF86fMH+pcpt7AX7+eKwCedpERsJLnm2CuBLsjVJCPXBw7TC/iApfymRM8nE52fpNX/Ou3rmpzhsZWL8qVzz2CIy5m3l/BAJ23i62l46qzWaVlzBYD98m8qiCiVwfroY60kIgBpcPyMxEUWI6ScBJfg02VTziKDD+I3zQ8ZZpxjSXvB+kbXR6bz+chLXC8+cGh/gk9w6rKWFcOM/5Ja7OTdCf3iYcrFpU/HgJ2eGNcG75Z0sv0rmQu4IC5vo2UispNWP9046e+EK3rGyfOPNBEPNNGmdiAiWDwcwKMfpuAUvLos0u8ZmYbZLfwdH70yQSweMf0Oondg1x4JvUL5bGpML0rxCrhkdVznbSAB0e8Zt1T4riaCRjgIsb7eTkTkcQqeMi58hZAEr+CWvCSvZ7ypWGFBeHEpAqM/JodzN5ebtN9fvPz70EverZ4sibAB6pap2usZnER/SRMR6FhqPNR+FAJEJj7BLfil1iODoehvf8F0vHMo92xg2n45wSc4NTKN38J/8S3EK/JRv0LR0zrfzhKrbR+n4BcelsPTa/E2xTXweEy19EZZx52rNHEKfuFh4T+7RrQjrHvejA/c+Lwut7MUnII3wGgNW5jP+rUCDF+WI1ldbmcpOAVvgJGXo2dUylDUXFoH9e2W4wAveMhs1qch4n+9gsslrWxjWYW37//4PlNJ9wnPjAAAAABJRU5ErkJggg==')]").click()
        #新增客户
        time.sleep(4)
        driver.find_element_by_xpath("//img[contains(@src,'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADwAAAA8CAYAAAA6/NlyAAAAAXNSR0IArs4c6QAAAnRJREFUaAXtm09rE0EYxt93dtvaKA3YFuppPajFiyfxULHYkx+gH8FbQfBLePBaqh/HS60B0YMXRQW1Ip56UVvzb3deZwNbttlAZyXzbAZmL9mZTOZ5f8+T7CYzhAl89A+SbdHyVIgWmfjJhXuHz5ElMFJM5H7c3/96JCTtXNeIpwut1TbffvsXVYdCCeU6g4Mf6wVs3jYpx8PB0Xp+jjqgwEoNR8mW4UzKi+W263MoMImKK0A6gtYAFavANtARgBswHSoZEoba3YAYNuFMoF90JvmJBZ5UAbgvAIMNh8uFhOGWgwVDwmDD4XLNJ6xT87MYdzQPjGMdKQVgsOFwuZAw3HKwYEgYbDhcDppwarYa4IRjgqfLpvLu1kXq/rlE6Xw0NmZqzQH3lnV2djqzSrsib5IrZ3vPaWm2/7LSizNqtU+K3Q3uvbr6gFK9Z2a4do6M10+bt9ZnitUj7u0nH0Xkhtc0lsXn0MokW9n+sHy9d8OEeUmZq9aed5X/Z8GK6dnoqtnvJDc54zta6yVSytlFi0Sum4/PTrleZrVrthG/lfusz9lmFZQzUfRLZfr1wub399DbRPdlskVaXpSB4og35u4edsp9Ls+h9+GJIOB7c/PAE11w1xmA3Xk7GzOHhGcjB3dVhITdeTsbM2MTlho/6xz5gwV2BFFn2gBcxy0fx4aEfUytTs0h4Tpu+Ti2+YRTm1WL6VnbPPD0WKxmCsBWNnk8KCTscXhWpUMTjlmllaoi1pU+hx1QYK3l9ziLaAX7z1KuDQWeb13+YFb+jwtoZh7ORWufijbiEQps9miHrKKHzPTFbI3/NICPeaPTRYAWGv8Abg2ACbuFkWQAAAAASUVORK5CYII=')]").click()
        time.sleep(4)
        driver.find_element_by_xpath("(//input[@type='text'])[11]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[11]").send_keys(data['name'])
        driver.find_element_by_xpath("//div[@id='app']/div/div[5]/div/div/div[2]").click()
        #证件类型
        time.sleep(2)
        if data['type']=="身份证":
            driver.find_element_by_xpath('/html/body/div[1]/div/div[5]/div/div[2]/form/div[3]/div[2]/select')\
                .find_element_by_xpath('/html/body/div[1]/div/div[5]/div/div[2]/form/div[3]/div[2]/select/option[1]').click()
        elif data['type']=="护照":
            driver.find_element_by_xpath('/html/body/div[1]/div/div[5]/div/div[2]/form/div[3]/div[2]/select')\
                .find_element_by_xpath('/html/body/div[1]/div/div[5]/div/div[2]/form/div[3]/div[2]/select/option[2]').click()
        elif data['type']=="军官证":
            driver.find_element_by_xpath('/html/body/div[1]/div/div[5]/div/div[2]/form/div[3]/div[2]/select')\
                .find_element_by_xpath('/html/body/div[1]/div/div[5]/div/div[2]/form/div[3]/div[2]/select/option[3]').click()
        elif data['type']=="户口本":
            driver.find_element_by_xpath('/html/body/div[1]/div/div[5]/div/div[2]/form/div[3]/div[2]/select')\
                .find_element_by_xpath('/html/body/div[1]/div/div[5]/div/div[2]/form/div[3]/div[2]/select/option[4]').click()
        elif data['type']=="出生证":
            driver.find_element_by_xpath('/html/body/div[1]/div/div[5]/div/div[2]/form/div[3]/div[2]/select')\
                .find_element_by_xpath('/html/body/div[1]/div/div[5]/div/div[2]/form/div[3]/div[2]/select/option[5]').click()
        elif data['type']=="士兵证":
            driver.find_element_by_xpath('/html/body/div[1]/div/div[5]/div/div[2]/form/div[3]/div[2]/select')\
                .find_element_by_xpath('/html/body/div[1]/div/div[5]/div/div[2]/form/div[3]/div[2]/select/option[6]').click()
        elif data['type']=="临时身份证":
            driver.find_element_by_xpath('/html/body/div[1]/div/div[5]/div/div[2]/form/div[3]/div[2]/select')\
                .find_element_by_xpath('/html/body/div[1]/div/div[5]/div/div[2]/form/div[3]/div[2]/select/option[7]').click()
        elif data['type']=="台湾居民来往大陆通行证":
            driver.find_element_by_xpath('/html/body/div[1]/div/div[5]/div/div[2]/form/div[3]/div[2]/select')\
                .find_element_by_xpath('/html/body/div[1]/div/div[5]/div/div[2]/form/div[3]/div[2]/select/option[8]').click()
        elif data['type']=="港澳居民来往内地通行证":
            driver.find_element_by_xpath('/html/body/div[1]/div/div[5]/div/div[2]/form/div[3]/div[2]/select')\
                .find_element_by_xpath('/html/body/div[1]/div/div[5]/div/div[2]/form/div[3]/div[2]/select/option[9]').click()


        #证件号码
        driver.find_element_by_xpath("(//input[@type='text'])[12]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[12]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[12]").send_keys(data['ID'])
        #
        driver.find_element_by_xpath("//div[@id='app']/div/div[5]/div/div[2]/form/div[5]/div/span").click()
        #证件有效期
        # driver.find_element_by_xpath("(//input[@type='text'])[14]").click()
        # driver.find_element_by_xpath("//body/div[3]/div/div[2]").click()
        # driver.find_element_by_xpath("//div[2]/div/div/div[4]/div[2]/div").click()
        driver.find_element_by_xpath('//*[@id="mbox"]').click()

        driver.find_element_by_xpath("//div[@id='app']/div/div[5]/div/div[2]/form/div[9]/div/span[2]").click()
        driver.find_element_by_xpath("//div[@id='app']/div/div[5]/div/div[2]/form/div[12]/div/input").click()
        driver.find_element_by_xpath("//div[@id='app']/div/div[5]/div[2]/div/ion-content/div[2]/div").click()
        driver.find_element_by_xpath("//div[@id='app']/div/div[5]/div[2]/div/ion-content/div[2]/div").click()
        driver.find_element_by_xpath("//div[@id='app']/div/div[5]/div[2]/div/ion-content/div[2]/div").click()
        driver.find_element_by_xpath("(//input[@type='text'])[17]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[17]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[17]").send_keys("177")
        driver.find_element_by_xpath("(//input[@type='text'])[18]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[18]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[18]").send_keys("77")
        driver.find_element_by_xpath("(//input[@type='text'])[19]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[19]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[19]").send_keys("77")
        driver.find_element_by_xpath("//div[@id='app']/div/div[5]/div/div[2]/form/div[17]/div/span").click()
        driver.find_element_by_xpath("//ion-icon[@name='add-circle-outline']").click()
        driver.find_element_by_xpath("(//input[@type='text'])[20]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[20]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[20]").send_keys(int(data['tel']))
        driver.find_element_by_xpath("//input[@type='email']").clear()
        driver.find_element_by_xpath("//input[@type='email']").send_keys("32732783@126.com")
        driver.find_element_by_xpath("(//input[@type='text'])[22]").click()
        driver.find_element_by_xpath("//div[@id='app']/div/div[5]/div[2]/div[2]/div/ion-content/div/div").click()
        driver.find_element_by_xpath("//div[@id='app']/div/div[5]/div[2]/div[2]/div/ion-content/div/div").click()
        driver.find_element_by_xpath("//div[@id='app']/div/div[5]/div[2]/div[2]/div/ion-content/div/div").click()
        driver.find_element_by_xpath("(//input[@type='text'])[23]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[23]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[23]").send_keys(u"石景山区88号")
        driver.find_element_by_xpath("(//input[@type='number'])[2]").clear()
        driver.find_element_by_xpath("(//input[@type='number'])[2]").send_keys("776633")
        driver.find_element_by_xpath("(//button[@type='button'])[3]").click()
        driver.find_element_by_xpath("(//ion-icon[@name='add-circle-outline'])[2]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[20]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[20]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[20]").send_keys("617420100037139511")
        driver.find_element_by_xpath("//div[@id='app']/div/div[5]/div[2]/div/ion-content/form/div[3]/div[2]/select").click()
        Select(driver.find_element_by_xpath("//div[@id='app']/div/div[5]/div[2]/div/ion-content/form/div[3]/div[2]/select")).select_by_visible_text(u"农业银行")
        driver.find_element_by_xpath("//option[@value='103']").click()
        driver.find_element_by_xpath("(//input[@type='text'])[21]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[21]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[21]").send_keys(int(data['tel']))
        driver.find_element_by_id("btn").click()
        time.sleep(4)
        driver.find_element_by_xpath("(//button[@type='button'])[2]").click()
        print(data['name']+"客户添加成功！")
        time.sleep(2)

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
