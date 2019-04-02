### 介绍
> python项目加密工具， 加密核心使用cythonize， 原理是先编译python文件为c，然后再编译为动态链接库so； 使用此工具可灵活对希望的代码文件加密并替换；

### 优势
> 理论上执行加密替换后项目不需要改动就可以运行， 针对项目的加密选择也比较灵活;

### 安装
```
#安装
make install 

#卸载
make uninstall
```

### 用法
> 对于使用加密的项目， 请先备份再使用;
> 对于使用加密的项目， 请先备份再使用;
> 对于使用加密的项目， 请先备份再使用;

```
Usage: pyenc [options]

Options:
  -h, --help            show this help message and exit
  -d /opt/project, --dir=/opt/project
                        项目路径
  -e main.py, --ext=main.py
                        不做处理的文件, 如入口文件main.py
  -x, --isfile          是否为文件列表
  -c, --clean           加密完成清空删除其他文件
  -f enc_file.py,enc_file1.py, --files=enc_file.py,enc_file1.py
                        需要加密的py代码文件列举, 多文件逗号隔离
```


### 使用举例
> 对多文件执行加密

```
#执行加密
pyenc -x -f enc_file.py,enc_file1.py 

#加密完成清空缓存文件及源代码py文件
pyenc -x -f enc_file.py,enc_file1.py -c
```

> 对文件夹执行加密

```
#执行加密， 可使用-e 设置不加密的文件或者入口文件
pyenc -d test -e test/main.py 

#加密完成清空缓存文件及源代码py文件
pyenc -d test -e test/main.py -c
```
