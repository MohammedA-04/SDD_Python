# Customer Service Bot | Largest Project So Far...
# Greeting
def greeting():
    name = input(' Thanks for Contacing Tiny Space! May I have your Name? ').capitalize()
    print(f'Thanks, {name}!\n')
    return

# Cat Select
def Category_Select():
    Category = input('Please select from one of the categories via numbers from 1 to 5'
                     '\n[1] Store Hours & Location'
                     '\n[2] Status Order'
                     '\n[3] Issue w Order '
                     '\n[4] Design Services '
                     '\n[5] Other'
                     '\nAnswer Here =')

    if Category == '1' or ' 1':
        StoreLocation_Hours()
        return

    if Category == '2'or ' 2':
        OrderStatus()
        return

    if Category == '3'or ' 3':
        OrderIssue()
        return

    if Category == '4' or ' 4':
        DesignServices()
        return

    if Category == '5' or ' 5':
        OtherServices()
        return

#if Category not in ['1', '2', '3', '4', '5']:
    #Category_Select()

# The 5 Categories
def StoreLocation_Hours():
    Location = '2300 Riverside Lane Boston, MA 02101'
    Hrs = 'Monday - Saturday from 10am to 6pm'
    print(f' Tiny Space is located in {Location}.\n The store is open at {Hrs}.')

    Addtional_Q = input('   May i help you with anything else? [Yes/No] ').lower()
    if Addtional_Q == 'Yes' or ' Yes':
        Category_Select()
    elif Addtional_Q == ' No':
        print('Thanks for contacting Tiny Space')
    return

def OrderStatus():
    Name = input(' I can help you with that, input your Full Name that was on the Order ')
    OrderID = Input(' Can you input your Order Identifaction Number'
                    ' This can be found on the Online Reciept or Parcel Near The Barcode... ')

    print('Thanks your info is being passed to Dpt.OrderStatus collegues whereby they`ll check the Order Status ')
    Transfer_Elliot()
    return

def OrderIssue():
    print('I`m sorry that you`re expwercing issues with your order.' )
    Name = input('Input Full Name on the order? ')
    OrderID = input('Input Order Number')
    issue = ('Could briefly describe your issue with your order?'
             'So We can transfer you to a colleague')
    Transfer_Colleague()
    return

def DesignServices():
    print('I can help you out with your Desgin Quesitons')
    Transfer_Ramon()
    return

def OtherServices():
    print('Your being transferred to Colleague Trinty')
    Transfer_Trinty()
    return

# Agents of Each Dpt. | Cat'd by Function UDF
def Transfer_Elliot():
    print('Thanks for contacting Tiny Space')
    print("Awesome! I`m checking the status of the order now.")
    return

def Trasnfer_Chrissa():
    print('Thanks for contacting Tiny Space')
    print("Thanks for providing that information. I'm looking into this now")
    return

def Transfer_Ramon():
    Design_Q = input('Tell me how may i assist you')
    print(f'Thanks your Design Query,{Design_Q} will noted by Design Team!')

    Addtional_Q = input(' May i help you with anything else? [Yes/No] ').lower()
    if Addtional_Q == ' Yes':
        Category_Select()
    elif Addtional_Q == ' No':
        print('Thanks for contacting Tiny Space')
    return

def Trasnfer_Trinty():
    print('Thanks for contacting Tiny Space')
    Other_Q = input('No Problem, please describe to me how i may be of assistance')
    return

# Start the Call
greeting()
Category_Select()
