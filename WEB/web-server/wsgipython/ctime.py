# coding=utf-8
import time


def application(env, start_response):
    env = env
    # print(env)
    status = "200 OK"
    content = [
        ("Content-Type", "text/html")
    ]
    start_response(status, content)
    return time.ctime()