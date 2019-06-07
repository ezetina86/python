import sys
import csv
import os
# Creating the dictionary
CLIENT_TABLE = '/home/joseenrique/python/clients.csv'
CLIENT_SCHEMA = ['name', 'company', 'email', 'position']
clients = []

# Function to read the clients table
def _initialize_clients_from_storage():
    with open(CLIENT_TABLE, mode='r') as f:
        reader = csv.DictReader(f, fieldnames= CLIENT_SCHEMA)

        for row in reader:
            clients.append(row)

# Function to save the rows in a Client table
def _save_clients_to_storage():
    tmp_table_name ='{}.tmp'.format(CLIENT_TABLE)
    with open(tmp_table_name,mode='w') as f:
        writer = csv.DictWriter(f,fieldnames= CLIENT_SCHEMA)
        writer.writerows(clients)
        f.close

        os.remove(CLIENT_TABLE)
        os.rename(tmp_table_name, CLIENT_TABLE)

# ed to define that the  variable clients is global
# it means that it has been defined as 'Pablo and Ricardo'
def create_client(client):
    global clients

# Assigning the new value to the previus string state and then
# we add the comma
    if client not in clients:
    # Changing to works with list, so  i don't need commas anymore
        #clients += client_name
        #add_comma()
        clients.append(client)
    else:
        print('Client already exists...')


# Fucntion to add a comma after each name we add
#def _add_comma():
#    global clients
#    clients += ','

# Function to list clients
def list_clients():
    print('uid | name | company | email | position ')
    print('*'*50)
 # Changing to works with list, so  i don't need commas anymore
    #global clients
    #print(clients)
    for idx, client in enumerate(clients):
        print('{uid} | {name} | {company} | {email} | {position}'.format(
            uid=idx,
            name=client['name'],
            company=client['company'],
            email=client['email'],
            position=client['position']))

# Update clients recives a client name to update it
def update_client(client_id, updated_client):
 # Changing to works with liss
    global clients

    if len(clients) -1 >= client_id:
        clients[client_id] = updated_client
    else:
        print('Client not found!')

 # Delete clients recives a client name to delete it
def delete_client(client_id):
# Changing to works with list
    global clients

    for idx, client in enumerate(clients):
        if idx == client_id:
            del clients[idx]
            break

# Function to search a  client into list clients
# Changing to works with list
def search_client(client_name):
    #client_list = clients.split(',')

    for client in clients:
        if client['name'] != client_name:
            continue
        else:
            return True

# Function to print a welcome message


def _print_welcome():
    print('*'*75)

    print('WELCOME to e-SALES')

    print('*'*75)

    print('What would you like to do?')

    print('[C]reate client')
    print('[R]ead clients list')
    print('[U]pdate client')
    print('[D]elete client')
    print('[S]earch client')


# Private method to get the client dictionary
def _get_client_field(field_name, message='What is the client {}?'):
    field = None

    while not field:
        field = input(message.format(field_name))

    return field

#Another funtion to try get  values from clients
def _get_client_from_user():
    client = {
        'name': _get_client_field('name'),
        'company': _get_client_field('company'),
        'email': _get_client_field('email'),
        'position': _get_client_field('position'),
    }

    return client

# Private method  to get the  client name
def _get_client_name():
    client_name = None
    while not client_name:
        client_name = input('Please type the client name... ')

        if client_name == 'exit':
            client_name = None
            break
    if not client_name:
        sys.exit()

    return client_name

# main function calls crate_client
if __name__ == '__main__':
    _initialize_clients_from_storage()
    _print_welcome()

 # Stop the execution until we have a option selected
    command = input()
    command = command.upper()

 # Lets check what the user want to do
    if command == 'C':
        client = _get_client_from_user()
        create_client(client)
        #list_clients()
    elif command == 'R':
        list_clients()
    elif command == 'U':
        #list_clients()
        client_id = int(_get_client_field('id'))
        updated_client = _get_client_from_user()

        update_client(client_id, updated_client)
        #list_clients()   
    elif command == 'D':
        #list_clients()
        client_id = int(_get_client_field('id'))


        delete_client(client_id)
        list_clients()
    elif command == 'S':
        client_name = _get_client_field('name')
        found = search_client(client_name)
        if found:
            print(client_name + ' found!')
        else:
            print( ' {} not found!'.format(client_name))
    else:
        print('Invalid option')

    _save_clients_to_storage()
