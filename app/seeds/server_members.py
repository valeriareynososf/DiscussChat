from app.models import db, User, Server, Server_Member
import random

def seed_members():
    # channel1message1 = Server_Member(server_id=1, user_id=1)
    # channel1message2 = Server_Member(server_id=2, user_id=2)
    # channel1message3 = Server_Member(server_id=3, user_id=3)
    # channel2message1 = Server_Member(server_id=4, user_id=3)

    # db.session.add(channel1message1)
    # db.session.add(channel1message2)
    # db.session.add(channel1message3)
    # db.session.add(channel2message1)

    nums = [num for num in range(1, 29)]
    for i in range(1, 29):
        memberNums = []
        for _ in range(10):
            rand = random.choice(nums)
            if rand not in memberNums:
                memberNums.append(rand)
        for j in memberNums:
            if j != i:
                db.session.add(Server_Member(server_id=i, user_id=j))

    db.session.commit()

def undo_Server_Member():
    # if environment == "production":
    #     db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    # else:
    #     db.session.execute("DELETE FROM server_members")

    # db.session.commit()
    db.session.execute('TRUNCATE server_members RESTART IDENTITY CASCADE;')
    db.session.commit()
