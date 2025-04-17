####################################################
#   Devoir de Python   #
# Nom : TCHANGAI
# Prenom : Florentin
# Description : Je n'ai pas tout cassé
#################################################### 

import Contact
import ContactList as ctl

list_contacts = []

deleted_contacts = []

# Ajouter un contact a la liste des contacts
def add_contact_to_list():
    name = input("Nom du contact : ")
    phone_number = input("Numéro de téléphone : ")
    email = input("Adresse email : ")
    newContact = Contact.Contact(name, phone_number, email)
    list_contacts.append(newContact)
    print("Contact ajouté avec succès !")

# Fonction pour afficher la liste des contacts
def display_contacts():
    print("Liste des contacts :")
    if len(list_contacts) == 0:
        print("Vous n'avez pas de contact")
    else:
        for contact in list_contacts:
            print(f"Nom : {contact.contact_name} | Téléphone : {contact.phone_number} | Email : {contact.email}")

#  Fonction pour rechercher un contact
def search_contact():
    searched_contact_name = input("Entrez le nom du contact à rechercher : ")
    for contact in list_contacts:
        if contact.contact_name == searched_contact_name:
            print(f"Nom : {contact.contact_name} | Téléphone : {contact.phone_number} | Email : {contact.email}")
            return
        else:
            print("Contact non trouvé.")
    
# Fonction pour modifier un contact
def update_contact():
    updated_contact_name = input("Entrez le nom du contact à modifier : ")
    
    for contact in list_contacts:
        if contact.contact_name == updated_contact_name:
            new_phone = input("Nouveau numéro de téléphone : ")
            new_email = input("Nouvel email : ")
            contact.phone = new_phone
            contact.email = new_email
            print("Contact modifié avec succès.")
            return
    print("Contact non trouvé.")
    
def delete_contact():
    contact_delete_name = input("Entrez le nom du contact à supprimer : ")
    for contact in list_contacts:
        if contact.contact_name == contact_delete_name:
            list_contacts.remove(contact)
            deleted_contacts.append(contact)
            print("Contact supprimé avec succès.")
            return
    print("Contact non trouvé.")
    
def show_deleted_contacts():
    if len(deleted_contact) == 0:
        print("Pas de contact dans la corbeille.")
    else:
            for deleted_contact in deleted_contacts:
                print(f"Nom : {deleted_contact.contact_name} | Téléphone : {deleted_contact.phone_number} | Email : {delete_contact.email}")

def sort_contact():
    list_contacts.sort(key=lambda contact: contact.contact_name)
    print("Contacts triés avec succès.")


def __main__():
    
    while True:
        print("Bienvenue dans le gestionnaire de contacts !")
        print("")
        print("1. Ajouter un contact")
        print("2. Modifier un contact")
        print("3. Supprimer un contact")
        print("4. Afficher tous les contacts")
        print("5. Trier les contacts")
        print("6. Rechercher un contact")
        print("7. Corbeille")
        print("8. Quitter")
        
        choice = 0
        choice = input("Entrez le numero de l'option souhaitée : ")

        match choice:
            case '1':
                add_contact_to_list()
            case '2':
                update_contact
            case '3':
                update_contact()
            case '4':
                display_contacts()
            case '5':
                sort_contact()
            case '6':
                search_contact()
            case '7':
                show_deleted_contacts()
            case '8':
                break
                

__main__()
    