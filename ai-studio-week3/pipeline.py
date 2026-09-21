import pandas as pd
file_path="RAW_DATA.csv"
df=pd.read_csv(file_path, encoding="cp949")
print("[step 1] 데이터 로드 완료")
print(f"shape: {df.shape}")
df.info()
