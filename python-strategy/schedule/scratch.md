# Schedule

####  2021-05-21 19:38:32

* json模式
    - 修改保存数据到一个json file中
    - 观察保存数据是否是持仓数据，如果是则直接用持仓数据进行 则省略了创建文件的难点

* mysql 模式

#### 订单管理

1. 把订单流管理用tqsdk做一遍，方便以后:
    - 根据当前持仓 生产订单list，记录报单id。
    - 依据报单顺序
    
#### 2021-05-23 23:07:08

1. 订单工厂，实现对报单控制，用海归策略模拟/实盘测试一下
    - 订单管理能用就好，还缺一个riskcontrol这个用tqsdk自带的
    -  成交ok，订单ok，风控：tqsdk，日志：tqsdk
    - 貌似还是应该用个成交定时器 crontab做一个？目前不做也可以
    - 假设测试成功的话，就直接上高频策略吧 别墨迹了
    
2. 风控，日志 2d

#### 2021-05-24 21:37:18

```
回访
ws://139.196.53.95:27961/t/rmd/front/mobile
回测
wss://otg-sim.shinnytech.com/trade 
仿真
wss://free-api.shinnytech.com/t/nfmd/front/mobile
downLoader:
2021-03-28 12:56:47 -     INFO - 通知: 与 wss://otg-sim.shinnytech.com/trade 的网络连接已建立
2021-03-28 12:56:47 -     INFO - 通知: 与 wss://free-api.shinnytech.com/t/nfmd/front/mobile 的网络连接已建立
```

####  2021-05-25 23:07:45 

1. 日志：用logging做好了，实盘和模拟盘分别存在不同目录下
    - bug:TimedRotatingFileHandler logging这个handle不生效 就比较晕
    - 用test.yml是可以成功的 难道按日切割应该用when:H？
    
2. 风控：受阻:测试账户没法设置风控规则
    - 用Timer每隔60s输出一边规则？
    - 用风控RC控制交易策略，如果发现出问题，则停止交易kill thread
    - 也就是用另一个风控脚本控制
    
---
** TODO: 深度学习之股指期货日内交易策略 复现 **
>> 纵使再努力，也应坦然接受不好的结果。


    

