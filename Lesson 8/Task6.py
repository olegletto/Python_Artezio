#   Напишите шаблон регулярного выражения, который соответствует вопросительным
#   предложениям, в которых одно слово (более 2 символов) повторяется 4 или более раз.

words = r"?=(\b[a-z]{2,}){4,}\?&"