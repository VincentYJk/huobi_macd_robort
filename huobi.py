# -*- coding: utf-8 -*-
"""
Created on Sat Dec 02 14:44:30 2017

@author: elliott
"""

from email.mime.text import MIMEText
import smtplib
import talib
import numpy as np
import requests
import demjson
import time




def qqsmtp(money):
    _user = "1352133162@qq.com"
    _pwd  = "lpigwyhdhtaobacc"
    _to   = "2996399245@qq.com"
    msg = MIMEText("当前资金:"+str(money))
    msg["Subject"] = "资金变动"
    
    msg["From"]    = _user
    msg["To"]      = _to
    try:
        s = smtplib.SMTP_SSL("smtp.qq.com", 465)
        s.login(_user, _pwd)
        s.sendmail(_user, _to, msg.as_string())
        s.quit()
        print "Success!"
    except smtplib.SMTPException,e:
        print "Falied,%s"%e

def tupo_1(real,Open,Close,High,Low):
    '''
    if Open > Close:
        med = (Open-Close)/2.0 + Close
    else:
        med = (Close-Open)/2.0 + Open
    '''
    if 1==1: #暂设无条件执行
        print u"符合条件进行向上突破!"
        
            
        if 1==1:#也设无条件执行
            kaishi_1()
    
    return 1
    
def tupo_2(real,Open,Close,High,Low):
    '''
    if Open > Close:
        med = (Open-Close)/2.0 + Close
    else:
        med = (Close-Open)/2.0 + Open
    '''
    
    if 1==1:
        print u"符合条件进行向下突破!"
        
            
          
        if 1 == 1:
            kaishi_2()
                    
    return 1
def kaishi_1():
    global time_1
    
    #time.sleep(2)
    while(1):
        try:
            r = requests.get('https://api.huobi.pro/market/detail/merged?symbol=btcusdt').text
            n = demjson.decode(r)
            break
        except:
            #time.sleep(2)
            continue
    
    value = n['tick']['close'] #float
    zhisun = value*(1-0.005) #设止损为跌0.5%
    print u"下单价格:"+str(value)
    print u"向上突破第一阶段,止损价:"+str(zhisun)
    
    f = open(u"下单.txt","a+")
    f.write("向上突破第一阶段下单价格:"+str(value)+"止损价:"+str(zhisun)+"\n")
    f.close()
    
    
    #time.sleep(2)
    while(1):
        while(1):
            try:
                r = requests.get('http://120.24.241.55:61002/getDataHis.ashx?type=stock&min=5&symbol=EURUSD').text
                break
            except:
                #time.sleep(2)
                continue
        n = demjson.decode(r[11:-1])
        shijian = n['min'][-1]
        if shijian != time_1:
            a = []
            for i in range(-21,-1):
                a.append(float(n['data'][i][3]))
            
            a = np.array(a)
            dif,dea,bar = talib.MACD(a,fastperiod=6,slowperiod=13,signalperiod=6)
            if bar[-1] < 0:
                print u"bar<0加1"
                kk += 1
            time_1 = shijian
        #time.sleep(2)
        print u"进入22"
        while(1):
            try:
                r = requests.get('http://120.24.241.55:61001/?query=price&type=jsonret&symbol=EURUSD').text
                n = demjson.decode(r)
                break
            except:
                #time.sleep(2)
                continue
        close_1 = float(n['list'][0]['price'])
        
        if close_1 <= zhisun:
            autopy.mouse.move(p_1,p_2)
            autopy.mouse.click()
            time.sleep(3)
            autopy.mouse.move(qr_1,qr_2)
            autopy.mouse.click()
            print u"向上突破第一阶段止损完毕"
            
            zijin -= (value-close_1)*25000
            print u"当前资金池:"+str(zijin)
            
            f = open(u"下单.txt","a+")
            f.write("向上突破第一阶段止损完毕价格:"+str(close_1)+"  当前资金池:"+str(zijin)+"\n\n\n\n")
            f.close()
            qqsmtp(zijin)
            
            break
        if close_1 >= zhiyin:
            autopy.mouse.move(p_1,p_2)
            autopy.mouse.click()
            time.sleep(3)
            autopy.mouse.move(qr_1,qr_2)
            autopy.mouse.click()
            print u"向上突破第一阶段止盈完毕"
            zijin += (close_1-value)*25000
            print u"当前资金池:"+str(zijin)
            f = open(u"下单.txt","a+")
            f.write("向上突破第一阶段止盈完毕价格:"+str(close_1)+"  当前资金池:"+str(zijin)+"\n\n\n\n\n")
            f.close()
            qqsmtp(zijin)
            #num = second_1(df,num,zhiyin,r,r_1,bar_len)
            
           
            
            break
        
    return 1
        
