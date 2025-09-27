from datetime import date, datetime
data = date.today()
data_formatada = data.strftime("%d/%m/%Y")
print(datetime.strptime(data_formatada, "%d/%m/%Y").date())
