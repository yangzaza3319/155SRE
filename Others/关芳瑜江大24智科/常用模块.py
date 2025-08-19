"""
序列化相关模块

将原本的字典、列表等内容转换成一个字符串的过程就叫做序列化

序列化的目的

以某种存储形式使自定义对象持久化。
将对象从一个地方传递到另一个地方。
使程序更具维护性。

Python 可序列化的数据类型，序列化出来之后的结果如下:

Python	    JSON
dict	    object
list,tuple	array
str	        string
int,float	number
True	    true
False	    false
None	    null

json 模块
Python 的 json 模块用于处理 JSON（JavaScript Object Notation）数据格式。JSON 是一种轻量级的数据交换格式，易
于人类阅读和编写，同时也易于机器解析和生成。json 模块提供了简单的方法来编码（序列化）和解码（反序列化）JSON 数据。

常用功能
序列化：将 Python 数据类型转换为 JSON 格式。
反序列化：将 JSON 格式的数据转换为 Python 数据类型。
"""

#基本用法

#序列化&反序列化

import json

data = {
    "name": "EaglesLab",
    "age": 30,
    "is_student": False,
    "courses": ["SRE", "Python"]
}

json_string = json.dumps(data)  # 将 Python 对象转换为 JSON 字符串
print(json_string)

data = json.loads(json_string)  # 将 JSON 字符串转换为 Python 对象
print(data)
print(data['name'])  # 访问字典中的值

#文件内容相关

with open('json_data.json', 'r') as file:
    data = json.load(file)  # 将文件中 JSON 数据转换为 Python 对象
    print(data)

data = {
    "name": "Bob",
    "age": 25,
    "is_student": True,
    "courses": ["English", "History"]
}

with open('output.json', 'w') as file:  # 将 Python 对象转换为文件中 JSON 数据
    json.dump(data, file)

"""
序列化相关参数

参数            作用
skipkeys        用于控制对字典键类型的严格性检查，默认为 False，当字典的键不是 JSON 规范支持的基本类型时，直接抛出 TypeError 异常，反之，跳过这些键，不引发错误，但会导致数据丢失。
indent	        控制 JSON 字符串的格式化缩进，默认值 None 会生成最紧凑的 JSON 字符串，无缩进和多余空格。
ensure_ascii	控制非 ASCII 字符转义行为，默认为 True，中文会被转义为 Unicode 转义序列。
separators	    自定义 JSON 字符串中元素间的分隔符和键值对的分隔符。
sort_keys	    是否将数据根据 key 进行排序
"""

"""
pickle 模块
Python 的 pickle 模块用于对象的序列化（将对象转换为字节流）和反序列化（将字节流转换回对象）。这使得在程序之
间传递对象或将对象保存到文件中变得非常方便。

不同的是 json 模块序列化出来的是通用格式，其它编程语言都认识，就是普通的字符串，而 pickle 模块序列化出来的只有
python 可以认识，其他编程语言不认识的，表现为乱码。
"""

#基本用法

#序列化 & 反序列化

import pickle

data = {
    'name': 'EaglesLab',
    'age': 30,
    'is_student': False,
    'courses': ['Math', 'Science']
}

print(pickle.dumps(data))   # 序列化

print(pickle.loads(pickle.dumps(data))) # 反序列化

#文件内容相关

import pickle

with open('./data.pkl', "wb") as f:
    pickle.dump(data, f)    # 序列化
    pickle.dump([1,2,3], f) # 多次调用处理多个对象


with open("./data.pkl", "rb") as f:
    print(pickle.load(f))  # 反序列化
    print(pickle.load(f))   # 多次调用处理多个对象

"""
shelve 模块

Python 的 shelve 模块提供了一种简单的持久化存储方式，类似于字典，但它可以将数据持久化到文件中。shelve 模块
允许将 Python 对象存储在文件中，以便在后续的程序运行中重新加载。
"""

#基本用法

import shelve

shelf = shelve.open('my_shelf')  # 打开文件

