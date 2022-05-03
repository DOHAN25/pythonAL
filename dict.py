# 파이썬의 딕셔너리는 키/값 구조로 이루어져 있다.
# 입력 순서가 유지되며, 내부적으로는 해시 테이블로 구현되어 있다.
# 인덱스를 숫자로만 지정할 수 있는 리스트와 달리 딕셔너리는 문자를 포함해 다양한 타입을 키로 사용할 수 있다.
# 문자, 집합 등 불변 객체 모두를 키로 사용할 수 있다.

# 딕셔너리 선언
import collections

a = dict()

# 선언 2
a = {}

# 다음과 같이 key1, key2는 초기값으로 지정해 선언하거나 나중에 별도로 선언도 가능하다.
a = {'key1': 'value1', 'key2': 'value2'}
print(a)

a['key3'] = 'value3'
print(a)
# 딕셔너리에서는 존재하지 않는 키를 조회하면 KeyError 에러가 발생한다. try 구문으로 예외 처리도 가능하다.
try:
    print(a['key4'])
except KeyError:
    print("존재하지 않는 키 입니다.")

print('key4' in a)

if 'key4' in a:
    print("존재하는 키")
else:
    print('존재하지 않는 키')
print('-----------')

# 딕셔너리에 있는 키/값은 for 반복문으로도 조회가 가능하다. items() 메소드를 사용하면 키와 값을 각각 꺼내올 수 있다.
for k,v in a.items():
    print(k,v)

# del 로 삭제한다.
del a['key1']
print(a)

# 딕셔너리 모듈
# 딕셔너리와 관련된 특수한 형태의 컨테이너 자료형인 defaultdict, Counter, OrderedDict
print('-----------')
# defaultdict 객체
# defaultdict 객체는 존재하지 않는 키를 조회할 경우, 에러 메시지를 출력하는 대신 디폴트 값을 기준으로
# 해당 키에 대한 딕셔너리 아이템을 제공해준다
a = collections.defaultdict(int)
a['A'] = 5
a['B'] = 4
print(a)
a['C'] += 1
print(a)
# C는 존재하지 않는 키다. 원래의 딕셔너리라면 앞서 살펴본 것처럼 KeyError가 발생하겠지만, defaultdict 객체는 에러 없이 바로 +1
# 연산이 가능하고 이 경우 디폴트인 0을 기준으로 자동 생성한 후 여기에 1을 더해 최종적으로 1이 만들어진다.

# Counter 객체
# Counter 객체는 아이템에 대한 개수를 계산해 딕셔너리로 리턴한다.
a = [1, 2, 3, 4, 5, 5, 6, 6]
b = collections.Counter(a)
print(b)
# Counter 객체는 이처럼 키에는 아이템의 값이, 값에는 해당 아이템의 개수가 들어간 딕셔너리를 생성한다.
# Counter 객체에서 가장 빈도 수가 높은 요소는 어떻게 추출할 수 있을까?
# most_common()을 사용하면 된다.
print('-------')
print(b.most_common(2))
# 가장 빈도가 높은 2개의 요소추출

# OrderedDict 객체
# 대부분의 언어에서 해시 테이블을 이용한 자료형은 입력 순서가 유지되지 않는다.
# 입력값을 부여할 경우 OrderedDict는 입력 그대로 순서가 유지된다.





