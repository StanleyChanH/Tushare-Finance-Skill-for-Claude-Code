# 个股资金流向（DC）

**文档ID**: 349
**原始链接**: https://tushare.pro/document/2?doc_id=349

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

## 个股资金流向（DC）

---

接口：moneyflow\_dc  
描述：获取东方财富个股资金流向数据，每日盘后更新，数据开始于20230911  
限量：单次最大获取6000条数据，可根据日期或股票代码循环提取数据  
积分：用户需要至少5000积分才可以调取，具体请参阅[积分获取办法](https://tushare.pro/document/1?doc_id=13)

  
  

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
| close | float | Y | 最新价 |
| net\_amount | float | Y | 今日主力净流入额（万元） |
| net\_amount\_rate | float | Y | 今日主力净流入净占比（%） |
| buy\_elg\_amount | float | Y | 今日超大单净流入额（万元） |
| buy\_elg\_amount\_rate | float | Y | 今日超大单净流入占比（%） |
| buy\_lg\_amount | float | Y | 今日大单净流入额（万元） |
| buy\_lg\_amount\_rate | float | Y | 今日大单净流入占比（%） |
| buy\_md\_amount | float | Y | 今日中单净流入额（万元） |
| buy\_md\_amount\_rate | float | Y | 今日中单净流入占比（%） |
| buy\_sm\_amount | float | Y | 今日小单净流入额（万元） |
| buy\_sm\_amount\_rate | float | Y | 今日小单净流入占比（%） |

  
  

**接口示例**

```
pro = ts.pro_api()

#获取单日全部股票数据
df = pro.moneyflow_dc(trade_date='20241011')

#获取单个股票数据
df = pro.moneyflow_dc(ts_code='002149.SZ', start_date='20240901', end_date='20240913')
```

  
  

```
    trade_date ts_code  name  pct_change  ...  buy_md_amount  buy_md_amount_rate  buy_sm_amount  buy_sm_amount_rate
0   20240913  002149.SZ  西部材料       -1.34  ...         -12.65               -0.35         -62.43               -1.72
1   20240912  002149.SZ  西部材料        1.43  ...          13.71                0.33        -388.43               -9.25
2   20240911  002149.SZ  西部材料       -0.79  ...         -26.10               -1.68          95.69                6.15
3   20240910  002149.SZ  西部材料       -0.08  ...        -199.50               -7.26         -69.29               -2.52
4   20240909  002149.SZ  西部材料        1.12  ...          66.76                2.48        -198.12               -7.37
5   20240906  002149.SZ  西部材料       -2.49  ...        -104.57               -2.74         769.65               20.19
6   20240905  002149.SZ  西部材料       -0.70  ...        -307.62               -8.11         346.51                9.14
7   20240904  002149.SZ  西部材料       -0.92  ...         370.98                9.56         -23.25               -0.60
8   20240903  002149.SZ  西部材料        0.93  ...        -195.45               -3.87         643.41               12.75
9   20240902  002149.SZ  西部材料       -3.44  ...         195.50                2.32         988.69               11.71
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