shelf['name'] = 'EaglesLab' # 存储数据
shelf['age'] = 30
shelf['courses'] = ['Math', 'Science']

print(shelf['name'])    # 读取数据

shelf['age'] = 11  # 更新数据

del shelf['courses']    # 删除数据

shelf.close()   # 关闭文件

"""
hashlib 模块
Python 的 hashlib 模块提供了多种安全哈希和消息摘要算法的接口。这些算法用于生成数据的唯一哈希值，广泛应用于数据完整性校验、密码存储和数字签名等领域。

什么是摘要算法呢？摘要算法又称哈希算法、散列算法。它通过一个函数，把任意长度的数据转换为一个长度固定的数据串（通常用16进制的字符串表示）。

摘要算法就是通过摘要函数对任意长度的数据计算出固定长度的摘要，目的是为了发现原始数据是否被人篡改过。

摘要算法之所以能指出数据是否被篡改过，就是因为摘要函数是一个单向函数，计算摘要很容易，但通过摘要反推数据却非常困难。而且，对原始数据做一个 bit 的修改，都会导致计算出的摘要完全不同。

hashlib 支持多种哈希算法，包括：

MD5
SHA-1
SHA-224
SHA-256
SHA-384
SHA-512
BLAKE2
"""

#基本用法

import hashlib

# sha256_hash = hashlib.sha256(b'xxxx')
sha256_hash = hashlib.sha256()  # 创建一个 SHA-256 哈希对象
md5_hash = hashlib.md5()    

data = b"123456"

sha256_hash.update(data)    # 更新哈希对象

sha256_digest = sha256_hash.hexdigest() # 获取哈希值

print("SHA-256:", sha256_digest)

#加盐

import hashlib
import os

salt = os.urandom(16)   # 生成随机盐
password = b"123456"

hashed = hashlib.pbkdf2_hmac('sha256', password, salt, 10)  # 使用 sha256 和 10次迭代
print(hashed)

import binascii
print(binascii.hexlify(stored_hash).decode('utf-8'))    # 转成十六进制表示

"""
注意事项
不可逆性：哈希函数是不可逆的，意味着无法从哈希值恢复原始数据。
碰撞：不同的输入可能生成相同的哈希值（称为碰撞），但现代的哈希算法力求使碰撞的概率尽量低。
安全性：对于密码存储，建议使用更安全的哈希算法（如 SHA-256 或更高版本）和适当的盐值（salt）来增强安全性。
使用场景
数据完整性：用于验证文件或数据在传输过程中未被篡改。
密码存储：将用户密码的哈希值存储在数据库中，而不是明文密码。
数字签名：用于创建数字签名，确保数据来源的可靠性。
"""

#案例：密码验证

import hashlib
import os

salt = os.urandom(16)
password = b"123456"

stored_hash = hashlib.pbkdf2_hmac('sha256', password, salt, 10)

def verify_password(stored_hash, stored_salt, input_password):
    new_hash = hashlib.pbkdf2_hmac('sha256', input_password, stored_salt, 10)
    return new_hash == stored_hash

pwd = bytes(input('input passwrod: '), encoding='utf-8')

print(verify_password(stored_hash, salt, pwd))

"""
collections 模块
在内置数据类型（dict、list、set、tuple）的基础上，collections 模块还提供了几个额外的数据类型：Counter、deque、
defaultdict、namedtuple 和 OrderedDict 等。

namedtuple: 生成可以使用名字来访问元素内容的 tuple
deque: 双端队列，可以快速的从另外一侧追加和推出对象
Counter: 计数器，主要用来计数
OrderedDict: 有序字典
defaultdict: 带有默认值的字典
"""

#namedtuple

from collections import namedtuple
point = namedtuple('point',['x','y'])
p = point(1,2)
print(p.x)  # 通过名字访问 tuple 元素

"""
deque
使用 list 存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为 list 是线性存储，数据量大的时候，插入
和删除效率很低。

deque 是为了高效实现插入和删除操作的双向列表，适合用于队列和栈。
"""

from collections import deque

