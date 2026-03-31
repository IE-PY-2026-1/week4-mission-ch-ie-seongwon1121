# 파일이름 : 4주차
# 작 성 자 :60261941 박성원
list = []
res = input("맛집 리스트 입력: ")
res1 = input("맛집 리스트 입력: ")
res2 = input("맛집 리스트 입력: ")

list.append(res)
list.append(res1)
list.append(res2)
print(f'리스트: {list}')
print()

res4 = input("맛집 리스트 추가: ")
list.insert(0,res4)
print(f'리스트: {list}')
print()

input("도장 깨기: ")
list.remove("성심당")
print(f'리스트: {list}')