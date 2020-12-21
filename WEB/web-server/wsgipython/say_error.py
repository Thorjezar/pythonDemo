
def application(env, start_response):
    """假设没有找到对应的文件"""
    # env = env
    status = "404 Not Found"
    content = [
        # ("Content-Type", "text/html")
    ]
    start_response(status, content)
    return "Not found file"