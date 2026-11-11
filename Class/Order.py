from Class.OrderLine import OrderLine
from Class.Product import Product

class Order:
    
    def __init__(self, order_id: str) -> None:
        self.__order_id = order_id
        self.__order_lines: list[OrderLine] = []

    def get_order_id(self) -> str:
        return self.__order_id

    def get_order_lines(self) -> list[OrderLine]:
        return list(self.__order_lines)

    def add_order_line(self, product: Product, quantity: int) -> None:
        order_line = OrderLine(product, quantity)
        self.__order_lines.append(order_line)

    def remove_order_line(self, product_id: str) -> None:
        for order_line in self.__order_lines:
            if order_line.get_product().get_product_id() == product_id:
                self.__order_lines.remove(order_line)
                return
        print("Order line not found.")

    def calculate_total(self) -> float:
        total = 0.0
        for order_line in self.__order_lines:
            total += order_line.calculate_subtotal()
        return total

    def display_order(self) -> str:
        lines = [f"Order ID: {self.__order_id}"]
        if not self.__order_lines:
            lines.append("  (No order lines)")
        else:
            for order_line in self.__order_lines:
                lines.append(f"  - {order_line.display_information()}")
        lines.append(f"Order Total: ${self.calculate_total():.2f}")
        return "\n".join(lines)