"""Файл для хранения фейковых данных."""
from typing import Any

from faker import Faker


class FakeData:
    """Класс фейковых данных."""

    def __init__(
        self,
        credit_card: str = None,
        name: str = None,
        credit_card_expire_mouth: int = None,
        credit_card_expire_year: int = None,
        csv: int = None,
        text: str = None,
        title: str = None
    ) -> None:
        self.credit_card = credit_card
        self.name = name
        self.credit_card_expire_mouth = credit_card_expire_mouth
        self.credit_card_expire_year = credit_card_expire_year
        self.csv = csv
        self.credit_card_expire_date = (
            str(self.credit_card_expire_mouth) + "/" + str(self.credit_card_expire_year)
        )
        self.text = text
        self.title = title

    @staticmethod
    def lets_random_bitchas() -> Any:
        """Метод возвращает экземляр класса FakeData."""
        fake = Faker()
        return FakeData(
            credit_card=fake.credit_card_number(),
            name=fake.name(),
            credit_card_expire_mouth=fake.credit_card_expire()[0:2],
            credit_card_expire_year=fake.credit_card_expire()[3:] + "20",
            csv=fake.credit_card_security_code(),
            text=fake.text(max_nb_chars=1000),
            title=fake.sentence()
        )