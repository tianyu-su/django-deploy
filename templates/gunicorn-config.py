import logging
import logging.handlers
from logging.handlers import WatchedFileHandler
import os
from multiprocessing import cpu_count

bind = "127.0.0.1:<gunicorn-port>"   #配置nginx时，需要将此地址写入nginx配置文件中
proc_name = '<web-name>'   #进程名
worker_class = "<gunicorn-work-class>" # 使用gevent模式，还可以使用sync 模式，默认的是sync模式
errorlog = '/var/log/<web-name>/gunicorn.error.log'  #错误日志文件，不会自动创建需要脚本创建
accesslog = "/var/log/<web-name>/gunicorn.access.log"      #访问日志文件


daemon = False  #守护进程：如果使用 supervisor 就不要开启，否则会冲突
workers = cpu_count()*2
threads = cpu_count()*4

forworded_allow_ips = '*'

reload=True
keepalive = 6
timeout = 65
graceful_timeout = 30
worker_connections = 65535


loglevel = 'info' #日志级别，这个日志级别指的是错误日志的级别，而访问日志的级别无法设置
access_log_format = '%(t)s %(h)s "%(r)s" %(s)s %(L)s %(b)s "'