q = deque(['a','b','c'])
q.append('x')   # 尾部添加
print(q)    
q.pop()     # 尾部删除
q.appendleft('y')   # 头部添加
print(q)
q.popleft() # 头部删除

"""
OrderedDict
OrderedDict会按照插入的顺序排列，不是 key 本身排序。Python 3.6 之前普通字典完全无序，键值顺序由哈希表存储方式决定。
"""


d1 = {'a':1, 'b':2}
d2 = {'b':2, 'a':1}
print(d1 == d2)  # 输出：True（内容相同即视为相等）

from collections import OrderedDict
od1 = OrderedDict([('a',1), ('b',2)])
od2 = OrderedDict([('b',2), ('a',1)])
print(od1 == od2)  # 输出：False（有序字典比较顺序）

"""
defaultdict
当键不存在时，自动生成默认值，普通 dict 抛出 KeyError 异常，需要频繁处理缺失键。
"""

#基本用法

from collections import defaultdict

defaultdict(list)  # 值类型为列表（分组）
defaultdict(set)   # 值类型为集合（去重）
defaultdict(int)   # 值类型为整数（计数）

#案例1：计数器实现

# 以前写法
count = {}
for char in "hello":
    if char not in count:
        count[char] = 0
    count[char] += 1

# defaultdict 实现
from collections import defaultdict
count = defaultdict(int)
for char in "hello":
    count[char] += 1  # 首次访问自动初始化为0

#案例2：统计单词首字母分组

from collections import defaultdict

words = ["apple", "banana", "avocado", "blueberry"]
index = defaultdict(list)   # 初始化

for word in words:
    first_char = word[0]
    index[first_char].append(word)  # 无需判断键是否存在
print(index['a'])  # 输出：['apple', 'avocado']

"""
counter
Counter 类的目的是用来跟踪值出现的次数。它是一个无序的容器类型，以字典的键值对形式存储，其中元素作为 key，其计数作为 value。
"""

from collections import Counter

c = Counter('qazxswqazxswqazxswsxaqwsxaqws') 
print(c)

"""
时间相关的模块
time 模块
常用方法

time.sleep(secs)：(线程)推迟指定的时间运行。单位为秒。
time.time()：获取当前时间戳。
在 Python 中，通常有这三种方式来表示时间：时间戳、结构化时间和格式化时间：

时间戳：通常来说，时间戳表示的是从1970年1月1日00:00:00开始按秒计算的偏移量。如 1747114142.79492
格式化时间：如 1999-12-06
结构化时间：如 time.struct_time(tm_year=2025, tm_mon=5, tm_mday=13, tm_hour=13, tm_min=29, tm_sec=54, tm_wday=1, tm_yday=133, tm_isdst=0)
"""

import time

# 时间戳
print(time.time())

# 格式化时间
print(time.strftime('%Y-%m-%d %X'))
print(time.strftime('%Y-%m-%d %H-%M-%S'))

# 结构化时间
print(time.localtime())

"""
格式化时间

常见符号含义

符号	含义
%y	    两位数的年份表示（00-99）
%Y	    四位数的年份表示（000-9999）
%m	    月份（01-12）
%d	    月内中的一天（0-31）
%H	    24小时制小时数（0-23）
%I	    12小时制小时数（01-12）
%M	    分钟数（00=59）
%S	    秒（00-59）
%a	    本地简化星期名称
%A	    本地完整星期名称
%b	    本地简化的月份名称
%B	    本地完整的月份名称
%c	    本地相应的日期表示和时间表示
%j	    年内的一天（001-366）
%p	    本地A.M.或P.M.的等价符
%U	    一年中的星期数（00-53）星期天为星期的开始
%w	    星期（0-6），星期天为星期的开始
%W	    一年中的星期数（00-53）星期一为星期的开始
%x	    本地相应的日期表示
%X	    本地相应的时间表示
%Z	    当前时区的名称
%%	    %号本身

结构化时间

常见索引、属性和值

索引	属性	值
0	tm_year（年）	比如2011
1	tm_mon（月）	1月12日
2	tm_mday（日）	1月31日
3	tm_hour（时）	0 - 23
4	tm_min（分）	0 - 59
5	tm_sec（秒）	0 - 60
6	tm_wday（weekday）	0 - 6（0表示周一）
7	tm_yday（一年中的第几天）	1 - 366
8	tm_isdst（是否是夏令时）	默认为0

"""

