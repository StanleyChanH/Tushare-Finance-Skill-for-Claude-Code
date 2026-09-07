# 大盘资金流向（DC）

**文档ID**: 345
**原始链接**: https://tushare.pro/document/2?doc_id=345

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

## 大盘资金流向（DC）

---

接口：moneyflow\_mkt\_dc  
描述：获取东方财富大盘资金流向数据，每日盘后更新  
限量：单次最大3000条，可根据日期或日期区间循环获取  
积分：120积分可试用，6000积分可正式调取，具体请参阅[积分获取办法](https://tushare.pro/document/1?doc_id=13)

**输入参数**

| 名称 | 类型 | 必选 | 描述 |
| --- | --- | --- | --- |
| trade\_date | str | N | 交易日期(YYYYMMDD格式，下同） |
| start\_date | str | N | 开始日期 |
| end\_date | str | N | 结束日期 |

**输出参数**

| 名称 | 类型 | 默认显示 | 描述 |
| --- | --- | --- | --- |
| trade\_date | str | Y | 交易日期 |
| close\_sh | float | Y | 上证收盘价（点） |
| pct\_change\_sh | float | Y | 上证涨跌幅(%) |
| close\_sz | float | Y | 深证收盘价（点） |
| pct\_change\_sz | float | Y | 深证涨跌幅(%) |
| net\_amount | float | Y | 今日主力净流入 净额（元） |
| net\_amount\_rate | float | Y | 今日主力净流入净占比% |
| buy\_elg\_amount | float | Y | 今日超大单净流入 净额（元） |
| buy\_elg\_amount\_rate | float | Y | 今日超大单净流入 净占比% |
| buy\_lg\_amount | float | Y | 今日大单净流入 净额（元） |
| buy\_lg\_amount\_rate | float | Y | 今日大单净流入 净占比% |
| buy\_md\_amount | float | Y | 今日中单净流入 净额（元） |
| buy\_md\_amount\_rate | float | Y | 今日中单净流入 净占比% |
| buy\_sm\_amount | float | Y | 今日小单净流入 净额（元） |
| buy\_sm\_amount\_rate | float | Y | 今日小单净流入 净占比% |

**接口示例**

```
#获取当日所有板块资金流向
df = pro.moneyflow_mkt_dc(start_date='20240901', end_date='20240930')
```

**数据示例**

```
     trade_date close_sh ptc_change_sh  close_sz pct_change_sz   buy_elg_amount    buy_lg_amount
0    20240930  3336.50          8.06  10529.76         10.67   -6500884480.00  -29199228928.00
1    20240927  3087.53          2.89   9514.86          6.71   17175101440.00   -3564773376.00
2    20240926  3000.95          3.61   8916.65          4.44   18894807552.00   -2446319616.00
3    20240925  2896.31          1.16   8537.73          1.21   -4010342144.00  -10390331392.00
4    20240924  2863.13          4.15   8435.70          4.36   22524846080.00    5433212928.00
5    20240923  2748.92          0.44   8083.38          0.10    -926530816.00   -5776028928.00
6    20240920  2736.81          0.03   8075.14         -0.15   -4991644160.00   -6899648256.00
7    20240919  2736.02          0.69   8087.60          1.19    3472006400.00    1882220032.00
8    20240918  2717.28          0.49   7992.25          0.11   -5056087040.00   -7836610048.00
9    20240913  2704.09         -0.48   7983.55         -0.88   -5527845376.00   -9092720640.00
10   20240912  2717.12         -0.17   8054.24         -0.63   -3747197184.00   -5645509632.00
11   20240911  2721.80         -0.82   8105.38          0.39   -3585276416.00   -6461025792.00
12   20240910  2744.19          0.28   8073.83          0.13   -2726709504.00   -3818158336.00
13   20240909  2736.49         -1.06   8063.27         -0.83   -7874987776.00   -8608827904.00
14   20240906  2765.81         -0.81   8130.77         -1.44   -5892936960.00  -13908542976.00
15   20240905  2788.31          0.14   8249.66          0.28    1211718400.00   -3910650112.00
16   20240904  2784.28         -0.67   8226.24         -0.51   -7008298240.00  -11212970496.00
17   20240903  2802.98         -0.29   8268.05          1.17     263304192.00   -3680828928.00
18   20240902  2811.04         -1.10   8172.21         -2.11  -18689678336.00  -20967354368.00
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
