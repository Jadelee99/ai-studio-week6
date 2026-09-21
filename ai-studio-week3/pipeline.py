import pandas as pd
file_path="RAW_DATA.csv"
df=pd.read_csv(file_path, encoding="cp949")
print("[step 1] 데이터 로드 완료")
print(f"shape: {df.shape}")
df.info()
df["단가"]=pd.to_numeric(df["단가"].astype(str).str.replace(",","",regex=False),errors="coerce").astype("Int64")
df["매출액"]=df["단가"]*df["수량"]
df["주문일자"]=pd.to_datetime(df["주문일자"])
df["월"]=df["주문일자"].dt.month
print("[Step 2] 데이터 정제 및 파생 열 생성 완료")
print(df[["주문일자","월","상품명","단가","수량","매출액"]].head())
monthly_category_summary=(df.groupby(["월","카테고리"])["매출액"].agg(총매출="sum",평균매출="mean",거래건수="count").reset_index())
category_summary=(df.groupby("카테고리")["매출액"].sum().reset_index(name="총매출").sort_values(by="총매출",ascending=False))
print("[step 3] 집계완료")
print("월별 카테고리 요약 상위 5행")
print(monthly_category_summary.head())
assert df["매출액"].sum()==monthly_category_summary["총매출"].sum(),("오류: 원본 매출액 총합과 집계표 총매출 합이 일치하지 않습니다.")
print("[step 4] 정합성 검증 통과")
output_path="Monthly_Report.xlsx"
with pd.ExcelWriter(output_path, engine="openpyxl")as writer:
    monthly_category_summary.to_excel(writer,sheet_name="월별카테고리요약",index=False)
    category_summary.to_excel(writer,sheet_name="카테고리별합계",index=False)
print(f"'{output_path}' 저장 완료")