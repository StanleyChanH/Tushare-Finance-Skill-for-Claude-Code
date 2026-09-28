# AH股比价

**文档ID**: 399
**原始链接**: https://tushare.pro/document/2?doc_id=399

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
    - [券商盈利预测数据](/document/2?doc_id=292)
    - [每日筹码及胜率](/document/2?doc_id=293)
    - [每日筹码分布](/document/2?doc_id=294)
    - [股票技术面因子](/document/2?doc_id=296)
    - [股票技术面因子(专业版）](/document/2?doc_id=328)
    - [股票开盘集合竞价数据](/document/2?doc_id=353)
    - [股票收盘集合竞价数据](/document/2?doc_id=354)
    - [神奇九转指标](/document/2?doc_id=364)
    - [AH股比价](/document/2?doc_id=399)
    - [机构调研数据](/document/2?doc_id=275)
    - [券商月度金股](/document/2?doc_id=267)
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

## AH股比价

---

接口：stk\_ah\_comparison，可以通过[**数据工具**](https://tushare.pro/webclient/)调试和查看数据。  
描述：AH股比价数据，可根据交易日期获取历史  
权限：5000积分起  
提示：每天盘后17:00更新，单次请求最大返回1000行数据，可循环提取,本接口数据从20250812开始，由于历史不好补充，只能累积

  
  

**输入参数**

| 名称 | 类型 | 必选 | 描述 |
| --- | --- | --- | --- |
| hk\_code | str | N | 港股股票代码（xxxxx.HK) |
| ts\_code | str | N | A股票代码(xxxxxx.SH/SZ/BJ) |
| trade\_date | str | N | 交易日期（格式：YYYYMMDD下同） |
| start\_date | str | N | 开始日期 |
| end\_date | str | N | 结束日期 |

  
  

**输出参数**

| 名称 | 类型 | 默认显示 | 描述 |
| --- | --- | --- | --- |
| hk\_code | str | Y | 港股股票代码 |
| ts\_code | str | Y | A股股票代码 |
| trade\_date | str | Y | 交易日期 |
| hk\_name | str | Y | 港股股票名称 |
| hk\_pct\_chg | float | Y | 港股股票涨跌幅 |
| hk\_close | float | Y | 港股股票收盘价 |
| name | str | Y | A股股票名称 |
| close | float | Y | A股股票收盘价 |
| pct\_chg | float | Y | A股股票涨跌幅 |
| ah\_comparison | float | Y | 比价(A/H) |
| ah\_premium | float | Y | 溢价(A/H)% |

  
  

**接口用法**

```
pro = ts.pro_api()

#获取20250812日所有的AH股比价数据
df = pro.stk_ah_comparison(trade_date='20250812')
```

  
  

**数据样例**

```
            hk_code    ts_code trade_date   hk_name  hk_pct_chg  hk_close  name  close  pct_chg  ah_comparison  ah_premium
0    02068.HK  601068.SH   20250812      中铝国际        0.78      2.60  中铝国际   5.14     0.00           2.16      115.84
1    03993.HK  603993.SH   20250812      洛阳钼业        0.60     10.07  洛阳钼业   9.85     0.31           1.07        6.80
2    06066.HK  601066.SH   20250812    中信建投证券        1.77     13.25  中信建投  26.09     0.66           2.15      114.99
3    06680.HK  300748.SZ   20250812      金力永磁       -5.67     18.30  金力永磁  27.30    -3.05           1.63       62.88
4    02333.HK  601633.SH   20250812      长城汽车        3.55     14.60  长城汽车  22.93     1.82           1.71       71.48
..        ...        ...        ...       ...         ...       ...   ...    ...      ...            ...         ...
155  06196.HK  002936.SZ   20250812      郑州银行        1.41      1.44  郑州银行   2.10     0.48           1.59       59.22
156  06818.HK  601818.SH   20250812    中国光大银行        1.61      3.78  光大银行   4.10     0.99           1.18       18.43
157  06693.HK  600988.SH   20250812      赤峰黄金        1.76     25.44  赤峰黄金  24.58     0.24           1.05        5.49
158  02196.HK  600196.SH   20250812      复星医药        2.22     19.77  复星医药  27.70     3.36           1.53       52.98
159  01065.HK  600874.SH   20250812  天津创业环保股份        2.24      4.10  创业环保   6.01     0.00           1.60       60.05
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
