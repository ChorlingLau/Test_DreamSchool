## 外汇牌价查询

输入：日期、货币代号

输出：该日期该货币的“现汇卖出价” （位于result.txt）

---

### 环境配置

```
python >= 3.6
selenium
```

### 使用方法

 1. 安装 Microsoft Edge 浏览器及其[驱动器](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/?form=MA13LH)，修改`exchange_inquiry.py`内变量`edge_driver_path`为驱动器本地路径
 2. 命令行运行：
```
python exchange_inquiry.py <date[YYYYMMDD]> <currency_code>
# e.g. python exchange_inquiry.py 20211231 USD
```
