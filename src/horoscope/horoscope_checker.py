import typer
from months import Months

app = typer.Typer()

@app.command()
def version():
    print("v0.0.1")

AQUARIUS = "Aquarius"
PISCES = "Pisces"
ARIES = "Aries"
TAURUS = "Taurus"
GEMINI = "Gemini"
CANCER = "Cancer"
LEO = "Leo"
VIRGO = "Virgo"
SCORPIO = "Scorpio"
LIBRA = "Libra"
SAGITTARIUS = "Sagittarius"
CAPRICORN = "Capricorn"


@app.command()
def check(day: str, month: str):
    day = int(day)
    if month.lower() == Months.JANUARY:
        if 20 <= day <= 31:
            return AQUARIUS
        elif 1 <= day <= 19:
            return CAPRICORN
        else:
            return "ERROR"
    elif month.lower() == Months.FEBRUARY:
        if 19 <= day <= 29:
            return PISCES
        elif 1 <= day <= 18:
            return AQUARIUS
        else:
            return "ERROR"
    elif month.lower() == Months.MARCH:
        if 21 <= day <= 31:
            return ARIES
        elif 1 <= day <= 20:
            return PISCES
        else: 
            return "ERROR"
    elif month.lower() == Months.APRIL:
        if 20 <= day <= 30:
            return TAURUS
        elif 1 <= day <= 19:
            return ARIES
        else:
            return "ERROR"
    elif month.lower() == Months.MAY:
        if 21 <= day <= 31:
            return GEMINI
        elif 1 <= day <= 20:
            return TAURUS
        else:
            return "ERROR"
    elif month.lower() == Months.JUNE:
        if 21 <= day <= 30:
            return CANCER
        elif 1 <= day <= 20:
            return GEMINI
        else:
            return "ERROR"
    elif month.lower() == Months.JULY:
        if 23 <= day <= 32:
            return LEO
        elif 1 <= day <= 22:
            return CANCER
        else:
            return "ERROR"
    elif month.lower() == Months.AUGUST:
        if 23 <= day <= 31:
            return VIRGO
        elif 1 <= day <= 22:
            return LEO
        else:
            return "ERROR"
    elif month.lower() == Months.SEPTEMBER:
        if 23 <= day <= 30:
            return LIBRA
        elif 1 <= day <= 22:
            return VIRGO
        else:
            return "ERROR"
    elif month.lower() == Months.OCTOBER:
        if 23 <= day <= 31:
            return SCORPIO
        elif 1 <= day <= 22:
            return LIBRA
        else:
            return "ERROR"
    elif month.lower() == Months.NOVEMBER:
        if 22 <= day <= 30:
            return SAGITTARIUS
        elif 1 <= day <= 21:
            return SCORPIO
        else:
            return "ERROR"
    elif month.lower() == Months.DECEMBER:
        if 22 <= day <= 31:
            return CAPRICORN
        elif 1 <= day <= 21:
             return SAGITTARIUS
        else:
            return "ERROR"
    else:
        pass

if __name__ == "__main__":
    app()
