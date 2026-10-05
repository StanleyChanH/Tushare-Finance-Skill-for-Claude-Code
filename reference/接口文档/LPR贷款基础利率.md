# LPR贷款基础利率

**文档ID**: 151
**原始链接**: https://tushare.pro/document/2?doc_id=151

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
  - [国内宏观](/document/2?doc_id=224)
    - [中国经济数据发布日程](/document/2?doc_id=461)
    - [利率数据](/document/2?doc_id=148)
      - [Shibor利率](/document/2?doc_id=149)
      - [Shibor报价数据](/document/2?doc_id=150)
      - [LPR贷款基础利率](/document/2?doc_id=151)
      - [Libor利率](/document/2?doc_id=152)
      - [Hibor利率](/document/2?doc_id=153)
      - [温州民间借贷利率](/document/2?doc_id=173)
      - [广州民间借贷利率](/document/2?doc_id=174)
    - [国民经济](/document/2?doc_id=225)
    - [价格指数](/document/2?doc_id=226)
    - [金融](/document/2?doc_id=240)
    - [景气度](/document/2?doc_id=324)
  - [国际宏观](/document/2?doc_id=217)
- [大模型语料](/document/2?doc_id=142)
- [量化因子库](/document/2?doc_id=485)
- [自选组合](/document/2?doc_id=474)

## LPR贷款基础利率

---

接口：shibor\_lpr  
描述：LPR贷款基础利率  
限量：单次最大4000(相当于单次可提取18年历史)，总量不限制，可通过设置开始和结束日期分段获取  
积分：用户积累120积分可以调取，具体请参阅[积分获取办法](https://tushare.pro/document/1?doc_id=13)

  

**LPR介绍**

> 贷款基础利率（Loan Prime Rate，简称LPR），是基于报价行自主报出的最优贷款利率计算并发布的贷款市场参考利率。目前，对社会公布1年期贷款基础利率。
>
> LPR报价银行团现由10家商业银行组成。报价银行应符合财务硬约束条件和宏观审慎政策框架要求，系统重要性程度高、市场影响力大、综合实力强，已建立内部收益率曲线和内部转移定价机制，具有较强的自主定价能力，已制定本行贷款基础利率管理办法，以及有利于开展报价工作的其他条件。市场利率定价自律机制依据《贷款基础利率集中报价和发布规则》确定和调整报价行成员，监督和管理贷款基础利率运行，规范报价行与指定发布人行为。
>
> 全国银行间同业拆借中心受权贷款基础利率的报价计算和信息发布。每个交易日根据各报价行的报价，剔除最高、最低各1家报价，对其余报价进行加权平均计算后，得出贷款基础利率报价平均利率，并于11:30对外发布。

  

**输入参数**

| 名称 | 类型 | 必选 | 描述 |
| --- | --- | --- | --- |
| date | str | N | 日期 (日期输入格式：YYYYMMDD，下同) |
| start\_date | str | N | 开始日期 |
| end\_date | str | N | 结束日期 |

  

**输出参数**

| 名称 | 类型 | 默认显示 | 描述 |
| --- | --- | --- | --- |
| date | str | Y | 日期 |
| 1y | float | Y | 1年贷款利率 |
| 5y | float | Y | 5年贷款利率 |

  

**接口调用**

```
pro = ts.pro_api()

df = pro.shibor_lpr(start_date='20180101', end_date='20181130', fields='date,1y')
```

  

**数据样例**

```
     date       1y
0    20181130  4.31
1    20181129  4.31
2    20181128  4.31
3    20181127  4.31
4    20181126  4.31
5    20181123  4.31
6    20181122  4.31
7    20181121  4.31
8    20181120  4.31
9    20181119  4.31
10   20181116  4.31
11   20181115  4.31
12   20181114  4.31
13   20181113  4.31
14   20181112  4.31
15   20181109  4.31
16   20181108  4.31
17   20181107  4.31
18   20181106  4.31
19   20181105  4.31
20   20181102  4.31
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
