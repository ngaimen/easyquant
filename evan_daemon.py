import easyquotation

import easyquant
from easyquant import DefaultQuotationEngine, DefaultLogHandler, PushBaseEngine

broker = None

need_data = None


class LFEngine(PushBaseEngine):
    EventType = 'lf'

    def init(self):
        self.source = easyquotation.use('lf')

    def fetch_quotation(self):
        return self.source.stocks(['162411', '000002'])


quotation_choose = '1'

quotation_engine = DefaultQuotationEngine if quotation_choose == '1' else LFEngine

push_interval = int(input('请输入行情推送间隔(s)\n:'))
quotation_engine.PushInterval = push_interval

log_type_choose = '1'
log_type = 'stdout' if log_type_choose == '1' else 'file'

log_filepath = input('请输入 log 文件记录路径\n: ') if log_type == 'file' else ''

log_handler = DefaultLogHandler(name='Monitor', log_type=log_type, filepath=log_filepath)

m = easyquant.MainEngine(broker, need_data, quotation_engines=[quotation_engine], log_handler=log_handler)
m.is_watch_strategy = True  # 策略文件出现改动时,自动重载,不建议在生产环境下使用
m.load_strategy()
m.start()
