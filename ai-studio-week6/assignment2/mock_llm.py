import random
import json

malformed_counter = {
    "total_malformed": 0,
    "codefence": 0,
    "chatty": 0,
    "truncated": 0
}

def mock_llm_call(system_prompt: str, user_prompt: str) -> dict:
    """
    1차시 모듈을 확장한 가짜 LLM API.
    80%는 정상 JSON, 20%는 고의적인 불량 응답을 dict 형태 {"text": ...} 로 반환합니다.
    """
    categories = ["배송", "품질", "가격", "서비스", "기타"]
    sentiments = ["긍정", "부정", "중립"]
    
    valid_obj = {
        "category": random.choice(categories),
        "sentiment": random.choice(sentiments),
        "score": random.randint(1, 5)
    }
    valid_json_str = json.dumps(valid_obj, ensure_ascii=False)

    if random.random() < 0.20:
        malformed_counter["total_malformed"] += 1
        error_type = random.choice(["codefence", "chatty", "truncated"])
        malformed_counter[error_type] += 1

        if error_type == "codefence":
            bad_text = f"```json\n{valid_json_str}\n```"
        elif error_type == "chatty":
            bad_text = f"물론입니다! 분석 결과는 다음과 같습니다. {valid_json_str}"
        elif error_type == "truncated":
            bad_text = f'{{"category": "{valid_obj["category"]}", "sentim'

        return {"text": bad_text}

    return {"text": valid_json_str}