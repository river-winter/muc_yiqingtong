#coding=utf-8
"""author:jiangjd"""

from xml.dom.minidom import parse
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def login(usn,psw):
    #无弹窗
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--headless')
    # browser = webdriver.Chrome(options=chrome_options)

    '''
    //*[@id="wapat"]/div/div[2]/div    #定位失败时的xpath
    '''

    browser = webdriver.Chrome()                     #有弹窗
    url = 'https://move.muc.edu.cn/ncov/wap/default/index'
    browser.get(url)

    browser.find_element(*(By.XPATH,'//*[@id="app"]/div[2]/div[1]/input')).send_keys(usn) #账号框

    browser.find_element(*(By.XPATH,'//*[@id="app"]/div[2]/div[2]/input')).send_keys(psw)   #密码框 密码

    browser.find_element(*(By.XPATH,"//*[@class='btn']")).click()

    
    WebDriverWait(browser,10,0.5).until(lambda x:browser.find_element(*(By.XPATH,'/html/body/div[1]/div/div/section/div[4]/ul/li[8]/div/input')).is_displayed())
    browser.find_element(*(By.XPATH,'/html/body/div[1]/div/div/section/div[4]/ul/li[8]/div/input')).click()
    time.sleep(1)
    WebDriverWait(browser,10,0.5).until_not(lambda x:browser.find_element(*(By.XPATH,'/html/body/div[3]/div/div')).is_displayed())

    browser.find_element(*(By.XPATH,'/html/body/div[1]/div/div/section/div[4]/ul/li[9]/div/div/div[2]/span[1]/i')).click()

    browser.find_element(*(By.XPATH,'/html/body/div[1]/div/div/section/div[5]/div/a')).click()

    try:
        browser.find_element(*(By.XPATH,'//*[@id="wapcf"]/div/div[2]/div[2]')).click()
    except:
        browser.find_element(*(By.XPATH,'//*[@id="wapat"]/div/div[2]/div')).click()
        print('您已填写过疫情通')

    browser.quit()
def getelement_xml():
    """
    function:从xml获取用户名和密码
    """
    DOMTree=parse(r'usn_psw.xml')
    list=DOMTree.documentElement
    name=list.getElementsByTagName('item')

    userinfo={}
    for item in name:
        userinfo[item.getElementsByTagName('usn')[0].childNodes[0].data]=item.getElementsByTagName('psw')[0].childNodes[0].data

    return userinfo

userinfo=getelement_xml()
for usr,psw in userinfo.items():
    login(usr,psw)
