from faker import Faker


def mount_fake(faker: Faker, fake_term: str) -> Faker:
    fake_types = [
            ("name", faker.name()),
            ("job", faker.job()),
            ("cpf", faker.cpf()),
            ("email", faker.email()),
            ("color", faker.color_name()),
            ("city", faker.city()),
            ("country", faker.country()),
            ("country_code", faker.country_code()),
            ("street_address", faker.street_address()),
            ("street_name", faker.street_name()),
            ("estado", faker.estado_nome()),
            ("estado_sigla", faker.estado_sigla()),
            ("municipio", faker.street_address()),
            ("address", faker.address()),
            # ("loren", faker.loren()),
            ("company", faker.company()),
            ("credit_card", faker.credit_card_full()),
            ("currency", faker.currency()),
            ("currency_name", faker.currency_name()),
            ("currency_code", faker.currency_code()),
            ("price", faker.pricetag()),
            ("crypto", faker.cryptocurrency()),
            ("crypto_name", faker.cryptocurrency_name()),
            ("crypto_code", faker.cryptocurrency_code()),
            ("credit_card_number", faker.credit_card_number()),
            ("credit_card_provider", faker.credit_card_provider()),
            ("credit_card_security_code", faker.credit_card_security_code()),
            ("credit_card_expire", faker.credit_card_expire()),
            ("windows_version", faker.windows_platform_token()),
            ("mac_processor", faker.mac_processor()),
            ("mac_platform", faker.mac_platform_token()),
            ("linux_processor", faker.linux_processor()),
            ("linux_platform", faker.linux_platform_token()),
            ("ios_platform", faker.ios_platform_token()),
            ("android_platform", faker.android_platform_token()),
            ("decimal", faker.pydecimal()),
            ("int", faker.pyint()),
            ("float", faker.pyfloat()),
            ("str", faker.pystr()),
            ("bool", faker.pybool()),
            ("list", faker.pylist()),
            ("tuple", faker.pytuple()),
            ("dict", faker.pydict()),
            ("password", faker.password()),
            ("algarism", faker.century()),
            ("date_time", faker.date_time()),
            ("date", faker.date()),
            ("day_of_week", faker.day_of_week()),
            ("month", faker.month()),
            ("month_name", faker.month_name()),
            ("month_name", faker.month_name()),
            ("year", faker.year()),
            ("code", faker.localized_ean8()),
            ("cnpj", faker.cnpj()),
            ("time", faker.time()),
            ("service_phone_number", faker.service_phone_number()),
            ("phone", faker.phone_number()),
            ("cep", faker.postcode()),
            ("rg", faker.rg()),
            ("char_test", "ab")
        ]

    fake = list(filter(
        lambda x: x[0] == fake_term, fake_types
    ))

    # TODO: user customer error here
    if not fake:
        raise FileExistsError

    return fake[0][1]
