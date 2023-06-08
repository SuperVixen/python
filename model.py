class PhoneBook:

    def __init__(self, path: str = 'phones.txt'):
        self._phone_book: list[dict[str, str]] = []
        self._path = path
        self._last_id = 0

    def open(self):
        with open(self._path, 'r', encoding='UTF-8') as file:
            data = file.readlines()





        for contact in data:

            contact = contact.strip().split(':')
            new = {'id': contact[0], 'name': contact[1], 'phone': contact[2], 'comment': contact[3]}
            self._phone_book.append(new)
            self._last_id += 1

    def save(self):
        data = []

        for contact in self._phone_book:
            data.append(':'.join([value for value in contact.values()]))


        data = '\n'.join(data).strip()

        with open(self._path, 'w', encoding='UTF-8') as file:
            file.write(data)




    def load(self):
        return self._phone_book

    def add(self, new):
        self._last_id += 1
        new['id'] = str(self._last_id)
        self._phone_book.append(new)
        return new.get('name')

    def search(self, word: str):
        result: list[dict[str, str]] = []
        for contact in self._phone_book:
            for field in contact.values():
                if word.lower() in field.lower():
                    result.append(contact)
                    break
        return result

    def change(self, new: dict, index):
        for contact in self._phone_book:
            if index == contact.get('id'):
                contact['name'] = new.get('name', contact.get('name'))
                contact['phone'] = new.get('phone', contact.get('phone'))
                contact['comment'] = new.get('comment', contact.get('comment'))
                return contact.get('name')

    def delete(self, index):
        for contact in self._phone_book:
            if index == contact.get('id'):

                # приветствую возможно поможет такая история
                #
                # def delete(self, index):
                #     for contact in self._phone_book:
                #         if index == contact.get('id'):
                
                self._phone_book.remove(contact)
                
                # а может и не поможет:)
                
                return #contact.get('name')

    # def show(self):
    #     print('\n' + '=' * 71)
    #     for contact in self._phone_book:
    #         print(
    #             f'{contact.get("id"):>3}. {contact.get("name"):<20} | {contact.get("phone"):^20} | {contact.get("comment"):<20}')
    #     print('=' * 71 + '\n')
