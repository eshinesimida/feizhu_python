# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from scrapy.http import HtmlResponse
from datetime import datetime
import re
import time
import uuid
import random
from mysql import xiechengDAO

class XiechengDriverService(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        #self.driver = webdriver.PhantomJS()
        self.xiechengDao = xiechengDAO()
        # 存放列表页数据
        self.listPageInfo = []


        self.commList = []
        #self.urls=['http://you.ctrip.com/sight/beijing1/234.html','http://you.ctrip.com/sight/beijing1/229.html','http://you.ctrip.com/sight/beijing1/231.html','http://you.ctrip.com/sight/yanqing770/230.html','http://you.ctrip.com/sight/beijing1/5174.html','http://you.ctrip.com/sight/beijing1/233.html','http://you.ctrip.com/sight/huairou120418/243.html']
        self.urls=['https://traveldetail.fliggy.com/item.htm?id=534280065174&spm=181.7395991.1998089960.3.43a81a35jff9Ir&expiredate=',
'https://traveldetail.fliggy.com/item.htm?id=542638396605&spm=181.7395991.1998089960.6.43a81a35jff9Ir&expiredate=','https://traveldetail.fliggy.com/item.htm?id=546390469812&spm=181.7395991.1998089960.3.515bb0e6n1wuk5&expiredate=','https://traveldetail.fliggy.com/item.htm?id=538415550443&spm=181.7395991.1998089960.3.1c80ae37id8Mgq&expiredate=','https://traveldetail.fliggy.com/item.htm?id=554960016772&spm=181.7395991.1998089960.6.1c80ae37id8Mgq&expiredate=','https://traveldetail.fliggy.com/item.htm?id=521492240665&spm=181.7395991.1998089960.3.bb2d947PMob1X&expiredate=','https://traveldetail.fliggy.com/item.htm?id=37740444857&spm=181.7395991.1998089960.3.586436cdhpjCrB&expiredate=','https://traveldetail.fliggy.com/item.htm?id=530264750268&spm=181.7395991.1998089960.3.1f6f6c659pJdj0&expiredate=','https://traveldetail.fliggy.com/item.htm?id=530264750268&spm=181.7395991.1998089960.3.1f6f6c659pJdj0&expiredate=',
'https://traveldetail.fliggy.com/item.htm?id=544592246299&spm=181.7395991.1998089960.3.4957a610BevIQC&expiredate=','https://traveldetail.fliggy.com/item.htm?id=24965168454&spm=181.7395991.1998089960.6.4957a610BevIQC&expiredate=','https://traveldetail.fliggy.com/item.htm?id=538006872633&spm=181.7395991.1998089960.3.30aed337auuGBP&expiredate=&smToken=e689ca188b6f40abbce5aace6ab6e003&smSign=E%2FqgVrf2qmFXkq0atvSSnw%3D%3D','https://traveldetail.fliggy.com/item.htm?id=537959328015&spm=181.7395991.1998089960.6.30aed337auuGBP&expiredate=','https://traveldetail.fliggy.com/item.htm?id=37035712707&spm=181.7395991.1998089960.3.410795d7jYvqEI&expiredate=',
'https://traveldetail.fliggy.com/item.htm?id=521097833745&spm=181.7395991.1998089960.6.5c60df77FqJQpP&expiredate=','https://traveldetail.fliggy.com/item.htm?id=37380297030&spm=181.7395991.1998089960.37.5c60df77FqJQpP&expiredate=','https://traveldetail.fliggy.com/item.htm?id=536597069124&spm=181.7395991.1998089960.9.67c513bas2JD2K&expiredate=','https://traveldetail.fliggy.com/item.htm?id=38495865641&spm=181.7395991.1998089960.36.67c513bas2JD2K&expiredate=','https://traveldetail.fliggy.com/item.htm?id=520185293565&spm=181.7395991.1998089960.3.11f45503huWjl3&expiredate=&smToken=2169be71573145feb3c890850858eae3&smSign=EFNkLG3P478uKluI9BXBdQ%3D%3D','https://traveldetail.fliggy.com/item.htm?id=535487371599&spm=181.7395991.1998089960.3.57cee06a3oEDpo&expiredate=','https://traveldetail.fliggy.com/item.htm?id=536338726405&spm=181.7395991.1998089960.3.3157e3a9rL8xeu&expiredate='




                  ]
    def start(self):
        for url1 in self.urls:
            self.driver.get(url1)
            # 将界面最大化
            self.driver.maximize_window()
            self.driver.implicitly_wait(30)

            time.sleep(3)
            target = self.driver.find_element_by_class_name(
               'item-desc-tabview')
            #target = self.driver.find_element_by_xpath('//div[@id="dp_content"]')
            y = target.location['y']
            print y
            y = y - 100

            js = "var q=document.documentElement.scrollTop=" + str(y)
            self.driver.execute_script(js)
            self.crawlxiecheng()





    def crawlxiecheng(self):
        # 单页循环次数
        loopNum = 0

        ifHandle = False
        # #//*[@id="content"]/div[3]/div[2]/div[5]/p/a
        # #//*[@id="content"]/div[3]/div[2]/div[5]/p/a
        self.driver.find_element_by_xpath('//*[@id="itemDescTab"]/div/div/ul/li[2]').click()
        time.sleep(random.uniform(3, 6))

        #///*[@id="J_Comments"]/div[3]/div[1]/div[1]/div[1]
        self.driver.find_element_by_xpath('//*[@id="J_Comments"]/div[3]/div[1]/div[1]/div[1]').click()
        time.sleep(random.uniform(3, 6))
        #time.sleep(3)

        response1 = HtmlResponse(url="my HTML string", body=self.driver.page_source, encoding="utf-8")
        num = response1.xpath('//*[@id="itemDescTab"]/div/div/ul/li[2]/em/text()').extract()[0]
        print 'num = ' + str(num)

        #获取总页面数
        pageNum = 2800
        num2 = 0
        while(pageNum>=1):
            # 循环次数加1
            loopNum = loopNum + 1
            target = self.driver.find_element_by_class_name(
                'comments-page')
            y = target.location['y']
            # print y
            y = y - 100

            js = "var q=document.documentElement.scrollTop=" + str(y)
            self.driver.execute_script(js)

            time.sleep(3)
            if u"累计评价" in self.driver.page_source:

                if ifHandle == False:
                    a = self.crawllianjie(self.driver.page_source)
                    num2 = int(num2) + 20
                    print 'num2 = ' + str(num2)
                    if(int(num2) >= int(num)):
                        break
                    #if(a ==2):
                    #    break
                    ifHandle = True

                try:
                    #print u"下一页" in self.driver.page_source
                    if u"下一页" in self.driver.page_source:
                        pageNum = pageNum - 1


                        self.driver.find_element_by_xpath('//*[@id="J_Comments"]/div[3]/div[4]/div[2]').click()
                        ifHandle = False
                        loopNum = 0

                        time.sleep(5)
                        #print "页数：" + str(pageNum)

                        num1 = 2800 - pageNum + 1
                        print '页数：' + str(num1)
                    else:
                        break


                except:
                    pageNum = pageNum + 1





        return False if pageNum > 1 else True

    def crawllianjie(self, page_sourse):
        #print page_sourse
        response = HtmlResponse(url="my HTML string", body=page_sourse, encoding="utf-8")
        #/html/body/div[3]/div[1]/ul/li[4]/a/text()
        #//*[@id="page-description-content"]/div[2]/div[2]/ul[1]/li[1]
        #jingqu = response.xpath('//div[@class="content cf"]/div[@class="dest_toptitle detail_tt"]/div[@class="cf"]/div[@class="f_left"]/h1/a/text()').extract()[0]
        jingqu = response.xpath('//*[@id="page-description-content"]/div[2]/div[2]/ul[1]/li[1]/text()').extract()[0]
        jingqu = jingqu.split(':')[1].strip()

        province = response.xpath('//*[@id="page-description-content"]/div[2]/div[2]/ul[1]/li[2]/text()').extract()[0]
        province = province.split(':')[1].strip()
        #print jingqu,province
        A = response.xpath("//div[@class='item-comments']/div[@class='comments-list']/table[@class='table']/tr")
        #print A

        for B in A:
            comment = B.xpath("td[@class='comment']/div[@class='clearfix']/div/div[@class='content']/text()").extract()[0]
            time = B.xpath("td[@class='comment']/div[@class='clearfix']/div/div[@class='date']/text()").extract()[0]

            category = B.xpath("td[@class='sku-info']/p[2]/text()").extract()[0]

            category = category.split(":")[1].strip()
            user = B.xpath("td[@class='user']/text()").extract()[0]
            ID = user +'_'+ jingqu

           # print comment,time,category,user
            #print ID

            self.listPageInfo.append({"ID":ID,"jingqu":jingqu,"province":province, "user": user, "comment":comment,"time":time,
                                      'category':category})
        xiechengService.saveListPageInfo()

        print len(self.listPageInfo)
        #len(self.listPageInfo)
        self.listPageInfo = []





    def saveListPageInfo(self):
        self.xiechengDao.savehotellink(self.listPageInfo)

    def depose(self):
        self.driver.close()

if __name__=="__main__":
    xiechengService = XiechengDriverService()
    xiechengService.start()

    xiechengService.depose()

