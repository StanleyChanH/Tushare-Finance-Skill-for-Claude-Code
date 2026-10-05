# 行业资金流向（THS）

**文档ID**: 343
**原始链接**: https://tushare.pro/document/2?doc_id=343

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

## 同花顺行业资金流向（THS）

---

接口：moneyflow\_ind\_ths  
描述：获取同花顺行业资金流向，每日盘后更新  
限量：单次最大可调取5000条数据，可以根据日期和代码循环提取全部数据  
积分：6000积分可以调取，具体请参阅[积分获取办法](https://tushare.pro/document/1?doc_id=13)

**输入参数**

| 名称 | 类型 | 必选 | 描述 |
| --- | --- | --- | --- |
| ts\_code | str | N | 代码 |
| trade\_date | str | N | 交易日期(YYYYMMDD格式，下同) |
| start\_date | str | N | 开始日期 |
| end\_date | str | N | 结束日期 |

**输出参数**

| 名称 | 类型 | 默认显示 | 描述 |
| --- | --- | --- | --- |
| trade\_date | str | Y | 交易日期 |
| ts\_code | str | Y | 板块代码 |
| industry | str | Y | 板块名称 |
| lead\_stock | str | Y | 领涨股票名称 |
| close | float | Y | 收盘指数 |
| pct\_change | float | Y | 指数涨跌幅 |
| company\_num | int | Y | 公司数量 |
| pct\_change\_stock | float | Y | 领涨股涨跌幅 |
| close\_price | float | Y | 领涨股最新价 |
| net\_buy\_amount | float | Y | 流入资金(亿元) |
| net\_sell\_amount | float | Y | 流出资金(亿元) |
| net\_amount | float | Y | 净额(亿元) |

**接口示例**

```
#获取当日所有同花顺行业资金流向
df = pro.moneyflow_ind_ths(trade_date='20240927')
```

**数据示例**

```
  trade_date   ts_code industry     close  company_num net_buy_amount net_sell_amount net_amount
0    20240927  881267.TI     能源金属  15021.70           16         490.00           46.00       3.00
1    20240927  881273.TI       白酒   3251.85           20        1890.00          179.00      10.00
2    20240927  881279.TI     光伏设备   5940.19           70        1120.00           94.00      17.00
3    20240927  881157.TI       证券   1407.41           50        3680.00          319.00      49.00
4    20240927  877137.TI     软件开发   1375.49          137        2260.00          204.00      22.00
..        ...        ...      ...       ...          ...            ...             ...        ...
85   20240927  881148.TI     港口航运    901.87           37         190.00           20.00      -1.00
86   20240927  881105.TI   煤炭开采加工   2271.57           34         220.00           26.00      -4.00
87   20240927  881169.TI      贵金属   2141.46           12         240.00           32.00      -8.00
88   20240927  881149.TI   公路铁路运输   1224.59           31         210.00           29.00      -7.00
89   20240927  877035.TI       银行   1080.14           84        1190.00          159.00     -40.00

[90 rows x 8 columns]
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
