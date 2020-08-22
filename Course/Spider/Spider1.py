#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 查看当前挂载的数据集目录, 该目录下的变更重启环境后会自动还原
# View dataset directory. This directory will be recovered automatically after resetting environment. 
get_ipython().system('ls /home/aistudio/data')


# In[2]:


# 查看工作区文件, 该目录下的变更将会持久保存. 请及时清理不必要的文件, 避免加载过慢.
# View personal work directory. All changes under this directory will be kept even after reset. Please clean unnecessary files in time to speed up environment loading.
get_ipython().system('ls /home/aistudio/work')


# In[3]:


# 如果需要进行持久化安装, 需要使用持久化路径, 如下方代码示例:
# If a persistence installation is required, you need to use the persistence path as the following:
get_ipython().system('mkdir /home/aistudio/external-libraries')
get_ipython().system('pip install BeautifulSoup4 -t /home/aistudio/external-libraries')


# In[4]:


# 同时添加如下代码, 这样每次环境(kernel)启动的时候只要运行下方代码即可:
# Also add the following code, so that every time the environment (kernel) starts, just run the following code:
import sys
sys.path.append('/home/aistudio/external-libraries')


# ### 作业任务
# * 打开buct程序设计竞赛集训队网站，网址为：[http://www.acmer.site:81](http://www.acmer.site:81)
# * 查看网站提供的api数据接口，网址为：[http://www.acmer.site:81/acmerdata/API](http://www.acmer.site:81/acmerdata/API)
# * 任选3个api数据接口完成数据爬取，输出数据

# In[19]:


from bs4 import BeautifulSoup # 需要用到beautifulsoup对网站进行解析
import requests
import json, time

# 获取html网页中信息的函数
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

# 获取学生名单
def getStudents(isactive=1, year=None, school=0, order=0, size=10000):
    isactive_str = 'isactive=' + str(isactive) # 默认为现役队员
    
    # 修改学生年级
    year_str = ''
    if year:
        year_str = 'year=' + str(year)
    
    school_str = 'school=' + str(school) # 默认为所有学校
    order = 'order=' + str(order) # 按照默认排序返回结果
    size = 'size=' + str(size) # 默认大小为10000

    # 根据api字段设置domain，注意domian前加http://，否则得不到正确连接
    domain = "http://jhas.top:8000/api/students/?format=json" + '&' + isactive_str + '&' + year_str +                 '&' + school_str + '&' + order + '&' + size
    
    html = getUrlText(domain)    # 调用自定义函数获取网页中的文本
    js = json.loads(html)    # 将html用json格式打开

    datalist = []
    for item in js:
        stuNo = item['stuNO']
        realName = item['realName']
        className = item['className']
        sex = item['sex']
        year = item['year']
        cfID = item['cfID']
        cfRating = item['cfRating']
        cfTimes = item['cfTimes']
        school = item['school']

        datalist.append({
            '学校': school,
            '学号': stuNo,
            '姓名': realName,
            '班级': className,
            '性别': sex,
            '年级': year,
            'cfID': cfID,
            '参加cf次数': cfTimes,
            'cf评分': cfRating
        })

    # print(datalist)
    return datalist

# 获取比赛列表
def getContestList(isdetail=0, _type=0, page=None, size=10000):
    isdetail_str = 'isdetail=' + str(isdetail)
    type_str = 'type=' + str(_type)
    page_str = ''
    if page != None:
        page_str = 'page=' + str(page)
    size_str = 'size=' + str(size)
    domain = 'http://jhas.top:8000/api/contests/?format=json' + '&' + isdetail_str                 + '&' + type_str + '&' + page_str + '&' + size_str

    html = getUrlText(domain) 
    js = json.loads(html)
    
    datalist = []
    for item in js:
        cid = item['id']
        cname = item['cname']
        cdate = item['cdate']
        questionnum = item['questionnum']
        start_time = time.localtime(item['starttimestamp'])
        #转换为新的时间格式
        start_time = time.strftime("%Y-%m-%d %H:%M:%S", start_time)
        end_time = time.localtime(item['endtimestamp'])
        end_time = time.strftime("%Y-%m-%d %H:%M:%S", end_time)

        datalist.append({
            'id': cid,
            'name': cname,
            'date': cdate,
            'starttime': start_time,
            'endtime': end_time,
            'questionnum': questionnum
        })

    # print(datalist)
    return datalist



# 获取学生月排名
def getMonthlyRankings(year=None, month=None, school=0, size=10000):
    # 设置年份，默认为当前年份
    year_str = ''
    if year:
        year_str += 'year=' + str(year)

    # 设置月份，默认为当前月份
    month_str = ''
    if month:
        month_str = 'school=' + str(month)

    # 设置学校，默认为所有学校
    school_str = 'school=' + str(school)

    # 设置返回的结果数量
    size_str = 'size=' + str(size)
    
    domain = 'http://jhas.top:8000/api/studentsmonth/?format=json' + '&' + school_str + '&' + size_str             + '&' + year_str + '&' + month_str

    html = getUrlText(domain) 
    js = json.loads(html)
    
    datalist = []
    for item in js:
        stuNo = item['stuNO']
        realName = item['realName']
        className = item['className']
        score = item['score']
        cfdiff = item['cfdiff']
        cf = item['cf']
        cfp = item['cfp']
        cfpp = item['cfpp']
        ac = item['ac']
        acp = item['acp']
        acpp = item['acpp']
        acdiff = item['acdiff']
        jsk = item['jsk']
        jskp = item['jskp']
        nc = item['nc']
        ncp = item['ncp']
        localcontest = item['localcontest']
        localcontestp = item['localcontestp']

        datalist.append({
            '学号': stuNo,
            '姓名': realName,
            '班级': className,
            'cf': cf,
            'cfdiff': cfdiff,
            'cfp': cfp,
            'cfpp': cfpp,
            'ac': ac,
            'acp': acp,
            'acpp': acpp,
            'acdiff': acdiff,
            'jsk': jsk,
            'jskp': jskp,
            'nc': nc,
            'ncp': ncp,
            'localcontest': localcontest,
            'localcontestp': localcontestp,
            'score': score
        })
    
    # print(datalist)
    return datalist

def acmersite():
    # 获取北京化工大学2017级前20位现役学生名单
    print('获取北京化工大学2017级前20位现役学生名单:')
    studentsList = getStudents(isactive=0, school=1, year=2017, size=20)
    for index, item in enumerate(studentsList):
        print(index+1, item)

    print('\n\n')

    # 获取比赛列表
    print("获取比赛列表:")
    ContestList = getContestList()
    for index, item in enumerate(ContestList):
        print(index+1, item)

    print('\n\n')

    # 获取上半年北化学生排名
    print('获取北京化工大学上半年排名前50队员:')
    RankingList = getMonthlyRankings(school=1, size=50, month='h1')
    for index, item in enumerate(RankingList):
        print(index+1, item)

if __name__ == "__main__":
    acmersite()


# In[ ]:




