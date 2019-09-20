#!/usr/bin/env python
# -*- coding:utf-8 -*-

######################################################################
## The most import thing :  makedir in your client_ip
## 1. mkdir -p ~/stest/output
## 2. mkdir -p ~/stest/script
######################################################################

import sys
import os
import subprocess
import pxssh
import stest_drive
import paramiko
from stest_log import sLog

request_code = sys.argv[1]
key_command = sys.argv[2]

stest = stest_drive.StestSDKApi (request_code)

client_ip = ""
client_user = ""
client_passwd = ""
client_dir = ""

script_file_fullname = ""
script_file_basename = ""

dest_script_path = ""


def reg():
    sLog.info ("*reg*: ('robot_drive',[fname],[result]")
    stest.reg_param_group ('robot_drive', ['fname'], ['result'])
    sLog.info ("*reg*: ('shell_drive',[fname],[result]")
    stest.reg_param_group ('shell_drive', ['fname'], ['result'])


def exec_robot_drive():
    # *1*get_param_values : START*  *********#
    sLog.info ("*get_param_values*: client_ip,client_user,client_passwd,client_dir ...")
    client_ip, client_user, client_passwd, client_dir = stest.get_env_value ("client_conf").split (':')
    sLog.info ("*get_param_values*: client_ip:%s,client_user:%s,client_passwd:%s,client_dir:%s" % (
    client_ip, client_user, client_passwd, client_dir))

    sLog.info ("*get_param_values*: script_file_fullname,script_file_basename ...")
    script_file_fullname = stest.get_param_value ("fname")
    script_file_basename = os.path.basename (script_file_fullname)
    sLog.info ("*get_param_values*: script_file_fullname:%s,script_file_basename:%s" % (
    script_file_fullname, script_file_basename))

    dest_script_path = client_dir + "/stest/script"
    sLog.info ("*get_param_values*: dest_script_path:%s" % dest_script_path)
    # *1*get_param_values : FINISHED*  *********#

    # *2******   *exec_robot_drive : START*  *********#

    sLog.info ("*exec_robot_drive*: upload %s to %s ..." % (script_file_fullname, dest_script_path))
    resinfo = stest.put_file (script_file_fullname, dest_script_path, client_ip, client_user, client_passwd)
    sLog.info ("*exec_robot_drive*:" + resinfo)

    command = "robot --outputdir " + client_dir + "/stest/output " + dest_script_path + "/" + script_file_basename
    sLog.info ("*exec_robot_drive*: robot command:%s " % command)
    sLog.info (
        "*exec_robot_drive*: client_ip %s, client_user %s,client_passwd %s" % (client_ip, client_user, client_passwd))
    result = stest.exec_command (command, client_ip, client_user, client_passwd, False)
    sLog.info ("*exec_robot_drive*: remote_exec_command res: %s" % result["ret"])
    # sLog.info("*exec_robot_drive*: remote_exec_command out: %s"%result["out"])
    stest.set_ans ("result", result["ret"])

    # command = "mv "+client_dir+"/stest/output/log.html "+client_dir+"/stest/output/"+script_file_basename+".html"
    # result = stest.exec_command(command,client_ip,client_user,client_passwd,True)

    logfilename = client_dir + "/stest/output/log.html"
    localfile = script_file_fullname + ".html"
    sLog.info ("*exec_robot_drive*: SCP %s to %s " % (logfilename, localfile))
    stest.get_file (logfilename, localfile, client_ip, client_user, client_passwd)
    if os.path.exists (localfile):
        sLog.info ("*exec_robot_drive*:  Scpfile OK:%s" % localfile)
    else:
        sLog.error ("*exec_robot_drive*:  Scpfile Fail:%s" % localfile)
        # *2******   *exec_robot_drive : FINISHED*  *********#


if __name__ == "__main__":
    if key_command == "reg":
        reg ()
    if key_command == "exec":
        if stest.get_groupname () == "robot_drive":
            exec_robot_drive ()