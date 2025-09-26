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

@app.command()
def check(day: str, month: str):
    day = int(day)
    if month.lower() == 'jan':
        if day > 19:
            print(AQUARIUS)
        else:
            print(CAPRICORN)
    elif month.lower() == 'feb':
        if day > 18:
            print(PISCES)
        else:
            print(AQUARIUS)
    elif month.lower() == 'mar':
        if day > 21:
            print(ARIES)
        else:
            print(PISCES)
    elif month.lower() == 'apr':
        if day > 19:
            print(TAURUS)
        else:
            print(ARIES)
    elif month.lower() == 'may':
        if day > 20:
            print(GEMINI)
        else:
            print(TAURUS)
    elif month.lower() == 'jun':
        if day > 20:
            print("Cancer")
        else:
            print(TAURUS)
    elif month.lower() == 'jul':
        if day > 22:
            print(LEO)
        else:
            print("Cancer")
    elif month.lower() == 'aug':
        if day > 22:
            print(VIRGO)
        else:
            print(LEO)
    elif month.lower() == 'sep':
        if day > 22:
            print(LIBRA)
        else:
            print(VIRGO)
    elif month.lower() == 'oct':
        if day > 22:
            print(SCORPIO)
        else:
            print(VIRGO)
    elif month.lower() == 'nov':
        if day > 21:
            print(SAGITTARIUS)
        else:
            print(SCORPIO)
    elif month.lower() == 'dec':
        if day > 21:
            print(CAPRICORN)
        else:
            print(SAGITTARIUS)
    else:
        pass

if __name__ == "__main__":
    app()
