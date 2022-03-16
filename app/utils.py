from flask import jsonify

# 转换为Select下拉框的参数
select_opts = lambda x, label, value: [{'label': getattr(it, label), 'value': getattr(it, value)} for it in x]


def make_json_resp(obj=None, code=20000):
    """
    :param obj
    :param code: 20000: success; 50008: Illegal token; 50012: Other clients logged in; 50014: Token expired;
    :return:
    """
    if obj is None:
        obj = {}
    return jsonify(data=obj, code=code)
