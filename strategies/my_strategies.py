from easyquant import StrategyTemplate
import json


class Strategy(StrategyTemplate):
    name = 'zhisun策略'

    def strategy(self, event):
        print('\n\n')
        self.log.info('--------------------------------')
        self.config = self.file2dict('config.json')
        for key in self.config.keys():
            zhisun = float(self.config[key]['zs'])
            zhisunbili = float(self.config[key]['zsbl'])

            zhisun2 = float(self.config[key]['zs2'])
            zhisunbili2 = float(self.config[key]['zsbl2'])

            data = event.data[key]
            now = float(data['now'])
            high = float(data['high'])

            if high * zhisunbili > zhisun:
                self.config[key]['zs'] = str(high * zhisunbili)
                self.config[key]['zs2'] = str(high * zhisunbili2)
                self.dict2file('config.json', self.config)

            baifenbi = (1 - zhisun / (now == 0 and 0.01 or now)) * 100.0
            baifenbi2 = (1 - zhisun2 / (now == 0 and 0.01 or now)) * 100.0

            if now > zhisun:
                self.log.info('%s now:%.2f' % (data['name'], now))
                self.log.info('止损价:%.2f 止损百分比:%.2f%% high:%.2f 默认比例:%.2f%%\n' % (zhisun, baifenbi, high, zhisunbili * 100))
            elif now > zhisun2:
                self.log.info('!!!!!!!!!!!!!!! 跌破止损 1 !!!!!!!!!!!!!!!!')
                self.log.info('%s now:%.2f' % (data['name'], now))
                self.log.info('止损价:%.2f 止损百分比:%.2f%% high:%.2f 默认比例:%.2f%%\n' % (zhisun, baifenbi, high, zhisunbili * 100))
                self.log.info('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n')
            else:
                self.log.info('!!!!!!!!!!! 跌破止损 2 !!!!! 危险 !!!!!!!!!!')
                self.log.info('%s now:%.2f' % (data['name'], now))
                self.log.info('止损价:%.2f 止损百分比:%.2f%% high:%.2f 默认比例:%.2f%%\n' % (zhisun2, baifenbi2, high, zhisunbili2 * 100))
                self.log.info('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n')

    def file2dict(self, path):
        with open(path, mode='r', encoding='utf-8') as f:
            return json.load(f) 

    def dict2file(self, path, data):
        with open(path, mode='w', encoding='utf-8') as f:
            json_str = json.dumps(data)
            f.write(json_str)
            f.flush()



