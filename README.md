
# name = input('이름을 입력하세요 >>> ')
# email = input('이메일을 입력하세요 >>> ')
# number = input('전화번호를 입력하세요 >>> ')
# email = input('이메일을 입력하세요 >>> ')
# job = input('직책을 입력하세요 >>> ')
# group = input('부서를 입력하세요 >>> ')
# namecardproject
display = '''
----------------------------------------------------------
1. 명함 입력, 2. 명함 수정, 3. 명함 삭제, 4. 명함 목록 보기, 5. 종료
----------------------------------------------------------
메뉴를 선택하세요 >>> '''
card_display = '''
--------------------------------------------------------------
1. 이름, 2. 전화번호, 3. 소속 4. email #5. 종료
--------------------------------------------------------------
메뉴 번호를 선택하세요 >>> '''



# 명함 정보를 저장할 리스트
names = []
phones = []
companies = []
email = []
list = [names, phones, companies, email]
card_list = []

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
while True:
    email = input('이메일 >>>')
    check = 0
    for index in range(len(card_list))
        if card+list[index][3] == email:
        check = 1
        break
card_list.append([name, tel, address, email])


# 명함수정
# 명함수정 강주현
    elif menu == 2 :
        print(card_display)
# ?? card_num = int(input('수정할 명함의 번호 입력 >')) >> 강사님은 email로 판별
while True : 
email = input('이메일 >>>')
check = 0
    for index in range(len(card_list)):
        if card_list[index][3] == email :
        check = 1
        break
    if check == 0
    break
card_list.append([name, tel, address, email])
print(card_list)
    elif menu == '2'
    print('명함수정')
    email = input('수정할 데이터의 이메일을 입력')
    check = 0
for index in range(len(card_list)):
    if card_list[index][3] == email:
    check = 1
while True:
    item = input('수정할 항목을 선택하세요(1. 이름 2. 전화번호, 3.주소, 4. 종료)')
if item == '4':
    break
    item = int(item)
    if item in (1,2,3):
    card_list[index][item-1] = input('수정할 값을 입력 >>')
 
if check == 0
print("데이터가 없습니다")
elif menu == 3
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

# elif menu == 2
# print("명함 수정")
# email



# 명함삭제 이수연
    elif menu == 3 :
        print('명함 삭제')

# email = input("삭제할 데이터의 이메일을 입력하시오")
# check = 1
# for index in range(len(card_list)): 
# if card_list[index][2] == email: 
# print('삭제 >>> ', card_list.pop(index))
# break
# if check == 0:
# print("데이터가 없습니다.")
# if


    elif menu == '4':
        print('명함 목록 보기')
        if 명함: 
         for person in 명함:
                print(person)
# print("-"*50)

# for card in card_list
# print(f'(card[0]:10),(card[1]:10),(card[2]:20))

# print("-"*50)

    elif menu == '5':
        print('프로그램 종료')
        sys.exit()

 else:
    print('메뉴를 잘못 선택하셨습니다. 다시 선택해주세요.\n')

    