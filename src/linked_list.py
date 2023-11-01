class DictExcept(Exception):
    print("Данные не являются словарем или в словаре нет id.")


class Node:
    """Класс для узла односвязного списка"""

    def __init__(self, data, next_node):
        self.data = data
        self.next_node = next_node


class LinkedList:
    """Класс для односвязного списка"""

    def __init__(self):
        self.tail = Node(None, None)
        self.head = Node(None, self.tail)

    def insert_beginning(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с
         этими данными в начало связанного списка"""
        # try:
        #     assert isinstance(data, dict) is True
        # except AssertionError:  # В ридми сказано через ошибку TypeError
        #     # но как-то наверно тему не до конца понял, придумал как через
        #     # AssertionError сделать
        #     print("Данные не являются словарем или в словаре нет id.")
        # else:
        self.head = Node(data, self.head)
        if self.tail.data is None:
            self.tail = self.head

    def insert_at_end(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел
         с этими данными в конец связанного списка"""
        # try:
        #     assert isinstance(data, dict) is True
        # except AssertionError:
        #     print("Данные не являются словарем или в словаре нет id.")
        # else:
        new_data = Node(data, None)
        self.tail.next_node = new_data
        self.tail = new_data
        if self.head.data is None:
            self.head = self.tail

    def __str__(self) -> str:

        """Вывод данных односвязного списка в строковом представлении"""
        node = self.head
        if node.data is None:
            return str(None)

        ll_string = ''
        while node:
            if not node.data:
                break
            ll_string += f'{str(node.data)} -> '
            node = node.next_node

        ll_string += 'None'
        return ll_string

    def to_list(self):
        return str(self).split(" -> ")[:-1]

    def get_data_by_id(self, user_id):
        # all_item = str(self).split(" -> ")[:-1]
        # for item in all_item:
        #     if eval(item).get("id") == user_id:
        #         return eval(item)
        # return "Элемента с таким id нет"
        node = self.head
        while node:
            if not node.data:
                break
            try:
                # print(node.data.get("id"))
                assert node.data.get("id", TypeError) == user_id
            except TypeError:
                raise DictExcept
            except AttributeError:
                raise DictExcept
            except AssertionError:
                node = node.next_node
                continue
            else:
                return node.data
            # finally:
            #     node = node.next_node
