# 두개의 딕셔너리에서 동일 값, 동일 키를 얻어오기

x = {
    "a": 100,
    "b": 200,
    "c": 300
}

y = {
    "c": 300,
    "d": 200,
    "a": 120
}

#키와 값이 동일한 아이템을찾기
xy_val = x.items()&y.items()
print(xy_val)

# 특정 키 값을 제거한 새로운 딕셔너리 만들기

z = { key:x[key] for key in x.keys() - {'b','c'}}
print(z)

z = { key:y[key] for key in y.keys() - {"b", "c"}}
print(z)