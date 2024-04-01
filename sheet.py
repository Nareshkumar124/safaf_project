import gspread

gc = gspread.service_account("auth.json")

sh = gc.open_by_key("1WpKYKefM6dShyF3Qp-NOG9ksgZ_KjqOVdCmTCXBE3fY")


def sendData(data:list[str]):
    return sh.sheet1.append_row(data)


def getData():
    return sh.sheet1.get_all_values()
