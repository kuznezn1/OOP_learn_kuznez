import sys

class StreamData:
    def create(self, fields, lst_values):
        if len(fields) != len(lst_values):
            return False
        else:
            for indx,name in enumerate(fields):
                setattr(self,str(name),lst_values[indx])
            return True

class StreamReader:
    FIELDS = ('id', 'title', 'pages')

    def readlines(self):
        lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
        sd = StreamData()
        res = sd.create(self.FIELDS, lst_in)
        return sd, res


sr = StreamReader()
data, result = sr.readlines()