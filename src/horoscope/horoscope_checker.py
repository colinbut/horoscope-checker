import typer

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

JAN = "jan"
FEB = "feb"
MAR = "mar"
APR = "apr"
MAY = "may"
JUN = "jun"
JUL = "jul"
AUG = "aug"
SEP = "sep"
OCT = "oct"
NOV = "nov"
DEC = "dec" 

@app.command()
def check(day: str, month: str):
    day = int(day)
    if month.lower() == JAN:
        if 20 <= day <= 31:
            return AQUARIUS
        elif 1 <= day <= 19:
            return CAPRICORN
        else:
            return "ERROR"
    elif month.lower() == FEB:
        if day > 18:
            return PISCES
        else:
            return AQUARIUS
    elif month.lower() == MAR:
        if day > 20:
            return ARIES
        else:
            return PISCES
    elif month.lower() == APR:
        if day > 19:
            return TAURUS
        else:
            return ARIES
    elif month.lower() == MAY:
        if day > 20:
            return GEMINI
        else:
            return TAURUS
    elif month.lower() == JUN:
        if day > 20:
            return CANCER
        else:
            return GEMINI
    elif month.lower() == JUL:
        if day > 22:
            return LEO
        else:
            return CANCER
    elif month.lower() == AUG:
        if day > 22:
            return VIRGO
        else:
            return LEO
    elif month.lower() == SEP:
        if day > 22:
            return LIBRA
        else:
            return VIRGO
    elif month.lower() == OCT:
        if day > 22:
            return SCORPIO
        else:
            return VIRGO
    elif month.lower() == NOV:
        if day > 21:
            return SAGITTARIUS
        else:
            return SCORPIO
    elif month.lower() == DEC:
        if day > 21:
            return CAPRICORN
        else:
             return SAGITTARIUS
    else:
        pass

if __name__ == "__main__":
    app()
