from jinja2 import Template

info:dict = {
    "num":1,
    "name":"김구라",
    "body":{
        "height": 180,
        "weight": 80
    },
    "hobby":["피아노","당구","프로그래밍"]
}

'''
    위의 info 안에 들어 있는 데이터를 이용해서 아래와 같은 형식의 문자열을 출력해 보세요.

    번호: 1
    이름: 김구라
    키: 180 cm
    몸무게: 80 kg
    취미 : 
        - 피아노   
        - 당구  
        - 프로그래밍
'''

my_template = '''   
        번호: {{ num }}
        이름: {{ name }}
        키: {{ body.height }} cm
        몸무게: {{ body.weight }} kg
        취미 :
        {% for item in hobby %} 
        - {{ item }}
        {% endfor %}  
'''
# Template 객체생성
temp:Template = Template(my_template)
# Template 객체의 render() 메소드를 이용해서 랜더링한다.
result = temp.render(info)
print(result)