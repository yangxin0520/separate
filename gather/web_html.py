from flask import Blueprint, current_app, send_from_directory


# 提供静态文件的蓝图
html = Blueprint("web_html", __name__)


@html.route("/<re(r'.*'):html_file_name>")
def get_html_fc(html_file_name):
    """提供html文件"""
    # 如果html_file_name为""，表示访问的是/，请求的是主页
    if not html_file_name:
        html_file_name = "index.html"

    # 如果资源名不是favicon.ico
    if html_file_name != "favicon.ico":
        html_file_name = "html/" + html_file_name

    # flask提供的返回静态文件的方法
    print(current_app.send_static_file(html_file_name))
    return current_app.send_static_file(html_file_name)