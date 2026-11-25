import sys
import json

#함수 정의

def appstart():

    print("> 수업 시간: ", 60)
    print("> 실행기 정보: ", sys.executable)

#프로그램 이름, 수업 시간(60), 파이썬 실행기 정보(sys.executable)를 출력


def quote(price, quantity, shipping = 3000):

    total = price * quantity + shipping

    return total


def sum_values(*args):

    return sum(args)


def clean_quantities(values):
        
        clean_quauntity, errors = [],[]

        for value in values:
            try:
                quantity = int(value)

                if not quantity > 0:
                    raise ValueError("range")
                
                clean_quauntity.append(quantity)

            except ValueError:
                errors.append(value)

        return clean_quauntity, errors
        


def profile(**kwargs):

    return kwargs
    

# -----------------------------------------------------------------------------------------

# 실행 부분

# 1. 앱 시작 화면 및 초기 데이터 설정
print("=== 파이썬 콘솔 애플리케이션 ===")
appstart()

productlist = {"product" : "book", "price" : 12000}, {"product" : "note", "price" : 8000}, {"product" : "pen", "price" : 1500}, {"product" : "bag", "price" : 25000}, {"product" : "cup", "price" : 6000}
# 초기 상품 카탈로그를 딕셔너리 또는 (상품명, 가격) 튜플 리스트로 구성 // key : 값

owned_items = {"book", "pen", "note"}
wish_items = {"pen", "bag", "cup", "book"}
# 사용자 프로필 및 보유/관심 상품 집합(set)을 초기화

# 튜플 확인용 출력
# print(productlist)


