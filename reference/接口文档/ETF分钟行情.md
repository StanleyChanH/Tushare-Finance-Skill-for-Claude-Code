# ETF分钟行情

**文档ID**: 387
**原始链接**: https://tushare.pro/document/2?doc_id=387

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

## ETF历史分钟行情

---

接口：etf\_mins  
描述：获取ETF分钟数据，支持1min/5min/15min/30min/60min行情，提供Python SDK和 http Restful API两种方式  
限量：单次最大8000行数据，可以通过股票代码和时间循环获取，本接口可以提供超过10年ETF历史分钟数据  
权限：正式权限请参阅 [权限说明](https://tushare.pro/document/1?doc_id=290)

**输入参数**

| 名称 | 类型 | 必选 | 描述 |
| --- | --- | --- | --- |
| ts\_code | str | Y | ETF代码，e.g. 159001.SZ |
| freq | str | Y | 分钟频度（1min/5min/15min/30min/60min） |
| start\_date | datetime | N | 开始日期 格式：2025-06-01 09:00:00 |
| end\_date | datetime | N | 结束时间 格式：2025-06-20 19:00:00 |

**freq参数说明**

| freq | 说明 |
| --- | --- |
| 1min | 1分钟 |
| 5min | 5分钟 |
| 15min | 15分钟 |
| 30min | 30分钟 |
| 60min | 60分钟 |

**输出参数**

| 名称 | 类型 | 默认显示 | 描述 |
| --- | --- | --- | --- |
| ts\_code | str | Y | ETF代码 |
| trade\_time | str | Y | 交易时间 |
| open | float | Y | 开盘价 |
| close | float | Y | 收盘价 |
| high | float | Y | 最高价 |
| low | float | Y | 最低价 |
| vol | int | Y | 成交量（股） |
| amount | float | Y | 成交金额（元） |

**接口用法**

```
pro = ts.pro_api()

#获取沪深300ETF华夏510330.SH的历史分钟数据
df = pro.etf_mins(ts_code='510330.SH', freq='1min', start_date='2025-06-20 09:00:00', end_date='2025-06-20 19:00:00')
```

**数据样例**

```
       ts_code           trade_time  close   open   high    low        vol      amount
0    510330.SH  2025-06-20 15:00:00  3.991  3.991  3.992  3.990   800600.0   3194805.0
1    510330.SH  2025-06-20 14:59:00  3.991  3.990  3.991  3.989   182500.0    728177.0
2    510330.SH  2025-06-20 14:58:00  3.990  3.992  3.992  3.990   113700.0    453763.0
3    510330.SH  2025-06-20 14:57:00  3.992  3.992  3.992  3.991    17400.0     69460.0
4    510330.SH  2025-06-20 14:56:00  3.992  3.992  3.992  3.991   447500.0   1786373.0
..         ...                  ...    ...    ...    ...    ...        ...         ...
236  510330.SH  2025-06-20 09:34:00  3.994  3.994  3.995  3.994  2528100.0  10097818.0
237  510330.SH  2025-06-20 09:33:00  3.994  3.991  3.994  3.991   143300.0    572084.0
238  510330.SH  2025-06-20 09:32:00  3.992  3.990  3.993  3.990  1118500.0   4463264.0
239  510330.SH  2025-06-20 09:31:00  3.988  3.984  3.992  3.984  1176100.0   4691600.0
240  510330.SH  2025-06-20 09:30:00  3.983  3.983  3.983  3.983    20700.0     82448.0
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
