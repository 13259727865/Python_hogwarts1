"""
创建数据库sql：
CREATE DATABASE bms

创建数据表：
CREATE TABLE `bms`.`book`  (
  `bid` int(20) NOT NULL AUTO_INCREMENT COMMENT '编号,主键自动增长',
  `name` char(100) NOT NULL COMMENT '书名',
  `price` decimal(10, 2) NOT NULL COMMENT '单价',
  `summary` varchar(255) NOT NULL COMMENT '概要',
  `quantity` int(20) NOT NULL COMMENT '库存',
  PRIMARY KEY (`bid`)
);
"""

from flask import *
from Library_Management_System.book_api import book_bp



app = Flask(import_name=__name__)
# app.config['JSON_AS_ASCII'] = False
app.json.ensure_ascii = False
# app.config['JSONIFY_MIMETYPE'] = "application/json;charset=utf-8"

if __name__ == '__main__':
    app.register_blueprint(book_bp)

    app.run(debug=True)
