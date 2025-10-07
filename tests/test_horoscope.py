from src.horoscope import horoscope_checker

def test_horoscope_check_aquarius():
    assert horoscope_checker.check("19", "jan") == 'Capricorn'

def test_horoscope_check_pisces():
    assert horoscope_checker.check("20", "feb") == 'Pisces'

def test_horoscope_check_aries():
    assert horoscope_checker.check("25", "mar") == "Aries"

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

