import akshare as ak
import pandas as pd
from datetime import datetime
import os

# 要记录的标的，可自行添加多个股票代码
stock_list = ["sh000001","600498"]  # 上证指数
csv_path = "stock_data.csv"

# 获取今日日期
today = datetime.now().strftime("%Y-%m-%d")

all_data = []
for code in stock_list:
    # 获取日线当日行情
    df = ak.stock_zh_index_daily(symbol=code)
    # 只保留最新1条当日数据
    today_row = df.tail(1).copy()
    today_row["日期"] = today
    today_row["代码"] = code
    all_data.append(today_row)

new_df = pd.concat(all_data)

# 判断CSV是否存在：不存在则新建表头，存在则追加写入
if os.path.exists(csv_path):
    old_df = pd.read_csv(csv_path, encoding="utf-8-sig")
    final_df = pd.concat([old_df, new_df], ignore_index=True)
else:
    final_df = new_df

# 保存表格
final_df.to_csv(csv_path, encoding="utf-8-sig", index=False)
print(f"{today} 行情数据保存完成")
