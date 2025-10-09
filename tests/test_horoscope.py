from src.horoscope import horoscope_checker

def test_horoscope_check_aquarius():
    for x in range(21, 32):
        print(f"test {x} of Jan is Aquarius")
        assert horoscope_checker.check(x, "jan") == 'Aquarius'
    for y in range(1, 18):
        print(f"test {y} of Feb is Aquarius")
        assert horoscope_checker.check(y, "feb") == 'Aquarius'

def test_horoscope_check_pisces():
    for x in range(19, 29):
        assert horoscope_checker.check(x, "feb") == 'Pisces'
    for y in range(1, 19):
        assert horoscope_checker.check(y, "mar") == 'Pisces'

def test_horoscope_check_aries():
    for x in range(21, 30):
        assert horoscope_checker.check(x, "mar") == "Aries"
    for y in range(1, 20):
        assert horoscope_checker.check(y, "apr") == "Aries"

def test_horoscope_check_taurus():
    assert horoscope_checker.check("20", "apr") == "Taurus"

def test_horoscope_check_gemini():
    assert horoscope_checker.check("2", "jun") == "Gemini"

def test_horoscope_check_cancer():
    assert horoscope_checker.check("30", "jun") == "Cancer"

def test_horoscope_check_leo():
    assert horoscope_checker.check("28", "jul") == "Leo"

def test_horoschope_check_virgo():
    assert horoscope_checker.check("26", "Aug") == "Virgo"

def test_horoscope_check_scorpio():
    assert horoscope_checker.check("24", "Oct") == "Scorpio"

def test_horoscope_check_libra():
    assert horoscope_checker.check("23", "Sep") == "Libra"

def test_horoscope_check_sagittarius():
    assert horoscope_checker.check("26", "Nov") == "Sagittarius"

def test_horoscope_check_capricorn():
    assert horoscope_checker.check("22", "Dec") == "Capricorn"


def test_not_valid_day():
    assert horoscope_checker.check("0", "Jan") == "ERROR"