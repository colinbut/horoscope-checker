import typer

app = typer.Typer()

@app.command()
def version():
    print("v0.0.1")

@app.command()
def check(day: str, month: str):
    if month.lower() == 'jan':
        print("Aquarius")
    elif month.lower() == 'feb':
        print("Pisces")
    elif month.lower() == 'mar':
        print("Aries")
    elif month.lower() == 'apr':
        print("Taurus")
    elif month.lower() == 'may':
        print("Gemini")
    elif month.lower() == 'jun':
        print("Cancel")
    elif month.lower() == 'jul':
        print("Leo")
    elif month.lower() == 'aug':
        print("Virgo")
    elif month.lower() == 'sep':
        print("Libra")
    elif month.lower() == 'oct':
        print("Scorpio")
    elif month.lower() == 'nov':
        print("Sagittarius")
    elif month.lower() == 'dec':
        print("Capricorn")
    else:
        pass

if __name__ == "__main__":
    app()