#格式之间的转换

import time

#  时间戳 <---> 结构化时间
timestamp = time.time()
struct_time = time.localtime(timestamp)
new_timestamp = time.mktime(struct_time)

# 结构化时间 <---> 格式化时间
## struct_time -> format_time
ft = time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(1550312090))
## format_time -> struct_time
st = time.strptime("2024/05/14 11:57:30", "%Y/%m/%d %H:%M:%S")

import time

# 结构化时间 --> %a %b %d %H:%M:%S %Y 字符串
# time.asctime(结构化时间) 如果不传参数，直接返回当前时间的格式化串
print(time.asctime(time.localtime(1550312090.4021888)))

# 时间戳 --> %a %d %d %H:%M:%S %Y 字符串
# time.ctime(时间戳)  如果不传参数，直接返回当前时间的格式化串
print(time.ctime(1550312090.4021888))

#计算时间差

import time

start_time = time.mktime(time.strptime('2017-09-11 08:30:00','%Y-%m-%d %H:%M:%S'))
end_time = time.mktime(time.strptime('2024-10-12 11:00:50','%Y-%m-%d %H:%M:%S'))
dif_time = end_time - start_time
struct_time = time.gmtime(dif_time)
print('过去了%d年%d月%d天%d小时%d分钟%d秒' % (struct_time.tm_year-1970,struct_time.tm_mon-1,
                                       struct_time.tm_mday-1,struct_time.tm_hour,
                                       struct_time.tm_min,struct_time.tm_sec))

"""
datatime 模块
某些情况下，我们需要写一个定时的任务，比如几分钟后，几分钟前，这种情况下，用 time 模块就不太好操作。这个时候我们需要 datatime 模块来完成这个操作。
"""

# datatime模块
import datetime

current_time = datetime.datetime.now()  # 当前时间

# 只能调整的字段：weeks days hours minutes seconds
print(datetime.datetime.now() + datetime.timedelta(weeks=3)) # 三周后
print(datetime.datetime.now() + datetime.timedelta(weeks=-3)) # 三周前
print(datetime.datetime.now() + datetime.timedelta(days=-3)) # 三天前
print(datetime.datetime.now() + datetime.timedelta(days=3)) # 三天后
print(datetime.datetime.now() + datetime.timedelta(hours=5)) # 5小时后
print(datetime.datetime.now() + datetime.timedelta(hours=-5)) # 5小时前
print(datetime.datetime.now() + datetime.timedelta(minutes=-15)) # 15分钟前
print(datetime.datetime.now() + datetime.timedelta(minutes=15)) # 15分钟后
print(datetime.datetime.now() + datetime.timedelta(seconds=-70)) # 70秒前
print(datetime.datetime.now() + datetime.timedelta(seconds=70)) # 70秒后

current_time = datetime.datetime.now()
# 可直接调整到指定的 年 月 日 时 分 秒 等

print(current_time.replace(year=1977))  # 直接调整到1977年
print(current_time.replace(month=1))  # 直接调整到1月份
print(current_time.replace(year=1989,month=4,day=25))  # 1989-04-25 18:49:05.898601

# 时间戳 ---> 格式化时间
print(datetime.date.fromtimestamp(1232132131))  # 2009-01-17

#random 模块
#用来生成随机数模块

import random

print(random.random())          # 大于0且小于1之间的小数
print(random.uniform(1,3))      # 大于1小于3的小数

print(random.randint(1,5))      # 大于等于1且小于等于5之间的整数
print(random.randrange(1,10,2))   # 大于等于1且小于10之间的奇数

ret = random.choice([1,'23',[4,5]])     # 1或者23或者[4,5]
print(ret)

