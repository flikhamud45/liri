class MusicNotes():
    def __init__(self):
        self.teder_num = -1
        self.tedarim = [55, 61.74, 65.41,73.42,82.41,87.31,98,110,123.48,130.82,146.84,164.82,174.62,196, 220, 246.96
                        ,261.64, 293.68,329.64, 349.24, 392,440,493.92, 523.28, 587.36, 659.28, 698.48 ,784, 880,987.84,
                        1046.56,1174.72, 1318.56 ,1396.96,1568 ]

    def __iter__(self):
        return self

    def __next__(self):
        if self.teder_num >= len(self.tedarim) -1:
            raise StopIteration()
        self.teder_num +=1
        return self.tedarim[self.teder_num]

notes_iter = iter(MusicNotes())
for freq in notes_iter:
    print(freq)