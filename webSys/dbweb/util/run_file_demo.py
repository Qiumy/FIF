# -*- coding: utf-8 -*-

import os
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
      "plot": True,
      "output_file": r"E:\codingCode\stockPre\webAPP\dbweb\static\upload\pickle"
    }
  }
}

strategy_file_path = r"E:\codingCode\stockPre\webAPP\dbweb\util\tmpstrategy.py"

def changeConfig(start_date, end_date, config):
    config['base']['start_date'] = start_date
    config['base']['end_date'] = end_date


# changeConfig('2016-01-17', '2016-04-01', config)
run_file(strategy_file_path, config)
