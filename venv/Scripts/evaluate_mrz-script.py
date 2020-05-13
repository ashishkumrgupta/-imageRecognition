#!E:\My-Python-Workspace\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'PassportEye==1.4.1','console_scripts','evaluate_mrz'
__requires__ = 'PassportEye==1.4.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('PassportEye==1.4.1', 'console_scripts', 'evaluate_mrz')()
    )
