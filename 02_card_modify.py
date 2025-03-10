
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
