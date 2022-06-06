alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"


def encrypt_caesar(msg, shift=3):
    результат = ""
    words = msg.split()
    для word in words:
        для char в списке(word):
            если char.lower() в алфавите:
                pos = alphabet.index(char.lower()) + shift
                если pos > 33:
                    pos -= 33
                если char.isupper():
                    результат += алфавит[pos].upper()
                ещё:
                    результат += алфавит[pos]
            ещё:
                результат += char
        результат += " "
    возвращает результат


def decrypt_caesar(msg, shift):
    результат = ""
    words = msg.split()
    для word in words:
        для char в списке(word):
            если char.lower() в алфавите:
                pos = alphabet.index(char.lower()) - сдвиг
                если pos > 33:
                    pos -= 33
                если char.isupper():
                    результат += алфавит[pos].upper()
                ещё:
                    результат += алфавит[pos]
            ещё:
                результат += char
        результат += " "
    возвращает результат


msg = "Да здравствует салат Цезарь!"
shift = 3
encrypted = encrypt_caesar(msg, shift)
decrypted = decrypt_caesar(шифрование, сдвиг)
печать(зашифрованная)
печать(расшифровка)