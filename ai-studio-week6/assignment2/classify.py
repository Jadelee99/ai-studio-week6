import json
import re
from mock_llm import mock_llm_call

SYSTEM = """당신은 고객 리뷰 분류기입니다. 반드시 아래 JSON 형식으로만 응답하세요. 다른 텍스트를 절대 포함하지 마세요.
{"category": "배송|품질|가격|서비스|기타", "sentiment": "긍정|부정|중립", "score": 1~5 사이의 정수}"""

recovery_counter = {
    "normal": 0,
    "codefence_recovered": 0,
    "chatty_recovered": 0,
    "unrecoverable_truncated": 0
}

def classify_review(review_text: str):
    """
    리뷰 1건을 분류하여 딕셔너리로 반환. 실패 시 None.
    프로그램이 중단(Crash)되지 않도록 다단계 방어 및 복구를 수행합니다.
    """
    result = mock_llm_call(SYSTEM, f"리뷰: {review_text}")
    raw = result["text"].strip()
    is_codefence = False

    if raw.startswith("```"):
        is_codefence = True
        raw = raw.strip("`")
        raw = raw.replace("json", "", 1).strip()

    data = None
    try:
        data = json.loads(raw)
        if is_codefence:
            recovery_counter["codefence_recovered"] += 1
        else:
            recovery_counter["normal"] += 1
    except json.JSONDecodeError:
        match = re.search(r"\{.*?\}", raw)
        if match:
            try:
                data = json.loads(match.group(0))
                recovery_counter["chatty_recovered"] += 1
            except json.JSONDecodeError:
                pass

    if data is None:
        recovery_counter["unrecoverable_truncated"] += 1
        return None

    if data.get("category") not in ["배송", "품질", "가격", "환불", "서비스", "기타"]:
        return None

    return data