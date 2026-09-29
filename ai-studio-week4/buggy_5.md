1. **무엇이**
IndexError: list index out of range
2. **어디서**
buggy_5.py, 27번째 줄 (find_big_jumps 함수 내부)
실행 코드: diff = prices[i + 1] - prices[i]
3. **왜**
- 전체 가격 데이터 prices 500개 중 유효한 인덱스는 0부터 499까지.
- 반복문이 range(len(prices))로 설정되어 있어 마지막 순회 시 i = 499가 됨.
- prices[i + 1]은 prices[500]을 참조하게 되므로 리스트의 범위를 벗어나 IndexError가 발생.