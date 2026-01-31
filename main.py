def hisobla(*soatlar):
    jami = 0
    for soat in soatlar:
        if soat <= 8:
            jami += soat * 100_000
        else:
            odatiy = 8
            qoshimcha = soat - 8
            jami += odatiy * 100_000 + qoshimcha * 200_000
    return f"Oyligingiz: {jami}"
print(hisobla(10,1,8,9))