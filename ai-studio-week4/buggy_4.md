1. **무엇이**
1,511억 원(151,198,388,824원), 평균 단가 28,342원 출력
2. **어디서**
buggy_4.py, 23~28번째 줄
실행 코드: df["price"] = pd.to_numeric(...), df["revenue"] = df["price"] * df["quantity"], total = df["revenue"].sum()["revenue"].sum()
3. **왜**
- 단가 결측치 2개, 단가 음수 이상치 1개, 단가 극단 이상치 1개, 수량 극단 이상치 1개