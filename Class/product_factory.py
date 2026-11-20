from Class.product import Product
from Class.physical_product import PhysicalProduct
from Class.digital_product import DigitalProduct
from Class.subscription_product import SubscriptionProduct
from Class.supplier import Supplier


class ProductFactory:
    @staticmethod
    def create(product_type: str, supplier: Supplier, product_id: str, name: str, price: float, stock: int,size: float | str | None = None, ) -> Product:
        product_type = product_type.strip().lower()
        if product_type == "physical":
            if size is None:
                raise ValueError("PhysicalProduct requires a numeric size (weight in kg).")
            return PhysicalProduct(supplier, product_id, name, price, stock, product_type, float(size))
        elif product_type == "digital":
            if size is None:
                raise ValueError("DigitalProduct requires a numeric size (file size in MB).")
            return DigitalProduct(supplier, product_id, name, price, stock, product_type, float(size))
        elif product_type == "subscription":
            sub_size = "No size" if size is None else str(size)
            return SubscriptionProduct(supplier, product_id, name, price, stock, product_type, sub_size)
        else:
            raise ValueError(f"Unknown product type: {product_type}")
