import pandas as pd
import mysql.connector

cnx = mysql.connector.connect(user='root', password='rootpassword', host='localhost')
cursor = cnx.cursor()


# 显示所有数据库
def show_databases(cursor):
    cursor.execute("SHOW DATABASES")
    databases = cursor.fetchall()
    for db in databases:
        print(db)


# 删除一个数据库
def delete_databases(cursor, database_name):
    cursor.execute("DROP DATABASE IF EXISTS {}".format(database_name))
    print("Database {} is deleted.".format(database_name))
    print("删除后的所有数据库如下：")
    show_databases(cursor)


# 创建数据库
def create_database(cursor, database_name):
    cursor.execute("CREATE DATABASE IF NOT EXISTS {}".format(database_name))
    print("Database {} is created.".format(database_name))


# 查询数据库
def query_table(database_name, table_name, cursor):
    cursor.execute(f"USE {database_name}")
    query = "SELECT * FROM {}".format(table_name)
    cursor.execute(query)
    # 提取查询结果
    results = cursor.fetchall()
    for row in results:
        print(row)


def insert_excel_to_mysql(excel_file, database_name):
    # 读取Excel文件中的所有表格并将它们存储到一个字典中
    food_composition = pd.read_excel(excel_file, sheet_name=None)
    cursor.execute(f"USE {database_name}")
    # 遍历字典中的每个表格
    for table_name, df in food_composition.items():
        # 将列名中的空格替换成下划线
        df.columns = [col.replace(' ', '_') for col in df.columns]

        # 创建数据表
        cursor.execute("DROP TABLE IF EXISTS {}".format(table_name))
        cursor.execute("CREATE TABLE {} (food_name VARCHAR(255), {})".format(table_name, ', '.join(
            ['{} FLOAT'.format(col) for col in df.columns[1:]])))

        # 插入数据
        for row in df.itertuples(index=False):
            values = "', '".join([str(cell) for cell in row])
            cursor.execute("INSERT INTO {} ({}) VALUES ('{}')".format(table_name, ', '.join(
                ['food_name'] + df.columns[1:].tolist()), values))

        # 提交事务
        cnx.commit()


def query_mysql_to_dataframe(database_name, table_name, cursor, cnx):
    cursor.execute(f"USE {database_name}")
    # 查询数据表格
    query = "SELECT * FROM {}".format(table_name)
    df = pd.read_sql(query, con=cnx)

    # 返回查询结果
    return df


# insert_excel_to_mysql('中国食物成分表整理版.xlsx', 'food_composition')
# query_table('food_composition', '水产品', cursor)

df = query_mysql_to_dataframe('food_composition', '主食', cursor, cnx)
print(df)

# 关闭数据库连接
cursor.close()
cnx.close()
