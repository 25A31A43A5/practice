import contact as Contact
import storage 

class ContactManager:
    def __init__(self):

            self.contacts:list[Contact.Contact]=storage.import_contacts()
        
        
    def search_contact_name(self,Name:str="")->Contact:
        for c in self.contacts:
            if c.name==Name:
                return c
        return None

    def add_contact(self,c:Contact=None)->None:
        if self.search_contact_name(c.name)==None:
            self.contacts.append(c)
        else:
            raise ValueError("Contact already exists!")
        
    def delete_contact(self,Name:str="")->None:
        if self.search_contact_name(Name)!=None:
            self.contacts.remove(self.search_contact_name(Name))
        else:
            raise ValueError("Contact you wanted to delete does not exist!")
        
    def update_contact(self,original_name:str="",Name:str="",Phn_no:str="",Email:str="")->None:
        n=self.search_contact_name(original_name)
        if n is not None:

            if Name!="":
                n.name=Name
            if Phn_no!="":
                n.phone_no=Phn_no
            if Email!="":
                n.email_id=Email
        else:
            raise ValueError("Contact not found!")

    def display_contacts(self)->list:
        if self.contacts:
            display_list=[]
            for a in self.contacts:
                display_list.append(f"name: {a.name} || Phone number: {a.phone_no} || Email Id: {a.email_id}")
            return display_list
        
    def save_contacts(self)->None:
        storage.export_contacts(self.contacts)