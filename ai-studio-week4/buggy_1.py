import csv

def clean_price(val):
    if not val or not val.strip():
        return 0
    # FIXED: 쉼표(,), '원', 양 끝 공백을 제거하여 int 변환 시 ValueError 방지
    cleaned = val.replace(",", "").replace("원", "").strip()
    return int(cleaned)

def calc_total(path):
    total = 0
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader):
            # FIXED: raw 문자열 대신 clean_price() 전처리 함수를 통과시켜 변환 실패 해결
            price = clean_price(row["price"])
            qty = int(row["quantity"])
            total += price * qty
    return total

if __name__ == "__main__":
    print(">>> 계산 시작")
    total = calc_total("dirty_sales.csv")
    print(f"총 매출액: {total:,}원")
    print(">>> 계산 완료")
