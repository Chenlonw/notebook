# -*- coding: utf-8 -*-

# [section name]
# option name = value  #item
# option name = value
# option name = value

import configparser
cf = configparser.ConfigParser()
cf.read('./config.ini')

# 所有的sections
s = cf.sections()
print(s)
# 该section下所有的options
o = cf.options(s[0])
print(o)
# 该section下所有的options key 组合
v = cf.items(s[0])
print(v)

# 获取某一个section下的一个option
db_host = cf.get('db','db_host')
db_user = cf.get('db','db_user')
db_passwd = cf.getfloat('db','db_passwd')
print(db_host)
print(db_user)
print(db_passwd)

# 修改某个变量
cf.set('db', 'db_test', 'test')

# 增加section
cf.add_section('chenlong')
cf.set('chenlong', 'age', '15')
cf.write(open('./config.ini', 'w'))

# 删除section or option
cf.remove_section('chenlong')
cf.remove_option('chenlong', 'age')
