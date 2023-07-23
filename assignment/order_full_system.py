

class Order:
    def __init__(self, order_id: str, list: list, status: str) -> str:
        self.order_id = order_id
        self.list = list
        self.status = status


class OrderFulfillmentSystem():
    def __init__(self):
        self.order = {}

    def place_order(self, id, order: list) -> int:
        self.order["items"] = order
