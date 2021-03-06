import alchemy as db
from openpyxl import Workbook

def output_data(table_name):
    wb = Workbook()
    ws = wb.active
    ws.append(['职位代码','职位名称','招录机关','机构性质','机构层级','职位类别','职位层次','专业','学历','学位','年龄','性别','经历要求','专业科目','其他','申论类别','备注（职位简介）','考生咨询电话','招录人数','提交信息人数','资审合格人数','缴费人数'])
    posts = db.db_session.query(db.Posts).all()  #修改查询以输出不同数据
    for post in posts:
        item = []
        item.append(post.code)
        item.append(post.name)
        item.append(post.agency)
        item.append(post.agency_type)
        item.append(post.agency_level)
        item.append(post.job_type)
        item.append(post.job_position)
        item.append(post.major)
        item.append(post.education)
        item.append(post.degree)
        item.append(post.age)
        item.append(post.sex)
        item.append(post.experience)
        item.append(post.subject)
        item.append(post.others)
        item.append(post.category_type)
        item.append(post.ps)
        item.append(post.phone)
        item.append(post.plan)
        item.append(post.submitted_num)
        item.append(post.qualified_num)
        item.append(post.paid_num)
        ws.append(item)

    wb.save(table_name)

if __name__ == '__main__':
    output_data('安徽省2021考试录用公务员3.6.8:31信息汇总.xlsx')