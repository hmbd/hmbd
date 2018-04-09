#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import subprocess

from conf import dbconf


def run_cmd(cmd, force=False):
    p = subprocess.Popen(cmd,
                         stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         shell=True)
    stdout, stderr = p.communicate()
    if stderr:
        if not force:
            raise Exception("cmd: %s, stderr: %s" % (cmd, stderr))
    else:
        return stdout


def create_database():
    """创建数据库
    """
    create_sql = "create database if not exists {};".format(dbconf.MYSQL_DB_MAIN)
    cmd = "mysql -u{} -p{} -e '{}'".format(dbconf.MYSQL_USER_MAIN, dbconf.MYSQL_PWD_MAIN,
                                           create_sql)
    run_cmd(cmd, force=True)


def create_table():
    """创建表
    """
    commands = [
        "python3 manage.py migrate",
        "python3 manage.py makemigrations  app"
        "python3 manage.py migrate",
    ]
    for cmd in commands:
        run_cmd(cmd)


def init_database():
    curr_path = os.path.dirname(__file__)
    sql_path = os.path.join(curr_path, "model", "counsellor.sql")
    cmd = "mysql -h127.0.0.1  -P3306 -uroot -proot {} < {}".format(dbconf.MYSQL_DB_MAIN, sql_path)
    run_cmd(cmd, force=True)


def main():
    create_database()
    create_table()
    init_database()


if __name__ == '__main__':
    main()
