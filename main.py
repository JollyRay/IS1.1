from cryptography import Cryptography2Bigram

def main():

    # Получаем имя исходного файла
    srcFileName = input("Введите имя исходно файла: ")
    # Получаем имя файла куда писать будем
    dstFileName = input("Введите имя файла для результатов: ")
    # Решаем зашифровываем или расшифровываем, если пользователь не понял, то зашифровываем
    isCryp = False if input("Зашифровать? (Y/n): ").lower() == 'n' else True
    # Активно пытаем получить от пользователя ключ шифрования, нам ведь нужно знать как расшифровывать
    if not isCryp:
        while 1:
            crypKey = input("Введите ключ для расшифровки: ").strip()
            if crypKey.isdigit():
                crypKey = int(crypKey)
                break
            else:
                print("Ключ должен состоять из цифр!")

    try:
        if isCryp:
            # Зашифровываем
            c1 = Cryptography2Bigram(srcFileName, dstFileName)
            c1.crypt()
            # Выводим ключ, чтобы потом пользователь мог расшифровать
            print("Ключ шифрования %d" % c1.crypKey)
        else:
            # Расшифровываем
            c2 = Cryptography2Bigram(srcFileName, dstFileName, crypKey)
            c2.uncrypt()
    except FileNotFoundError:
        print("Исходный файл не найден")
    except PermissionError:
        print("Упс, не хватает прав")

if __name__ == "__main__": main()