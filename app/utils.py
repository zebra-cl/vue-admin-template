from flask import jsonify


def make_json_resp(obj, code=20000):
  """
  :param obj
  :param code: 20000: success; 50008: Illegal token; 50012: Other clients logged in; 50014: Token expired;
  :return:
  """
  return jsonify(data=obj, code=code)
