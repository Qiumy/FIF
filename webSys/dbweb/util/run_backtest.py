# -*- coding:utf-8 -*-

import subprocess
from rqalpha import run_file

config = {
  "base": {

    "securities": ['stock'],
    "stock_starting_cash": 100000,
    "benchmark": "000300.XSHG"
  },
  "extra": {
    "log_level": "verbose",
  },
  "mod": {
    "sys_analyser": {
      "enabled": True,
      "plot": False,
      "output_file": r"E:\codingCode\stockPre\webAPP\dbweb\static\upload\pickle"
    }
  }
}

strategy_file_path = r"E:\codingCode\stockPre\webAPP\dbweb\util\tmpstrategy.py"

def changeConfig(start_date, end_date, config):
    config['base']['start_date'] = start_date
    config['base']['end_date'] = end_date

def run_strategy(start_date, end_date):
    try:
        changeConfig(start_date, end_date, config)
        run_file(strategy_file_path, config)
        pass
    except Exception as e:
        pass
    return "Done!"


if __name__ == '__main__':
    run_strategy('2016-01-01', '2016-04-01')
