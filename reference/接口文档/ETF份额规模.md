# ETF份额规模

**文档ID**: 408
**原始链接**: https://tushare.pro/document/2?doc_id=408

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

# ETF份额规模

### 接口介绍

接口：etf\_share\_size  
描述：获取沪深ETF每日份额和规模数据，能体现规模份额的变化，掌握ETF资金动向，同时提供每日净值和收盘价；数据指标是分批入库，交易所于次日早8点30左右更新上一交易日的数据；另外，涉及海外的ETF数据更新会晚一些属于正常情况。  
限量：单次最大5000条，可根据代码或日期循环提取  
积分：需要8000积分可以调取，具体请参阅[积分获取办法](https://tushare.pro/document/1?doc_id=13)

### 输入参数

| 名称 | 类型 | 必选 | 描述 |
| --- | --- | --- | --- |
| ts\_code | str | N | 基金代码 （可从ETF基础信息接口提取） |
| trade\_date | str | N | 交易日期（YYYYMMDD格式，下同） |
| start\_date | str | N | 开始日期 |
| end\_date | str | N | 结束日期 |
| exchange | str | N | 交易所（SSE上交所 SZSE深交所） |

### 输出参数

| 名称 | 类型 | 默认显示 | 描述 |
| --- | --- | --- | --- |
| trade\_date | str | Y | 交易日期 |
| ts\_code | str | Y | ETF代码 |
| etf\_name | str | Y | 基金名称 |
| total\_share | float | Y | 总份额（万份） |
| total\_size | float | Y | 总规模（万元） |
| nav | float | N | 基金份额净值(元) |
| close | float | N | 收盘价（元） |
| exchange | str | Y | 交易所（SSE上交所 SZSE深交所 BSE北交所） |

### 代码示例

```
#获取”沪深300ETF华夏”ETF2025年以来每个交易日的份额和规模情况
df = pro.etf_share_size(ts_code='510330.SH', start_date='20250101', end_date='20251224')

#获取2025年12月24日上交所的所有ETF份额和规模情况
df = pro.etf_share_size(trade_date='20251224', exchange='SSE')
```

### 数据结果

```
    trade_date    ts_code       etf_name  total_share    total_size exchange
0     20251224  510330.SH  沪深300ETF华夏   4741854.98  2.287898e+07      SSE
1     20251222  510330.SH  沪深300ETF华夏   4746894.98  2.279127e+07      SSE
2     20251219  510330.SH  沪深300ETF华夏   4756974.98  2.262512e+07      SSE
3     20251218  510330.SH  沪深300ETF华夏   4757514.98  2.253778e+07      SSE
4     20251217  510330.SH  沪深300ETF华夏   4756884.98  2.266418e+07      SSE
..         ...        ...         ...          ...           ...      ...
232   20250108  510330.SH  沪深300ETF华夏   4032384.98  1.599808e+07      SSE
233   20250107  510330.SH  沪深300ETF华夏   4009164.98  1.592962e+07      SSE
234   20250106  510330.SH  沪深300ETF华夏   3999084.98  1.577239e+07      SSE
235   20250103  510330.SH  沪深300ETF华夏   3994674.98  1.578176e+07      SSE
236   20250102  510330.SH  沪深300ETF华夏   3986754.98  1.593905e+07      SSE
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
