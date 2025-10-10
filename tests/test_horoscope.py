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
    for x in range(20, 31):
        assert horoscope_checker.check(x, "apr") == "Taurus"
    for y in range(1, 21):
        assert horoscope_checker.check(y, "may") == "Taurus"

def test_horoscope_check_gemini():
    for x in range(21, 32):
        assert horoscope_checker.check(x, "may") == "Gemini"
    for y in range(1, 21):
        assert horoscope_checker.check(y, "jun") == "Gemini"

def test_horoscope_check_cancer():
    for x in range(21, 31):
        assert horoscope_checker.check(x, "jun") == "Cancer"
    for y in range(1, 23):
        assert horoscope_checker.check(y, "jul") == "Cancer"

def test_horoscope_check_leo():
    for x in range(23, 32):
        assert horoscope_checker.check(x, "jul") == "Leo"
    for y in range(1, 23):
        assert horoscope_checker.check(y, "aug") == "Leo"

def test_horoschope_check_virgo():
    for x in range(23, 32):
        assert horoscope_checker.check(x, "aug") == "Virgo"
    for y in range(1, 23):
        assert horoscope_checker.check(y, "sep") == "Virgo"

def test_horoscope_check_libra():
    for x in range(23, 31):
        assert horoscope_checker.check(x, "sep") == "Libra"
    for y in range(1, 23):
        assert horoscope_checker.check(y, "oct") == "Libra"

def test_horoscope_check_scorpio():
    for x in range(23, 32):
        assert horoscope_checker.check(x, "oct") == "Scorpio"
    for y in range(1, 22):
        assert horoscope_checker.check(y, "nov") == "Scorpio"


def test_horoscope_check_sagittarius():
    for x in range(22, 31):
        assert horoscope_checker.check(x, "nov") == "Sagittarius"
    for y in range(1, 22):
        assert horoscope_checker.check(y, "dec") == "Sagittarius"

def test_horoscope_check_capricorn():
    for x in range(22, 31):
        assert horoscope_checker.check(x, "dec") == "Capricorn"
    for y in range(1, 20):
        assert horoscope_checker.check(y, "jan") == "Capricorn"


def test_not_valid_day():
    assert horoscope_checker.check("0", "jan") == "ERROR"