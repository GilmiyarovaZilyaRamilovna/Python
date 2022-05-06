import re

t = 'https://yandex.ru/text=images/search?source=images_drawing&text=котики'
print(re.search('text=(\w+)&', t)[1])
