# AI 사용 기록
## 1. 사용한 프롬프트
- "RAW_DATA.csv를 불러와 단가의 쉼표를 제거하고 매출액 파생열을 생성한 뒤, 월별/카테고리별 매출을 집계하여 엑셀 다중 시트로 내보내는 판다스 파이프라인 코드 작성 가이드 요청"
- "ModuleNotFoundError, FileNotFoundError 등 실행 오류 디버깅 및 터미널 경로 문제 해결 요청"
## 2. 채택 및 수정 내역
- **채택 내역**:
  - `pd.read_csv` 실행 시 `encoding='cp949'` 지정하여 한글 인코딩 오류 해결.
  - `str.replace(',', '')` 및 `pd.to_numeric`을 활용한 단가 쉼표 제거 및 숫자 변환 로직 채택.
  - `pd.ExcelWriter`를 사용한 '월별카테고리요약', '카테고리별합계' 2개 시트 분리 저장 로직 채택.
- **수정 내역**:
  - 과제 명세에 맞춰 시트 이름 및 컬럼명(`총매출`, `평균매출`, `거래건수`) 통일.
## 3. 검증 결과 및 데이터 확인
- **데이터 로드 shape**: `(500, 5)`
- **컬럼 정보**:
  - 주문일자 (object -> datetime 변환 후 월 추출)
  - 상품명 (object)
  - 카테고리 (object)
  - 단가 (object -> Int64 변환)
  - 수량 (int64)
- **정합성 검증**:
  - `assert df['매출액'].sum() == monthly_category_summary['총매출'].sum()` 통과 (원본 총매출과 집계 총매출 일치 확인).
  - `Monthly_Report.xlsx` 정상 생성 확인.