a,b = random.sample([1,'23',[4,5]],2)   # 列表元素任意2个组合
print(a,b)

item = [1,3,5,7,9]
random.shuffle(item)    # 打乱次序
print(item)

#生成随机验证码

import random

def v_code():
    code = ''
    for i in range(5):
        num = random.randint(0,9)
        alf = chr(random.randint(65,90))    # 大写字母
        add = random.choice([num,alf])
        code = "".join([code,str(add)])

    return code

print(v_code())

"""
os 模块
操作系统交互接口

工作路径相关

方法	                含义
os.getcwd()	            获取当前工作目录
os.chdir("dirname")	    改变当前脚本工作目录
os.curdir	            返回当前目录 .
os.pardir	            获取当前目录的父目录字符串名 ..

文件夹相关

方法	                            含义
os.makedirs("dirname1/dirname2")	可生成多层递归目录
os.removedirs("dirname1/dirname2")	若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依此类推
os.mkdir("dirname")	                生成单级目录
os.rmdir("dirname")	                删除单级空目录，若目录不为空则无法删除，报错
os.listdir("dirname")	            列出指定目录下的所有文件和子目录

文件相关

方法	                        含义
os.remove("path/to/filename")	删除一个文件
os.rename("oldname","newname")	重命名文件/目录
os.stat('path/to/filename')	    获取文件/目录信息

操作系统差异相关

方法	    含义
os.sep	    输出操作系统特定的路径分隔符
os.linesep	输出当前平台使用的行终止符
os.pathsep	输出用于分割文件路径的字符串
os.name	    输出字符串指示当前使用平台

执行系统命令相关

方法	                    含义
os.system(command)	        运行命令，直接输出执行结果
os.popen(command).read()	运行命令，获取执行结果
os.environ	                获取系统环境变量

路径相关

方法	                                含义
os.path.abspath(path)	                返回 path 规范化的绝对路径
os.path.split(path)	                    将 path 分割成目录和文件名二元组返回
os.path.dirname(path)	                返回 path 的目录
os.path.basename(path)	                返回 path 最后的文件名
os.path.exists(path)	                如果 path 存在，返回 True；如果 path 不存在，返回 False
os.path.isabs(path)	                    如果 path 是绝对路径，返回 True
os.path.isfile(path)	                如果 path 是一个存在的文件，返回 True。否则返回 False
os.path.isdir(path)	                    如果 path 是一个存在的目录，则返回 True。否则返回 False
os.path.join(path1[, path2[, ...]])	    将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
os.path.getatime(path)	                返回 path 所指向的文件或者目录的最后访问时间
os.path.getmtime(path)	                返回 path 所指向的文件或者目录的最后修改时间
os.path.getsize(path)	                返回 path 的大小

文件属相关

属性	    含义
st_mode	    inode 保护模式
st_ino	    inode 节点号
st_dev	    inode 驻留的设备
st_nlink	inode 的链接数
st_uid	    所有者的用户ID
st_gid	    所有者的组ID
st_size	    普通文件以字节为单位的大小；包含等待某些特殊文件的数据
st_atime	上次访问的时间
st_mtime	最后一次修改的时间
st_ctime	由操作系统报告的"ctime"。在某些系统上（如Unix）是最新的元数据更改的时间，在其它系统上（如Windows）是创建时间（详细信息参见平台的文档）

sys 模块
sys 模块是与 python 解释器交互的一个接口

方法	        作用
sys.argv	    命令行参数 List，第一个元素是程序本身路径
sys.exit(n)	    退出程序，正常退出时 exit(0)，错误退出 sys.exit(1)
sys.version	    获取 Python 解释程序的版本信息
sys.path	    返回模块的搜索路径，初始化时使用 PYTHONPATH 环境变量的值
sys.platform	返回操作系统平台名称

re 模块
正则表达式
正则表达式（Regular Expression，简称Regex）是处理字符串的核心工具之一，它通过预定义的模式规则实现文本的快速检索、匹配和替换。在 Python 中，正则表达式通过内置的 re 模块实现，广泛应用于数据清洗、表单验证、日志分析等领域。

元字符	匹配内容
\w	    匹配字母（包含中文）或数字或下划线
\W	    匹配非字母（包含中文）或数字或下划线
\s	    匹配任意的空白符
\S	    匹配任意非空白符
\d	    匹配数字
\D	    匹配非数字
\A	    匹配字符串的起始，严格匹配字符串的绝对开始
\Z	    匹配字符串的结尾，严格匹配字符串的绝对末尾
\n	    匹配一个换行符
\t	    匹配一个制表符
^	    匹配字符串的起始，re.MULTILINE 匹配每一行的起始
$	    匹配字符串的结尾，末尾或末尾的换行符前的位置，re.MULTILINE 匹配每一行的末尾
.	    匹配任意字符，除了换行符，当 re.DOTALL 标记被指定时，则可以匹配包括换行符的任意字符
[...]	匹配字符组中的字符
...	    匹配除了字符组中的字符的所有字符
*	    匹配0个或者多个左边的字符。
+	    匹配一个或者多个左边的字符。
？	    匹配0个或者1个左边的字符，非贪婪方式。
{n}	    精准匹配n个前面的表达式。
{n,m}	匹配n到m次由前面的正则表达式定义的片段，贪婪方式
a	b
()	    匹配括号内的表达式，也表示一个组
"""
#单字符匹配

