import csv
import ast
print('Welcome to iPhonebook !')
# function

# python has a built-in function for that: capitalize()

def makelis(string):
    res = ast.literal_eval(string)
    return res

def done(Book):
    with open('E:\F\Study\Python\Phonebook2.0\DataBase.csv','w') as csv_w:
        fnames = ['name','data']
        writer = csv.DictWriter(csv_w,fieldnames=fnames)
        writer.writeheader()
        for each in Book:
            writer.writerow({'name':each,'data':Book[each]})
            
# Database or phonebook
Book = {}
with open('E:\F\Study\Python\Phonebook2.0\DataBase.csv','r') as csv_file:
    reader = csv.DictReader(csv_file)
    for line in reader:
        Book[line['name']] = makelis(line['data'])

# Adding function
def add(n,p,c):
    global Book
    data =[p,c]
    Book[n] = data 

while True:
#Adding
    Choice = input('Adding to book (a) , Deleting (d) , finding (f) ,show all (s):')
    if Choice == 'a' :
        Add_name = input('Name :').capitalize()
        Add_NO = str(input('Phone number :'))
        Add_city = input('City :').capitalize()
        add(Add_name , Add_NO,Add_city)
        print('Updated!')
        secChoice = (input('Exit? (y/n) ')).lower()
        if secChoice == 'y':
            done(Book)
            exit()
        else:
            pass
    #Deleting
    elif Choice == 'd' :
        Del_Target = input('Who should i delete? ').capitalize()
        if Del_Target in Book:
            del Book[Del_Target]
        else:
            print('Sorry invalid name!')
        print("Done!")
        secChoice = (input('Exit? (y/n) ')).lower()
        if secChoice == 'y':
            done(Book)
            exit()
        else:
            pass
    #Finding
    elif Choice == 'f' :
        F_Target = input('Name :').capitalize()
        Choice_1 = input('City (c) , Phone number (p) and all (a)')
        #city
        if Choice_1 == 'c':
            if F_Target in Book :
                print("%s 's City is %s" %(F_Target , Book[F_Target][1]))
            else:
                print('invalid name!')
            secChoice = (input('Exit? (y/n) ')).lower()
            if secChoice == 'y':
                done(Book)
                exit()
            else:
                pass
        #phone number
        elif Choice_1 == 'p' :
            if F_Target in Book:
                print("%s 's Phone number is %s" %(F_Target, Book[F_Target][0]))
            else:
                print('invalid name!')
            secChoice = (input('Exit? (y/n) ')).lower()
            if secChoice == 'y':
                done(Book)
                exit()
            else:
                pass
        #all
        elif Choice_1 == 'a':
            Display_All = "%s's Phone number : %s\nCity : %s"
            if F_Target in Book:
                print(Display_All %(F_Target , Book[F_Target][0], Book[F_Target][1]))
            else:
                print('Invalid name')
            secChoice = (input('Exit? (y/n) ')).lower()
            if secChoice == 'y':
                done(Book)
                exit()
            else:
                pass
        else:
            print('Invalid input')
    elif Choice == 's':
        for each in Book:
            shape = 'Name: %s PhoneNo: %s City: %s' %(each,Book[each][0],Book[each][1]) 
            print(shape)       
    else:
        print('Invalid input.')
    # loop
