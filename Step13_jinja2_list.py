from jinja2 import Template


my_template:str= '''
    친구 목록
    {% for name in friends %}
    - {{ name }}
    {% endfor %}
'''
# Template 객체 생성
temp:Template = Template(my_template)

# Template 객체의 render() 메소드 호출하면서 friends에 names 전달하기
names = ["김구라", "해골", "원숭이"]

result:str = temp.render(friends=names)

#결과 확인
print(result)