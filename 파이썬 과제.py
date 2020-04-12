import random

top1=0
top2=0
best=0

while True:
    print("""UP & DOWN 게임에 오신걸 환영합니다~
1. 게임시작 2. 기록확인 3. 게임종료""")
    menu = int(input(">>"))
    if menu == 1:
        num = random.randint(1,100)
        maxNum = 100
        miniNum = 1
        for i in range(0,10):
            expectNum = int(input("%d번째 숫자 입력(%d~%d)" %(i+1,miniNum,maxNum)))
            if num == expectNum:
                print("""정답입니다!!
%d번째만에 맞추셨습니다""" %(i+1))
                result=i+1
                if best == 0:
                    best = result
                    top1= best
                    print("최고기록 갱신~!")
                elif best > result:
                    top1 = result
                    top2=best
                    best = result
                    print("최고기록 갱신~!")
                elif best < result:
                    top2 = result
                break
            elif num > expectNum:
                print("UP")
                if miniNum < expectNum:
                    miniNum = expectNum
            elif num < expectNum:
                print("DOWN")
                if maxNum > expectNum:
                    maxNum = expectNum
    elif menu == 2:
        if top1 == 0:
            print("")
        elif top2 == 0:
            print("1. %d" %top1)
        else:
            print("""1. %d
2. %d""" %(top1,top2))
    elif menu == 3:
        break
    else:
        print("다시 입력하여 주십시오")
