class Pixel:
    def __init__(self, x=0, y=0, red=0, green=0, blue=0):
        self._x = x
        self._y = y
        self._red = red
        self._green = green
        self._blue = blue

    def set_coords(self, x, y):
        self._x = x
        self._y = y

    def set_grayscale(self):
        num = (self._blue + self._green + self._red)/3
        self._blue = num
        self._green = num
        self._red = num

    def print_pixel_info(self):
        print ("x: " + str(self._x) + ", y: "+ str(self._y) + ", color: (" + str(self._red)+", "+ str(self._green)
               + " ," + str(self._blue) + ")")


if __name__ == '__main__':
    p = Pixel(5, 6, 250)
    p.print_pixel_info()
    p.set_grayscale()
    p.print_pixel_info()
