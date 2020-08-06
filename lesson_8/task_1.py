class Data:
    @classmethod
    def number(cls, data):
        valid = cls.validation(data)
        my_list = []
        for i in valid:
            my_list.append(int(i))
        print(my_list)

    @staticmethod
    def validation(data):
        data_list = data.split("-")
        if int(data_list[0]) > 31:
            print("дата не может быть > 31")
        if int(data_list[1]) > 12:
            print("месяц не может быть > 12")
        if int(data_list[2]) > 2020:
            print("год не может быть > 2020")
        return data_list


my_data = Data()
my_data.number("21-13-1992")
