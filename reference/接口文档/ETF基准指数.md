# ETF基准指数

**文档ID**: 386
**原始链接**: https://tushare.pro/document/2?doc_id=386

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

## ETF基准指数列表

---

接口：etf\_index  
描述：获取ETF基准指数列表信息  
限量：单次请求最大返回5000行数据（当前未超过2000个）  
权限：用户积累8000积分可调取，具体请参阅[积分获取办法](https://tushare.pro/document/1?doc_id=13)

  
  

**输入参数**

| 名称 | 类型 | 必选 | 描述 |
| --- | --- | --- | --- |
| ts\_code | str | N | 指数代码 |
| pub\_date | str | N | 发布日期（格式：YYYYMMDD） |
| base\_date | str | N | 指数基期（格式：YYYYMMDD） |

  
  

**输出参数**

| 名称 | 类型 | 默认显示 | 描述 |
| --- | --- | --- | --- |
| ts\_code | str | Y | 指数代码 |
| indx\_name | str | Y | 指数全称 |
| indx\_csname | str | Y | 指数简称 |
| pub\_party\_name | str | Y | 指数发布机构 |
| pub\_date | str | Y | 指数发布日期 |
| base\_date | str | Y | 指数基日 |
| bp | float | Y | 指数基点(点) |
| adj\_circle | str | Y | 指数成份证券调整周期 |

  
  

**接口示例**

```
#获取当前ETF跟踪的基准指数列表
df = pro.etf_index(fields='ts_code,indx_name,pub_date,bp')
```

  
  

**数据示例**

```
          ts_code        indx_name         pub_date           bp
0        000068.SH         上证自然资源指数  20100528  1000.000000
1        000001.SH           上证综合指数  19910715   100.000000
2        000989.SH       中证全指可选消费指数  20110802  1000.000000
3       000990.CSI       中证全指主要消费指数  20110802  1000.000000
4        000043.SH         上证超级大盘指数  20090423  1000.000000
...            ...              ...       ...          ...
1458    932368.CSI     中证800自由现金流指数  20241211  1000.000000
1460     000680.SH        上证科创板综合指数  20250120  1000.000000
1461     000681.SH      上证科创板综合价格指数  20250120  1000.000000
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
