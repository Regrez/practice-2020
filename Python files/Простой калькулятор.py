while True:
  print("Инструкция")
  print("Введите '+' что бы сложить два числа")
  print("Введите '-'  чтобы вычесть два числа")
  print("Введите '*' чтобы умножить два числа")
  print("Введите '/' чтобы разделить два числа")
  print("Введите 'q' чтобы завершить программу")
  пользователь=input(": ")

  if пользователь == "q":
    break

  elif пользователь == "+":
    num1 = float(input("Введите число:"))
    num2 = float(input("Введите другое число:"))
    result = str(num1 + num2)
    print("ответ" + result)

  elif пользователь == "-":
    num1 = float(input("Введите число:"))
    num2 = float(input("Введите другое число:"))
    result = str(num1 - num2)
    print("ответ" + result)

  elif пользователь =="*":
    num1 = float(input("Введите число:"))
    num2 = float(input("Введите другое число:"))
    result = str(num1 * num2)
    print("ответ" + result)

  elif пользователь =="/":
    num1 = float(input("Введите число:"))
    num2 = float(input("Введите другое число:"))
    result = str(num1 / num2)
    print("ответ" + result)

  else:
    print("Неизвестный ввод")