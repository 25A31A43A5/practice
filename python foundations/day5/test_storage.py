import contact
import storage
import csv

def test_import(tmp_path):
    PATH=(tmp_path)/"day5"
    temp_header=["name","phone_no","email_id"]
    temp_data=[["hi","0000000000","xyz@gmail.com"]]
    with open(PATH,"w",newline="") as temp_file:
        writer=csv.writer(temp_file)
        writer.writerow(temp_header)
        writer.writerows(temp_data)

    imported_data=storage.import_contacts(PATH)

    assert len(imported_data)==1
    assert imported_data[0].name=="hi"
    assert imported_data[0].phone_no=="0000000000"
    assert imported_data[0].email_id=="xyz@gmail.com"

def test_export(tmp_path):
    PATH=(tmp_path)/"day5"
    temp_header=["name","phone_no","email_id"]
    temp_data=[["hi","0000000000","xyz@gmail.com"]]
    with open(PATH,"w",newline="") as temp_file:
        writer=csv.writer(temp_file)
        writer.writerow(temp_header)
        writer.writerows(temp_data)

    storage.export_contacts([contact.Contact(*temp_data[0])],PATH)
    imported=storage.import_contacts(PATH)
    assert len(imported)==1
    assert imported[0].name=="hi"
    assert imported[0].phone_no=="0000000000"
    assert imported[0].email_id=="xyz@gmail.com"


def test_file_missing():
    assert []==storage.import_contacts("fake_file.csv")

def test_empty_file(tmp_path):
    PATH=tmp_path/"day5"
    with open(PATH,"w",newline="") as temp_file:
        temp_file.write("")
    assert []==storage.import_contacts(PATH)
