# 国内生产总值（GDP）

**文档ID**: 227
**原始链接**: https://tushare.pro/document/2?doc_id=227

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
      - [国内生产总值（GDP）](/document/2?doc_id=227)
    - [价格指数](/document/2?doc_id=226)
    - [金融](/document/2?doc_id=240)
    - [景气度](/document/2?doc_id=324)
  - [国际宏观](/document/2?doc_id=217)
- [大模型语料](/document/2?doc_id=142)
- [量化因子库](/document/2?doc_id=485)
- [自选组合](/document/2?doc_id=474)

## GDP数据

---

接口：cn\_gdp  
描述：获取国民经济之GDP数据  
限量：单次最大10000，一次可以提取全部数据  
权限：用户积累600积分可以使用，具体请参阅[积分获取办法](https://tushare.pro/document/1?doc_id=13)

  
  

**输入参数**

| 名称 | 类型 | 必选 | 描述 |
| --- | --- | --- | --- |
| q | str | N | 季度（2019Q1表示，2019年第一季度） |
| start\_q | str | N | 开始季度 |
| end\_q | str | N | 结束季度 |
| fields | str | N | 指定输出字段（e.g. fields='quarter,gdp,gdp\_yoy'） |

  
  

**输出参数**

| 名称 | 类型 | 默认显示 | 描述 |
| --- | --- | --- | --- |
| quarter | str | Y | 季度 |
| gdp | float | Y | GDP累计值（亿元） |
| gdp\_yoy | float | Y | 当季同比增速（%） |
| pi | float | Y | 第一产业累计值（亿元） |
| pi\_yoy | float | Y | 第一产业同比增速（%） |
| si | float | Y | 第二产业累计值（亿元） |
| si\_yoy | float | Y | 第二产业同比增速（%） |
| ti | float | Y | 第三产业累计值（亿元） |
| ti\_yoy | float | Y | 第三产业同比增速（%） |

  
  

**接口调用**

```
pro = ts.pro_api()

df = pro.cn_gdp(start_q='2018Q1', end_q='2019Q3')


#获取指定字段
df = pro.cn_gdp(start_q='2018Q1', end_q='2019Q3', fields='quarter,gdp,gdp_yoy')
```

  

**数据样例**

```
    quarter          gdp gdp_yoy          pi pi_yoy           si si_yoy           ti ti_yoy
0    2019Q4  990865.1000    6.10  70466.7000   3.10  386165.3000   5.70  534233.1000   6.90
1    2019Q3  712845.4000    6.20  43005.0000   2.90  276912.5000   5.60  392927.9000   7.00
2    2019Q2  460636.7000    6.30  23207.0000   3.00  179122.1000   5.80  258307.5000   7.00
3    2019Q1  218062.8000    6.40   8769.4000   2.70   81806.5000   6.10  127486.9000   7.00
4    2018Q4  900309.5000    6.60  64734.0000   3.50  366000.9000   5.80  469574.6000   7.60
..      ...          ...     ...         ...    ...          ...    ...          ...    ...
147  1956Q4    1028.0000   15.00    443.9000   4.70     280.7000  34.50     303.4000  14.10
148  1955Q4     910.0000    6.80    421.0000   7.90     222.2000   7.60     266.8000   4.60
149  1954Q4     859.0000    4.20    392.0000   1.70     211.7000  15.70     255.3000  -0.60
150  1953Q4     824.0000   15.60    378.0000   1.90     192.5000  35.80     253.5000  27.30
151  1952Q4     679.0000    None    342.9000   None     141.8000   None     194.3000   None
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