import re

# re.findall() 匹配所有返回列表
print(re.findall('\w','上大人123asdfg%^&*(_ \t \n)'))
print(re.findall('\W','上大人123asdfg%^&*(_ \t \n)'))

print(re.findall('\s','上大人123asdfg%^&*(_ \t \n)'))
print(re.findall('\S','上大人123asdfg%^&*(_ \t \n)'))

print(re.findall('\d','上大人123asdfg%^&*(_ \t \n)'))
print(re.findall('\D','上大人123asdfg%^&*(_ \t \n)'))

print(re.findall('\A上大','上大人123asdfg%^&*(_ \t \n)'))
print(re.findall('^上大','上大人123asdfg%^&*(_ \t \n)'))
print(re.findall('\A上大','上大人123asdfg%^&*(_ \t \n上大人456', re.MULTILINE))
print(re.findall('^上大','上大人123asdfg%^&*(_ \t \n上大人456', re.MULTILINE))

print(re.findall('666\Z','上大人123asdfg%^&*(_ \t \n)666'))
print(re.findall('666$','上大人123asdfg%^&*(_ \t \n)666'))
print(re.findall('666\Z','上大人123asdfg%^&*(_ \t \n)666\n'))
print(re.findall('666$','上大人123asdfg%^&*(_ \t \n)666\n'))
print(re.findall('666\Z','上大人123asdfg%^&*(_ \t 666\n)666', re.MULTILINE))
print(re.findall('666$','上大人123asdfg%^&*(_ \t \n)666\n666', re.MULTILINE))

print(re.findall('\n','上大人123asdfg%^&*(_ \t \n)'))
print(re.findall('\t','上大人123asdfg%^&*(_ \t \n)'))

#重复匹配

import re

print(re.findall('a.b', 'ab aab a*b a2b a牛b a\nb'))
print(re.findall('a.b', 'ab aab a*b a2b a牛b a\nb',re.DOTALL))

print(re.findall('a?b', 'ab aab abb aaaab a牛b aba**b'))
print(re.findall('a+b', 'ab aab aaab abbb'))

print(re.findall('a*b', 'ab aab aaab abbb'))
print(re.findall('ab*', 'ab aab aaab abbbbb'))

print(re.findall('a{2,4}b', 'ab aab aaab aaaaabb'))

# .*? 非贪婪匹配
print(re.findall('a.*b', 'ab aab a*()b'))
print(re.findall('a.*?b', 'ab a1b a*()b, aaaaaab'))

# []: 任意一个字符
print(re.findall('a[abc]b', 'aab abb acb adb afb a_b'))

