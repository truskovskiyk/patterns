from abc import ABCMeta, abstractmethod


class AbsDocumentComponents(metaclass=ABCMeta):

    @abstractmethod
    def gather_data(self):
        pass

    @abstractmethod
    def add_component(self, document_components):
        pass

class CustomerDocumentComponent(AbsDocumentComponents):

    def __init__(self, custome_id):
        self.custome_id = custome_id

    def gather_data(self):
        if self.custome_id == 41:
            customer_data = 'some with id 41'
        else:
            customer_data = 'some with id UNK'
        return "<Customer>{}</Cutomer>".format(customer_data)

    def add_component(self, document_components):
        print("Cannot add to leaf..")

class DocumentComponent(AbsDocumentComponents):

    def __init__(self, name):
        self.name = name
        self.doc_components = []

    def gather_data(self):
        components = " ".join([x.gather_data() for x in self.doc_components])
        return "<{}>".format(self.name) + components + "</{}>".format(self.name)

    def add_component(self, document_components):
        self.doc_components.append(document_components)

if __name__ == '__main__':
    main = DocumentComponent('main')

    head = DocumentComponent('head')
    head_text = DocumentComponent('head_text')
    head.add_component(head_text)

    body = DocumentComponent('body')
    order1 = DocumentComponent('order1')
    order2 = DocumentComponent('order2')
    order3 = DocumentComponent('order3')
    body.add_component(order1)
    body.add_component(order2)
    body.add_component(order3)

    main.add_component(head)
    main.add_component(body)
    print(main.gather_data())
