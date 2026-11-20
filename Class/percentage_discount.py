from Class.discount_strategy import DiscountStrategy

class PercentageDiscount(DiscountStrategy):

    def __init__(self, percentage: int):
        self.percentage = percentage

    def apply_discount(self, total: float) -> float:
        return total - (total * self.percentage / 100)