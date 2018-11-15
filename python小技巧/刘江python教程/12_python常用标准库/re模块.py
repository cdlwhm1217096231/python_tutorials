import re
'''正则表达式模块'''
'''
方法	                                描述	                                       返回值
compile(pattern[, flags])	        根据包含正则表达式的字符串创建模式对象	          re对象
search(pattern, string[, flags])	在字符串中查找                          	    第一个匹配到的对象或者None
match(pattern, string[, flags])	    在字符串的开始处匹配模式	                    在字符串开头匹配到的对象或者None
split(pattern, string[, maxsplit=0,flags])	根据模式的匹配项来分割字符串	            分割后的字符串列表
findall(pattern, string,flags)	            列出字符串中模式的所有匹配项	            所有匹配到的字符串列表
sub(pat,repl, string[,count=0,flags])	将字符串中所有的pat的匹配项用repl替换	    完成替换后的新字符串
finditer(pattern, string,flags)	        将所有匹配到的项生成一个迭代器	            所有匹配到的字符串组合成的迭代器
subn(pat,repl, string[,count=0,flags])	在替换字符串后，同时报告替换的次数	        完成替换后的新字符串及替换次数
escape（string）                      	将字符串中所有特殊正则表达式字符串转义	    转义后的字符串
purge(pattern)	                        清空正则表达式	
template(pattern[,flags])	            编译一个匹配模板	                        模式对象
fullmatch(pattern, string[, flags])	match方法的全字符串匹配版本	                    类似match的返回值
'''
# 几种匹配模式，单个大写字母是缩写，单词是完整模式名称，引用方法为re.A或者re.ASCII
'''
A  ：ASCII       
I  ：IGNORECASE  
L  ：LOCALE      
M  ：MULTILINE  
S  ：DOTALL      
X  ：VERBOSE    
U  ：UNICODE
'''
# 反斜杠的困扰：\
'''
假如需要匹配文本中的字符\,Python提供了原生字符串的功能，很好地解决了这个问题.
这个例子中的正则表达式可以使用r"\\"表示。同样，匹配一个数字的"\\d"可以直接写成r"\d"
'''
# 1.compile(pattern, flags=0)-----用于将字符串形式的正则表达式编译为Pattern模式对象，可以实现更高效率的匹配
pat = re.compile(r'abc')   # 返回re对象
print(pat.match('abc123'))
print(pat.match('abc123').group())
print(pat.match('abc123').group)
'''
如果你只是简单的匹配一下后就不用了，那么re.match()这种简便的调用方式无疑来得更简单快捷。
如果你有个模式需要进行大量次数的匹配，那么先compile编译一下再匹配的方式，效率会高很多。
'''
# 2.match(pattern, string, flags=0)
'''match()方法会在给定字符串的开头进行匹配，如果匹配不成功则返回None，匹配成功返回一个匹配对象，这个对象有个group()方法，可以将匹配到的字符串给出'''
ret = re.match(r'abc', 'ab1c123')
print(ret)
res = re.match(r'abc', 'abc123')
print('返回一个匹配的对象:', res)  # span指的是匹配到的字符在字符串中的位置下标，分别对应start和end,不包括end
print('将匹配到的字符串给出:', res.group())
obj = re.match(r'abc', 'abc123')
print(obj.start())
print(obj.end())
print(obj.span())
print(obj.group())

# 3. search(pattern, string, flags=0)
'''在文本内查找，返回第一个匹配到的字符串。它的返回值类型和使用方法与match()是一样的，唯一的区别就是查找的位置不用固定在文本的开头。'''
obj = re.search(r'abc', '123abc5678abc45667abc776')
print(obj)
print(obj.group())

# 4.findall(pattern, string, flags=0)
'''
findall()和match()、search()的不同之处在于，前两者都是单值匹配，找到一个就忽略后面，直接返回不再查找了
而findall是全文查找，它的返回值是一个匹配到的字符串的列表
这个列表没有group()方法，没有start、end、span，更不是一个匹配对象，仅仅是个列表！如果一项都没有匹配到那么返回一个空列表
'''
obj = re.findall(r'abc', '123abc5678abc45667abc776')
print(obj)
# print(obj.group()) 无group()方法，此行代码出错
obj = re.findall(r'ABC', 'abc34545abc65677abc545')
print(obj)

# 5.split(pattern, string, maxsplit=0, flags=0)
'''
re模块的split()方法和字符串的split()方法很相似，都是利用特定的字符去分割字符串
re模块的split()可以使用正则表达式，因此更灵活，更强大
'''
s = '8+7*5+6/3'
a_list = re.split(r'[\+\-\*\/]', s)
print(a_list)
# split有个参数maxsplit，用于指定分割的次数
b_list = re.split(r'[\+\-\*\/]', s, maxsplit=2)
print(b_list)
# 利用分组的概念，re.split()方法还可以保存被匹配到的分隔符
c_list = re.split(r'([\+\-\*\/])', s)  # 注意这里添加了括号！
print(c_list)

