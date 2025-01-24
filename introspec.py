def introspection_info(obj):
    info = {
        'type': type(obj).__name__,  # Тип объекта
        'attributes': dir(obj),      # Все атрибуты и методы объекта
        'methods': [method for method in dir(obj) if callable(getattr(obj, method))],  # Только методы
        'module': obj.__class__.__module__  # Модуль, к которому принадлежит объект
    }
    return info

# Пример использования
class ExampleClass:
    def __init__(self):
        self.value = 42

    def example_method(self):
        return self.value

example_obj = ExampleClass()
print(introspection_info(example_obj))