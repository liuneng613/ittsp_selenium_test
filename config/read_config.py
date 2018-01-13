import os
import configparser

# 获取文件的当前绝对路径
cur_path = os.path.dirname(os.path.realpath(__file__))

# 获取项目根目录
root_path = os.path.abspath(os.path.join(os.getcwd(), ".."))

# 获取config.ini的路径
config_path = os.path.join(cur_path, 'config.ini')

conf = configparser.ConfigParser()
conf.read(config_path)

ittsp_url = conf.get('ittsp', 'ittsp_url')

if __name__ == '__main__':
    print(cur_path)
    print(root_path)
    print(config_path)
