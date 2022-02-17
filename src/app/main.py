from fastapi import FastAPI
import uvicorn
import csv
import numpy as np

app = FastAPI()

kwh_price = []
grid_fees = []
unit_price = []
hs_splitter = []
zp_cde = []
cty = []
strt = []

def tariff_gen(postal_code, city, street, house_number,ykc ):
    file = open('data/data.csv', encoding="utf-8")
    data_list = list(csv.reader(file))
    locations = data_list[1:]

    for rows in locations:
        if rows[0] == postal_code:
            zp_cde.append(rows)

    for rows in zp_cde:
        if rows[1] == city:
            cty.append(rows)

    for rows in cty:
        if rows[2] == street:
            strt.append(rows)

    for rows in strt:
        hs = rows[3]
        hs_splitter = hs.split('-', 2)
    hs_min = int(hs_splitter[0])
    hs_max = int(hs_splitter[1])

    if hs_min <= house_number <= hs_max:
        for row in strt:
            kwh_price = row[-1]
            grid_fees = row[-2]
            unit_price = row[-3]
            kwh_price_np = np.array(kwh_price).astype(float)
            grid_feess_np = np.array(grid_fees).astype(float)
            grid_unitprice_np = np.array(unit_price).astype(float)
    avg_kwh_price = np.average(kwh_price_np)
    avg_grid_price = np.average(grid_feess_np)
    avg_unit_price = np.average(grid_unitprice_np)

    total_bill = avg_unit_price + avg_grid_price + ykc * avg_kwh_price

    print(avg_kwh_price)
    print(avg_grid_price)
    print(avg_unit_price)
    print(ykc)
    print(total_bill)
    result = {
        "unit_price": avg_unit_price,
        "grid_fees": avg_grid_price,
        "kwh_price": avg_kwh_price,
        'total_price': total_bill

    }
    return(result)

@app.get("/main")
def post_data(postal_code: str, city: str, street: str, house_number: int,ykc: int ):

    return tariff_gen(postal_code, city, street, house_number, ykc)

