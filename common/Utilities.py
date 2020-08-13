from faker import Faker


class FakeData:
    def __init__(self, credit_card=None, name=None, credit_card_expire_mouth=None,
                 credit_card_expire_year=None, csv=None):
        self.credit_card = credit_card
        self.name = name
        self.credit_card_expire_mouth = credit_card_expire_mouth
        self.credit_card_expire_year = credit_card_expire_year
        self.csv = csv

    @staticmethod
    def lets_random_bitchas():
        fake = Faker()
        return FakeData(credit_card=fake.credit_card_number(),
                        name=fake.name(),
                        credit_card_expire_mouth=fake.credit_card_expire()[0:2],
                        credit_card_expire_year=fake.credit_card_expire()[3:] + '20',
                        csv=fake.credit_card_security_code())

