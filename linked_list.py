class LinkedList:
    def __init__(self):
        self.index = 0
        self.linked_list = {}

    def insert(self, value, value_before):
        if len(self.linked_list) <= 0:
            self.linked_list['head'] = {'VALUE': value, 'POINTER': None}
            return self.linked_list['head']
        else:
            previous_pointer = None
            current_node_pointer = 'head'
            while True:
                if current_node_pointer is None:
                    self.linked_list[self.index] = {'VALUE': value,
                                                    'POINTER': self.linked_list[previous_pointer]['POINTER']}
                    self.linked_list[previous_pointer]['POINTER'] = self.index
                    self.index += 1
                    return self.linked_list[self.index - 1]
                else:
                    if self.linked_list[current_node_pointer]['VALUE'] == value_before:
                        self.linked_list[self.index] = {'VALUE': value,
                                                        'POINTER': self.linked_list[current_node_pointer]['POINTER']}
                        self.linked_list[current_node_pointer]['POINTER'] = self.index
                        self.index += 1
                        return self.linked_list[self.index - 1]

                previous_pointer = current_node_pointer
                current_node_pointer = self.linked_list[current_node_pointer]['POINTER']

    def pop(self):
        if len(self.linked_list) > 0:
            self.index -= 1
            return self.linked_list.pop(self.index)

    def delete(self, value):
        if len(self.linked_list) <= 0:
            return None
        else:
            previous_pointer = None
            current_node_pointer = 'head'
            while True:
                if current_node_pointer is None:
                    return None
                else:
                    if self.linked_list[current_node_pointer]['VALUE'] == value:
                        self.linked_list[previous_pointer]['POINTER'] = self.linked_list[current_node_pointer][
                            'POINTER']

                        return self.linked_list.pop(current_node_pointer)

                previous_pointer = current_node_pointer
                current_node_pointer = self.linked_list[current_node_pointer]['POINTER']

    def push(self, value):
        if len(self.linked_list) <= 0:
            self.linked_list['head'] = {'VALUE': value, 'POINTER': None}
            return self.linked_list['head']
        else:
            if self.index - 1 < 0:
                self.linked_list[self.index] = {'VALUE': value,
                                                'POINTER': None}
                self.linked_list['head']['POINTER'] = self.index
                self.index += 1
                return self.linked_list[self.index - 1]
            else:
                self.linked_list[self.index] = {'VALUE': value,
                                                'POINTER': None}
                self.linked_list[self.index - 1]['POINTER'] = self.index
                self.index += 1
                return self.linked_list[self.index - 1]

    def search(self, value):
        if len(self.linked_list) < 0:
            return None
        else:
            current_node_pointer = 'head'
            while True:
                if current_node_pointer is None:
                    return None
                elif self.linked_list[current_node_pointer]['VALUE'] == value:
                    return current_node_pointer

                current_node_pointer = self.linked_list[current_node_pointer]['POINTER']

    def get_linked_list(self):
        return self.linked_list

    def clear(self):
        self.linked_list = {}
