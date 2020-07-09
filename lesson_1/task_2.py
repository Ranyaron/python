time_seconds = int(input('Введите время в секундах: '))
hour = time_seconds // 3600
print(f'{hour:02}:{(time_seconds - hour * 3600) // 60:02}:{(time_seconds - hour * 3600) % 60:02}')
