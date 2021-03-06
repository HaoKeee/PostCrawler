import alchemy as db

data = db.db_session.query(db.Posts).all()
plan_num = submitted_num = qualified_num = paid_num = 0
for item in data:
    plan_num += int(item.plan)
    submitted_num += int(item.submitted_num)
    qualified_num += int(item.qualified_num)
    paid_num += int(item.paid_num)
    
print("总招录人数：" + str(plan_num))
print("总提交人数：" + str(submitted_num))
print("总资审人数：" + str(qualified_num))
print("总缴费人数：" + str(paid_num))
