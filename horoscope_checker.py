import typer

app = typer.Typer()

@app.command()
def version():
    print("v0.0.1")

@app.command()
def check(day: str, month: str):
    day = int(day)
    if month.lower() == 'jan':
        if day > 19:
            print("Aquarius")
        else:
            print("Capricorn")
    elif month.lower() == 'feb':
        if day > 18:
            print("Pisces")
        else:
            print("Aquarius")
    elif month.lower() == 'mar':
        if day > 21:
            print("Aries")
        else:
            print("Pisces")
    elif month.lower() == 'apr':
        if day > 19:
            print("Taurus")
        else:
            print("Aries")
    elif month.lower() == 'may':
        if day > 20:
            print("Gemini")
        else:
            print("Taurus")
    elif month.lower() == 'jun':
        if day > 20:
            print("Cancel")
        else:
            print("Taurus")
    elif month.lower() == 'jul':
        if day > 22:
            print("Leo")
        else:
            print("Cancel")
    elif month.lower() == 'aug':
        if day > 22:
            print("Virgo")
        else:
            print("Leo")
    elif month.lower() == 'sep':
        if day > 22:
            print("Libra")
        else:
            print("Virgo")
    elif month.lower() == 'oct':
        if day > 22:
            print("Scorpio")
        else:
            print("Virgo")
    elif month.lower() == 'nov':
        if day > 21:
            print("Sagittarius")
        else:
            print("Scorpio")
    elif month.lower() == 'dec':
        if day > 21:
            print("Capricorn")
        else:
            print("Sagittarius")
    else:
        pass

if __name__ == "__main__":
    app()
