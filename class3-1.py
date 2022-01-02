## 시퀀스형
# 컨테이너(container : 서로다른 자료형[List, tuple, collections.deque])
# 플랫(Flat : 한개의 자료형[str, bytes, bytearray, array.array, memoryview])
# 가변(list, bytearray, array.array, memoryview, deque)
# 불변(tuple, str, bytes)
# 리스트 및 튜플 고급

# 지능형 리스트(Comprehending lists)
chars = '+_)(*&^%$#@!)'
print(dir(chars))


code_list1 = []

for s in chars:
    # 유니코드 리스트
    code_list1.append(ord(s))

print(code_list1)

# (Comprehending lists)
code_list2 = [ord(s) for s in chars]

print(code_list2)


# Comprehending lists + Map, Filter
code_list3 = [ord(s) for s in chars if ord(s) > 40]
code_list4 = list(filter(lambda x : x > 40, map(ord, chars)))
print()
print("###############전체 출력###############")
print(code_list1)
print(code_list2)
print(code_list3)
print(code_list4)
print([chr(s) for s in code_list1])
print([chr(s) for s in code_list2])
print([chr(s) for s in code_list3])
print([chr(s) for s in code_list4])

print()
print()


# Generator 생성
## 시퀀스 값을 만들고 로컬 상태를 유지하며 다음에 반환할 값을 가지고 있음
### __iter__ : for 문으로 진행할수 있음  
import array

# Generator : 한 번에 한 개의 항목을 생성(메모리 유지X)
tuple_g = (ord(s) for s in chars)
array_g = array.array('I', (ord(s) for s in chars))

print(type(tuple_g))
print(next(tuple_g))
print(array_g)
print(type(array_g))
print(array_g.tolist())

print()
print()

# 제네레이터 예제
print(('%s' % c +str(n) for c in ['A','B','C','D'] for n in range(1,21)))
for s in ('%s' % c +str(n) for c in ['A','B','C','D'] for n in range(1,21)):
    print(s)

print()
print()

# 리스트 주의
## 깊은 복사 얕은 복사
marks1 = [['~'] * 3 for _ in range(4)]
marks2 = [['~'] * 3] * 4
print(marks1)
print(marks2)

marks1[0][1] = 'X'
marks2[0][1] = 'X'
print(marks1)
print(marks2)

# 증명 
print([id(i) for i in marks1])
print([id(i) for i in marks2])