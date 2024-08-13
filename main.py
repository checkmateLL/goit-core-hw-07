from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        super().__init__(value)
        

class Phone(Field):
    def __init__(self, value):
        if not self.validate(value):
            raise ValueError("Invalid phone number format. Should start from 0 and be 10 digits")
        super().__init__(value)

    def validate(self, value):
        # Validating phone number and raising exception if number is not 10 digits
        return len(value) == 10 and value.isdigit()      
        
   


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

        
    def add_phone(self, phone_number):
        self.phones.append(Phone(phone_number))

    def remove_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                self.phones.remove(phone)

    def edit_phone(self, old_phone, new_phone):
        phone = self.find_phone(old_phone)
        if not phone:
           raise ValueError
       self.add_phone(new_phone)
       self.remove_phone(old_phone)

        
    def find_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                return phone
        return None
            
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
        

class AddressBook(UserDict):

    # Adds new record to the address book
    def add_record(self, record):
        self.data[record.name.value] = record

    # Seaches for phone using name
    def find(self, name):
        return self.data.get(name, None)

    # Deletes phone
    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def __str__(self):
        if not self.data:
            return "Address book is empty"
        return "\n".join(str(record) for record in self.data.values())
