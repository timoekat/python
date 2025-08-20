from address import Address
from mailing import Mailing

to_address = Address("198334", "Санкт-Петербург", "ул. Шапошникова", "34", "33")
from_address = Address("198555", "Санкт-Петербург", "ул. Кирсанова", "55", "1")

mailing = Mailing(to_address, from_address, 5, "4567J")

print(f"Отправление {mailing.track} из {mailing.from_address.postalcode}, "
      f"{mailing.from_address.city}, {mailing.from_address.street}, "
      f"{mailing.from_address.house} - {mailing.from_address.flat} "
      f"в {mailing.to_address.postalcode}, {mailing.to_address.city}, "
      f"{mailing.to_address.street}, {mailing.to_address.house} - "
      f"{mailing.to_address.flat}. Стоимость {mailing.cost} рублей.")