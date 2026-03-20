'''
    1. 클래스를 객체를 생성할 수 있는 설계도 역할
    2. Data type의 역할
    
    객체는 속성(저장소)와 기능(함수) 로 이루어 진다.
'''
class Car:
    def drive(self):
        print("달려요!")

if __name__ == "__main__":
    #Car() 는 Car 클래스로 객체(인스턴스)를 생성하는 표현식이다
    c1: Car = Car()
    c1.drive()
    #필요한 만큼 객체를 생성할 수 있다.
    c2: Car = Car()
    c3: Car = Car()
