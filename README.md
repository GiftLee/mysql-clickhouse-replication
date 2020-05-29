# mysql-clickhouse-replication

用于从mysql增量同步数据到clickhouse



环境要求：

python 3.8.2



pypy部署命令

```bash
yum -y install pypy-libs pypy pypy-devel
/usr/local/Cellar/pypy3/6.0.0/bin/pip_pypy3 install pymysql
/usr/local/Cellar/pypy3/6.0.0/bin/pip_pypy3 install mysql-replication
/usr/local/Cellar/pypy3/6.0.0/bin/pip_pypy3 install clickhouse-driver
/usr/local/Cellar/pypy3/6.0.0/bin/pip_pypy3 install redis
```

如果是使用python，那么模块安装命令

```bash
pip install pymysql
pip install mysql-replication
pip install clickhouse-driver
pip install redis
```

基于原代码：

https://github.com/yymysql/mysql-clickhouse-replication