#!/usr/bin/env python
# coding: utf-8

# In[2]:


# 查看当前挂载的数据集目录, 该目录下的变更重启环境后会自动还原
# View dataset directory. This directory will be recovered automatically after resetting environment. 
get_ipython().system('ls /home/aistudio/data')


# In[3]:


# 查看工作区文件, 该目录下的变更将会持久保存. 请及时清理不必要的文件, 避免加载过慢.
# View personal work directory. All changes under this directory will be kept even after reset. Please clean unnecessary files in time to speed up environment loading.
get_ipython().system('ls /home/aistudio/work')


# In[4]:


# 如果需要进行持久化安装, 需要使用持久化路径, 如下方代码示例:
# If a persistence installation is required, you need to use the persistence path as the following:
get_ipython().system('mkdir /home/aistudio/external-libraries')
get_ipython().system('pip install BeautifulSoup4 -t /home/aistudio/external-libraries')


# In[5]:


get_ipython().system('pip install lxml -t /home/aistudio/external-libraries')
get_ipython().system('pip install html5lib -t /home/aistudio/external-libraries')


# In[6]:


# 同时添加如下代码, 这样每次环境(kernel)启动的时候只要运行下方代码即可:
# Also add the following code, so that every time the environment (kernel) starts, just run the following code:
import sys
sys.path.append('/home/aistudio/external-libraries')


# ### 作业任务
# * 打开BUCTOJ网站，网址为：[http://39.106.31.26/](http://39.106.31.26/)
# * 任选2个网页进行数据爬取，输出数据

# In[42]:


from bs4 import BeautifulSoup # 需要用到beautifulsoup对网站进行解析
import requests
import json, time

# 自定义函数显示html网页文本
def getUrlText(url):
    while True:
        try:
            html = requests.get(url)
            html = html.text
            break
        except requests.exceptions.ConnectionError:
            print('ConnectionError -- please wait 3 seconds')
            time.sleep(3)
        except requests.exceptions.ChunkedEncodingError:
            print('ChunkedEncodingError -- please wait 3 seconds')
            time.sleep(3)    
        except:
            print('Unfortunitely -- An Unknow Error Happened, Please wait 3 seconds')
            time.sleep(3)
    return html

# 爬取排名前50的用户
def getTop50Users():
    # 获取html网页
    url = 'http://39.106.31.26/ranklist.php'
    html = getUrlText(url)

    # 进行网址解析
    soup = BeautifulSoup(html, features='html.parser')

    # 进行css选择
    table = soup.select('tbody')
    
    if len(table) > 0:
        t = table[0]
    else:
        return []

    datalist = []
    for index, tr in enumerate(t.select('tr')):
        result = tr.select('td')

        # 获取排名数据
        ranking = result[0].text

        # 获取id
        id = result[1].select('a')[0].text

        # 获取用户名
        username = result[2].select('div')[0].text

        # 正确提交数
        AC_num = result[3].select('a')[0].text

        # 总提交数
        total_num = result[4].select('a')[0].text

        # 准确率
        accuracy = result[5].text

        datalist.append({
            'ranking': int(ranking),
            'id': id,
            'username': username,
            'AC': int(AC_num),
            'Total': int(total_num),
            'ACC': accuracy
        })
    
    print('\n爬取的排名前50用户列表:')
    for item in datalist:
        print(item)
    return datalist

# 爬取oj提交状态页面
def getStatusPage():
    url = 'http://39.106.31.26/status.php'
    html = getUrlText(url)

    soup = BeautifulSoup(html, 'html.parser')

    # 进行css选择
    table = soup.select('tbody')

    if len(table) > 0:
        t = table[0]
    else:
        return []

    datalist = []
    for index, tr in enumerate(t.select('tr')):
        result = tr.select('td')
        
        submit = int(result[0].text)
        user = result[1].select('a')[0].text
        problem = int(result[2].select('a')[0].text)

        # 对提交状态进行特殊处理
        td_result = ''
        temp = result[3].select('a')

        # 无查重结果
        if len(temp):
            td_result = temp[0].text
        # 有查重结果
        else:
            td_result = result[3].select('.label')
            td_result = td_result[0].text + ', ' + '查重编号:' + td_result[1].text
            # print(index, submit, td_result)

        memory = int(result[4].select('div')[0].text)
        runtime = int(result[5].select('div')[0].text)
        language = result[6].text
        length = result[7].text
        submittime = result[8].text
        judge_machine = result[9].text 

        datalist.append({
            "提交编号": submit,
            '用户': user,
            '问题': problem,
            '提交结果': td_result,
            '内存(kb)': memory,
            '运行时间(ms)': runtime,
            '语言': language,
            '代码长度': length,
            '提交时间': submittime,
            '判题机': judge_machine
        })
    
    print('\n提交状态页面爬取结果:')
    for item in datalist:
        print(item)
    return datalist

def buctoj():
    url = "http://39.106.31.26/"

    # 爬取排名前50的用户
    Top50Users = getTop50Users()

    # 爬取提交状态页面
    statuslist = getStatusPage()

if __name__=="__main__":
    buctoj()


# In[ ]:




