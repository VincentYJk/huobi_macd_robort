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



#下面为QQ邮件提醒功能
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



#突破后执行的函数
def tupo_1(real,Open,Close,High,Low,b):
    
    '''
    if Open > Close:
        med = (Open-Close)/2.0 + Close
    else:
        med = (Close-Open)/2.0 + Open
    '''
    if 1==1: #暂设无条件执行
        print u"符合条件进行向上突破!"
        
            
        if 1==1:#也设无条件执行
            kaishi_1(b)
    
    return 1
    
def get_5min_med(): #获取最近5分钟的中间价
    while(1):
        time.sleep(2)
        try:
            print "进入"
            r = requests.get('https://api.huobi.pro/market/history/kline?symbol=btcusdt&period=5min&size=1',timeout=5).text        
        except:
            time.sleep(2)
            print "出错"
            continue
    Open,Close = n['data'][0]['open'],n['data'][0]['close']
    
    #获取实时的中间价
    if Open > Close:
        med = (Open-Close)/2.0 + Close #return float
    else:
        med = (Close-Open)/2.0 + Open
    
    return med
    
        
    
def get_value(): #获取当前币价
    while(1):
        try:
            r = requests.get('https://api.huobi.pro/market/detail/merged?symbol=btcusdt').text
            n = demjson.decode(r)
            break
        except:
            #time.sleep(2)
            continue
    
    
    return n['tick']['close'] # return float
    
    
def get_smavalue(how_long): #获取当前SMA值  ep: how_long 必须为int型
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
    a = [] #数组暂存收盘价用来接下来MACD,SMA生成
        
    for i in range(1,25):
        a.append(n['data'][i]['close']) #return float, this is close value
        
        
    a.reverse() #此处翻转是为了下面的MACD及SMA生成        
    a = np.array(a)
        
    real = talib.SMA(a,timeperiod=how_long) #EMA线
    
    return real[-2] #-2无误
    

def success_sma20(v):
    zhisun = v #将下单时的价格设置为止损价
    bitcoin_med = get_5min_med() #获取5min中间价格
    sma_value = get_smavalue(20) #获取与之对应的SMA10日均线
    bitcoin_value = get_value()
    
    if bitcoin_value <= zhisun:
        sell()
    
    if bitcoin_med <= sma_value:
        sell()

def pc(shijian,b,v):#ep:  shijian 循环处理时用的时间戳,b:MACD柱子值,v下单时的价格
    bitcoin_value = get_value() #获取价格
    sma_value = get_smavalue(10) #获取与之对应的SMA10日均线
    if bitcoin_value > sma_value: #先清半仓,若大于十日线则开始20日均线止盈措施
        sell(bitcoin_value,1) #清半仓
        success_sma20(v) #开始20sma止盈措施
    else:
        sell(bitcoin_value,2) #否则全仓卖出
    
    

def buy(value): #买入默认全仓买入
    global zijin
    global bitcoin
    
    bitcoin_num = (zijin*0.997)/value #手续费是0.2% 即 0.002  1-0.002 = 0.998 在此我提高一点算0.997,除以value最后\
    #得到币的数量 return float
    
    bitcoin = bitcoin_num #更新持币数量
    zijin = zijin*0.003
    return 1 #返回1表示成功买入
    


def sell(value,status): # ep: value:实时币价,status：1半仓卖出还是2全仓卖出
    global zijin
    global bitcoin
    if status == 1:
        zijin += bitcoin * value * 0.997 #扣除手续费
        bitcoin = 0.0 #清空持仓
    if status == 2:
        zijin += (bitcoin/2.0) * value * 0.997
        bitcoin -= bitcoin/2.0 #更新持仓
    return 1#返回1表示卖出成功

def kaishi_1(b):
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
    buy(value) #执行买单
    zhisun = value*(1-0.005) #设止损为跌0.5%
    print u"下单价格:"+str(value)
    print u"向上突破第一阶段,止损价:"+str(zhisun)
    
    f = open(u"下单.txt","a+")
    f.write("向上突破第一阶段下单价格:"+str(value)+"止损价:"+str(zhisun)+"\n")
    f.close()
    
    
    #time.sleep(2)
    while(1):
        
        while(1):
            time.sleep(2)
            try:
                r = requests.get('https://api.huobi.pro/market/history/kline?symbol=btcusdt&period=5min&size=30').text
                break
            except:
                time.sleep(2)
                continue
        
        n = demjson.decode(r)
        shijian = n['data'][0]['id'] #return int
        if shijian != time_1:
            a = []
            for i in range(1,25):
                a.append(n['data'][i]['close']) #return float, this is close value
                
            a.reverse()
            a = np.array(a)
            dif,dea,bar = talib.MACD(a,fastperiod=6,slowperiod=13,signalperiod=6)

            if bar[-1] < b:#当macd柱小于前柱时平半仓
               pc(shijian,bar[-1],value) #进入平半仓函数
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
        


#程序入口
if __name__ == '__main__':
    
    global ss #择时中间变量
    global time_1 #择时中间变量
    global zijin #现金数
    global bitcoin
    global all_zijin #资金总值
    



    all_zijin = 0
    zijin = 5000 #出事资金5000
    bitcoin = 0  #出事比特币数量0
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

