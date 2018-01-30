# -*- coding: utf-8 -*-
import requests
def setdata(_from,_to):
    data['from'] = _from
    data['to'] = _to
while(True):
  en = raw_input('输入q退出\n#输入0英译中\n#输入1中译英\n别指望彩蛋,输入2与其他无效:')
  data = {
  'from':'',
  'to':'',
  'text':''
  } #某江网站的参数
  if en == '0':
     setdata('en','zh-CN')
     es = raw_input('Enter Need translate str:')#只能重复了
     data['text']=es.decode('utf-8') #将es的编码转为utf-8
  if en == 'q':
      print‘再见...’
      break
  if en == '2':
      print'都说无效了'
      break
  if en == '1':
     setdata('zh-CN','en')
     es = raw_input('Enter Need translate str:')
     data['text']=es.decode('gbk')  #中文转英文最要的地方--将es的utf-8编码转为gbk
                                    #可能网站编码是gbk,所以需要转码。
  headers = {
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
  }          # 有就是谷歌 没有就是IE
  url = 'https://dict.hjenglish.com/services/Translate.ashx' #某江小站的翻译接口
  re = requests.post(url,headers=headers,data = data).text #想目标网站带有参数的发起请求
  re = re.replace("\"", ""); #删除\ 号
  re = re.replace(":", ""); #删除引号：
  re = re.replace(",", ""); #删除逗号，
  re = re.replace("status  0  content  ", ""); #删除某某文字
  re = re.replace("{", ""); #删除{
  re = re.replace("}", ""); # 删除}
  #以上几句会正则的就忽视吧，作者不会!!!!!!
  re = re.decode('unicode_escape') # 将unicode 文字转为 汉字   本文唯一一句由网上复制而来的.
  print "result:"+re #输出
  
