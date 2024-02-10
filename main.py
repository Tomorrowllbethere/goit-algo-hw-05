def parse_input(user_input): #функція, яка приймає введений рядок. ділить та сортує дані.
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def input_error(func): # декоратор- обробка помилок при введенні
    def inner(args, contacts):
        try:
            name = args[0]
            if name in contacts:
                print("\nThis name is in your contacts\n") 
                if len(args) == 1:
                    return func(args, contacts)
                else:
                    if args[1].isdigit():
                        return func(args, contacts)
                    else:
                        return "\n->Phone number must contain only numbers."
            else:
                return func(args, contacts) 
            
        except ValueError:
            return "\n->Give me name and phone please."
        except KeyError:
            return "\n->Is a key error. You should check it and repeat."
        except IndexError:
            return "\n->What's wrong?\nRepeat this, correctly please."
            # return "Phone must be a number"
    return inner


@input_error
def add_contact(args, contacts):# функція додає дані в словник
    name, phone = args
    contacts[name] = phone
    return "Contact added."
    
@input_error
def change_contact(args, contacts):#фукнція змінює номер телефону, якщо імя співпадає
    name, phone= args
    if name in contacts:
        contacts[name] = phone
        return "Number updated"
    else:
        contacts[name] = phone
        print("Didn't find this name.")
        return "Contact added"


def show_all(contacts):#функція показує всі контакти
    for person, person_number in contacts.items():
         print(f"for {person} is a number {person_number}")
    return "----done----"

@input_error
def show_phone(args, contacts):
    name = args[0]
    phone=contacts[name]
    if name in contacts: 
        return f"This\'s phone number for {name}:\n{phone}"
    else:
        print ("Didn't find this name.\n")
    

@input_error
def delete_name(args, contacts):
    name = args[0]
    if name in contacts:
        del contacts[name]
        return "Contact deleted\n"
    else:
        return "Didn't find this name.\n"

def main():#основна функція
    contacts  = {}
    help: list=[
        ['add (name) (phone)   ->for add a new contacts to me'],
        ['change (name) (phone)-> for change contacts i have'],
        ['all                  -> to see all contacts i save'],
        ['delete (name)        -> to delete one contact'],
        ['show (name)          -> to see number of somebody']
        ]
    print("_____________\nHello. \nI'm glad to see you")
    print("\nI have some list of commands. If you need this - enter help\n")
    while True:
        # try:
            user_input  = input("\n>>>Enter a command: ")
            command, *args = parse_input(user_input)
            if command in ["close", "exit"]:
                print("Good bye!")
                break
            elif command == "hello":
                print("How can I help you?")
            elif command == "add":
                print(add_contact(args, contacts))
            elif command == "change":
                print(change_contact(args, contacts))
            elif command == "all":
                print(show_all(contacts))
            elif command == "show":
                print (show_phone(args, contacts))
            elif command == "delete":
                print(delete_name(args, contacts))
            elif command == "help":
                for el in help:
                    print(el)
            else:
                print("Invalid command.\nTry one more time")
        # except Exception as e:
            # print("there are something wrong",f" \n{e}", "\n Plese, try again.")



if __name__ == "__main__":
    main()