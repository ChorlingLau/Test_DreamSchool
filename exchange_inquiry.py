import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 设置 Edge 驱动器路径
edge_driver_path = "C:/Program Files (x86)/Microsoft/Edge/Application/msedgedriver.exe"


def std_sym_2_cn_name(sym):

    driver = webdriver.Edge(executable_path=edge_driver_path)
    driver.get("https://www.11meigui.com/tools/currency")

    # 找到包含标准符号的单元格元素 - 对应父级元素 - 货币中文名称的单元格文本
    symbol_cell = driver.find_element_by_xpath(f"//td[contains(text(), '{sym} ')]")
    parent_element = symbol_cell.find_element_by_xpath("..")
    currency_name = parent_element.find_element_by_xpath(".//td[2]").text

    driver.quit()

    return currency_name.strip()


def fetch_forex_rate(date, currency_code):

    driver = webdriver.Edge(executable_path=edge_driver_path)

    try:
        driver.get("https://www.boc.cn/sourcedb/whpj/")

        # 输入日期
        date = date[:4] + "-" + date[4:6] + "-" + date[6:]
        date_start = driver.find_element(By.NAME, "erectDate")
        date_start.clear()
        date_start.send_keys(date)
        date_end = driver.find_element(By.NAME, "nothing")
        date_end.clear()
        date_end.send_keys(date)

        # 选择货币
        selected_item = std_sym_2_cn_name(currency_code)
        currency_select = driver.find_element(By.NAME, "pjname")
        currency_select.send_keys(selected_item)

        # 点击查询按钮
        query_button = driver.find_elements(By.CLASS_NAME, "search_btn")[1]
        query_button.click()

        # 等待结果加载完成
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "BOC_main.publish")))

        # 获取现汇卖出价
        forex_rate = driver.find_element(By.XPATH, "//tr[@class='odd'][1]/td[5]").text

        # 将结果写入文件
        with open("result.txt", "w") as f:
            f.write(forex_rate)

        return forex_rate

    except Exception as e:
        print("An error occurred:", e)
        return None

    finally:
        driver.quit()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python exchange_inquiry.py <date[YYYYMMDD]> <currency_code>")
        sys.exit(1)

    date = sys.argv[1]
    currency_code = sys.argv[2]

    forex_rate = fetch_forex_rate(date, currency_code)
    if forex_rate:
        print(f"The forex rate for {date} and currency code {currency_code} is: {forex_rate}")
    else:
        print("Usage: python exchange_inquiry.py <date[YYYYMMDD]> <currency_code>")
