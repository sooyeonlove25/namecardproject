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