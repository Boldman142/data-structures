from src.stack import Node, Stack

if __name__ == '__main__':
    stack = Stack()
    stack.push('data1')
    data = stack.pop()

    # стэк стал пустой
    print(stack.top)
    assert stack.top is None

    # pop() удаляет элемент и возвращает данные удаленного элемента
    print(data)
    assert data == 'data1'

    stack = Stack()
    stack.push('data1')
    stack.push('data2')
    data = stack.pop()

    # теперь последний элемента содержит данные data1
    print(stack.top.data)
    assert stack.top.data == 'data1'

    # данные удаленного элемента
    print(data)
    assert data == 'data2'
