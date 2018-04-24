import os
import configparser

# 获取文件的当前绝对路径
cur_path = os.path.dirname(os.path.realpath(__file__))

# 获取项目根目录
root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 获取config目录
conf_path = root_path + r"\seConfig\\"


class ReadConfig:
    """
    创建ConfigParser对象，读取指定目录conf_path配置文件config_name
    """
    def __init__(self, config_name):
        self.conf = configparser.ConfigParser()
        # 中文乱码问题需要添加encoding="utf-8-sig"
        self.conf.read(conf_path + config_name, encoding="utf-8-sig")

    def get_ittsp(self, name):
        value = self.conf.get("ittsp", name)
        return value


if __name__ == '__main__':
    co = ReadConfig("config.ini")
    print(co.get_ittsp("ittsp_url"))