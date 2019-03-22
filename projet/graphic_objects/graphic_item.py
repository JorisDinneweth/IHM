class GraphicItem:
    def __init__(self, pos, size):
        self.__x, self.__y = self.__pos = pos
        self.__size = self.__width, self.__height = size

    def _get_pos(self):
        return self.__pos

    def _set_pos(self, new_pos):
        self.__x, self.__y = self.__pos = new_pos

    def _get_x(self):
        return self.__x

    def _set_x(self, x):
        self.__x = x
        self.__pos = self.__x, self.__y

    def _get_y(self):
        return self.__y

    def _set_y(self, y):
        self.__y = y
        self.__pos = self.__x, self.__y

    def _get_size(self):
        return self.__size

    def _set_size(self, size):
        self.__size = self.__width, self.__height = size

    def _get_width(self):
        return self.__width

    def _set_width(self, w):
        self.__width = w
        self.__size = self.__width, self.__height

    def _get_height(self):
        return self.__height

    def _set_height(self, h):
        self.__height = h
        self.__size = self.__width, self.__height

    x = property(_get_x, _set_x)
    y = property(_get_y, _set_y)
    pos = property(_get_pos, _set_pos)
    width = property(_get_width, _set_width)
    height = property(_get_height, _set_height)
    size = property(_get_size, _set_size)
