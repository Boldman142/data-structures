class Node:
    """Класс для узла стека"""


    def __init__(self, data = None, next_node = None):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


    def __str__(self):
        return str(self.data)


class Stack:
    """Класс для стека"""


    def __init__(self):
        """Конструктор класса Stack"""
        self.top = None


    def push(self, data):
        """
        Метод для добавления элемента на вершину стека

        :data: данные, которые будут добавлены на вершину стека
        """


        next = self.top
        new = Node(data, next)
        self.top = new
        # new = Node(data)
        # self.top = Node(new, self.top)


    def pop(self):
        """
        Метод для удаления элемента с вершины стека и его возвращения

        :return: данные удаленного элемента
        """
        if self.top is None:
            return None
        pop_ = self.top.data
        self.top.data = self.top.next_node
        return pop_
