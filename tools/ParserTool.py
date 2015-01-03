# --coding:utf-8--
__author__ = 'renliang'


import os
from ConfigParser import ConfigParser

"""
此类的用于配置文件的读取
"""


# 用于ini文件的读取
class IniConfigParser:
    # 参数的初始化
    def __init__(self):
        self.file_path = ""
        try:
            self.c = ConfigParser()
        except Exception, e:
            raise "init ConfigParser has error:", e

    # 配置文件的读取
    def readConfig(self, file_path):
        if file_path.strip() == "":
            raise "===config file is null==="
        try:
            self.c = ConfigParser()
            self.c.read(file_path)
        except Exception, e:
            raise "Configparser read config file has error:", e


    # 根据type的key来获得具体的value
    def getValueByKey(self, type, key):
        if type.strip() == "" or key.strip() == "":
            raise "===key not is null==="
        value = ""
        try:
            value = self.c.get(type, key)
        except Exception, e:
            raise "Configparser read config file has error:", e
        return value


if __name__ == '__main__':
    c = IniConfigParser()
