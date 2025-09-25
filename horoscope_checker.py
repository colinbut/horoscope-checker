import typer

app = typer.Typer()

@app.command()
def version():
    print("v0.0.1")

@app.command()
def check(day: str, month: str):
    if month.lower() == 'jan':
        if int(day) > 19:
            print("Aquarius")
        else:
            print("Capricorn")
    elif month.lower() == 'feb':
        if int(day) > 18:
            print("Pisces")
        else:
            print("Aquarius")
    elif month.lower() == 'mar':
        if int(day) > 21:
            print("Aries")
        else:
            print("Pisces")
    elif month.lower() == 'apr':
        if int(day) > 19:
            print("Taurus")
        else:
            print("Aries")
    elif month.lower() == 'may':
        if int(day) > 20:
            print("Gemini")
        else:
            print("Taurus")
    elif month.lower() == 'jun':
        if int(day) > 20:
            print("Cancel")
        else:
            print("Taurus")
    elif month.lower() == 'jul':
        if int(day) > 22:
            print("Leo")
        else:
            print("Cancel")
    elif month.lower() == 'aug':
        if int(day) > 22:
            print("Virgo")
        else:
            print("Leo")
    elif month.lower() == 'sep':
        if int(day) > 22:
            print("Libra")
        else:
            print("Virgo")
    elif month.lower() == 'oct':
        if int(day) > 22:
            print("Scorpio")
        else:
            print("Virgo")
    elif month.lower() == 'nov':
        if int(day) > 21:
            print("Sagittarius")
        else:
            print("Scorpio")
    elif month.lower() == 'dec':
        print("Capricorn")
    else:
        pass

if __name__ == "__main__":
    app()
