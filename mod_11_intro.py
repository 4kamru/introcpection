# ИНТРОСПЕКЦИЯ

from pprint import pprint
import inspect as ict

# импорт исследуемого модуля (кусочек из лекций) - его можно заменить на другой
import pikaev_2 as pk


# Предварительно смотрим, что есть в импортированном модуле:
# print(dir(pk))
# вывод в консоли такой:
# ['MyThread', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'threading', 'time']
# Возьмем для исследования 'MyThread'


def introspection_info(obj):
    dict_obj = {}
    res = ''
    # определим тип объекта
    dict_obj['type'] = type(obj)

    if ict.isclass(obj):
        list_attr = []

        # получаем атрибуты
        for attr in dir(obj):
            list_attr.append(getattr(obj, attr))

        # получаем методы
        list_methods = ict.getmembers(obj, predicate=ict.ismethod)

        # помещаем в словарь
        dict_obj['attributes'] = list_attr
        dict_obj['methods'] = list_methods

        # получаем модуль и сразу в словарь его!
        dict_obj['module'] = obj.__module__

        # если у объекта есть имя - то найдем его
        try:
            res = obj.__name__
        except (AttributeError, NameError):
            res = 'Нет имени '
        else:
            res = obj.__name__
        finally:
            # в любом случае надо вставить в словарь что-то
            dict_obj['__name__'] = res

        dict_obj['base_class'] = obj.__bases__

    return dict_obj


if __name__ == '__main__':
    # n = 42
    # obj = n
    obj = pk.MyThread
    intro_info = introspection_info(obj)
    # Питон словари по умолчанию выводит в алфавитном порядке.
    # чтобы он выводил в порядке добавления элементов, надо отключать сортировку
    pprint(intro_info, sort_dicts=False)
