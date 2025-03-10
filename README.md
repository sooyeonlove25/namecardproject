
# name = input('이름을 입력하세요 >>> ')
# email = input('이메일을 입력하세요 >>> ')
# number = input('전화번호를 입력하세요 >>> ')
# email = input('이메일을 입력하세요 >>> ')
# job = input('직책을 입력하세요 >>> ')
# group = input('부서를 입력하세요 >>> ')
# namecardproject
# display = '''
----------------------------------------------------------
1. 명함 입력, 2. 명함 수정, 3. 명함 삭제, 4. 명함 목록 보기, 5. 종료
----------------------------------------------------------
메뉴를 선택하세요 >>> '''




명함 정보를 저장할 리스트
names = []
phones = []
companies = []




while True:
    menu = input(display).strip()




    # 1. 명함 입력
    if menu == '1':
        print("명함입력")
        name_tmp = input("이름: ").strip()




        names.append(name_tmp)
        phones.append(input("전화번호: ").strip())
        companies.append(input("소속: ").strip())




        print(f"{name_tmp}님의 명함이 추가되었습니다.")



# 명함수정
# 명함수정 강주현
elif menu == 2 :
        print(card_display)
        list_num = input('수정할 명함의 번호 입력 >')
        number = int(input('수정할 부분 번호 입력 >'))
        if number == 1 :
            card_list[list_num-1][0] = input('수정할 이름 입력>')
        if number == 2 :
            card_list[list_num-1][1] = input('수정할 이메일 주소 입력 >')
        if number == 3 :
            card_list[list_num-1][2] = input('수정할 전화번호 입력 >')
        if number == 4 :
            card_list[list_num-1][3] = input('수정할 직장 또는 학교 입력 >')
       
        print("명함이 수정되었습니다", card_list[list_num-1])

# 이수연 수정
display = '''
------------------------------------------------------------------------------------
1.명함입력, 2.명함수정, 3.명함삭제, 4.명함목록, 5.종료
------------------------------------------------------------------------------------
메뉴를 선택하세요 >>> '''

card_list = []
menu = ''
while True:
    menu = input(display)
# 1. 명함 입력  
    if menu == '1':
        print("명함입력")
         name_tmp = input("이름: ").strip()
         phone_tmp = input("전화번호: ").strip()
         email_tmp = input("이메일: ").strip()
         address_tmp = input("주소: ").strip()

        print(f"{name_tmp}님의 명함이 추가되었습니다.")
    
     # 명함 정보를 하나의 리스트
    card = [name_tmp, phone_tmp, email_tmp, address_tmp]
    cards.append(card)

# 2. 명함 수정
    elif menu == '2':
        print("명함 수정")
        print(card_display)


# 3. 명함 삭제
    elif menu == '3':
        print('명함 삭제')
        email = input('삭제할 데이터의 이메일을 입력 >>> ')
        check = 0  # 데이터가 있는지 여부를 확인할 변수

    # 인덱스를 뒤에서부터 확인 (pop 시 인덱스 변화 문제 방지)
    for index in range(len(card_list)):
        if card_list[index][2] == email:  # 이메일이 card_list의 세 번째 항목에 있음
            check = 1
            print('삭제 >>> ', card_list.pop(index))  # 해당 항목 삭제
            break  # 이메일을 찾은 후에는 반복문을 종료
    
    if check == 0:  # 삭제되지 않았을 경우
        print('해당 이메일을 가진 데이터가 없습니다.')

    #  명함 목록을 저장한 리스트 -> 이름, 전화번호, 이메일, 주소

# 4. 명함 목록
    elif menu == '4':
    print('명함목록보기')
    print('=' * 30)
    for card in card_list:
        print(f'{card[0]:10} {card[1]:15} {card[2]:10} {card[3]:10}')
    print('=' * 30)
# card_list 안의 각 항목(명함)을 하나씩 card에 대입하며 반복 -> ['이름', '전화번호', '이메일', '주소']
# 10자리로 맞추어서 출력, 15자리로 맞추어서 출력, 10자리로 맞추어서 출력, 10자리로 맞추어서 출력
# 10자보다 짧다? -> 오른쪽 -> 공백추가 -> 자리 차지(10자리)

# 5. 종료
elif menu == '5':
    print('프로그램 종료')
    sys.exit()
else:
    print('메뉴선택을 잘못하셨습니다.')