import pymysql
from flask import Blueprint, render_template, request, make_response, jsonify

book_bp = Blueprint(name="book", import_name=__name__, url_prefix="/book")
db_con = pymysql.Connect(host="192.168.1.30", port=3306, user="root", database="bms",charset="utf8")

def select_all():
    book_list = []
    get_all_sql = """
                         select * from book
                           """
    cur = db_con.cursor()
    cur.execute(get_all_sql)
    all_book = cur.fetchall()
    if all_book:
        for i in all_book:
            book_dict = {}
            book_dict["id"] = i[0]
            book_dict["name"] = i[1]
            book_dict["price"] = i[2]
            book_dict["summary"] = i[3]
            book_dict["quantity"] = i[4]
            book_list.append(book_dict)
    return book_list

@book_bp.route("/book_list", methods=["GET", "POST"])
def get_list():
    if request.method == "GET":
        return render_template("get_list.html")
    else:
        book_list = select_all()

        return book_list


@book_bp.route("/add", methods=["GET", "POST"])
def add_book():
    print(request.args)
    if request.method == "GET":
        return render_template("add_book.html")
    else:
        get_all_sql = """
                insert into book (`name`, `price`, `summary`, `quantity`) value (%s,%s,%s,%s)
                """
        cur = db_con.cursor()
        name = request.args["name"]
        price = request.args["price"]
        summary = request.args["summary"]
        quantity = request.args["quantity"]
        print(name)
        cur.execute(get_all_sql,(name,price,summary,quantity))
        db_con.commit()
        cur.close()
        response = make_response({"msg":"添加成功","data":select_all()})
        # response.headers["Content-Type:"]="application/json; charset=utf-8"

        return response


@book_bp.route("/change/<int:bookid>",methods=["GET","POST"])
def change_book(bookid):
    if request.method == "GET":
        return render_template("change_book.html")
    else:
        change_book_sql = """
                        update book set `name` = %s, `price` = %s, `summary` = %s, `quantity` = %s WHERE `bid` = %s;
                        """
        cur = db_con.cursor()
        name = request.args["name"]
        price = request.args["price"]
        summary = request.args["summary"]
        quantity = request.args["quantity"]
        cur.execute(change_book_sql, (name, price, summary, quantity,bookid))
        db_con.commit()
        cur.close()
        return {"msg": "添加成功", "data": select_all()}

@book_bp.route("/changedata/<int:book_id>")
def change_data(book_id):
    cur = db_con.cursor()
    changedata_sql = f"""select * from book where id={book_id}"""
    cur.execute(changedata_sql)
    data = cur.fetchone()
    cur.close()
    data_dict = {}
    data_dict["name"]=data[0]
    data_dict["price"] = data[1]
    data_dict["summary"] = data[2]
    data_dict["quantity"] = data[3]
    return data_dict

@book_bp.route("/delbook/<int:book_id>")
def del_book(book_id):
    cur = db_con.cursor()
    delbook_sql = f"""delete from book where id = {book_id}"""
    cur.execute(delbook_sql)
    db_con.commit()
    cur.close()
    return {"msg": "删除成功", "data": select_all()}

@book_bp.route("/search/<searchkey>")
def search(searchkey):
    book_list = []
    get_all_sql = f"""
                             select * from book where name like '%{searchkey}%' or summary like '%{searchkey}%'
                               """
    cur = db_con.cursor()
    cur.execute(get_all_sql)
    all_book = cur.fetchall()
    if all_book:
        for i in all_book:
            print(i)
            book_dict = {}
            book_dict["id"] = i[0]
            book_dict["name"] = i[1]
            book_dict["price"] = i[2]
            book_dict["summary"] = i[3]
            book_dict["quantity"] = i[4]
            book_list.append(book_dict)
    response = make_response(jsonify(book_list))
    response.headers["Content-Type"] = "application/json;charset=UTF-8"


    return response