from Class.discount_strategy import DiscountStrategy

class BulkDiscount(DiscountStrategy):
    def __init__(self, threshold: float, discount: float):
        self.threshold = threshold
        self.discount = discount

    def apply_discount(self, total: float) -> float:
        if total >= self.threshold:
            return total - self.discount
        else:
            return total