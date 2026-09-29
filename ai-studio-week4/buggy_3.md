1. **무엇이**
AttributeError: 'NoneType' object has no attribute 'groupby'
2. **어디서**
buggy_3.py, 26번째 줄 (main 함수 내부)
실행 코드: result = df.groupby("category")["revenue"].sum()
3. **왜**
- result를 계산하기 직전 줄에서 df = load_and_clean("dirty_sales.csv")를 호출했으나 load_and_clean 함수 내부에 return 문이 누락.
- 파이썬 함수는 기본적으로 None을 반환하므로 변수 df에 DataFrame 대신 None(NoneType)이 할당됨.
- None 객체에는 .groupby() 메서드가 존재하지 않아 AttributeError가 발생.