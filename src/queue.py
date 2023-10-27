class Node:
    """Класс для узла очереди"""

    def __init__(self, data, next_node):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Queue:
    """Класс для очереди"""

    def __init__(self):
        """Конструктор класса Queue"""
        self.tail = Node(None, None)
        self.head = Node(None, self.tail)
        self.all = []

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        return "\n".join(self.all)

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """

        new_data = Node(data, None)

        if self.head.data is None:
            self.head = new_data
            self.tail = new_data
            self.all.append(data)
        else:
            self.tail.next_node = new_data
            self.tail = new_data
            self.all.append(data)

    def dequeue(self):
        """
        Метод для удаления элемента из очереди.
        Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        if self.head is None:
            return None
        prop = self.head.data
        self.head = self.head.next_node
        return prop
