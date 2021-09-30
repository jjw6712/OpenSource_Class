def findMax(a,b,c):
    if a>b:
        biger=a
    else:
        biger=b

    if c>biger:
        biger=c

    return biger


a=int(input("첫번째 숫자입력: "))
b=int(input("두번째 숫자입력: "))
c=int(input("세번째 숫자입력: "))

biger=findMax(a,b,c)

print(a,b,c,"중 가장 큰 수는", biger,"입니다.")
