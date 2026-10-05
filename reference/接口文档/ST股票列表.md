# ST股票列表

**文档ID**: 397
**原始链接**: https://tushare.pro/document/2?doc_id=397

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
    - [股票列表](/document/2?doc_id=25)
    - [每日股本（盘前）](/document/2?doc_id=329)
    - [交易日历](/document/2?doc_id=26)
    - [ST股票列表](/document/2?doc_id=397)
    - [ST风险警示板股票](/document/2?doc_id=423)
    - [沪深港通股票列表](/document/2?doc_id=398)
    - [股票曾用名](/document/2?doc_id=100)
    - [上市公司基本信息](/document/2?doc_id=112)
    - [上市公司管理层](/document/2?doc_id=193)
    - [管理层薪酬和持股](/document/2?doc_id=194)
    - [北交所新旧代码对照](/document/2?doc_id=375)
    - [IPO新股上市](/document/2?doc_id=123)
    - [股票历史列表](/document/2?doc_id=262)
  - [行情数据](/document/2?doc_id=15)
  - [财务数据](/document/2?doc_id=16)
  - [参考数据](/document/2?doc_id=17)
  - [特色数据](/document/2?doc_id=291)
  - [两融及转融通](/document/2?doc_id=330)
  - [资金流向数据](/document/2?doc_id=342)
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

## ST股票列表

---

接口：stock\_st，可以通过[**数据工具**](https://tushare.pro/webclient/)调试和查看数据。  
描述：获取ST股票列表，可根据交易日期获取历史上每天的ST列表  
权限：3000积分起  
提示：每天上午9:20更新，单次请求最大返回1000行数据，可循环提取,本接口数据从20000101开始,太早历史无法补齐

**输入参数**

| 名称 | 类型 | 必选 | 描述 |
| --- | --- | --- | --- |
| ts\_code | str | N | 股票代码 |
| trade\_date | str | N | 交易日期（格式：YYYYMMDD下同） |
| start\_date | str | N | 开始时间 |
| end\_date | str | N | 结束时间 |

**输出参数**

| 名称 | 类型 | 默认显示 | 描述 |
| --- | --- | --- | --- |
| ts\_code | str | Y | 股票代码 |
| name | str | Y | 股票名称 |
| trade\_date | str | Y | 交易日期 |
| type | str | Y | 类型 |
| type\_name | str | Y | 类型名称 |

**接口用法**

```
pro = ts.pro_api()

#获取20250813日所有的ST股票
df = pro.stock_st(trade_date='20250813')
```

**数据样例**

```
             ts_code   name trade_date type type_name
0    300313.SZ  *ST天山   20250813   ST     风险警示板
1    605081.SH  *ST太和   20250813   ST     风险警示板
2    300391.SZ  *ST长药   20250813   ST     风险警示板
3    300343.SZ   ST联创   20250813   ST     风险警示板
4    300044.SZ   ST赛为   20250813   ST     风险警示板
..         ...    ...        ...  ...       ...
170  300175.SZ   ST朗源   20250813   ST     风险警示板
171  603721.SH  *ST天择   20250813   ST     风险警示板
172  600289.SH   ST信通   20250813   ST     风险警示板
173  000929.SZ  *ST兰黄   20250813   ST     风险警示板
174  000638.SZ  *ST万方   20250813   ST     风险警示板
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
