
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


# 명함수정