# 2. 메인 메뉴 루프
while(True):

    print("")
    print("=== 파이썬 스마트 스토어 & 학습 매니저 ===")

    print("")
    print("1. 상품 목록 보기 (가격 정렬)")
    print("2. 주문 담기 및 견적 계산")
    print("3. 수량 일괄 정산 리포트(컴프리헨션)")
    print("4. 보유 vs 관심 상품 비교 (집합 연산)")
    print("5. 주문 내역 JSON 저장 및 불러오기")
    print("6. 회원 프로필 / 추가 메모 등록 (**kwargs)")
    print("0. 종료")

    print("")
    pickmenu = input("> 메뉴 선택: ").strip()
    menunum = int(pickmenu)

    # 3. 메뉴별 세부 구현 조건

    if (menunum == 1):

        # 메뉴 1 - 상품 목록 보기

        print("===================================================")
        print("1. 상품 목록 보기 (가격 정렬)")

        # 상품 리스트
        items = [("book", 12000), ("note", 8000), ("pen", 1500), ("bag", 25000), ("cup", 6000)]

        #가격 높은 순으로 상품명과 단가 출력
        print("")
        print("[상품 가격 높은순 정렬]")
        print(sorted(items, key=lambda item: item[1], reverse=True))

        # 리스트 인덱싱/슬라이싱을 활용해 "최고가 상품"과 "추천 TOP 3"를 함께 안내
        print("")
        print("[최고가 상품]")
        print(max(items, key=lambda item: item[-1])) 

        print("")
        print("[추천 TOP 3]")
        print(items[:3]) 
    
        print("===================================================")


    elif (menunum == 2):

        # 메뉴 2 - 주문 담기 및 견적 계산

        print("===================================================")
        print("2. 주문 담기 및 견적 계산")

        # 사용자 이름(.strip()), 회원 여부(y/n → bool),
        # 주문할 상품들(예: "book,pen" → .split(",")), 수량을 입력

        print("")
        user_name = input("> 사용자 이름: ").strip()

        onoff = True

        while onoff :
            input_bool = input("> 회원 여부(y/n): ").strip()

            if input_bool == "y":
                user_bool = True
                onoff = False

            elif input_bool == "n":
                user_bool = False
                onoff = False

            else:
                print("잘못 입력하셨습니다. 다시 입력해 주세요.")
        # 값 받은 후 bool 타입으로 변경

        buy_product = input("> 주문할 상품 (구분 기호 ,): ").strip().split(",")

        onoff = True

        while(onoff):
            try:
                input_quantity = input("> 주문할 수량: ").strip()
                product_quantity = int(input_quantity)
                onoff = False

            except ValueError:
                print("잘못 입력하였습니다. 정수를 입력해 주세요.")
                #수량 입력 시 숫자가 아니면 "정수를 입력하세요" 출력하고 다시 입력받기

        print("---------------------------------------------------")

        # quote 함수를 호출해 금액을 계산하되,
        # total >= 30000 and is_member 조건을 만족하면 shipping=0을 전달해 "무료배송",
        # 그 외에는 "배송비 3000원" 메시지를 출력

        #누적 주문 금액은 *args를 받는 sum_values(*args) 함수로 합산

        is_member = True
        price = 3000

        total = price * product_quantity

        if total >= 30000 and is_member:
            print("> 주문 상품: ", buy_product)
            print("> 총 결제 금액: ", sum_values(quote(price, product_quantity, shipping=0)))

            total_price = sum_values(quote(price, product_quantity, shipping=0))

            print("")
            print(f": 상품 금액 {total}원으로 무료배송입니다.")

        else:
            print("> 주문 상품: ", buy_product)
            print("> 총 결제 금액: ", sum_values(quote(price, product_quantity)))

            total_price = sum_values(quote(price, product_quantity))
            
            print("")
            print(f": 상품 금액 {total}원으로 배송비 3,000원 추가됩니다.")

        print("===================================================")


    elif (menunum == 3):

        # 메뉴 3 - 수량 일괄 정산 리포트

        print("===================================================")
        print("3. 수량 일괄 정산 리포트(컴프리헨션)")

        quantity_list = [2, 3, 0, -1, 1]

        values, errors = clean_quantities(quantity_list)
        totals = [quantity * 3000 for quantity in values]

        # 여러 건의 수량 리스트(예: [2, 3, 0, -1, 1])에서 0 이하의 값은 제외(if n > 0 또는 continue)하고,
        # 리스트 컴프리헨션으로 각 건의 금액 리스트를 생성합니다.
        
        print("")
        print("> 기존 수량 리스트: ", quantity_list)

        print("")
        print("> 잘못된 수량 리스트: ", errors)
        print("> 정상 수량 리스트: ", values)

        print("")
        print("> 각 건의 금액 리스트: ", totals)

        print("---------------------------------------------------")

        report = {str(i + 1): value for i, value in enumerate(totals)}
        print("> 정산 리포트: ", report)

        #enumerate를 활용한 딕셔너리 컴프리헨션으로 {"1": 16000, "2": 24000, ...} 형태의
        # 정산 리포트를 만들어 출력합니다.

        print("===================================================")
        

    elif (menunum == 4):

        # 메뉴 4 — 보유 vs 관심 상품 비교

        # 두 집합(owned_items, wish_items)의 교집합(&), 차집합(-), 합집합(|)을 구해
        # sorted()로 정렬한 뒤 각각 출력

        print("===================================================")
        print("4. 보유 vs 관심 상품 비교 (집합 연산)")

        print("")
        print("owned_item과 wish_items의 교집합입니다.")
        print(sorted(owned_items & wish_items))

        print("")
        print("owned_item과 wish_user_items의 차집합입니다.")
        print(sorted(owned_items - wish_items))

        print("")
        print("owned_item과 wish_user_items의 합집합입니다.")
        print(sorted(owned_items | wish_items))

        print("===================================================")

    elif (menunum == 5):

        #메뉴 5 — 주문 내역 JSON 내보내기 및 검증

        print("===================================================")
        print("메뉴 5 — 주문 내역 JSON 내보내기 및 검증")

        try:
            owner_info = {"name" : user_name, "user" : user_info, "order_product" : buy_product, "order_price": total_price}
            print(json.dumps(owner_info, ensure_ascii=False))   
            text = json.dumps(owner_info, ensure_ascii=False)

            print("")
            print("정보를 json으로 내보냈습니다.")

            print("---------------------------------------------------")

            print("[정보 요약]")

            print("")
            print("> 저장된 이름: ", json.loads(text)["name"])
            print("> 저장된 회원 등급: ", json.loads(text)["user"])
            print("> 저장된 주문 목록: ", json.loads(text)["order_product"])
            print("> 저장된 총 주문액: ", json.loads(text)["order_price"])
            
        except:
            print("")
            print("정보를 내보낼 수 없습니다.")
            # 내보낼 정보가 없을 때 출력

        print("===================================================")

    elif (menunum == 6):

        #메뉴 6 — 회원 프로필 등록

        print("===================================================")
        print("6. 회원 프로필 / 추가 메모 등록 (**kwargs)")

        print("")

        x, y = (10, 20)
        print("* 포인트 좌표 설정 *")
        print("- 포인트 x 좌표: ", x)
        print("- 포인트 y 좌표: ", y)
        # 튜플 언패킹(x, y = (10, 20))으로 매장 좌표나 포인트 좌표를 출력

        print("---------------------------------------------------")

        try:

            print("")

            if user_bool == True:
                user_info = "일반회원"
            else:
                user_info = "비회원"
            
            user_profile = profile(name = user_name, level = "0", info = user_info)

            print("> 입력된 사용자 정보: ", user_profile)
            print("> 사용자 정보가 저장되었습니다.")
            # def profile(**kwargs): 함수를 호출해 사용자 이름·레벨·등급 정보를 딕셔너리로 생성해 저장
        
        except:
            print("")
            print("정보를 등록할 수 없습니다.")
            # 등록할 정보가 없을 때 출력

        print("===================================================")

    elif (menunum == 0):
        break

    else:
        print("번호를 잘못 입력하셨습니다. 다시 입력해 주세요.")