import pymysql

def get_conn():
    return pymysql.connect(
        host="127.0.0.1",
        user="ranfood",
        password="1234",
        database="ranfood",
        charset="utf8",
        cursorclass=pymysql.cursors.DictCursor)

def select_data(conn):
    with conn.cursor() as cursor:
        pass
        query = """
            select * from tb_dnn_model_result
        """
        cursor.execute(query)
        result = cursor.fetchall()
        print("데이터 수:", len(result))
        for data in result:
            print(data)

        return result

def save_data_for_one(conn):
    with conn.cursor() as cursor:
        query = """
            insert into tb_dnn_model_result ( id, prj, run_id, result, is_success )
            values (%(id)s, %(prj)s, uuid(), %(result)s, %(is_success)s)
        """
        insert_data = {'id': 1, 'prj': 'test', 'result':'<div id="mola"></div>', 'is_success': 1}
        cursor.execute(query, insert_data)
    conn.commit()

def save_data_for_many(conn):
    with conn.cursor() as cursor:
        query = """
            insert into tb_dnn_model_result ( id, prj, run_id, result, is_success )
            values (%(id)s, %(prj)s, uuid(), %(result)s, %(is_success)s)
        """
        insert_data = [
            {'id': 1, 'prj': 'test', 'result':'<div id="mola">가</div>,\n<div id="mola">나</div>', 'is_success': 1},
            {'id': 1, 'prj': 'test', 'result':'<div id="mola">다</div>,\n<div id="mola">라</div>,\n<div id="mola">마</div>', 'is_success': 1},
            {'id': 1, 'prj': 'test', 'result':'<div id="mola">바</div>,\n<div id="mola">사</div>,\n<div id="mola">아</div>,\n<div id="mola">자</div>', 'is_success': 1}
        ]
        cursor.executemany(query, insert_data)
    conn.commit()

def delete_all_data(conn):
    with conn.cursor() as cursor:
        query = """
            delete from tb_dnn_model_result
        """
        cursor.execute(query)
    conn.commit()

if __name__ == '__main__':
    conn = get_conn()
    try:
        # result = select_data(conn)
        # save_data_for_one(conn)
        # print(type(conn.cursor()))

        delete_all_data(conn)
        save_data_for_many(conn)
        result = select_data(conn)

        for data in result:
            # print(len(str(data['result']).split((','))))
            # print(data[3])
            for idx, dom in enumerate(data['result'].split("\n")):
                print(idx, dom)
    except Exception as e:
        print(e)
    else:
        conn.close()