contacts = {}


def input_error(funk):
    def inner(*args):
        try:
            return funk(*args)
        except IndexError:
            return "Not enough params. Print 'Help'"
        except KeyError:
            return "This contact doesn't exist in the phonebook"
        except ValueError:
            return "Please enter name and correct phone number separated by a space"
    return inner


def help(*args):
    return """Please enter: Name, Lastname and Phone number separated by space"""


@input_error
def add(*args):
    list_of_param = args[0].split()
    name = tuple(list_of_param[0:2])
    phone = tuple(list_of_param[2:])
    if phone:
        contacts[name]= phone
        return '\n'.join([f"Name: {' '.join(name)}, Phone: {''.join(phone)} has been added to contact"])
    if not phone:
        raise IndexError()
    else:
        return ""
    

def exit(*args):   
    return "Good bye!"


def no_command(*args):
    return "Unknown command, try again"


@input_error
def hello(*args):
    return "How can I help you?"

@input_error
def show_all(*args):
    return '\n'.join(f'name: {" ".join(k)} phone: {",".join(v)}' for k,v in contacts.items())
    
@input_error
def change(*args):
    list_of_param = args[0].split()
    name = tuple(list_of_param[0:2])
    phone = tuple(list_of_param[2:])
    if phone:
        contacts[name]= phone
        return '\n'.join([f"Name: {' '.join(name)}, Phone: {''.join(phone)} has been updated"])  # noqa: E501 
    if not phone:
        raise ValueError()
    else:
        return ""
    
    
@input_error
def find_phone(*args):
    name = tuple(args[0].split())
    if name in contacts: 
        return f"The phone number for {' '.join(name)} is: {' '.join(contacts[name])}"
    else:
        raise KeyError()
    

COMMANDS = {help: "help",
            add: "add",
            exit: ["exit", "close", 'good bye'],
            hello: "hello",
            show_all: "show all",
            change: "change",
            find_phone: "phone"}

@input_error
def command_handler(text):
    for command, kword in COMMANDS.items():
        if isinstance(kword, str):
            if text.startswith(kword):
                return command, text.replace(kword, '').strip()
        elif isinstance(kword, list):
            for word in kword:
                if text.startswith(word):
                    return command, text.replace(word, '').strip()
    return no_command, None



def main():
    while True:
        user_input = input("Enter command: ")
        command, data = command_handler(user_input.lower())
        print(command(data))

        if command == exit:
            break


if __name__ == "__main__":
    main()