# 6.sub(pattern, repl, string, count=0, flags=0)
'''
sub()方法类似字符串的replace()方法，用指定的内容替换匹配到的字符，可以指定替换次数
'''
s = "i am jack! i am nine years old ! i like shanghai!"
s = re.sub(r'i', 'I', s)
print(s)
# sub()方法有一个高级功能——“分组引用”
origin = "Hello,world!"
r = re.sub(r'(world)', r'<em>\1<em>', origin)   # 注意括号和\1的作用！
print(r)

# 7. flag匹配模式
'''
匹配模式	描述
re.A	ASCII字符模式
re.I	使匹配对大小写不敏感，也就是不区分大小写的模式
re.L	做本地化识别（locale-aware）匹配
re.M	多行匹配，影响 ^ 和 $
re.S	使 . 这个通配符能够匹配包括换行在内的所有字符，针对多行匹配
re.U	根据Unicode字符集解析字符。这个标志影响 \w, \W, \b, \B
re.X	该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解
'''

# re.I模式：正则表达式是区分字母大小写的，但在re.I模式下，则忽略大小写
res = re.findall(r'a', 'ABC1a456A6', flags=re.I)
print(res)
# re.S模式：
s = """
<p>水调歌头·明月几时有\n
宋代：苏轼\n
\n
丙辰中秋，欢饮达旦，大醉，作此篇，兼怀子由。\n
\n
明月几时有？把酒问青天。\n
不知天上宫阙，今夕是何年。\n
我欲乘风归去，又恐琼楼玉宇，高处不胜寒。\n
起舞弄清影，何似在人间？\n
转朱阁，低绮户，照无眠。\n
不应有恨，何事长向别时圆？\n
人有悲欢离合，月有阴晴圆缺，此事古难全。\n
但愿人长久，千里共婵娟。\n</p>
"""
ret = re.search(r'<p>(.*?)</p>', s, re.S)
print(ret)
print(ret.group(1))

# 8.分组功能
'''
所谓的分组就是去已经匹配到的内容里面再筛选出需要的内容，相当于二次过滤
实现分组靠圆括号()，而获取分组的内容靠的是group()、groups()和groupdict()方法
'''
origin = 'huedfid123123gflgjfo123'
# match()方法，不分组时的情况：
r = re.match(r'h\w+', origin)
print(r.group())
print(r.groups())
print(r.groupdict())
# match()方法，有分组的情况（注意圆括号！）
r = re.match(r'h(\w+).*(?P<name>\d)$', origin)  # group()和group(0)是对等的，都表示整个匹配到的字符串
## 从group(1)开始，分别是从左往右的小组序号，按位置顺序来,(?P<name>\d)中?P<name>是个正则表达式的特殊语法，表示给这个小组取了个叫“name”的名字，?P<xxxx>是固定写法
print(r.group())  # 获取匹配到的整体结果
print(r.group(1))  # 获取匹配到的分组1的结果
print(r.group(2))  # 获取匹配到的分组2的结果
print(r.groups())  # 获取模型中匹配到的分组结果元组
print(r.groupdict())  # 获取模型中匹配到的分组中所有key的字典

# search()方法，有分组的情况：
origin = "sdfi1ha23123safd123"      # 注意这里对匹配对象做了下调整
# 有分组
r = re.search("h(\w+).*(?P<name>\d)$", origin)
print(r.group())
print(r.group(0))
print(r.group(1))
print(r.group(2))
print(r.groups())
print(r.groupdict())
# findall()方法，没有分组的情况：
origin = "has something have do"
# 无分组
r = re.findall("h\w+", origin)
print(r)
# findall()方法，有一个分组的情况
# 一个分组
r = re.findall("h(\w+)", origin)
print(r)
# findall()方法，有两个以上分组的情况
# 两个分组
origin = "hasabcd something haveabcd do"    # 字符串调整了一下
r = re.findall("h(\w+)a(bc)d", origin)
print(r)
# sub()方法，有分组的情况:
origin = "hasabcd something haveabcd do"
# 有分组
r = re.sub("h(\w+)", "haha",origin)
print(r)
# split()方法，有一个分组的情况：
origin = "has abcd something abcd do"
# 有一个分组
r = re.split("(abcd)", origin)
print(r)
# split()方法，有两个分组，并且嵌套：
origin = "has abcd something abcd do"
# 有两个分组
r = re.split("(a(bc)d)", origin)
print(r)
