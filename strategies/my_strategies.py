from easyquant import StrategyTemplate
import json


class Strategy(StrategyTemplate):
    name = 'zhisun策略'

    def strategy(self, event):
        self.log.info('--------------------------------')
        self.config = self.file2dict('config.json')
        for key in self.config.keys():
            zhisun = float(self.config[key])
            data = event.data[key]
            now = float(data['now'])
            high = float(data['high'])

            if high * 0.91 > zhisun:
                self.config[key] = str(high * 0.91)
                self.dict2file('config.json', self.config)

            baifenbi = (1 - zhisun / now) * 100.0
            if now > zhisun:
                self.log.info('%s now:%.2f' % (data['name'], now))
                self.log.info('止损价:%.2f 止损百分比:%.2f%% high:%.2f\n' % (zhisun, baifenbi, high))
            else:
                self.log.info('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                self.log.info('%s now:%.2f' % (data['name'], now))
                self.log.info('止损价:%.2f 止损百分比:%.2f%% high:%.2f' % (zhisun, baifenbi, high))
                self.log.info('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n')

    def file2dict(self, path):
        with open(path, mode='r', encoding='utf-8') as f:
            return json.load(f) 

    def dict2file(self, path, data):
        with open(path, mode='w', encoding='utf-8') as f:
            json_str = json.dumps(data)
            f.write(json_str)
            f.flush()



