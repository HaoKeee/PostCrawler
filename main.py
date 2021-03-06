import alchemy as db
import requests
from lxml import etree

def onepage_category(pi):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,zh-TW;q=0.5',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Host': 'www.apta.gov.cn',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.81',
    }
    params = {
        'examid': '280',
        'type': '',
        'pcode': '',
        'pi': pi
    }
    response = requests.get('http://www.apta.gov.cn/Officer_PositionView', headers=headers, params=params ,timeout=10)
    selector = etree.HTML(response.text)
    obj = selector.xpath('//table[@width="99%"]//tr')
    items = []

    for x in obj[1:]:
        item = {}
        item['code'] = x.xpath('td[1]')[0].text.strip()
        item['name'] = x.xpath('td[2]')[0].text.strip()
        item['agency'] = x.xpath('td[4]')[0].text.strip()
        item['agency_type'] = x.xpath('td[5]')[0].text.strip()
        item['agency_level'] = x.xpath('td[6]')[0].text.strip()
        item['job_type'] = x.xpath('td[7]')[0].text.strip()
        item['job_position'] = x.xpath('td[8]')[0].text.strip()
        item['major'] = x.xpath('td[9]')[0].text.strip()
        item['education'] = x.xpath('td[10]')[0].text.strip()
        item['degree'] = x.xpath('td[11]')[0].text.strip()
        item['age'] = x.xpath('td[12]')[0].text.strip()
        item['sex'] = x.xpath('td[13]')[0].text.strip()
        item['experience'] = x.xpath('td[14]')[0].text.strip()
        item['subject'] = x.xpath('td[15]')[0].text.strip()
        item['others'] = x.xpath('td[16]')[0].text.strip()
        item['category_type'] = x.xpath('td[17]')[0].text.strip()
        item['ps'] = x.xpath('td[18]')[0].text.strip()
        item['phone'] = x.xpath('td[19]')[0].text.strip()
        item['plan'] = x.xpath('td[3]')[0].text.strip()
        items.append(item)
    
    for item in items:
        pipeline(item)

    db_commit()

def onepage_count(pi):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,zh-TW;q=0.5',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Host': 'www.apta.gov.cn',
        'Pragma': 'no-cache',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.81',
    }
    params = {
        'examid': '280',
        'pcode': '',
        'pi': pi
    }
    response = requests.get('http://www.apta.gov.cn/Officer/Summary', headers=headers, params=params ,timeout=10)
    selector = etree.HTML(response.text)
    obj = selector.xpath('//table[@width="99%"]/tr')
    items = []

    for x in obj[2:]:
        item = {}
        item['code'] = x.xpath('td[1]')[0].text.strip().replace('·', '')
        item['name'] = x.xpath('td[2]')[0].text.strip()
        item['submitted_num'] = x.xpath('td[4]')[0].text.strip()
        item['qualified_num'] = x.xpath('td[5]')[0].text.strip()
        item['paid_num'] = x.xpath('td[6]')[0].text.strip()
        items.append(item)
    
    for item in items:
        add_info(item)

    db_commit()

def add_info(item):
    try:
        obj = db.db_session.query(db.Posts).get(item['code'])
        obj.submitted_num = item['submitted_num']
        obj.qualified_num = item['qualified_num']
        obj.paid_num = item['paid_num']
    except Exception as e:
        print(item)
        print("Failed to add num info")
        print(e)

def pipeline(item):
    try:
        new_post = db.Posts(
            code=item['code'],
            name=item['name'],
            agency=item['agency'],
            agency_type=item['agency_type'],
            agency_level=item['agency_level'],
            job_type=item['job_type'],
            job_position=item['job_position'],
            major=item['major'],
            education=item['education'],
            degree=item['degree'],
            age=item['age'],
            sex=item['sex'],
            experience=item['experience'],
            subject=item['subject'],
            others=item['others'],
            category_type=item['category_type'],
            ps=item['ps'],
            phone=item['phone'],
            plan=item['plan']
        )

        db.db_session.add(new_post)

    except Exception as e:
        print(item)
        print("Failed to into database")
        print(e)

def db_commit():
    try:
        db.db_session.commit()
        db.db_session.close()

    except Exception as e:
        print("Failed to commit")
        print(e)

if __name__ == '__main__':
    for x in range(1,206):   #206修改为所要爬取的工作职位页数+1
        print(x)
        onepage_category(x)
    for y in range(1,63):    #63修改为所要爬取的报名情况页数+1
        print(y)
        onepage_count(y)