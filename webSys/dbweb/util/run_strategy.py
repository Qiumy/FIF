#! /usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
from flask_babel import gettext


# 运行python策略
def run_strategy(filepath):
    filepath = r"E:\codingCode\stockPre\webAPP\dbweb\util\backtest.py"
    result = {}
    try:
        result['state'] = 200
        # result['output'] = subprocess.check_output(['python', filepath], stderr=subprocess.STDOUT, timeout=100)
        result['output'] = subprocess.check_output(['python', filepath])
    except subprocess.CalledProcessError as e:
        error_str = e.output.decode('utf-8')
        print("error str:", error_str)
        line_str = error_str[error_str.find(',')+2]
        except_str = line_str[:line_str.find('\r')] + '\n' + line_str[line_str.find('^'+1):].strip()
        result = dict(error='Exception', output=except_str, state=201)
    except subprocess.TimeoutExpired as e:
        result = dict(error='Timeout', output=gettext('Timeout'), state=202)
    except subprocess.CalledProcessError as e:
        result = dict(error='Error', output=gettext('Error'), state=203)
    # print(result)
    return result

if __name__ == '__main__':
    import time
    t0 = time.time()
    run_strategy(" ")
    t1 = time.time()
    print(t1-t0)