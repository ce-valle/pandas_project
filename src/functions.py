def columns_name(arr): #función para crear un diccionario y cambiar el nombre de las columnas
    dict_columns = {columna: columna.replace(" ", "_").lower().strip() for columna in arr}
    return dict_columns

def cambio(col):
    month_lst = ["Jan", "Feb", "Mar", "May", "Apr", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    if col not in month_lst:
        return "unknown"
    else:
        return col 