# -*- coding: utf-8 -*-
"""
buggy_4.py  ―  총 매출액 집계 (결측치 및 이상치 정제 버전) - 수정본
"""
import pandas as pd

def main():
    df = pd.read_csv("dirty_sales.csv", encoding="utf-8")

    # 1. price 문자열 정제 후 숫자형 변환
    df["price"] = (df["price"].astype(str)
                              .str.replace(",", "")
                              .str.replace("원", "")
                              .str.strip())
    df["price"] = pd.to_numeric(df["price"], errors="coerce")
    valid_mask = (
        (df["price"].notna()) &
        (df["price"] > 0) &
        (df["price"] < 100000) &
        (df["quantity"] > 0) &
        (df["quantity"] < 1000)
    )
    
    clean_df = df[valid_mask].copy()
    clean_df["revenue"] = clean_df["price"] * clean_df["quantity"]
    total = clean_df["revenue"].sum()
    avg_price = clean_df["price"].mean()
    print(f"제외된 이상/결측 행 수: {len(df) - len(clean_df)}건")
    print(f"정상 분석 데이터 건수: {len(clean_df)}건")
    print(f"총 매출액: {total:,.0f}원")
    print(f"평균 단가: {avg_price:,.0f}원")
if __name__ == "__main__":
    main()