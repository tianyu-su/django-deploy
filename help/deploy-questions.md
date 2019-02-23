# Deploy Questions

## 出错
> 使用 wget 测试网站
>
> 使用 一键修复脚本
- 检查代码是否run？ 
    - 进入虚拟环境 python manage.py runserver
- 检查 gunicorn 是否运行成功
    - 进入虚拟环境执行,通过  `pstree -ap | grep "gunicorn"` 查看是否成功
    - 运行简易命令，测试gunicorn是否正确安装：`gunicorn --bind 0.0.0.0:8000 myproject.wsgi:application`
    - 运行根据配置文件启动的命令, `/home/.pyenvs/GpsDisp/bin/gunicorn -c server-config/gunicorn-config.py GpsDisp.wsgi:application` ，如果屏幕卡住了，运行`pstree -ap | grep "gunicorn"`查看是否成功
- 检查 supervisor 是否运行成功
    - `sudo service supervisor status`
    - 重启 superviosr `sudo service supervisor restart`
- 更改了 supervisor 配置文件一定要重启 supervisor 
- 检查 supervisorctl 是否成功运行所有管理的项目
    - supervisorctl status
    - sudo supervisorctl stop all 
    - sudo supervisorctl start all // 查看是否启动了目标项目
- 检查 nginx 是否运行成功
    - `sudo service nginx status`
    - `sudo service nginx restart`
- 本机可以访问，外部访问失败，检查 nginx 日志
- 代码使用 runserver 正常，使用 gunicorn 异常，检查 gunicorn 日志