def add(a,b):   #함수지정
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    if b == 0:
        raise ZeroDivisionError() #만약 나누는 수가 0 이라면 에러를 출력  ZeroDivisionError는 직접 오류를 발생시키는 코드
    
    return a / b

def main():
    try:
       mode = input('계산 방식 입력(1:수식입력 2: 분해입력):')

       if mode == '1' :
             
             a, op, b = input("Enter expression: ").split() # 보너스 과제 한 줄로 수식을 입력하면 해당 수식을 해석하여 계산 결과를 출력하는 기능 split은 문자열을 공백 기준으로 문자열을 잘라 리스트로 만들어준다,
             a, b = float(a), float(b) #문자열 숫자 변환
       elif mode == '2' :
            a = float(input('첫번째 숫자 입력:'))
            op = input("연산자 입력(+, -, *, /):")
            b = float(input('두번째 숫자 입력:'))
       else:
            print("Invalid operator.")
            return

            
       ans = 0 #결과값 변수 초기화
       if op == '+':
            ans = add(a, b)
       elif op == '-':
            ans = subtract(a, b)
       elif op == '*':
            ans = multiply(a, b)
       elif op == '/':
            ans = divide(a, b)
       else:
            print("Invalid operator.")
            return
        
       print("결과:", ans)

    except ValueError:  #에러 
        print("잘못된 숫자 입니다")
    
    except ZeroDivisionError: #나누는값 0 에러
        print("Error: Division by zero.")
    
if __name__ == "__main__": #실행문,
    main()