import contact
import csv
from pathlib import Path

def import_contacts()->list[contact.Contact]:
    PATH=Path("storage.csv")
    data:list[contact.Contact]=[]
    try:
        with open(PATH,"r",newline="") as csvfile:
            raw_data=csv.reader(csvfile)
            next(raw_data,None)
            for row in raw_data:
                data.append(contact.Contact(*row))
        return data
    except FileNotFoundError:
        return []

def export_contacts(data:list[contact.Contact]):

    PATH=Path("storage.csv")
    header=["name","phone_no","email_id"]
    raw_data:list=[]

    for row in data:
        raw_data.append([row.name,row.phone_no,row.email_id])
    try:
        with open(PATH,"w",newline="") as csvfile:
            writer=csv.writer(csvfile)
            writer.writerow(header)
            writer.writerows(raw_data)
    except FileNotFoundError:
        return