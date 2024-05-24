import os

def add():
  name = input("\nEnter Full name : ")
  phone = input("Enter Phone : ")
  email = input("Enter email : ")
  address = input("Enter address : ")
  filename = "".join(name.split(" ")).lower() + phone
  contactdetail = [name, phone, email, address]

  if not os.path.exists("Contacts"):
    os.mkdir("Contacts")

  with open(f"Contacts/{filename}.txt", "a") as file:
    file.write("\n".join(contactdetail))
    print("__________________________________________________")
    print("\nContact Added Sucessfully",contactdetail)
    print("__________________________________________________")


def show():
  if not os.path.exists("Contacts"):
    os.mkdir("Contacts")
  if os.listdir("Contacts"):
   i = 1
   filenames = [f for f in os.listdir("Contacts")]
   for filename in filenames:
     with open(f"Contacts/{filename}", "r") as file:
       contactdetails = file.read().split("\n")
       print("_______________________________________________________")
       print(f"\nContact {i}:-\nName :{contactdetails[0]}\nPhone : {contactdetails[1]}\nEmail :{contactdetails[2]}\nAddress : {contactdetails[3]}")
       i = i + 1
  else:
    print("_______________________________________________________")
    print("\nNo contacts available")
    print("_______________________________________________________")

     

def search():
  searchname = input("Enter the name to search: ").lower().strip()
  filenames = [f for f in os.listdir("Contacts")]
  found = False
  
  for filename in filenames:
    with open(f"Contacts/{filename}", "r") as file:
      contactdetails = file.read().split("\n")
      
    if searchname == contactdetails[0].lower().strip():
      print("_______________________________________________________")
      print(f"\nContact Found for {searchname} :-\nName :{contactdetails[0]}\nPhone : {contactdetails[1]}\nEmail :{contactdetails[2]}\nAddress : {contactdetails[3]}")
      print("__________________________________________________")
      found = True
      break
      
  if not found:
      print("__________________________________________________")
      print(f"\nContact with name '{searchname}' not found.")
      print("__________________________________________________")



def update():
  updatename = input("Enter the full name of contact : ")
  updatephone = input("\nEnter the phone number of contact you want to update : ")
  filename = "".join(updatename.split(" ")).lower() + updatephone
  if not os.path.exists(f"Contacts/{filename}.txt"):
    print("__________________________________________________")
    print("\nUser Not Found")
    print("__________________________________________________")
  else:  
    print("\nUpdate the details below : - ")
    name = input("\nEnter Full name : ")
    phone = input("Enter Phone : ")
    email = input("Enter email : ")
    address = input("Enter address : ")
    updatefile = "".join(name.split(" ")).lower() + phone
    contactdetail = [name, phone, email, address]
    
    with open(f"Contacts/{updatefile}.txt", "a") as file:
      file.write("\n".join(contactdetail))
      print("__________________________________________________")
      print(f"\nUpdated Details : {contactdetail}")
      os.remove(f"Contacts/{filename}.txt")
      print("__________________________________________________")


def delete():
  deletename = input("\nEnter Full Name of Contact : ")
  deletephone = input("\nEnter Number of Contact : ").strip()
  filename = "".join(deletename.split(" ")).lower() + deletephone
  if os.path.exists(f"Contacts/{filename}.txt"):
    os.remove(f"Contacts/{filename}.txt")
    print("__________________________________________________")
    print("\nUser Sucessfully Deleted")
    print("__________________________________________________")
  else:
    print("__________________________________________________")
    print("\nUser Not Found") 
    print("__________________________________________________")




print("WELCOME TO CONTACT BOOK BY PANKAJ SHARMA")
print("________________________________________________________")

while True:
 print(f"\n{{A}} Show/All Contact    {{B}} Add/Contact")
 print(f"\n{{C}} Update/Contact      {{D}} Delete/Contact")
 print(f"\n{{E}} Search/Contact      {{F}} Stop\n")
 response = input("Enter Choice : ")

 while response != "a" and response != "b" and response != "c" and response != "d" and response != "e" and response != "f":
   response = input(f"Choose only from (A/B/C/D/E/F) : ")
   response.lower()
 else:
   show() if response == "a" else add() if response == "b" else update() if response == "c" else delete() if response == "d" else search() if response == "e" else print("\nExiting...........\nThanks for using✌️")
 if response == "f":
   break    