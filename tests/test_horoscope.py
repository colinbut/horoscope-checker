from src.horoscope import horoscope_checker

def test_horoscope_check_aquarius():
    assert horoscope_checker.check("19", "jan") == 'Aquarius'
