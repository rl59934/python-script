__author__ = 'renliang'

import unittest
from ParserTool import IniConfigParser

class MyTestCase(unittest.TestCase):

    def test_readconfig(self):
        c = IniConfigParser()
        res = True
        try:
            file_path = "config.ini"
            c.readConfig(file_path)
        except Exception, e:
            print "read config file has error"
            res = False
        self.assertEqual(True, res)

    def test_readconfig_has_error(self):
        c = IniConfigParser()
        res = True
        try:
            file_path = ""
            c.readConfig(file_path)
        except Exception, e:
            res = False
        self.assertEqual(False, res)

    def test_get_value_by_key(self):
        type = "type"
        key = "main_ip"
        res = "192.168.53.221"
        c = IniConfigParser()
        c.readConfig("config.ini")
        act_res = c.getValueByKey(type, key)
        self.assertEqual(res, act_res)

    def test_getvalue_type_has_error(self):
        type = "type11"
        key = "main_ip"
        res = None
        act_res = None
        try:
            c = IniConfigParser()
            c.readConfig("config.ini")
            act_res = c.getValueByKey(type, key)
        except Exception, e:
            print "get value has error"
        self.assertEqual(res, act_res)

    def test_getvalue_key_has_error(self):
        type = "type"
        key = "main_ip2323"
        res = None
        act_res = None
        try:
            c = IniConfigParser()
            c.readConfig("config.ini")
            act_res = c.getValueByKey(type, key)
        except Exception, e:
            print "get value has error"
        self.assertEqual(res, act_res)


if __name__ == '__main__':
    unittest.main()
