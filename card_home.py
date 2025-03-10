import sys

display = '''
----------------------------------------------------------
1. 명함 입력, 2. 명함 수정, 3. 명함 삭제, 4. 명함 목록 보기, 5. 종료
----------------------------------------------------------
메뉴를 선택하세요 >>> '''
card_display = '''
--------------------------------------------------------------
1. 이름, 2. 전화번호, 3. 소속 4. email 5. 종료
--------------------------------------------------------------
'''


# 명함 정보를 저장할 리스트
menu = ''
card = []
card_list = []

while True:
    menu = input(display).strip()
    
    if menu == '1':
    
        print(display)
        name = input("성함을 입력하세요 >> ").strip()
        tel = (input("전화번호를 입력하세요 >> ")).strip()
        belong = input("소속을 입력하세요 >> ").strip()
        email = input("이메일을 입력하세요 >> ").strip()
        
        card.append([name, tel, belong, email])
        print("명함이 등록되었습니다", card)
        
    elif menu == '2':
        print(card_display)
        while True : 
            email = input('이메일 >>>')
            check = 0
            for index in range(len(card_list)):
                if card_list[index][3] == email :
                    check = 1
                    break
                # if check = 0:
                    break
            card_list.append([name, tel, belong, email])
            print(card_list)

    while True:
        item = input('수정할 항목을 선택하세요(1. 이름 2. 전화번호, 3.주소, 4. 종료)')
        if item == '4':
          break
        item = int(item)
        if item in (1,2,3):
            card_list[index][item-1] = input('수정할 값을 입력 >>')
 
        if check == 0:
            print("데이터가 없습니다")
        elif menu == 3:
            print('명함삭제')


        modify_num = int(input('수정할 부분 번호 입력 >'))
        if modify_number == 1 :
            card_list[card_num-1][0] = input('수정할 이름 입력>')
        elif modify_num == 2 :
            card_list[card_num-1][1] = input('수정할 전화번호 입력 >')
        elif modify_num == 3 :
            card_list[card_num-1][2] = input('수정할 소속 입력 >')
        elif modify_num == 4 :
            card_list[card_num-1][3] = input('수정할 이메일 입력 >')
        elif modify_num == 5 :
            break

        print("명함이 수정되었습니다", card_list[list_num-1])    
            
         