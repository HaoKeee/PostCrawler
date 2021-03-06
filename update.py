from openpyxl import Workbook,load_workbook
import alchemy as db

wb = load_workbook('ddd.xlsx')  #修改文件名以修改打开的xlsx文件
sheet = wb['Sheet1']
for row in sheet.rows:
    code = row[0].value
    if code == "职位代码":
        pass
    else:
        obj = db.db_session.query(db.Posts).filter(db.Posts.code == str(code)).one()
        print(obj.submitted_num)
        row[19].value = obj.submitted_num
        row[20].value = obj.qualified_num
        row[21].value = obj.paid_num

wb.save('updated.xlsx')
