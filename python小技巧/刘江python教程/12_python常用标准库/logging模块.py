import logging


# 1.基础使用

## 1.1 logging使用场景
'''
## 不是所有的场景都需要使用logging模块，下面是Python官方推荐的使用方法:
任务场景                                       最佳工具
普通情况下，在控制台显示输出                     print()
报告正常程序操作过程中发生的事件                 logging.info()(或者更详细的logging.debug())
发出有关特定事件的警告                         warnings.warn()或者logging.warning()
报告错误                                     弹出异常
在不引发异常的情况下报告错误                   logging.error(), logging.exception()或者logging.critical()
'''
## logging模块定义了下表所示的日志级别，按事件严重程度由低到高排列（注意是全部大写！因为它们是常量):
'''
级别                    级别数值            使用时机
DEBUG                     10             详细信息，常用于调试。
INFO                      20             程序正常运行过程中产生的一些信息。
WARNING                   30             警告用户，虽然程序还在正常工作，但有可能发生错误。
ERROR                     40             由于更严重的问题，程序已不能执行一些功能了。
CRITICAL                  50             严重错误，程序已不能继续运行。
默认级别是WARNING，表示只有WARING和比WARNING更严重的事件才会被记录到日志内，低级别的信息会被忽略。
因此，默认情况下，DEBUG和INFO会被忽略。WARING、ERROR和CRITICAL会被记录。
'''

## 1.2 简单案例
import logging

print(logging.warning('watch out!'))  # 消息会被打印到控制台上
print(logging.info('haha'))  # 这行不会被打印，因为级别低于默认级别
# 默认情况下，打印出来的内容包括日志级别、调用者和具体的日志信息

## 1.3 记录到文件中
logging.basicConfig(filename='logging.log', filemode='w', level=logging.DEBUG)  # 使用basicConfig()方法
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')

## 1.4 多模块中同时使用日志功能
'''见程序logging_app.py 和 logging_lib.py'''

## 1.5 日志的变量数据
import logging
logging.warning('%s before you %s', 'Look', 'leap!')

## 1.6 消息格式
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
logging.debug('This message should appear on the console')
logging.info('So should this')
logging.warning('And this, too')

## 1.7 附加时间信息
import logging
logging.basicConfig(format='%(asctime)s %(message)s')
logging.warning('is when this event was logged.')