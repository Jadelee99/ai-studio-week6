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