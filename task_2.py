def user_data(**kwargs):
    """Выводит данные о пользователе одной строкой."""
    for key, value in kwargs.items():
        print(f'{key}: {value}', end=", ")


user_data(name='Ilia', surname='Chechulin', year_birth=1992,
          city_residence='Krasnodar', email='ranyaron@mail.ru', telephone='+7(999)630-68-73')