# - 在[]中表示范围
print(re.findall('a[0-9]b', 'a1b a3b aeb a*b arb a_b'))
print(re.findall('a[a-z]b', 'a1b a3b aeb a*b arb a_b'))
print(re.findall('a[a-zA-Z]b', 'aAb aWb aeb a*b arb a_b'))
print(re.findall('a[0-9][0-9]b', 'a11b a12b a34b a*b arb a_b'))
print(re.findall('a[*-+]b','a-b a*b a+b a/b a6b'))

# ^ 在[]中表示取反
print(re.findall('a[^a-z]b', 'acb adb a3b a*b'))

# 分组() 制定一个规则，将满足规则的结果匹配出来
print(re.findall('(.*?)_66', 'cs_66 zhao_66 日天_66'))
print(re.findall('href="(.*?)"','<a href="http://www.baidu.com">点击</a>'))

# 分组() 中加入?：表示将整体匹配出来而不只是()里面的内容
print(re.findall('compan(y|ies)','Too many companies have gone bankrupt, and the next one is my company'))
print(re.findall('compan(?:y|ies)','Too many companies have gone bankrupt, and the next one is my company'))

#常用方法举例

import re

# findall 全部找到返回一个列表
print(re.findall('a','aghjmnbghagjmnbafgv'))

# search 扫描​​整个字符串​​，找到第一个符合模式的子串即返回匹配对象。
print(re.search('Eagle', 'welcome to Eagleslab'))
print(re.search('Eagle', 'welcome to Eagleslab').group())

# match 仅从字符串的​​起始位置​​开始匹配，若起始位置不满足模式，则直接返回None。
print(re.match('chensong', 'chenong 66 66 demon 日天'))
print(re.match('chensong', 'chensong 66 66 barry 日天').group())

# split 可按照任意分割符进行分割
print(re.split('[:：,;；，]','1;3,c,a：3'))

# sub 替换
print(re.sub('镇江','英格科技','欢迎来到镇江'))

# complie 根据包含的正则表达式的字符串创建模式对象。可以实现更有效率的匹配。
obj = re.compile('\d{2}')
print(obj.search('abc123eeee').group())
print(obj.findall('1231232aasd'))

# finditer 返回一个存放匹配结果的迭代器
ret = re.finditer('\d','asd123affess32432')     
print(ret)
print(next(ret).group())
print(next(ret).group())
print([i.group() for i in ret])

#命名分组举例

import re

# 为分组命名，通过分组名获取对应值
ret = re.search("<(?P<tag_name>\w+)>\w+</(?P=tag_name)>","<h1>hello</h1>")
print(ret.group('tag_name'))
print(ret.group())

# 使用序号替换命名，通过分组序号获取对应值
ret = re.search(r"<(\w+)>\w+</\1>","<h1>hello</h1>")
print(ret.group(1))
print(ret.group())

"""
shutil 模块
shutil 是 Python 的标准库之一，提供了许多高级文件操作，例如复制和移动文件，以及创建和提取压缩文件

可以理解为高级的文件、文件夹、压缩包处理模块
"""

#常用方法

#拷贝内容

import shutil

# 拷贝内容
shutil.copyfileobj(open('a.txt','r'),open('a.txt.new','w')) 
# 拷贝文件
shutil.copyfile('file.txt','file1.txt') 
# 拷贝文件信息
shutil.copystat('file.txt','file1.txt') 
# 移动文件或目录
shutil.move(src_path, dst_path) 
# 删除整个目录树
shutil.rmtree(directory_path)
# 删除单个文件
shutil.remove(file_path)      
# 创建单个目录
shutil.mkdir(directory_path)   
# 创建嵌套目录
shutil.makedirs(directory_path)

#压缩和解压缩文件
#调用 ZipFile 和 TarFile 两个模块来进行

import zipfile

# 压缩
z = zipfile.ZipFile('ab.zip', 'w')
z.write('a.txt')
z.write('b.txt')
z.close()

# 解压
z = zipfile.ZipFile('ab.zip', 'r')
z.extractall(path=r'C:\Users\Atopos\Desktop')
z.close()



