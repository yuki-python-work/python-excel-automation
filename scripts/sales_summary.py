import pandas as pd

# CSVを読み込む
df = pd.read_csv("../data/sales_sample.csv")

# 売上金額を計算
df["total"] = df["amount"] * df["price"]

# 日付をdatetime型に変換
df["date"] = pd.to_datetime(df["date"])

# 月別・商品別に集計
summary = (
    df.groupby([df["date"].dt.to_period("M"), "product"])["total"]
    .sum()
    .reset_index()
)

# Excelに出力
summary.to_excel("../sales_summary.xlsx", index=False)

print("売上集計が完了しました")
