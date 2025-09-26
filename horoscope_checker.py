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
        if day > 19:
            print(AQUARIUS)
        else:
            print(CAPRICORN)
    elif month.lower() == FEB:
        if day > 18:
            print(PISCES)
        else:
            print(AQUARIUS)
    elif month.lower() == MAR:
        if day > 21:
            print(ARIES)
        else:
            print(PISCES)
    elif month.lower() == APR:
        if day > 19:
            print(TAURUS)
        else:
            print(ARIES)
    elif month.lower() == MAY:
        if day > 20:
            print(GEMINI)
        else:
            print(TAURUS)
    elif month.lower() == JUN:
        if day > 20:
            print(CANCER)
        else:
            print(TAURUS)
    elif month.lower() == JUL:
        if day > 22:
            print(LEO)
        else:
            print(CANCER)
    elif month.lower() == AUG:
        if day > 22:
            print(VIRGO)
        else:
            print(LEO)
    elif month.lower() == SEP:
        if day > 22:
            print(LIBRA)
        else:
            print(VIRGO)
    elif month.lower() == OCT:
        if day > 22:
            print(SCORPIO)
        else:
            print(VIRGO)
    elif month.lower() == NOV:
        if day > 21:
            print(SAGITTARIUS)
        else:
            print(SCORPIO)
    elif month.lower() == DEC:
        if day > 21:
            print(CAPRICORN)
        else:
            print(SAGITTARIUS)
    else:
        pass

if __name__ == "__main__":
    app()
