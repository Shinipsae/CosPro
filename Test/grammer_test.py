# 8 이름에 특정 문자가 포함된 개수를 구하는 코드 작성
def solution8(name_list):
    answer = 0
    for name in name_list:
        for char in name:
            if 'A' in char or 'K' in char:
                answer += 1
                break
    return answer

names = ['Adios', "Kickboard Association", "google"]
ret = solution8(names)
print(f'solution8 함수의 반환값은 {ret}입니다.')