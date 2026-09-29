# -*- coding: utf-8 -*-
"""
buggy_3.py  ―  데이터 로드 후 카테고리별 집계 - 수정본
"""
import pandas as pd
def load_and_clean(path):
    df = pd.read_csv(path, encoding="utf-8")
    # price 컬럼을 숫자로 정제
    df["price"] = (df["price"].astype(str)
                              .str.replace(",", "")
                              .str.replace("원", "")
                              .str.strip())
    df["price"] = pd.to_numeric(df["price"], errors="coerce")
    df["revenue"] = df["price"] * df["quantity"]
    return df

def main():
    df = load_and_clean("dirty_sales.csv")
    result = df.groupby("category")["revenue"].sum()
    print(result)
if __name__ == "__main__":
    main()