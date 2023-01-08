# words=["abc","defg", "i"]
# words_gr_1=filter(lambda v: len(v)>1, words)
# print(words_gr_1)
# a=list(words_gr_1)
# print(a)
# print(tuple(words_gr_1))

# for v in filter(lambda v: len(v)>1, words):
#     print(v)

# names=["ab", "c"]
# ids=['1',"2"]
# data=zip(names, ids)
# print(dict(data))
# print(list(data))
# print(list(zip(names,ids)))


# def f(data):
#     v=0
#     for e in data:
#         for el in e:
#             if el=='.':
#                 break
#             v+=1
#     return v    

# print(f("qwe.r a.sdf .zxcv")) #14

# print(f("qwe.r a.sdf .zxcv".split())) #4

# def f(data):
#     # for e in data:
#     #     tmp=e.split() ##сломается когда дойдем до пробела
#     #     a=tmp[-1]
#     return [e.split()[-1] for e in data]
# s="""Раз два стр
# че ты
# пя"""

#print(f(s).split("\n")) # тут последние слова были бы, но скобки не так

# try:           # oops done
#     print(f(s))
# except:
#     print("oops")
# finally:
#     print("done")


# def f(data):
#     try:
#         return [e.split()[-1] for e in data]
#     except:
#         return "oops-1"
#     finally:
#         return "done-1"
# s="""Раз два стр
# че ты
# пя"""

# try:
#     print(f(s))
# except:
#     print("oops-2")
# finally:
#     print("done-2")


# def f(data, number):
#   return [index for index, value in enumerate(data) if number // int(value) < 1]

# print(f("123 234 12 21 1 2".split(), 2))  #[0,1,2,3]


# def f(data, number):
#   try:
#     ans=[]
#     for index, value in enumerate(data):
#         if number // int(value) < 1:
#             ans.append(index)
#   #  return [index for index, value in enumerate(data) if number // int(value) < 1]
#   except:
#     print("oops-f-1")
#     return "oops-f-2"
#   finally:
#     print("done-f-1")

# try:
#   print(f("123 234 12 21 1 2", 2))
# except:
#   print("oops")
# finally:
#   print("done") 
# oops-f-1
# done-f-1
# oops-f-2
# done

s = """однажды в студеную зимнюю пору
Я из лесу вышел
Был сильный мороз"""
def f(data,frm, to):
    result =0
    for elem in data:
        parts = elem.split()
        result+=len(parts)
        print("".join(parts[frm:to]))
    return result

for e in s.split("\n"):
    print(f(e,1,-1))


# вход: текстовый файл
# фикс. имя файла
# прочитать этот файл и посчитать для каждого числа посчитать кол-во слов с такой длинной
# точки и запятые: все удалить из слов 
# `adsadsa.` -> "adsadsa", удалить все что снаружи слова
# вывод: по возрастанию

# 15:50