def run():
    hr_tr = input("Puede decirnos cuantas horas trabaja para calcular los taxes que debe pagar ")
    pay_pretx = int(hr_tr) * 15000
    pay_postx = float(pay_pretx) * 0.12
    pay = int(pay_pretx) - (pay_postx)
    print( "Tiene que pagar  " + str(float(pay_postx)) + " pesos en Impuestos.")
    print("Te quedarán " + str(float(pay)) + " pesos este mes" )


if __name__ == "__main__":
    run()
