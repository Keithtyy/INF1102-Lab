from Class.discount_strategy import DiscountStrategy

class StudentDiscount(DiscountStrategy):
    def __init__(self, threshold: float, percentage: int, discount: float):
        self.threshold = threshold
        self.percentage = percentage
        self.discount = discount

    def apply_discount(self, total: float) -> float:
        if total >= self.threshold:
            return total - (total * self.percentage / 100) - self.discount
        else:
            return total