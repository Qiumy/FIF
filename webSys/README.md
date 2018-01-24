# 证券模拟交易系统

## 部署方法(Windows)：
1. **使用virtualenv虚拟化环境**([virtualenv简易教程](http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432712108300322c61f256c74803b43bfd65c6f8d0d0000))：根据项目下的requirements.txt把依赖包安装到虚拟环境中（有些依赖如MySQL-pyrhon、lxml安装不了的，去[windows下的python依赖包](http://www.lfd.uci.edu/~gohlke/pythonlibs/)下载安装）。以后启动项目前都需要先激活虚拟环境。

2. **安装数据库**：在项目下的cogfig.py里把*SQLALCHEMY_DATABASE_URI*这项改为自己的mysql数据库用户名密码，之后再进入项目主目录进行数据迁移，即依次执行
<pre><code>
# 首次迁移
# python manage.py db init
# python manage.py db migrate
python manage.py db upgrade
</code></pre>
之后可以导入sql文件（建议使用navicat，一个可视化管理mysql的工具）

3. **启动项目**：先激活虚拟环境，之后运行服务进程。<pre><code>venv/bin/activate
python manage.py runserver</code></pre>
