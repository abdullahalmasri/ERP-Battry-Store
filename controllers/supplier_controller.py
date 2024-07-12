from models.supplier import Supplier

class SupplierController:
    def __init__(self):
        self.suppliers = []

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
