def findMax(a,b,c):
    if a>b:
        big=a
    else:
        big=b

    if c>big:
        big=c

    return big


a=int(input("첫번째 숫자입력: "))
b=int(input("두번째 숫자입력: "))
c=int(input("세번째 숫자입력: "))

big=findMax(a,b,c)

print(a,b,c,"중 가장 큰 수는", big,"입니다.")
