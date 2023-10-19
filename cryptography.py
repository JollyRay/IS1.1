import random

class Cryptography2Bigram:

    def __init__(self, pathSrc: str, pathDst: str, key: int | None = None) -> None:

        """ Запоминаем пути к файлам и если нужно генерируем ключ шифрования """

        self.__pathSrc = pathSrc
        self.__pathDst = pathDst

        self.__crypKey = random.randint(0, 1707) if key is None else key

        self.__setup()

    def __setup(self) -> None:

        """ По ключу шифрования генерируем "кубы" для конвертации """

        self.__firstBigram = [i for i in range(256)]
        self.__secondBigram = [i for i in range(256)]

        random.Random(self.__crypKey).shuffle(self.__firstBigram)
        random.Random(self.__crypKey + 1).shuffle(self.__secondBigram)

    def crypt(self) -> None:

        """ Пользуемся нашей матрицей и зашифровываем """

        self.__pars()

    def uncrypt(self) -> None:

        """ Пользуемся нашей матрицей и расшифровываем """

        self.__pars(True)

    def __pars(self, isCryp: bool = False):

        """ Читаем из исходного файла 2 байта (биграмма), ищем их в матрицах(кубах).
        Если шифруем, то первый байт во второй матрице, а второй в первой, иначе наоборот.
        Если байт в файле нечётное количество, то последний шифруем отдельно, а второй игнорируем.
        Результаты поисков сразу заносим в файл для результатов."""

        srcFile = open(self.__pathSrc, "rb")
        dstFile = open(self.__pathDst, "wb")

        while (1):
            bigram = list(srcFile.read(2))

            if len(bigram) == 0:
                break

            if isCryp:
                out = self.__convert(bigram[0], bigram[1] if len(bigram) == 2 else None, self.__firstBigram, self.__secondBigram)
            else:
                out = self.__convert(bigram[0], bigram[1] if len(bigram) == 2 else None, self.__secondBigram, self.__firstBigram)

            bytesOut = bytes(out)

            dstFile.write(bytesOut)

            if len(bigram) == 1:
                break

        srcFile.close()
        dstFile.close()
        
    def __convert(self, value1: int, value2: int | None, bigram1: list[int], bigram2:list[int]) -> tuple:

        """ Тут мы ищем байты """

        if value2 is None:
            return (
                bigram1[bigram2.index(value1)],
            )
        else:
            return (
                bigram1[bigram2.index(value1)],
                bigram2[bigram1.index(value2)]
            )
        
    #################
    #               #
    #   PROPERTY    #
    #               #
    #################

    @property
    def crypKey(self) -> int:
        return self.__crypKey
    
    @crypKey.setter
    def crypKey(self, value: int) -> None:
        self.__crypKey = value
