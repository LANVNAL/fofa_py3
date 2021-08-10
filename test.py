import fofa_py3

def query():
    """
    使用FOFA ADK进行查询
    Args:
        ip_result: ip结果dict

    Returns:

    """
    email, key = ('xxxxx@qq.com', 'xxxxx')  # 输入email和key
    client = fofa_py3.Client(email, key)  # 将email和key传入fofa.Client类进行初始化和验证，并得到一个fofa client对象
    query_str = 'cert.subject="Tencent Technology (Shenzhen) Company Limited" && status_code="200"'
    data = client.get_json_data(query_str, page=1, fields="ip")
    print(data)


if __name__ == '__main__':
    query()