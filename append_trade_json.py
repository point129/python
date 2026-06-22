import json

# 1. 기존 데이터 불러오기
try:
    with open("journal.json", "r") as f:
        journal = json.load(f)
except:
    journal = []

# 2. 사용자 입력
stock = input("종목: ")
buy = int(input("매수가: "))
sell = int(input("매도가: "))

# 3. 계산
profit = sell - buy

# 4. 새 데이터 생성
new_trade = {
    "종목": stock,
    "매수가": buy,
    "매도가": sell,
    "수익률": profit
}

# 5. 추가
journal.append(new_trade)

# 6. 저장
with open("journal.json", "w") as f:
    json.dump(journal, f)

print("저장 완료")
