# -*- coding: utf-8 -*-
"""
buggy_2.py  ―  카테고리별 매출 집계 (pandas 버전) - 수정본
"""
import pandas as pd

def load(path):
    df = pd.read_csv(path, encoding="utf-8")
    return df

def summarize(df):
    price_clean = pd.to_numeric(
        df["price"].astype(str).str.replace(r"[^\d.-]", "", regex=True),
        errors="coerce"
    ).fillna(0)
    
    df["매출액"] = price_clean * df["quantity"]
    return df.groupby("category")["매출액"].sum()

if __name__ == "__main__":
    df = load("dirty_sales.csv")
    result = summarize(df)
    print(result)