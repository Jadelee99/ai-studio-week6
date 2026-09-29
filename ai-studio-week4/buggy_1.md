#무엇이
ValueError: invalid literal for int() with base 10: '5,200'
#어디서
buggy_1.py, 16번째 줄 (calc_total 함수 내부)
실행 코드: price = int(row["price"])
#왜
CSV 318번째 행에서 row["price"]의 값이 순수 정수 형태의 문자열이 아닌 쉼표가 포함된 '5,200'으로 들어옴. 파이썬의 내장 int() 함수는 쉼표, '원', 공백, 빈 문자열을 숫자로 직접 변환하지 못하고 ValueError를 발생시키기 때문(데이터셋 후반부에는 '4200원', 결측치 '' 등도 존재함)