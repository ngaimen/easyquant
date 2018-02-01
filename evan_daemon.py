#!/usr/bin/python3
import easyquotation

import easyquant
from easyquant import DefaultQuotationEngine, DefaultLogHandler, PushBaseEngine

quotation_engine = DefaultQuotationEngine

push_interval = int(input('请输入行情推送间隔(s)\n:'))
quotation_engine.PushInterval = push_interval

log_handler = DefaultLogHandler(name='Monitor', log_type='stdout', filepath='')

m = easyquant.MainEngine(None, None, quotation_engines=[quotation_engine], log_handler=log_handler)
m.is_watch_strategy = True  # 策略文件出现改动时,自动重载,不建议在生产环境下使用
m.load_strategy()
m.start()
