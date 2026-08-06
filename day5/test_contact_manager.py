import contact_manager
import contact
import pytest
import csv

def test_add(tmp_path):
    PATH=tmp_path/("day5.csv")

    PATH.touch()

    test_data=["name","0000000000","xyz@gmail.com"]

    test_obj=contact_manager.ContactManager(PATH)
    test_obj.add_contact(contact.Contact(*test_data))
    test_obj.save_contacts(PATH)
    with open(PATH,"r") as temp_file:
        data=list(csv.reader(temp_file))

    assert data[1]==test_data

def test_add_existing_value(tmp_path):
    PATH=tmp_path/("day5.csv")    
    test_data=["name","0000000000","xyz@gmail.com"]
    header=["name","phone_no","email_id"]

    with open(PATH,"w",newline="") as temp_file:
        writer=csv.writer(temp_file)
        writer.writerow(header)
        writer.writerow(test_data)

    test_obj=contact_manager.ContactManager(PATH)

    with pytest.raises(ValueError):
        test_obj.add_contact(contact.Contact(*test_data))

def test_search_contact(tmp_path):
    PATH=tmp_path/("day5.csv")    
    test_data=["abc","0000000000","xyz@gmail.com"]
    header=["name","phone_no","email_id"]

    with open(PATH,"w",newline="") as temp_file:
        writer=csv.writer(temp_file)
        writer.writerow(header)
        writer.writerow(test_data)

    test_obj=contact_manager.ContactManager(PATH)
    assert contact.Contact(*test_data).name==test_obj.search_contact_name("abc").name
    assert contact.Contact(*test_data).phone_no==test_obj.search_contact_name("abc").phone_no
    assert contact.Contact(*test_data).email_id==test_obj.search_contact_name("abc").email_id

def test_search_missing_contact(tmp_path):
    PATH=tmp_path/("day5.csv")
    PATH.touch()

    test_obj=contact_manager.ContactManager(PATH)

    assert test_obj.search_contact_name("name") is None

def test_delete_contact(tmp_path):
    PATH=tmp_path/("day5.csv")
    test_data=["abc","0000000000","xyz@gmail.com"]
    header=["name","phone_no","email_id"]

    with open(PATH,"w",newline="") as temp_file:
        writer=csv.writer(temp_file)
        writer.writerow(header)
        writer.writerow(test_data)

    test_obj=contact_manager.ContactManager(PATH)
    test_obj.delete_contact("abc")
    test_obj.save_contacts(PATH)
    with open(PATH,"r") as temp_file:
        data=list(csv.reader(temp_file))

    assert data==[header]

def test_delete_non_existant_contact(tmp_path):
    PATH=tmp_path/("day5.csv")
    test_obj=contact_manager.ContactManager(PATH)

    with pytest.raises(ValueError):
        test_obj.delete_contact("abc")

def test_update_contact(tmp_path):
    PATH=tmp_path/("day5.csv")
    test_data=["abc","0000000000","xyz@gmail.com"]
    header=["name","phone_no","email_id"]

    with open(PATH,"w",newline="") as temp_file:
        writer=csv.writer(temp_file)
        writer.writerow(header)
        writer.writerow(test_data)

    test_obj=contact_manager.ContactManager(PATH)

    modified_data=["modified_name","111111111","abc@gmail.com"]

    test_obj.update_contact("abc",*modified_data)
    test_obj.save_contacts(PATH)

    with open(PATH,"r") as temp_file:
        modified_input_data=list(csv.reader(temp_file))

    assert modified_data==modified_input_data[1]

def test_update_non_existing_contact(tmp_path):
    PATH=tmp_path/("day5.csv")
    PATH.touch()
    modified_data=["modified_name","111111111","abc@gmail.com"]
    test_obj=contact_manager.ContactManager(PATH)

    with pytest.raises(ValueError):
        test_obj.update_contact("none",*modified_data)

def test_display_contacts(tmp_path):
    PATH=tmp_path/("day5.csv")    
    test_data=["name","0000000000","xyz@gmail.com"]
    header=["name","phone_no","email_id"]

    with open(PATH,"w",newline="") as temp_file:
        writer=csv.writer(temp_file)
        writer.writerow(header)
        writer.writerow(test_data)

    test_obj=contact_manager.ContactManager(PATH)

    assert f"name: {test_data[0]} || Phone number: {test_data[1]} || Email Id: {test_data[2]}"==test_obj.display_contacts()[0]

def test_diplay_none_contacts(tmp_path):
    PATH=tmp_path/("day5.csv")

    test_obj=contact_manager.ContactManager(PATH)

    assert test_obj.display_contacts() is None