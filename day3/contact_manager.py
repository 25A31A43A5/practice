import contact

class contact_manager:
    def __init__(self):
        self.vector:list=[]
    
    def search_contact(self,c:contact)->int:
        if c in self.vector:
            return self.vector.index(c)
        else:
            return None

    def add_contact(self,c:contact)->None:
        if self.search_contact(c)==None:
            self.vector.append(c)
        else:
            raise NotImplementedError("Contact already exists!")
        
    def delete_contact(self,c:contact)->None:
        if self.search_contact(c)!=None:
            self.vector.remove(c)
        else:
            raise NotImplementedError("Contact you wanted to delete does not exist!")
        
    def update_contact(self,c:contact,Name:str="",Phn_no:int=0,Email:str="")->None:
        if self.search_contact(c)!=None:
            if Name!="":
                self.vector[self.search_contact(c)].name=Name
            if Phn_no!=0:
                self.vector[self.search_contact(c)].phone_no=Phn_no
            if Email!="":
                self.vector[self.search_contact(c)].email_id=Email

    def display_contacts(self):
        if self.vector:
            for a in self.vector:
                print(f"name: {a.name} || Phone number: {a.phone_no} || Email Id: {a.email_id}")
        else:
            print("Contact list is empty!!")
