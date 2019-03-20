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


# Update clients recives a client name to update it 
def update_client(client_name, updated_client_name):
    global clients

    if client_name in clients:
        clients = clients.replace(client_name + ',', updated_client_name + ',') 
    else:
        print('Client not found!')

# Function to print a welcome message
def _print_welcome():
    print('*'*75)

    print('WELCOME to e-SALES')

    print('*'*75)

    print('What wolud you like to do?')

    print('[C]reate client')
    print('[D]elete client')
    print('[U]pdate client')


# Private method  to get the  client name
def _get_client_name():
    return input('Please type the client name... ')

# main function calls crate_client
if __name__ == '__main__':
    _print_welcome()

 # Stop the execution until we have a option selected
    command = input()
    command = command.upper()

 # Lets check what the user want to do
    if command == 'C':
        client_name = _get_client_name()
        create_client(client_name)
        list_clients()
    elif command == 'D':
        pass
    elif command == 'U':
         client_name = _get_client_name()
         updated_client_name = input('Please type the new client name...')
         update_client(client_name,updated_client_name) 
    else:
        print('Invalid option')
        
