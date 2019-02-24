### 运行脚本不要乱用 sudo

乱使用 sudo 会导致执行脚本中，例如含有 `$USER`  就会获取到 root 用户，导致出错，本来想获取登陆用户

- bash xxx.sh  `不需要添加可执行权限`
- sh xxx.sh

### 查看 gunicorn 进程树

> `pstree -ap | grep gunicorn`
> 当修改代码时候重启使用 `kill -HUP pid` 如果用了 supervisor 管理，那么使用 sudo supervisorctl restart <appname>
> 杀死 kill -9 pid

### 重启nginx
> 当修改配置文件的时候 `sudo service nginx reload`

### Supervisor
> 一般不用开关 supervisor 只需要 使用 supervisorctl 即可
- 启动：service supervisor start
- 重启：service supervisor restart
#### 管理 Supervisor 里面的程序
- sudo supervisorctl restart all
- sudo supervisorctl stop all
- sudo supervisorctl start  all
- sudo supervisorctl start <project_name>


### 查看端口占用
> `sudo netstat -tlpn`

### ngxin, supervisor 位置
> /etc/

### 激活虚拟环境
> source /home/.pyenvs/appname/bin/activate

### 查看端口 
- lsof -i
- sudo netstat -ap | grep -E "7777|8999"

### 安装pip
> 切换到虚拟环境的python目录
```
$ wget https://bootstrap.pypa.io/get-pip.py
$ python get-pip.py
$ pip -V　　#查看pip版本
```

### 脚本运行时间太长，后台运行

> 后台运行脚本，并且输出到日志文件

`nohup bash /home/GpsDisp/server-config/init_web.sh > ~/web_depoly_log.log 2>&1 &`

查看运行的任务(只能看本机): `jobs`

查看其他主机运行的任务:  `ps -aux|grep init_web.sh`