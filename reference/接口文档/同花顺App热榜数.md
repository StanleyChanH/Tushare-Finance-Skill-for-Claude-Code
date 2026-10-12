# 同花顺App热榜数

**文档ID**: 320
**原始链接**: https://tushare.pro/document/2?doc_id=320

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
  - [打板专题数据](/document/2?doc_id=346)
    - [龙虎榜每日统计单](/document/2?doc_id=106)
    - [龙虎榜机构交易单](/document/2?doc_id=107)
    - [THS涨跌停榜单](/document/2?doc_id=355)
    - [涨跌停和炸板数据](/document/2?doc_id=298)
    - [涨停股票连板天梯](/document/2?doc_id=356)
    - [涨停最强板块统计](/document/2?doc_id=357)
    - [THS概念板块分类](/document/2?doc_id=259)
    - [THS概念板块行情](/document/2?doc_id=260)
    - [THS概念板块成分](/document/2?doc_id=261)
    - [DC概念板块分类](/document/2?doc_id=362)
    - [DC概念板块成分](/document/2?doc_id=363)
    - [DC概念板块行情](/document/2?doc_id=382)
    - [开盘竞价成交（当日）](/document/2?doc_id=369)
    - [市场游资最全名录](/document/2?doc_id=311)
    - [游资交易每日明细](/document/2?doc_id=312)
    - [THS热榜](/document/2?doc_id=320)
    - [DC热榜](/document/2?doc_id=321)
    - [TDX概念板块分类](/document/2?doc_id=376)
    - [TDX概念板块成分](/document/2?doc_id=377)
    - [TDX概念板块行情](/document/2?doc_id=378)
    - [榜单数据（KP）](/document/2?doc_id=347)
    - [题材成分（KP）](/document/2?doc_id=351)
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

## THS热榜

---

接口：ths\_hot  
描述：获取热榜数据，包括热股、概念板块、ETF、可转债、港美股等等，每日盘中提取4次，收盘后4次，最晚22点提取一次。  
限量：单次最大2000条，可根据日期等参数循环获取全部数据  
积分：用户积6000积分可调取使用，积分获取办法请参阅[积分获取办法](https://tushare.pro/document/1?doc_id=13)

**输入参数**

| 名称 | 类型 | 必选 | 描述 |
| --- | --- | --- | --- |
| trade\_date | str | N | 交易日期 |
| ts\_code | str | N | TS代码 |
| market | str | N | 热榜类型(热股、ETF、可转债、行业板块、概念板块、期货、港股、热基、美股) |
| is\_new | str | N | 是否最新（默认Y，如果为N则为盘中和盘后阶段采集，具体时间可参考rank\_time字段，***状态N每2小时更新一次***，***状态Y更新时间为22：30***） |

**输出参数**

| 名称 | 类型 | 默认显示 | 描述 |
| --- | --- | --- | --- |
| trade\_date | str | Y | 交易日期 |
| data\_type | str | Y | 数据类型 |
| ts\_code | str | Y | 股票代码 |
| ts\_name | str | Y | 股票名称 |
| rank | int | Y | 排行 |
| pct\_change | float | Y | 涨跌幅% |
| current\_price | float | Y | 当前价格 |
| concept | str | Y | 标签 |
| rank\_reason | str | Y | 上榜解读 |
| hot | float | Y | 热度值 |
| rank\_time | str | Y | 排行榜获取时间 |

**接口示例**

```
#获取查询月份券商金股
df = pro.ths_hot(trade_date='20240315', market='热股', is_new='N', fields='ts_code,ts_name,hot,concept')
```

**数据示例**

```
        ts_code ts_name       hot                  concept
0   300750.SZ    宁德时代  214462.0    ["钠离子电池", "同花顺漂亮100"]
1   603580.SH    艾艾精工  185431.0     ["人民币贬值受益", "台湾概念股"]
2   002085.SZ    万丰奥威  180332.0  ["飞行汽车(eVTOL)", "低空经济"]
3   600733.SH    北汽蓝谷  156000.0        ["一体化压铸", "华为汽车"]
4   603259.SH    药明康德  154360.0         ["CRO概念", "创新药"]
..        ...     ...       ...                      ...
95  300735.SZ    光弘科技   28528.0        ["智能穿戴", "EDR概念"]
96  002632.SZ    道明光学   28101.0       ["AI手机", "消费电子概念"]
97  601086.SH    国芳集团   28006.0          ["新零售", "网络直播"]
98  002406.SZ    远东传动   28003.0        ["工业互联网", "智能制造"]
99  600160.SH    巨化股份   27979.0      ["PVDF概念", "氟化工概念"]
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
