class Queue:
    def __init__(self, queue=None):
        if queue is None:
            queue = []
        self._queue = queue

    def __str__(self):
        return str(self._queue)

    def __len__(self):
        return len(self._queue)

    def add_element(self, new_element):
        if type(new_element) == list:
            for el in new_element:
                self._queue.append(el)
        else:
            self._queue.append(new_element)

    def get_element(self):
        first_element = self._queue.pop(0)
        return first_element


relationships = {'Monica': ['Alexandra', 'Ronald', 'Mikhail'], 'Alexandra': ['Leila', 'Jasmine'],
                 'Ronald': ['Myles', 'Khristina', 'Jasmine', 'Ruslan'],
                 'Mikhail': ['Ruslan', 'Karina', 'Maria', 'Khristina'],
                 'Myles': ['Andrey', 'Yaroslav', 'Jasmine', 'Adelina'], 'Yaroslav': ['Polina', 'Anna', 'Timofey'],
                 'Ruslan': ['Georgiy', 'Fedor']}


def breadth_first_search(graph, start_element, desired):
    search_queue = Queue()
    try:
        search_queue.add_element(graph[start_element])
    except KeyError:
        print(f'Element {start_element} not found in graph')
    searched = []

    while search_queue:
        first = search_queue.get_element()
        if first not in searched:
            if first is desired:
                return True
            else:
                if first in graph:
                    search_queue.add_element(graph[first])
                searched.append(first)
    return False


print(breadth_first_search(relationships, 'M', 'Georgiy'))
