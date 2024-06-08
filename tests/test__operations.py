def test__convert_date(operations_instance):
    assert operations_instance.convert_date() == "26.08.2019"


def test__mask_payment_info(operations_instance):
    assert operations_instance.mask_payment_info(
        operations_instance.from_
    ) == "**XXXX"
    assert operations_instance.mask_payment_info(
        operations_instance.to
    ) == "XXXX XX** **** XXXX"
