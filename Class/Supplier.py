class Supplier:
    def __init__(self, supplier_id, name, contact_info):
        self.supplier_id = supplier_id
        self.name = name
        self.contact_info = contact_info

    def display_information(self):
        return f"Supplier ID: {self.supplier_id}, Name: {self.name}, Contact Info: {self.contact_info}"