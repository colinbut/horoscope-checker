import typer
from months import Months
from horoscopes import Horoscopes

app = typer.Typer()

@app.command()
def version():
    print("v0.0.1")


@app.command()
def check(day: str, month: str):
    day = int(day)
    if month.lower() == Months.JANUARY:
        if 20 <= day <= 31:
            return Horoscopes.AQUARIUS
        elif 1 <= day <= 19:
            return Horoscopes.CAPRICORN
        else:
            return "ERROR"
    elif month.lower() == Months.FEBRUARY:
        if 19 <= day <= 29:
            return Horoscopes.PISCES
        elif 1 <= day <= 18:
            return Horoscopes.AQUARIUS
        else:
            return "ERROR"
    elif month.lower() == Months.MARCH:
        if 21 <= day <= 31:
            return Horoscopes.ARIES
        elif 1 <= day <= 20:
            return Horoscopes.PISCES
        else: 
            return "ERROR"
    elif month.lower() == Months.APRIL:
        if 20 <= day <= 30:
            return Horoscopes.TAURUS
        elif 1 <= day <= 19:
            return Horoscopes.ARIES
        else:
            return "ERROR"
    elif month.lower() == Months.MAY:
        if 21 <= day <= 31:
            return Horoscopes.GEMINI
        elif 1 <= day <= 20:
            return Horoscopes.TAURUS
        else:
            return "ERROR"
    elif month.lower() == Months.JUNE:
        if 21 <= day <= 30:
            return Horoscopes.ANCER
        elif 1 <= day <= 20:
            return Horoscopes.GEMINI
        else:
            return "ERROR"
    elif month.lower() == Months.JULY:
        if 23 <= day <= 32:
            return Horoscopes.LEO
        elif 1 <= day <= 22:
            return Horoscopes.CANCER
        else:
            return "ERROR"
    elif month.lower() == Months.AUGUST:
        if 23 <= day <= 31:
            return Horoscopes.VIRGO
        elif 1 <= day <= 22:
            return Horoscopes.LEO
        else:
            return "ERROR"
    elif month.lower() == Months.SEPTEMBER:
        if 23 <= day <= 30:
            return Horoscopes.LIBRA
        elif 1 <= day <= 22:
            return Horoscopes.VIRGO
        else:
            return "ERROR"
    elif month.lower() == Months.OCTOBER:
        if 23 <= day <= 31:
            return Horoscopes.SCORPIO
        elif 1 <= day <= 22:
            return Horoscopes.LIBRA
        else:
            return "ERROR"
    elif month.lower() == Months.NOVEMBER:
        if 22 <= day <= 30:
            return Horoscopes.SAGITTARIUS
        elif 1 <= day <= 21:
            return Horoscopes.SCORPIO
        else:
            return "ERROR"
    elif month.lower() == Months.DECEMBER:
        if 22 <= day <= 31:
            return Horoscopes.CAPRICORN
        elif 1 <= day <= 21:
             return Horoscopes.SAGITTARIUS
        else:
            return "ERROR"
    else:
        pass

if __name__ == "__main__":
    app()
