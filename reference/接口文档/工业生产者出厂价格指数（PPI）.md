# 工业生产者出厂价格指数（PPI）

**文档ID**: 245
**原始链接**: https://tushare.pro/document/2?doc_id=245

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
    - [国民经济](/document/2?doc_id=225)
    - [价格指数](/document/2?doc_id=226)
      - [居民消费价格指数（CPI）](/document/2?doc_id=228)
      - [工业生产者出厂价格指数（PPI）](/document/2?doc_id=245)
    - [金融](/document/2?doc_id=240)
    - [景气度](/document/2?doc_id=324)
  - [国际宏观](/document/2?doc_id=217)
- [大模型语料](/document/2?doc_id=142)
- [量化因子库](/document/2?doc_id=485)
- [自选组合](/document/2?doc_id=474)

## 工业生产者出厂价格指数

---

接口：cn\_ppi  
描述：获取PPI工业生产者出厂价格指数数据  
限量：单次最大5000，一次可以提取全部数据  
权限：用户600积分可以使用，具体请参阅[积分获取办法](https://tushare.pro/document/1?doc_id=13)

**输入参数**

| 名称 | 类型 | 必选 | 描述 |
| --- | --- | --- | --- |
| m | str | N | 月份（YYYYMM，下同），支持多个月份同时输入，逗号分隔 |
| start\_m | str | N | 开始月份 |
| end\_m | str | N | 结束月份 |

**输出参数**

| 名称 | 类型 | 默认显示 | 描述 |
| --- | --- | --- | --- |
| month | str | Y | 月份YYYYMM |
| ppi\_yoy | float | Y | PPI：全部工业品：当月同比 |
| ppi\_mp\_yoy | float | Y | PPI：生产资料：当月同比 |
| ppi\_mp\_qm\_yoy | float | Y | PPI：生产资料：采掘业：当月同比 |
| ppi\_mp\_rm\_yoy | float | Y | PPI：生产资料：原料业：当月同比 |
| ppi\_mp\_p\_yoy | float | Y | PPI：生产资料：加工业：当月同比 |
| ppi\_cg\_yoy | float | Y | PPI：生活资料：当月同比 |
| ppi\_cg\_f\_yoy | float | Y | PPI：生活资料：食品类：当月同比 |
| ppi\_cg\_c\_yoy | float | Y | PPI：生活资料：衣着类：当月同比 |
| ppi\_cg\_adu\_yoy | float | Y | PPI：生活资料：一般日用品类：当月同比 |
| ppi\_cg\_dcg\_yoy | float | Y | PPI：生活资料：耐用消费品类：当月同比 |
| ppi\_mom | float | Y | PPI：全部工业品：环比 |
| ppi\_mp\_mom | float | Y | PPI：生产资料：环比 |
| ppi\_mp\_qm\_mom | float | Y | PPI：生产资料：采掘业：环比 |
| ppi\_mp\_rm\_mom | float | Y | PPI：生产资料：原料业：环比 |
| ppi\_mp\_p\_mom | float | Y | PPI：生产资料：加工业：环比 |
| ppi\_cg\_mom | float | Y | PPI：生活资料：环比 |
| ppi\_cg\_f\_mom | float | Y | PPI：生活资料：食品类：环比 |
| ppi\_cg\_c\_mom | float | Y | PPI：生活资料：衣着类：环比 |
| ppi\_cg\_adu\_mom | float | Y | PPI：生活资料：一般日用品类：环比 |
| ppi\_cg\_dcg\_mom | float | Y | PPI：生活资料：耐用消费品类：环比 |
| ppi\_accu | float | Y | PPI：全部工业品：累计同比 |
| ppi\_mp\_accu | float | Y | PPI：生产资料：累计同比 |
| ppi\_mp\_qm\_accu | float | Y | PPI：生产资料：采掘业：累计同比 |
| ppi\_mp\_rm\_accu | float | Y | PPI：生产资料：原料业：累计同比 |
| ppi\_mp\_p\_accu | float | Y | PPI：生产资料：加工业：累计同比 |
| ppi\_cg\_accu | float | Y | PPI：生活资料：累计同比 |
| ppi\_cg\_f\_accu | float | Y | PPI：生活资料：食品类：累计同比 |
| ppi\_cg\_c\_accu | float | Y | PPI：生活资料：衣着类：累计同比 |
| ppi\_cg\_adu\_accu | float | Y | PPI：生活资料：一般日用品类：累计同比 |
| ppi\_cg\_dcg\_accu | float | Y | PPI：生活资料：耐用消费品类：累计同比 |

  
  

**接口调用**

```
pro = ts.pro_api()

df = pro.cn_ppi(start_m='201905', end_m='202005')


#获取指定字段
df = pro.cn_ppi(start_m='201905', end_m='202005', fields='month,ppi_yoy,ppi_mom,ppi_accu')
```

  

**数据样例**

```
    month ppi_yoy ppi_mom ppi_accu
0   202005   -3.70   -0.40    -1.70
1   202004   -3.10   -1.30    -1.20
2   202003   -1.50   -1.00    -0.60
3   202002   -0.40   -0.50    -0.20
4   202001    0.10    0.00     0.10
5   201912   -0.50    0.00    -0.30
6   201911   -1.40   -0.10    -0.30
7   201910   -1.60    0.10    -0.20
8   201909   -1.20    0.10     0.00
9   201908   -0.80   -0.10     0.10
10  201907   -0.30   -0.20     0.20
11  201906    0.00   -0.30     0.30
12  201905    0.60    0.20     0.40
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
