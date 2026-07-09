from datetime import datetime
import random

products = [
    {
        "name": "차량용 무선 청소기",
        "price": "저가형",
        "link": "여기에_알리_제휴링크_넣기"
    },
    {
        "name": "주방 싱크대 정리 선반",
        "price": "가성비",
        "link": "여기에_알리_제휴링크_넣기"
    }
]

product = random.choice(products)

post = f"""
오늘의 가성비 추천템 🔥

{product['name']}

가격 부담 적고 실사용 만족도가 좋은 제품입니다.
자영업자, 차량용품, 생활용품 찾는 분들께 추천!

👇 확인하기
{product['link']}

작성시간: {datetime.now()}
"""

print(post)

with open("result.txt", "w", encoding="utf-8") as f:
    f.write(post)
