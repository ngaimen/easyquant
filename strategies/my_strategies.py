from easyquant import StrategyTemplate
from evan_utils import config_io


class Strategy(StrategyTemplate):
    name = 'zhisun策略'

    def strategy(self, event):
        print('\n\n')
        self.log.info('--------------------------------')
        self.config = config_io.file2dict()
        for key in self.config.keys():
            zhisun = float(self.config[key]['zs'])
            zhisunbili = float(self.config[key]['zsbl'])

            zhisun2 = float(self.config[key]['zs2'])
            zhisunbili2 = float(self.config[key]['zsbl2'])

            data = event.data[key]
            now = float(data['now'])
            high = float(data['high'])
            close = float(data['close'])

            if high * zhisunbili > zhisun:
                self.config[key]['zs'] = str(high * zhisunbili)
                self.config[key]['zs2'] = str(high * zhisunbili2)
                config_io.dict2file(self.config)

            baifenbi = (1 - zhisun / (now == 0 and 0.01 or now)) * 100.0
            baifenbi2 = (1 - zhisun2 / (now == 0 and 0.01 or now)) * 100.0

            zhangdiefu = (now / close - 1) * 100

            print(' \033[1;31m%s\033[0m now:%.2f  涨跌幅:%.2f' % (data['name'], now, zhangdiefu), end = '')
            if now > zhisun:
                print('止损价:%.2f 止损百分比:%.2f%% high:%.2f 默认比例:%.2f%%\n' % (zhisun, baifenbi, high, zhisunbili * 100))
            elif now > zhisun2:
                print('止损价:%.2f \033[1;31m止损百分比:%.2f%% 跌破止损 1\033[0m high:%.2f 默认比例:%.2f%%\n' % (zhisun, baifenbi, high, zhisunbili * 100))
            else:
                print('止损价:%.2f \033[1;31m止损百分比:%.2f%% 跌破止损 2 \033[0m high:%.2f 默认比例:%.2f%%\n' % (zhisun2, baifenbi2, high, zhisunbili2 * 100))



