# encoding: UTF-8

"""
展示如何执行策略回测。
"""

from __future__ import division
import  os
from Back_test.ctaBacktesting import BacktestingEngine
if __name__ == '__main__':
    from strategy.strategyRSI import AtrRsiStrategy
    print(os.path.abspath(os.getcwd()))
    # 创建回测引擎
    engine = BacktestingEngine()

    # 设置引擎的回测模式为K线
    engine.setBacktestingMode(engine.BAR_MODE)

    # 设置回测用的数据起始日期
    engine.setStartDate('20120101')

    # 设置产品相关参数
    engine.setSlippage(0.2)  # 股指1跳
    engine.setRate(0.3 / 10000)  # 万0.3
    engine.setSize(300)  # 股指合约大小
    engine.setPriceTick(0.2)  # 股指最小价格变动

    # 设置使用的历史数据库
   # engine.setDatabase(MINUTE_DB_NAME, 'IF0000')
   # engine.setDatafile(os.path.join(__file__,)
    # 在引擎中创建策略对象
    d = {'atrLength': 11}
    engine.initStrategy(AtrRsiStrategy, d)

    Data_path = os.path.join(os.getcwd(),'Test_data')   # 获取数据文件夹地址

    file_name = os.path.join(Data_path , 'IF0000_1.min.csv')    # 获取回测数据绝对地址
    engine.setDatafile(file_name)  # file_name为储存的数据文件 ，放在Test_data文件夹中，并且为csv格式
    # 开始跑回测                   #csv必须包含字段
    engine.runBacktesting()

    # 显示回测结果
    engine.showBacktestingResult()