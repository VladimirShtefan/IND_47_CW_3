from datetime import datetime


class Operation:
    def __init__(
            self,
            date: str,
            state: str,
            amount: str,
            currency_name: str,
            description: str,
            from_: str,
            to: str,
    ):
        self.date = date
        self.state = state
        self.amount = amount
        self.currency_name = currency_name
        self.description = description
        self.from_ = from_
        self.to = to

    def get_iso_date(self) -> datetime:
        """

        :return:
        """
        return datetime.fromisoformat(self.date)

    def convert_date(self) -> str:
        """

        :return:
        """
        iso_date = self.get_iso_date()
        return iso_date.strftime("%d.%m.%Y")

    def mask_payment_info(self, payment_info: str) -> str:
        if payment_info.startswith("Счет"):
            return "**XXXX"
        return "XXXX XX** **** XXXX"

    def __gt__(self, other):
        return self.get_iso_date() > other.get_iso_date()

    def __lt__(self, other):
        return self.get_iso_date() < other.get_iso_date()

    def __str__(self):
        date = self.convert_date()
        from_ = self.mask_payment_info(self.from_)
        to = self.mask_payment_info(self.to)

        return (
            f"{date} {self.description}\n"
            f"{from_} -> {to}\n"
            f"{self.amount} {self.currency_name}\n"
        )
