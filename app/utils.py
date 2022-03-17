from flask import jsonify

from flask_sqlalchemy import Pagination
from marshmallow import Schema

# 转换为Select下拉框的参数
select_opts = lambda x, label, value: [{'label': getattr(it, label), 'value': getattr(it, value)} for it in x]


def make_json_resp(
        data=None,
        schema: Schema = None,
        code=20000):
    """
    序列化查询结果
    :param data
    :param schema: marshmallow.Schema
    :param code: 20000: success; 50008: Illegal token; 50012: Other clients logged in; 50014: Token expired;
    :return:
    """
    if data is None:
        return jsonify(data={}, code=code)

    if schema is not None:
        if isinstance(data, Pagination):
            return jsonify(
                data=schema.dump(data.items, many=True),
                page=data.page,
                pages=data.pages,
                total=data.total,
                pre_page=data.per_page,
                code=code
            )
        else:
            return jsonify(data=schema.dump(data, many=True), code=code)

    return jsonify(data=data, code=code)
