from models.supplier import Supplier

class SupplierController:
    def __init__(self):
        self.suppliers = [
            Supplier(supplier_id=1, name='Supplier One', contact_info='contact1@example.com', performance_rating=4.5),
            Supplier(supplier_id=2, name='Supplier Two', contact_info='contact2@example.com', performance_rating=4.0),
            Supplier(supplier_id=3, name='Supplier Three', contact_info='contact3@example.com', performance_rating=3.5)
        ]

    def add_supplier(self, supplier):
        self.suppliers.append(supplier)

    def update_supplier(self, supplier_id, name, contact_info, performance_rating):
        supplier = self.find_supplier_by_id(supplier_id)
        if supplier:
            supplier.name = name
            supplier.contact_info = contact_info
            supplier.performance_rating = performance_rating

    def find_supplier_by_id(self, supplier_id):
        for supplier in self.suppliers:
            if supplier.supplier_id == supplier_id:
                return supplier
        return None
