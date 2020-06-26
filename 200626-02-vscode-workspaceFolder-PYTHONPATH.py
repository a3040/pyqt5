# vscode에서 작업디렉토리 PYTHONPATH에 넣기

"""
/root/code
├── main
│   └── main.py
└── mod
    └── utils.py

#######main/main.py
import sys

from mod.utils import Utils
print(sys.path)

####### mod/utils.py
class Utils:
    u = 'a'


root@ka:~/code# /usr/bin/python3 /root/code/main/main.py
Traceback (most recent call last):
  File "/root/code/main/main.py", line 3, in <module>
    from mod.utils import Utils
ModuleNotFoundError: No module named 'mod'



/root/code
├── .vscode
│   └── settings.json
├── main
│   └── main.py
└── mod
    └── utils.py

#######.vscode/settings.json
{
    "terminal.integrated.env.osx": {
        "PYTHONPATH": "${workspaceFolder}:${env:PYTHONPATH}"
    },
    "terminal.integrated.env.linux": {
        "PYTHONPATH": "${workspaceFolder}:${env:PYTHONPATH}"
    },
    "terminal.integrated.env.windows": {
        "PYTHONPATH": "${workspaceFolder}:${env:PYTHONPATH}"
    }
}

######.vscode/settings.json 파일 생성 후 vscode 재시작 !!!!!!!!!!
###### 하면 알림이 뜸, 수락해 주고 실행하면

root@ka:~/code# /usr/bin/python3 /root/code/main/main.py
['/root/code/main', '/root/code', ...]
"""
