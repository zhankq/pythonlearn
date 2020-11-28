# >>> import os
# >>> os.getcwd()
# 'C:\\WINDOWS\\System32'
# >>> os.chdir('/server/accesslogs')
# Traceback (most recent call last):
#   File "<pyshell#2>", line 1, in <module>
#     os.chdir('/server/accesslogs')
# FileNotFoundError: [WinError 3] 系统找不到指定的路径。: '/server/accesslogs'
# >>> os.chdir("D:\\项目文档\\互阅\\接口文档")
# >>> os.getcwd()
# 'D:\\项目文档\\互阅\\接口文档'
# >>> os.system("mkdir today")
# 0
# >>> dir (os)
# ['DirEntry', 'F_OK', 'MutableMapping', 'O_APPEND', 'O_BINARY', 'O_CREAT', 'O_EXCL', 'O_NOINHERIT', 'O_RANDOM', 'O_RDONLY', 'O_RDWR', 'O_SEQUENTIAL', 'O_SHORT_LIVED', 'O_TEMPORARY', 'O_TEXT', 'O_TRUNC', 'O_WRONLY', 'P_DETACH', 'P_NOWAIT', 'P_NOWAITO', 'P_OVERLAY', 'P_WAIT', 'PathLike', 'R_OK', 'SEEK_CUR', 'SEEK_END', 'SEEK_SET', 'TMP_MAX', 'W_OK', 'X_OK', '_Environ', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_check_methods', '_execvpe', '_exists', '_exit', '_fspath', '_get_exports_list', '_putenv', '_unsetenv', '_wrap_close', 'abc', 'abort', 'access', 'altsep', 'chdir', 'chmod', 'close', 'closerange', 'cpu_count', 'curdir', 'defpath', 'device_encoding', 'devnull', 'dup', 'dup2', 'environ', 'error', 'execl', 'execle', 'execlp', 'execlpe', 'execv', 'execve', 'execvp', 'execvpe', 'extsep', 'fdopen', 'fsdecode', 'fsencode', 'fspath', 'fstat', 'fsync', 'ftruncate', 'get_exec_path', 'get_handle_inheritable', 'get_inheritable', 'get_terminal_size', 'getcwd', 'getcwdb', 'getenv', 'getlogin', 'getpid', 'getppid', 'isatty', 'kill', 'linesep', 'link', 'listdir', 'lseek', 'lstat', 'makedirs', 'mkdir', 'name', 'open', 'pardir', 'path', 'pathsep', 'pipe', 'popen', 'putenv', 'read', 'readlink', 'remove', 'removedirs', 'rename', 'renames', 'replace', 'rmdir', 'scandir', 'sep', 'set_handle_inheritable', 'set_inheritable', 'spawnl', 'spawnle', 'spawnv', 'spawnve', 'st', 'startfile', 'stat', 'stat_result', 'statvfs_result', 'strerror', 'supports_bytes_environ', 'supports_dir_fd', 'supports_effective_ids', 'supports_fd', 'supports_follow_symlinks', 'symlink', 'sys', 'system', 'terminal_size', 'times', 'times_result', 'truncate', 'umask', 'uname_result', 'unlink', 'urandom', 'utime', 'waitpid', 'walk', 'write']
# >>> dir(os)
# ['DirEntry', 'F_OK', 'MutableMapping', 'O_APPEND', 'O_BINARY', 'O_CREAT', 'O_EXCL', 'O_NOINHERIT', 'O_RANDOM', 'O_RDONLY', 'O_RDWR', 'O_SEQUENTIAL', 'O_SHORT_LIVED', 'O_TEMPORARY', 'O_TEXT', 'O_TRUNC', 'O_WRONLY', 'P_DETACH', 'P_NOWAIT', 'P_NOWAITO', 'P_OVERLAY', 'P_WAIT', 'PathLike', 'R_OK', 'SEEK_CUR', 'SEEK_END', 'SEEK_SET', 'TMP_MAX', 'W_OK', 'X_OK', '_Environ', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_check_methods', '_execvpe', '_exists', '_exit', '_fspath', '_get_exports_list', '_putenv', '_unsetenv', '_wrap_close', 'abc', 'abort', 'access', 'altsep', 'chdir', 'chmod', 'close', 'closerange', 'cpu_count', 'curdir', 'defpath', 'device_encoding', 'devnull', 'dup', 'dup2', 'environ', 'error', 'execl', 'execle', 'execlp', 'execlpe', 'execv', 'execve', 'execvp', 'execvpe', 'extsep', 'fdopen', 'fsdecode', 'fsencode', 'fspath', 'fstat', 'fsync', 'ftruncate', 'get_exec_path', 'get_handle_inheritable', 'get_inheritable', 'get_terminal_size', 'getcwd', 'getcwdb', 'getenv', 'getlogin', 'getpid', 'getppid', 'isatty', 'kill', 'linesep', 'link', 'listdir', 'lseek', 'lstat', 'makedirs', 'mkdir', 'name', 'open', 'pardir', 'path', 'pathsep', 'pipe', 'popen', 'putenv', 'read', 'readlink', 'remove', 'removedirs', 'rename', 'renames', 'replace', 'rmdir', 'scandir', 'sep', 'set_handle_inheritable', 'set_inheritable', 'spawnl', 'spawnle', 'spawnv', 'spawnve', 'st', 'startfile', 'stat', 'stat_result', 'statvfs_result', 'strerror', 'supports_bytes_environ', 'supports_dir_fd', 'supports_effective_ids', 'supports_fd', 'supports_follow_symlinks', 'symlink', 'sys', 'system', 'terminal_size', 'times', 'times_result', 'truncate', 'umask', 'uname_result', 'unlink', 'urandom', 'utime', 'waitpid', 'walk', 'write']
# >>> help(os)
#
# >>> import shutil
# >>> shutil.copyfile('data.db',"aa.dd")
# Traceback (most recent call last):
#   File "<pyshell#10>", line 1, in <module>
#     shutil.copyfile('data.db',"aa.dd")
#   File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.7_3.7.2544.0_x64__qbz5n2kfra8p0\lib\shutil.py", line 120, in copyfile
#     with open(src, 'rb') as fsrc:
# FileNotFoundError: [Errno 2] No such file or directory: 'data.db'
# >>> import glob
# >>> glob.glob("*.py")
# []
# >>> os.getcwd()
# 'D:\\项目文档\\互阅\\接口文档'
# >>> glob.glob("*.txt")
# ['API说明2异步版本 (2).txt', 'wx-xb-阅读下单API.txt', '互阅.txt', '地址.txt', '广州青年--加单接口规范(2).txt', '抖音快手下单API.txt', '渠道提供接口.txt', '结算SQL.txt', '返回页地址获取接口文档(1).txt']
# >>> for i in glob.glob("*.txt"):
# 	print(i)
#
#
# API说明2异步版本 (2).txt
# wx-xb-阅读下单API.txt
# 互阅.txt
# 地址.txt
# 广州青年--加单接口规范(2).txt
# 抖音快手下单API.txt
# 渠道提供接口.txt
# 结算SQL.txt
# 返回页地址获取接口文档(1).txt
# >>> type(glob.glob("*.txt"))
# <class 'list'>
# >>> import sys
# >>> print(sys.argv)
# ['']
# >>> 'good job'.replace('good job','hello world')
# 'hello world'
# >>> import math
# >>> math.cos(math.pi/4)
# 0.7071067811865476
# >>> math.pi
# 3.141592653589793
# >>> import random
# >>> random.choice(['a','b','e','f','s'])
# 'e'
# >>> import request
# Traceback (most recent call last):
#   File "<pyshell#27>", line 1, in <module>
#     import request
# ModuleNotFoundError: No module named 'request'
# >>> import requests
# >>> type(requests)
# <class 'module'>
# >>> from datetime import date
# >>> date.today()
# datetime.date(2020, 11, 28)
# >>> now
# Traceback (most recent call last):
#   File "<pyshell#32>", line 1, in <module>
#     now
# NameError: name 'now' is not defined
# >>> now()
# Traceback (most recent call last):
#   File "<pyshell#33>", line 1, in <module>
#     now()
# NameError: name 'now' is not defined
# >>> import zlib
# >>> s=b'1234567890 9874563210---------------------------'
# >>> len(s)
# 48
# >>> t=zlib.compress(s)
# >>> len(t)
# 30
# >>> t
# b'x\x9c3426153\xb7\xb04P\xb0\xb40\x072\x8d\x8d\x0c\rtq\x03\x00\xe3g\x08\xfa'
# >>> zlib.decompress(t)
# b'1234567890 9874563210---------------------------'
# >>> s='1234567890 9874563210---------------------------'
# >>>
# >>> len(s)
# 48
# >>> t=zlib.compress(s)
# Traceback (most recent call last):
#   File "<pyshell#44>", line 1, in <module>
#     t=zlib.compress(s)
# TypeError: a bytes-like object is required, not 'str'
# >>> t=zlib.compress(s)
# Traceback (most recent call last):
#   File "<pyshell#45>", line 1, in <module>
#     t=zlib.compress(s)
# TypeError: a bytes-like object is required, not 'str'
# >>>