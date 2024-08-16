"""
封装mysql操作
"""
import pymysql
class autoSql():
    def __init__(self):
        self.db=pymysql.connect(
            host='127.0.0.1',
            user='root',
            password='root',
            database='books',
            port=3306,
        )
    #获取游标
    def __creater(self):
        self.cur=self.db.cursor()
    #关闭游标
    def close(self):
        self.cur.close()
    #关闭数据库
    def close_db(self):
        self.db.close()   
    #对数据库的处理
    def opreator(self,sql):
        self.__creater()
        self.cur.execute(sql)
        if sql.split()[0].lower() == 'select':
            return self.cur.fetchall()
        else:
            try:
                self.db.commit()
                return self.cur.rowcount
            except Exception as e:
                print(e)
                self.db.rollback()
            # finally:
            #     self.__close()
            #     self.__close_db()
# db=autoSql(
#     host='127.0.0.1',
#     username='root',
#     password='root',
#     database='books',
#     port=3306,
# )
# sqls=['insert into t_book(id,title,pub_date) values(9,"西游记","1986-01-01")',
#     'insert into t_hero(name,gender,book_id) values("123",1,9)']
# for sql in sqls:
#     result=db.opreator(sql)
#     print(result)
# db.close()
# db.close_db()