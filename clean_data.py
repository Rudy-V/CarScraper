import pandas as pd
from datetime import date

today = date.today()
today = today.strftime("%d_%m_%Y")


class CleanData:
    def __init__(self):
        """Too lazy to write documentation here. So suck it nerd"""
        df = pd.read_csv(f'data_{today}.csv')
        df.columns = ['Random number', "Total price", "Montly installment", "Year.Car.Model", "Used.Transmission",
                      "Seller Name", "Seller location", "Km from you"]
        df.drop(df.columns[[0, 7]], axis=1, inplace=True)

        Year = []
        Car_brand = []
        Car_model = []
        Car_mis = []
        for row in df["Year.Car.Model"]:
            temp = row.split()
            Year.append(temp[0])
            Car_brand.append(temp[1])
            Car_model.append(temp[2])
            Car_mis.append(temp[3:])

        Transmission = []
        Milage = []
        for row in df['Used.Transmission']:
            if row == "Used Car1 kmManual":
                milage == "0"
                trans = "Manual"
                Milage.append(milage)
            else:
                milage = row[8:-6]
                milage = milage.replace("km", "")
                milage = milage.replace("Aut", "")
                milage = milage.replace(" ", "")
                milage = milage.strip()
                Milage.append(milage)

            if "Manual" in row:
                Transmission.append("Manual")
            else:
                Transmission.append("Automatic")

        df['transmission'] = Transmission
        df['milage (Thousands)'] = Milage
        df['milage (Thousands)'] = df['milage (Thousands)'].astype(int)
        df['milage (Thousands)'] = df['milage (Thousands)'] / 1000

        df['year'] = Year
        df['manufacturer'] = Car_brand
        df['model'] = Car_model
        df['extra'] = Car_mis

        df['Montly installment'] = df['Montly installment'].str.replace("R", "")
        df['Montly installment'] = df['Montly installment'].str.replace("p/m", "")
        df['Montly installment'] = df['Montly installment'].str.replace(" ", "")
        df['Montly installment'] = df['Montly installment'].str.strip()
        df['Montly installment'] = df['Montly installment'].astype(float)

        df['Total price'] = df['Total price'].str.replace("R", "")
        df['Total price'] = df['Total price'].str.replace(" ", "")
        df['Total price'] = df['Total price'].str.strip()
        df['Total price'] = df['Total price'].astype(float)

        df.to_csv(f"Clean_cars_{today}.csv", index=False)
