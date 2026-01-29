def hissobla(soat):
    if soat <= 8:
        return soat * 100
    else:
        odatiy = 8
        qoshimcha = soat - odatiy

        hammasi = odatiy * 100_000 + qoshimcha * 200_000
        return f"oyligingiz: {hammasi}"


user_vaqti = int(input("Ishlagan vaqtingizni kiriting: "))

print(hissobla(user_vaqti))
