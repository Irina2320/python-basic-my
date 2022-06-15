class MyDict(dict):

    my_dict = dict()

    def get(self, key, default=0):
        if key in my_dict:
            return my_dict[key]
        else:
            return default


my_dict = MyDict()
print(my_dict)
my_dict[5] = 3
print(my_dict)
print(my_dict.get(5))
print(my_dict.get(3))
my_dict.clear()
print(my_dict)