def kaishi_2():
    global zijin
    global time_1
    global p_1
    global p_2
    global qr_1
    global qr_2
    #time.sleep(2)
    while(1):
        try:
            r = requests.get('http://120.24.241.55:61001/?query=price&type=jsonret&symbol=EURUSD').text
            break
        except:
            #time.sleep(2)
            continue
    n = demjson.decode(r)
    value = float(n['list'][0]['price'])
    zhisun = value + 0.0010
    zhiyin = value - 0.0010
    print u"下单价格:"+str(value)
    print u"向下突破第一阶段下单价格:"+str(value)+u"止盈价"+str(zhiyin)+u"止损价:"+str(zhisun)
    
    f = open(u"下单.txt","a+")
    f.write("向下突破第一阶段下单价格:"+str(value)+"止盈价"+str(zhiyin)+"止损价:"+str(zhisun)+"\n")
    f.close()
    

    kk = 0
    #time.sleep(2)
    while(1):
        if kk >=3:
            autopy.mouse.move(p_1,p_2)
            autopy.mouse.click()
            time.sleep(3)
            autopy.mouse.move(qr_1,qr_2)
            autopy.mouse.click()
            while(1):
                try:
                    
                    r = requests.get('http://120.24.241.55:61001/?query=price&type=jsonret&symbol=EURUSD').text
                    n = demjson.decode(r)
                    break
                except:
                    #time.sleep(2)
                    continue
            
            close_1 = float(n['list'][0]['price'])
            sss = value-close_1
            if sss<0:
                zijin += sss*25000
                f = open(u"下单.txt","a+")
                f.write("向下突破第一阶段止损完毕1价格:"+str(close_1)+"  当前资金池:"+str(zijin)+"\n\n\n\n")
                f.close()
                qqsmtp(zijin)
                break
            if sss>0:
                zijin += sss*25000
                f = open(u"下单.txt","a+")
                f.write("向下突破第一阶段止赢完毕0价格:"+str(close_1)+"  当前资金池:"+str(zijin)+"\n\n\n\n")
                f.close()
                qqsmtp(zijin)
                break
        
        #time.sleep(3)
        print u"进入22"
        while(1):
            try:
                r = requests.get('http://120.24.241.55:61002/getDataHis.ashx?type=stock&min=5&symbol=EURUSD').text
                n = demjson.decode(r[11:-1])
                break
            except:
                #time.sleep(2)
                continue
        shijian = n['min'][-1]
        if shijian != time_1:
            a = []
            for i in range(-21,-1):
                a.append(float(n['data'][i][3]))
            
            a = np.array(a)
            dif,dea,bar = talib.MACD(a,fastperiod=6,slowperiod=13,signalperiod=6)
            
            if bar[-1] > 0:
                print u"bar>0 加1"
                kk += 1
            time_1 = shijian

        #time.sleep(2)
        while(1):
            try:
                r = requests.get('http://120.24.241.55:61001/?query=price&type=jsonret&symbol=EURUSD').text
                n = demjson.decode(r)
                break
            except:
                time.sleep(2)
                continue
        close_1 = float(n['list'][0]['price'])
        if close_1 <= zhiyin:
            autopy.mouse.move(p_1,p_2)
            autopy.mouse.click()
            time.sleep(3)
            autopy.mouse.move(qr_1,qr_2)
            autopy.mouse.click()
            print u"向下突破第一阶段止盈完毕,最低价:"+str(close_1)
            zijin += (value-close_1)*25000
            print u"当前资金池:"+str(zijin)
            
            f = open(u"下单.txt","a+")
            f.write("向下突破第一阶段止盈完毕价格:"+str(close_1)+"  当前资金池:"+str(zijin)+"\n\n\n\n")
            f.close()
            qqsmtp(zijin)
            
            
            break
        if close_1 >= zhisun:
            autopy.mouse.move(p_1,p_2)
            autopy.mouse.click()
            time.sleep(3)
            autopy.mouse.move(qr_1,qr_2)
            autopy.mouse.click()
            print u"向下突破第一阶段止损完毕,最高价:"+str(close_1)
            
            zijin -= (close_1-value)*25000
            
            f = open(u"下单.txt","a+")
            f.write("向下突破第一阶段止损完毕价格:"+str(close_1)+"  当前资金池为:"+str(zijin)+"\n\n\n\n")
            f.close()
            qqsmtp(zijin)
            
            break
    return 1


#程序入口
if __name__ == '__main__':
    
    global ss #择时中间变量
    global time_1 #择时中间变量
    global zijin




    zijin = 5000
    
    ss = 0
    time_1 = 0
    
    
    
    
    while(1):
        time.sleep(2)
        try:
            print "进入"
            r = requests.get('https://api.huobi.pro/market/history/kline?symbol=btcusdt&period=5min&size=25',timeout=5).text        
        except:
            time.sleep(2)
            print "出错"
            continue
        n = demjson.decode(r)
        shijian = n['data'][0]['id'] #return int  
        print u"当前获取最新时间戳:"+str(shijian)
        if ss == 0:
            stime = shijian
            ss += 1
        if shijian == stime:
            continue
        ss = 0
        
        time_1 = shijian
        print u"开始判断是否有突破"
        
    
    
        a = [] #数组暂存收盘价用来接下来MACD生成
        
        for i in range(1,25):
            a.append(n['data'][i]['close']) #return float, this is close value
        
        
        Open,Close,High,Low = n['data'][1]['open'],n['data'][1]['close'],n['data'][1]['high'],n['data'][1]['low']
        a.reverse() #此处翻转是为了下面的MACD生成        
        a = np.array(a)
        
        real = talib.EMA(a,timeperiod=10) #EMA线  
        dif,dea,bar = talib.MACD(a,fastperiod=6,slowperiod=13,signalperiod=6) #MACD 参数 6,13
        
        
        if bar[-2] < 0 and bar[-1] > 0:
            print "向上突破"
            pp = tupo_1(float(real[-1]),Open,Close,High,Low,bar[-1]) #向上突破
        if bar[-2] > 0 and bar[-1] < 0:
            print "向下突破"
            pp = tupo_2(float(real[-1]),Open,Close,High,Low,bar[-1]) #向下突破
