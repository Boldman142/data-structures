class Node:
    """Класс для узла стека"""

    def __init__(self, data=None, next_node=None):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node

    # def __repr__(self):
    #     return self.data


class Stack:
    """Класс для стека"""

    def __init__(self):
        """Конструктор класса Stack"""
        self.top = None

    def __str__(self):
        if self.top is None:
            return "Стэк пустой"
        else:
            return f"{self.top.data} next({self.top.next_node})"

    def push(self, data):
        """
        Метод для добавления элемента на вершину стека

        :data: данные, которые будут добавлены на вершину стека
        """

        next_ = self.top
        new = Node(data, next_)
        self.top = new

    def pop(self):
        """
        Метод для удаления элемента с вершины стека и его возвращения

        :return: данные удаленного элемента
        """
        if self.top is None:
            return None
        pop_ = self.top.data
        self.top = self.top.next_node
        return pop_

# q = Stack()
# print(q)
# q.push(1)
# print(q)
# q.push(2)
# print(q)
# q.push(3)
# print(q)
