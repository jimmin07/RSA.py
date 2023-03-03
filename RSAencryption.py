##RSA algorithm-encryption
##간략 소개: RSA는 최대공약수, 소수 등을 사용한 암호화 방법.
#공개키, 개인키, 두 소수 p, q로 이루어짐. 사용한 개념은 간단한 수학 개념!

#두 소수 p, q 입력받기
p = int(input("첫번쨰 소수: "))
q = int(input("두번쨰 소수: "))

#기본 틀 짜기 (기본 상수, 유클리드 호제법 함수-최대공약수 구하기)
n = p * q
T = (p -1) * (q-1)

def Euler(a, b):
    while b != 0:
        a, b = b, a%b
    return a

#publickey(e) 함수
def publickey():
    global T
    e =2
    while e < T and Euler(e, T) != 1:
        e += 1
    return e

#privatekey(d)
def privatekey():
    global e
    global T
    d = 1
    while (publickey() * d) % T != 1 or d == publickey():
        d += 1
    return d

#암호화할 숫자열 input 받기
arr = int((input("암호화할 숫자열: ")))

#암호화 과정: 모듈러 연산 사용
encr = ((arr**publickey())%n)

#암호화된 숫자열, publickey, privatekey print
print("암호문 : {}".format(encr))
print("공개키 : {}".format(publickey()))
print("개인키 : {}".format(privatekey()))

##아스키코드 변환과정 추가 예정!