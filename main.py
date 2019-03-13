#Creating the sting
clients = 'Pablo,Ricardo,' 


# global is used to define that the  variable clients is global
# it means that it has been defined as 'Pablo and Ricardo'
def create_client(client_name):
    global clients
 #Assigning the new value to the previus string state and then
 #we add the comma   
    clients += client_name
    _add_comma()


#Fucntion to add a comma after each name we add
def _add_comma():
    global clients

    clients += ','

#Function to list clients
def list_clients():
    global clients

    print clients

#main function calls crate_client
if __name__ == '__main__':
     list_clients()

     create_client('David')

     list_clients()  
