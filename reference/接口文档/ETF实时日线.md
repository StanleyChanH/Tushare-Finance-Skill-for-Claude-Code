# ETF实时日线

**文档ID**: 400
**原始链接**: https://tushare.pro/document/2?doc_id=400

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
- [大模型语料](/document/2?doc_id=142)
- [量化因子库](/document/2?doc_id=485)
- [自选组合](/document/2?doc_id=474)

## ETF实时日线

---

接口：rt\_etf\_k  
描述：获取ETF实时日k线行情，支持按ETF代码或代码通配符一次性提取全部ETF实时日k线行情  
积分：本接口是单独开权限的数据，单独申请权限请参考[权限列表](https://tushare.pro/document/1?doc_id=290)

**输入参数**

| 名称 | 类型 | 必选 | 描述 |
| --- | --- | --- | --- |
| ts\_code | str | Y | 支持通配符方式，e.g. 5\*.SH、15\*.SZ、159101.SZ |
| topic | str | Y | 分类参数，取上海ETF时，需要输入'HQ\_FND\_TICK'，参考下面例子 |

注：ts\_code代码一定要带.SH/.SZ/.BJ后缀

**输出参数**

| 名称 | 类型 | 默认显示 | 描述 |
| --- | --- | --- | --- |
| ts\_code | str | Y | ETF代码 |
| name | None | Y | ETF名称 |
| pre\_close | float | Y | 昨收价（元） |
| high | float | Y | 最高价（元） |
| open | float | Y | 开盘价（元） |
| low | float | Y | 最低价（元） |
| close | float | Y | 收盘价（最新价） |
| vol | int | Y | 成交量（股） |
| amount | int | Y | 成交金额（元） |
| num | int | Y | 开盘以来成交笔数 |
| ask\_volume1 | int | N | 委托卖盘（股） |
| bid\_volume1 | int | N | 委托买盘（股） |
| trade\_time | str | N | 交易时间 |

**接口示例**

```
#获取今日所有深市ETF实时日线和成交笔数
df = pro.rt_etf_k(ts_code='1*.SZ')

#获取今日沪市所有ETF实时日线和成交笔数
df = pro.rt_etf_k(ts_code='5*.SH', topic='HQ_FND_TICK')
```

**数据示例**

```
       ts_code      name      pre_close     high     open     low    close        vol     amount    num
0    520860.SH      港股通科      1.024    1.054    1.048   1.041    1.048   15071600   15780985    307
1    515320.SH    电子50        1.173    1.211    1.184   1.184    1.206    1830600    2191339     98
2    511600.SH    货币ETF     100.008  100.003  100.002  99.999  100.000      12022    1202204     28
3    501075.SH      科创主题      2.350    2.400    2.357   2.357    2.400       4200      10040     11
4    589990.SH      科创板综      1.282    1.311    1.280   1.280    1.305    4178600    5413728    147
..         ...       ...        ...      ...      ...     ...      ...        ...        ...    ...
933  516590.SH      电动汽车      1.244    1.277    1.252   1.252    1.270    1380800    1748398     79
934  502048.SH  50LOF         1.224    1.238    1.235   1.214    1.218       3200       3908      5
935  515850.SH      证券龙头      1.519    1.538    1.523   1.520    1.523   11460000   17484157    688
936  515790.SH    光伏ETF       0.912    0.929    0.919   0.910    0.923  411566128  379094370  14939
937  516190.SH    文娱ETF       1.137    1.154    1.151   1.146    1.151    1031700    1186303     87
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
