class Stationery:
    title = 'paint'

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    def draw(self):
        print(f'{self.title}\nPen Pen Pen')


class Pencil(Stationery):
    def draw(self):
        print(f'{self.title}\nPencil Pencil Pencil')


class Handle(Stationery):
    def draw(self):
        print(f'{self.title}\nHandle Handle Handle')


pen = Pen()
pen.draw()

pencil = Pencil()
pencil.draw()

handle = Handle()
handle.draw()
