age = int(input())
if age >= 18:
  print('Доступ разрешен')
elif age >= 14 and age <= 17:
  print('Доступ ограничен')
else:
  print('Доступ запрещен')
