#자료구조 선택 및 분석 리포트
##1. 상품코드를 입력하면 즉시 재고 수량을 확인해야 하는 재고 관리 데이터
-선택한 자료구조: 딕셔너리
-선택 근거: 상품의 갯수와 상관없이 상품코드 key를 통해 즉각적으로 재고 숫자를 확인할 수 있음
-예시코드:
stocks={"A1":30, "A2":45, "A3":10}
code="A2"
print(f"{code}재고:{stocks.get(code,0)}개")
##2. 이벤트 응모 고객 명단에서 중복 응모를 제거하고, 기존 회원 명단과의 교집합을 구해야 하는 상황
-선택한 자료구조: 세트
-선택 근거: 중복이 여러개 들어와도 자동으로 1개만 남기고 중복 제거 가능, 교집합을 기호로 즉각적 탐색 가능
-예시코드:
applicants=set(["철수","영희","철수","서강"])
member=set(["영희","서강","경영"])
target_users=applicants&members
print("이벤트 당첨 회원:",target_users)
##3. 월별 매출액을 1월부터 12월까지 순서대로 저장하고 순회하는 데이터
-선택한 자료구조: 리스트
-선택 근거: 1월부터 12월까지의 순서가 유지되면서 1월부터 차례대로 계산할 수 있음
-예시코드:
monthly_sales = [120, 135, 110, 150, 170, 160, 180, 175, 190, 210, 205, 230]
for month, sales in enumerate(monthly_sales, start=1):
print(f"{month}월 매출: {sales}만원")
##4. 한 번 발급되면 절대 변경되어서는 안 되는 (위도, 경도) 매장 좌표
-선택한 자료구조: 튜플
-선택 근거: 튜플은 수정이 불가능하기 때문에 이에 적합
-예시코드:
store_coords = (310.2005, 111.997)
lat, lng = store_coords
print(f"매장 위치 - 위도: {lat}, 경도: {lng}")
##5. 1,000만 줄짜리 웹 서버 접속 로그 파일에서 특정 조건의 줄 수를 세는 작업
-선택한 자료구조,처리방식: 스트리밍 방식
-선택 근거: 파일 용량이 매우 크기때문에 한줄씩 읽고 바로바로 버리는 스트리밍 방식 이용
-예시코드:
errorline_count=0
with open("web_server.log","r",encoding="utf-8") as file:
for line in file:
if "ERROOR" in line:
errorline_count+=1
print(f"에러 발생 줄 수:{errorline_count}개")