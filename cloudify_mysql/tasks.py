#!/usr/bin/env python

from cloudify import ctx
import mysql.connector as dbms

def execute(mysql_host,
            mysql_username,
            mysql_password,
            mysql_database,
            mysql_commands,
            **_):

    debug = 'debug' in _.keys() and _.get('debug') == True

    if debug:
        ctx.logger.debug(
            'Connecting to database {0} on host {1} with user {2}.'.format(
                mysql_database, mysql_host, mysql_username))

    db = dbms.connect(host=mysql_host,
                      user=mysql_username,
                      passwd=mysql_password,
                      db=mysql_database)

    cur = db.cursor()

    for mysql_command in mysql_commands:
        if debug:
            ctx.logger.debug(
                'Executing command: {0}.'.format(mysql_command))
        cur.execute(mysql_command)

    db.close()
