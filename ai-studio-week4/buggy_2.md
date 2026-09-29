1. **무엇이**
KeyError: '단가'
2. **어디서**
buggy_2.py, 18번째 줄 (summarize 함수 내부)
실행 코드: df["매출액"] = df["단가"] * df["수량"]
3. **왜**
- 실제 dirty_sales.csv의 헤더 확인하면 ['date', 'product', 'category', 'price', 'quantity', 'stock']로 영문으로 정의됨
- 데이터프레임 내에 한글 컬럼인 '단가'와 '수량'이 존재하지 않기 때문에 pandas에서 KeyError가 발생
- df["price"]는 문자열 타입이며 쉼표나 단위가 포함되어 있어, 컬럼명을 price와 quantity로 변경함과 동시에 숫자형 변환(pd.to_numeric)을 함께 수행해야 연산 오류를 방지할 수 있음.