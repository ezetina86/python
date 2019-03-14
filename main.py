# Creating the sting
clients = 'Pablo,Ricardo,'


# global is used to define that the  variable clients is global
# it means that it has been defined as 'Pablo and Ricardo'
def create_client(client_name):
    global clients

# Assigning the new value to the previus string state and then
# we add the comma
    if client_name not in clients:
       clients += client_name
       _add_comma()
    else:
        print(client_name + ' already exists...')   


# Fucntion to add a comma after each name we add
def _add_comma():
    global clients

    clients += ','

# Function to list clients


def list_clients():
    global clients

    print(clients)


# Function to print a welcome message
def _print_welcome():
    print('*'*75)

    print('WELCOME to e-SALES')

    print('*'*75)

    print('What wolud you like to do?')

    print('[C]reate client')
    print('[D]elete client')


# main function calls crate_client
if __name__ == '__main__':
    _print_welcome()

 # Stop the execution until we have a option selected
    command = input()

 # Lets check what the user want to do
    if command == 'C':
        client_name = input('Please type the client name... ')
        create_client(client_name)
        list_clients()
    elif command == 'D':
        pass
    else:
        print('Invalid option')
