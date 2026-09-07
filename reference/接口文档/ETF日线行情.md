# ETF日线行情

**文档ID**: 127
**原始链接**: https://tushare.pro/document/2?doc_id=127

---

Toggle navigation

#

- [首页](/)
- [平台介绍](/document/1)
- [数据接口](/document/2)
- [资讯数据](/news/sina)
- [数据工具](/webclient)
- [权限中心](/weborder/#/permission)
- [活动套餐](/weborder/#/combo)
- [登录/注册](/weborder/#/login)

- [股票数据](/document/2?doc_id=14)
- [ETF专题](/document/2?doc_id=384)
  - [ETF基本信息](/document/2?doc_id=385)
  - [ETF跟踪指数](/document/2?doc_id=386)
  - [ETF历史分钟](/document/2?doc_id=387)
  - [ETF日线行情](/document/2?doc_id=127)
  - [ETF复权因子](/document/2?doc_id=199)
  - [ETF份额规模](/document/2?doc_id=408)
  - [每日篮子组合(沪市PCF）](/document/2?doc_id=471)
  - [每日篮子组合(深市PCF）](/document/2?doc_id=472)
  - [ETF实时参考](/document/2?doc_id=454)
  - [指数公司公告](/document/2?doc_id=460)
- [指数专题](/document/2?doc_id=93)
- [公募基金](/document/2?doc_id=18)
- [期货数据](/document/2?doc_id=134)
- [现货数据](/document/2?doc_id=283)
- [期权数据](/document/2?doc_id=157)
- [债券专题](/document/2?doc_id=184)
- [外汇数据](/document/2?doc_id=177)
- [港股数据](/document/2?doc_id=190)
- [美股数据](/document/2?doc_id=251)
- [宏观经济](/document/2?doc_id=147)
- [大模型语料](/document/2?doc_id=142)
- [量化因子库](/document/2?doc_id=485)
- [自选组合](/document/2?doc_id=474)

## ETF日线行情

---

接口：fund\_daily  
描述：获取ETF行情每日收盘后成交数据，历史超过10年  
限量：单次最大5000行记录，可以根据ETF代码和日期循环获取历史，总量不限制  
积分：需要至少5000积分才可以调取，8000积分频次更高，具体请参阅[积分获取办法](https://tushare.pro/document/1?doc_id=13)

**输入参数**

| 名称 | 类型 | 必选 | 描述 |
| --- | --- | --- | --- |
| ts\_code | str | N | 基金代码 |
| trade\_date | str | N | 交易日期(YYYYMMDD格式，下同) |
| start\_date | str | N | 开始日期 |
| end\_date | str | N | 结束日期 |

**输出参数**

| 名称 | 类型 | 默认显示 | 描述 |
| --- | --- | --- | --- |
| ts\_code | str | Y | TS代码 |
| trade\_date | str | Y | 交易日期 |
| open | float | Y | 开盘价(元) |
| high | float | Y | 最高价(元) |
| low | float | Y | 最低价(元) |
| close | float | Y | 收盘价(元) |
| pre\_close | float | Y | 昨收盘价(元) |
| change | float | Y | 涨跌额(元) |
| pct\_chg | float | Y | 涨跌幅(%) |
| vol | float | Y | 成交量(手) |
| amount | float | Y | 成交额(千元) |

**接口示例**

```
pro = ts.pro_api()

#获取”沪深300ETF华夏”ETF2025年以来的行情，并通过fields参数指定输出了部分字段
df = pro.fund_daily(ts_code='510330.SH', start_date='20250101', end_date='20250618', fields='trade_date,open,high,low,close,vol,amount')
```

**数据示例**

```
   trade_date   open   high    low  close         vol       amount
0     20250618  4.008  4.024  3.996  4.017   382896.00   153574.446
1     20250617  4.015  4.022  4.000  4.014   440272.04   176617.125
2     20250616  4.000  4.018  3.996  4.015   423526.00   169788.251
3     20250613  4.023  4.028  3.992  4.004  1216787.53   487632.318
4     20250612  4.023  4.039  4.005  4.032   574727.00   231356.321
..         ...    ...    ...    ...    ...         ...          ...
104   20250108  3.971  3.992  3.908  3.963  3200416.00  1267465.456
105   20250107  3.939  3.974  3.929  3.973  2239739.00   885818.954
106   20250106  3.950  3.964  3.917  3.943  1583794.00   624004.760
107   20250103  4.002  4.013  3.944  3.963  2025111.00   805573.289
108   20250102  4.110  4.117  3.973  4.001  1768592.00   714820.885
```

使用文档

- [平台介绍](/document/1)
- [数据接口](/document/2)

关注我们

- 公众号：waditu
- Github：<https://github.com/waditu>
- 微 博：<https://weibo.com/u/1304687120>

© 2026 Tushare     
ICP许可证: 京B2-20262336
[京ICP备2026021642号-2](https://beian.miit.gov.cn)

[京公网安备11011202101917号](http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=11011202101917)
