# coding=utf-8
def application(env, start_response):
    env = env
    # print(env)
    status = "200 OK"  # 传入状态码，可以判断是否取到了
    content = [("Content-Type", "text/html")]  # 传入返回的格式
    start_response(status, content)
    return "use python programe"