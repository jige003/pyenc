#!/usr/bin/env python
# coding=utf-8
# author: jige003
import shutil
import sys
import os
import traceback

from glob import glob
from distutils.core import setup
from Cython.Build import cythonize
from optparse import OptionParser
from colorama import Fore,Back,Style,init

init(autoreset=True)

build_dir = "build"
build_tmp_dir = build_dir + "/temp"

module_list = []
exts = []

def parse():
    parser = OptionParser()
    if len(sys.argv) < 2:
        parser.print_help()
        sys.exit(1)
    
    parser.add_option("-d", "--dir", dest="ddir",  default=".", metavar="/opt/project", type="str", help = u"项目路径")
    parser.add_option("-e", "--ext", dest="ext",  default="", metavar="main.py", type="str", help = u"不做处理的文件, 如入口文件main.py")
    parser.add_option("-x", "--isfile",  dest="isfile", action="store_true", default=False, metavar = False, help = u"是否为文件列表")
    parser.add_option("-c", "--clean",  dest="clean", action="store_true", default=False, metavar = False, help = u"加密完成清空删除其他文件")
    parser.add_option("-f", "--files", dest= "files", default="", metavar="enc_file.py,enc_file1.py", type="str", help= u"需要加密的py代码文件列举, 多文件逗号隔离")
    return parser.parse_args()

def get_pys(filepath):
    for f in os.listdir(filepath):
        if f == '__init__.py': continue
        ff = os.path.join(filepath, f)
        if os.path.isdir(ff) and not ff.startswith("."):
            get_pys(ff)
        else:
            if ff.endswith(".py") and ff not in exts:
                module_list.append(ff)
    
def getpy():
    global exts
    if options.isfile:
        return options.files.split(",")
    else:
        exts = options.ext.split(",")
        print Fore.GREEN + "[+] ext files:%s " % str(exts)
        get_pys(options.ddir)
        return module_list
        
def clean():
    for x in module_list:
        cfile = x.replace(".py", ".c")
        pycfile = x.replace(".py", ".pyc")
        print Fore.GREEN + "[+] remove c file:%s py file:%s pyc file:%s " % (cfile, x, pycfile)    
        if os.path.exists(cfile):
            os.remove(cfile)
        if os.path.exists(x):
            os.remove(x)
        if os.path.exists(pycfile):
            os.remove(pycfile)
    print Fore.GREEN + "[+] remove build_tmp_dir:%s" % build_tmp_dir
    if os.path.exists(build_tmp_dir): shutil.rmtree(build_tmp_dir)

def copy():
    for x in module_list:
        xx = x.split(os.path.sep)[1:]
        soname = len(xx) and os.path.join(build_dir, os.path.sep.join(xx)) or os.path.join(build_dir, x)
        soname = soname.replace(".py", ".so")
        ffname = x.replace(".py", ".so")
        print Fore.GREEN + "[+] copy file: [ %s => %s ]" % (soname, ffname)
        shutil.copyfile(soname, ffname)

def main():
    global options, args
    (options, args) = parse()
    try:
        global module_list
        module_list = list(getpy())
        if options.clean:
            clean()
            sys.exit(1)
        print Fore.GREEN + "[+] encyption files:%s " % str(module_list)
        setup(ext_modules = cythonize(module_list), script_args=["build_ext", "-b", build_dir, "-t", build_tmp_dir])
    except Exception, ex:
        traceback.print_exc()
    else:
        copy()

if __name__ == "__main__":
    main()
