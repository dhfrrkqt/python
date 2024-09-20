# #############실습1###############
# a = int(input("첫 번째 숫자를 입력하세요 : "))
# b = int(input("두 번째 숫자를 입력하세요 : "))
# print(a , '+',  b, '=',  a+b)
# print(a , '-',  b, '=',  a-b)
# print(a , '*',  b, '=',  a*b)
# print(a , '/',  b, '=',  a/b)



# ##############실습2###############
# import turtle
# import random

# def leftClick(x, y): #좌클릭시 
#     global r, g, b
#     turtle.pencolor((r,g,b)) #색깔 
#     turtle.pendown() #펜 내리기 
#     turtle.goto(x,y) #x,y좌표로 펜이 이동

# def rightClick(x, y): #우클릭시
#     turtle.penup() #펜 들기
#     turtle.goto(x, y) #x,y좌표로 펜이 이동

# def midClick(x, y): #가운데 휠 클릭시 
#     global r,g,b
#     tSize = random.randrange(1, 10) #tSize = 1에서 9까지 중 임의의 정수 
#     turtle.shapesize(tSize) #거북이 사이즈 = tSize
#     r = random.random() #r에 0이상 1미만의 무작위 난수 넣기
#     g = random.random() #g에 0이상 1미만의 무작위 난수 넣기
#     b = random.random() #b에 0이상 1미만의 무작위 난수 넣기

# pSize = 10
# r, g, b = 0.0, 0.0, 0.0

# turtle.title('거북이로 그림 그리기')
# turtle.shape('turtle')
# turtle.pensize(pSize)

# #onscreenclick(함수이름, 번호 - 좌클릭=1,휠=2,우클릭=3)
# turtle.onscreenclick(leftClick,1) 
# turtle.onscreenclick(midClick, 2)
# turtle.onscreenclick(rightClick, 3)

# turtle.done()

