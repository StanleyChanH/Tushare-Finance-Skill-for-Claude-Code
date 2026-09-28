# 个股资金流向（THS）

**文档ID**: 348
**原始链接**: https://tushare.pro/document/2?doc_id=348

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
  - [基础数据](/document/2?doc_id=24)
  - [行情数据](/document/2?doc_id=15)
  - [财务数据](/document/2?doc_id=16)
  - [参考数据](/document/2?doc_id=17)
  - [特色数据](/document/2?doc_id=291)
  - [两融及转融通](/document/2?doc_id=330)
  - [资金流向数据](/document/2?doc_id=342)
    - [个股资金流向](/document/2?doc_id=170)
    - [个股资金流向（THS）](/document/2?doc_id=348)
    - [个股资金流向（DC）](/document/2?doc_id=349)
    - [板块资金流向（THS)](/document/2?doc_id=371)
    - [行业资金流向（THS）](/document/2?doc_id=343)
    - [板块资金流向（DC）](/document/2?doc_id=344)
    - [大盘资金流向（DC）](/document/2?doc_id=345)
  - [打板专题数据](/document/2?doc_id=346)
- [ETF专题](/document/2?doc_id=384)
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

## 个股资金流向（THS）

---

接口：moneyflow\_ths  
描述：获取同花顺个股资金流向数据，每日盘后更新  
限量：单次最大6000，可根据日期或股票代码循环提取数据  
积分：6000积分可调取，具体请参阅[积分获取办法](https://tushare.pro/document/1?doc_id=13)

**输入参数**

| 名称 | 类型 | 必选 | 描述 |
| --- | --- | --- | --- |
| ts\_code | str | N | 股票代码 |
| trade\_date | str | N | 交易日期（YYYYMMDD格式，下同） |
| start\_date | str | N | 开始日期 |
| end\_date | str | N | 结束日期 |

**输出参数**

| 名称 | 类型 | 默认显示 | 描述 |
| --- | --- | --- | --- |
| trade\_date | str | Y | 交易日期 |
| ts\_code | str | Y | 股票代码 |
| name | str | Y | 股票名称 |
| pct\_change | float | Y | 涨跌幅 |
| latest | float | Y | 最新价 |
| net\_amount | float | Y | 资金净流入(万元) |
| net\_d5\_amount | float | Y | 5日主力净额(万元) |
| buy\_lg\_amount | float | Y | 今日大单净流入额(万元) |
| buy\_lg\_amount\_rate | float | Y | 今日大单净流入占比(%) |
| buy\_md\_amount | float | Y | 今日中单净流入额(万元) |
| buy\_md\_amount\_rate | float | Y | 今日中单净流入占比(%) |
| buy\_sm\_amount | float | Y | 今日小单净流入额(万元) |
| buy\_sm\_amount\_rate | float | Y | 今日小单净流入占比(%) |

**接口示例**

```
pro = ts.pro_api()

#获取单日全部股票数据
df = pro.moneyflow_ths(trade_date='20241011')

#获取单个股票数据
df = pro.moneyflow_ths(ts_code='002149.SZ', start_date='20241001', end_date='20241011')
```

```
trade_date ts_code  name  pct_change  ...  buy_md_amount  buy_md_amount_rate  buy_sm_amount  buy_sm_amount_rate
0   20241011  002149.SZ  西部材料        2.47  ...         -589.0                5.43         -191.0                1.76
1   20241010  002149.SZ  西部材料        1.22  ...        -2732.0               15.38        -1031.0                5.81
2   20241009  002149.SZ  西部材料        7.00  ...        -1941.0                9.25        -2079.0                9.90
3   20241008  002149.SZ  西部材料        5.17  ...        -2985.0                7.93        -2507.0                6.66
```

注：由于源头数据调整，从2027-07-06开始不在提供5日主力净额和占比数据。

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
