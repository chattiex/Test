from pymysql import connect

def main():
    # 创建Connection连接
    conn = connect(host='localhost', user='root', password='root', database='python_test')
    # 获得Cursor对象
    cursor = conn.cursor()
    # 插入10万次数据
    for i in range(100000):
        cursor.execute("insert into test_index values('ha-%d')" % i)
    # 提交数据
    conn.commit()

if __name__ == "__main__":
    main()