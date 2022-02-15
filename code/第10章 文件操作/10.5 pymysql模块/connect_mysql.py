import pymysql
import traceback

INSERT = "INSERT INTO info VALUES \
            (3, 'Henry', 3.6)"
SEARCH = "SELECT * FROM info"

def main():
    try:
        # 连接数据库
        conn = pymysql.connect(
            host="localhost",
            port=3306,
            charset="UTF8",
            user="root",
            password="mysqladmin",
            database="student"
        )
        print("MySQL数据库连接成功")
        print("数据库版本：%s" % conn.get_server_info())

        db = conn.cursor()      # 获取数据库操作对象
        db.execute(INSERT)      # 执行SQL语句
        conn.commit()           # 提交事务，否则不会更新
        print("影响数据行数：%d" % db.rowcount)

        db.execute(SEARCH)
        for row in db.fetchall():   # 查询结果
            print(row)
    except Exception:
        print(traceback.format_exc())
    finally:
        db.close()

if __name__ == "__main__":
    main()
