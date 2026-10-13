import csv
import os
from mock_llm import malformed_counter
from classify import classify_review, recovery_counter

DATA_FILE = "reviews_sample.csv"

def main():
    if not os.path.exists(DATA_FILE):
        print(f"[오류] {DATA_FILE} 파일을 찾을 수 없습니다. assignment2 폴더에 위치시켜 주세요.")
        return

    total_count = 0
    success_count = 0
    fail_count = 0

    print("==================================================")
    print("      리뷰 데이터 파이프라인 일괄 처리 가동       ")
    print("==================================================")

    with open(DATA_FILE, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            total_count += 1
            text = row.get("review_text", "")
            
            result = classify_review(text)

            if result is not None:
                success_count += 1
            else:
                fail_count += 1

    print("\n" + "=" * 55)
    print("                 파이프라인 실행 요약 보고서")
    print("=" * 55)
    print(f"1. 총 처리 건수        : {total_count}건")
    print(f"2. 최종 처리 성공      : {success_count}건")
    print(f"3. 최종 처리 실패      : {fail_count}건 (건너뜀)")
    print("-" * 55)
    print("[불량 응답 발생 내역 (20% 확률)]")
    print(f"- 총 불량 응답 발생    : {malformed_counter['total_malformed']}건")
    print(f"  * 코드펜스형         : {malformed_counter['codefence']}건")
    print(f"  * 사족 포함형        : {malformed_counter['chatty']}건")
    print(f"  * 잘린 JSON형        : {malformed_counter['truncated']}건")
    print("-" * 55)
    print("[방어 및 복구 내역]")
    print(f"- 정상 응답 처리       : {recovery_counter['normal']}건")
    print(f"- 코드펜스 복구 성공   : {recovery_counter['codefence_recovered']}건 (방어 1)")
    print(f"- 사족형 정규식 복구   : {recovery_counter['chatty_recovered']}건 (도전 과제 적용)")
    print(f"- 복구 불가 건너뜀     : {recovery_counter['unrecoverable_truncated']}건 (잘린 JSON)")
    print("=" * 55)
    print("\n[핵심 분석: 실패 건수가 불량 응답 건수보다 적은 이유]")
    print(f"총 {malformed_counter['total_malformed']}건의 불량 응답 중 최종 실패는 {fail_count}건만 발생했습니다.")
    print("1. [코드펜스형]: 백틱(```)과 마크다운 키워드를 방어 1에서 걷어내어 온전한 JSON으로 복구했습니다.")
    print("2. [사족형]: 정규식(r'\\{.*?\\}')으로 인사말 등 군더더기 텍스트를 배제하고 내부의 온전한 JSON만 추출하여 복구했습니다.")
    print("3. [잘린 JSON형이 복구 불가능한 이유]:")
    print("   문자열 끝부분이 잘려 닫는 따옴표와 중괄호('}') 및 키-값 쌍의 문법 구조 자체가 영구 손상되었기 때문입니다.")
    print("   이 경우 어떤 파서로도 의미를 복원할 수 없어 안전하게 None으로 건너뛰도록 처리했습니다.")
    print("=" * 55)

if __name__ == "__main__":
    main()