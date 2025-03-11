import sys

display = '''
--------------------------------------------------------------
1. 명함 입력 2. 명함 수정 3. 명함 삭제 4. 명함 목록 보기 5. 종료
--------------------------------------------------------------
메뉴 번호를 선택하세요 >>> '''
card_display = '''
--------------------------------------------------------------
1. 이름, 2. 이메일 주소, 3. 전화 번호, 4. 직장/학교
--------------------------------------------------------------
메뉴 번호를 선택하세요 >>> '''
card_display2 = '''
--------------------------------------------------------------
1. 이름, 2. 이메일 주소, 3. 전화 번호, 4. 직장/학교, 5. 전체 삭제
--------------------------------------------------------------
메뉴 번호를 선택하세요 >>> '''

menu = ''
card_list = []

def show_cards():
    if not card_list:
        print("등록된 명함이 없습니다.")
    else:
        idx = 1  # 인덱스 값을 1부터 시작
        for card in card_list:
            print(f"{idx}. 이름: {card[0]}, 이메일: {card[1]}, 전화번호: {card[2]}, 직장/학교: {card[3]}")
            idx += 1  # 인덱스를 하나씩 증가

while menu != '5':
    print(display)
    menu = input()

    if menu == '1':
        name = input('이름 입력 > ')
        email = input('이메일 주소 입력 > ')
        tel = input('전화번호 입력 > ')
        belong = input('직장 또는 학교 입력 > ')
        card = [name, email, tel, belong]
        card_list.append(card)
        print("명함이 입력되었습니다")
        show_cards()

<<<<<<< HEAD
    if menu == 1 :
        name = input('이름 입력 >')
        email = input('이메일 주소 입력 >')
        tel = input('전화번호 입력 >')
        belong = input ('직장 또는 학교 입력 >')
        list = [name,email,tel,belong]
        card_list.append(list)
        list.insert(0,len(card_list))
        print("명함이 입력되었습니다", list)


    elif menu == 2 :
        print(card_display)
        list_num = int(input('수정할 명함의 번호 입력 >'))
        number = int(input('수정할 부분 번호 입력 >'))
        if number == 1 :
            card_list[list_num-1][0] = str(input('수정할 이름 입력>'))
        if number == 2 :
            card_list[list_num-1][1] = str(input('수정할 이메일 주소 입력 >'))
        if number == 3 :
            card_list[list_num-1][2] = str(input('수정할 전화번호 입력 >'))
        if number == 4 :
            card_list[list_num-1][3] = str(input('수정할 직장 또는 학교 입력 >'))
       
        print("명함이 수정되었습니다", card_list[list_num-1])

        if number == 1 :
            card_list[list_num-1][0] = input('수정할 이름 입력>')
        if number == 2 :
<<<<<<< HEAD
            del card_list[list_num-1][0]
        if number == 3 :
            del card_list[list_num-1][0]
        if number == 4 :
            del card_list[list_num-1][0]
        if number == 5 :
            del card_list[list_num-1]
=======
            card_list[list_num-1][1] = input('수정할 이메일 주소 입력 >')
        if number == 3 :
            card_list[list_num-1][2] = input('수정할 전화번호 입력 >')
        if number == 4 :
            card_list[list_num-1][3] = input('수정할 직장 또는 학교 입력 >')
>>>>>>> 449f61761350426ad1353b8f5fdaa7192aaf9e87
       
        print("명함이 수정되었습니다", card_list[list_num-1])
=======
    elif menu == '2':
        show_cards()
        print(card_display)
        search_name = input('수정할 명함의 이름 입력 > ')
        found = False
        
        for card in card_list:
            if card[0] == search_name:
                found = True
                number = int(input('수정할 부분 번호 입력 > '))
                if number == 1:
                    card[0] = input('수정할 이름 입력 > ')
                elif number == 2:
                    card[1] = input('수정할 이메일 주소 입력 > ')
                elif number == 3:
                    card[2] = input('수정할 전화번호 입력 > ')
                elif number == 4:
                    card[3] = input('수정할 직장 또는 학교 입력 > ')
                print("명함이 수정되었습니다")
                show_cards()
                break
        
        if not found:
            print("해당 이름의 명함이 없습니다.")

    elif menu == '3':
        show_cards()
        print(card_display2)
        search_name = input('삭제할 명함의 이름 입력 > ')
        found = False
        
        for card in card_list:
            if card[0] == search_name:
                found = True
                number = int(input('삭제할 부분 번호 입력 > '))
                if number in [1, 2, 3, 4]:
                    card[number - 1] = ''
                elif number == 5:
                    card_list.remove(card)
                print("명함이 삭제되었습니다.")
                show_cards()
                break
        
        if not found:
            print("해당 이름의 명함이 없습니다.")

    elif menu == '4':
        show_cards()

    elif menu == '5':
        print('프로그램 종료')
        sys.exit()
    else:
        print("메뉴 선택을 잘못하셨습니다.")