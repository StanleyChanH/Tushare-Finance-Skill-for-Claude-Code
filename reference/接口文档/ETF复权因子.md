# ETF复权因子

**文档ID**: 199
**原始链接**: https://tushare.pro/document/2?doc_id=199

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

## 基金复权因子

---

接口：fund\_adj  
描述：获取基金复权因子，用于计算基金复权行情  
限量：单次最大提取2000行记录，可循环提取，数据总量不限制  
积分：用户积2000积分可调取，超过5000积分以上频次相对较高。具体请参阅[积分获取办法](https://tushare.pro/document/1?doc_id=13)

**输入参数**

| 名称 | 类型 | 必选 | 描述 |
| --- | --- | --- | --- |
| ts\_code | str | N | TS基金代码（支持多只基金输入） |
| trade\_date | str | N | 交易日期（格式：yyyymmdd，下同） |
| start\_date | str | N | 开始日期 |
| end\_date | str | N | 结束日期 |
| offset | str | N | 开始行数 |
| limit | str | N | 最大行数 |

**输出参数**

| 名称 | 类型 | 默认显示 | 描述 |
| --- | --- | --- | --- |
| ts\_code | str | Y | ts基金代码 |
| trade\_date | str | Y | 交易日期 |
| adj\_factor | float | Y | 复权因子 |

**接口使用**

```
pro = ts.pro_api()

df = pro.fund_adj(ts_code='513100.SH', start_date='20190101', end_date='20190926')
```

**数据示例**

```
     ts_code    trade_date  adj_factor
0    513100.SH   20190926         1.0
1    513100.SH   20190925         1.0
2    513100.SH   20190924         1.0
3    513100.SH   20190923         1.0
4    513100.SH   20190920         1.0
5    513100.SH   20190919         1.0
6    513100.SH   20190918         1.0
7    513100.SH   20190917         1.0
8    513100.SH   20190916         1.0
9    513100.SH   20190912         1.0
10   513100.SH   20190911         1.0
11   513100.SH   20190910         1.0
12   513100.SH   20190909         1.0
13   513100.SH   20190906         1.0
14   513100.SH   20190905         1.0
15   513100.SH   20190904         1.0
16   513100.SH   20190903         1.0
17   513100.SH   20190902         1.0
18   513100.SH   20190830         1.0
19   513100.SH   20190829         1.0
20   513100.SH   20190828         1.0
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
