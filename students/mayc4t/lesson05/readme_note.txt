#!/usr/bin/env python3


def dict_1() :
    # Create a dictionary containing “name”, “city”, and “cake”
    # for “Chris from “Seattle” who likes “Chocolate” 
    print( "\n\ndict_1")
    d1 = {}
    d1['name'] = "Chris"
    d1['city']="Seattle"
    d1['cake']="Chocolate"
    print( d1 )
    
    # Delete the entry for “cake”.
    print( d1.popitem()) 
    print( d1 )
    
    # Add an entry for “fruit” with “Mango” and display the dictionary.
    d1['fruit'] = "Mango"
    print( d1 )
    
    # Display the dictionary keys & values
    print( d1.keys() )
    print(d1.values())
    
    # Display whether or not “cake” is a key in the dictionary (i.e. False) (now).
    print( 'cake' in d1 )
    
    # Display whether or not “Mango” is a value in the dictionary (i.e. True).
    print( "Mango" in d1.values())


def dict_2():
    """
    Creat the dictions2 from dictionaries 1
    
    Using the dictionary from item 1:
    Make a dictionary using the same keys but with the number of ‘t’s in eacih value as the value
    consider upper and lower case?).
    """
    print( "\n\ndict_2")
    d1 = {'name': "Chris",'city': "Seattle",'cake': "Chocolate"}
    d2={}

    for k,v in d1.items():
        d2[k]=v.lower().count('t')
    print(d2)
        

def set1():
    """ Creat set1 with pre-defined guideline
    
    Create sets s2, s3 and s4 that contain numbers from zero through twenty, divisible by 2, 3 and 4.
    Display the sets.
    Display if s3 is a subset of s2 (False)
    and if s4 is a subset of s2 (True).
    """
    
    print( "\n\nset1" )
    set2 = set(range(0,21,2))
    print("set 2: {}".format(set2) )
    
    set3 = set(range(0,21,3))
    print( "set 3: {}".format(set3 ))
    
    set4 = set(range(0,21,4))
    print( "set 4: {}".format(set4 ))

    print("\nSet 3 is subset s2: ", set3.issubset(set2)) 
    print("Set 4 is subset s2: ", set4.issubset(set2)) 
    

def set2():
    """ Create set 2 with required guideline.
    Sets 2
     
    Create a set with the letters in ‘Python’ and add ‘i’ to the set.
    Create a frozenset with the letters in ‘marathon’.
    display the union and intersection of the two sets.
    """

    print( "\n\nset2 " )
    pset = set("Python")
    pset.add('i')

    print("pset :{}".format(pset))
    mset = frozenset("marathon")
    print("mset :{}".format(mset))
    
    print ("Union: ", pset.union(mset))
    print ("Intersection: ", pset.intersection(mset))





def menu_selection( prompt, dispatch_dict):
    while True:
        response = input(prompt)
        if dispatch_dict[response]()=="exit menu":
            break

def fun1():
    print ("You selected the first option!")

def fun2():
    print ("You selected the second option!")

def fun3():
    print ("You selected the third option!")

def fun4():
    print ("You selected the fourth option!")

def sub_menu():
    menu_selection(sub_prompt, sub_dispatch)

def quit():
    print ("Quitting this menu now")
    return "exit menu"

main_prompt = ( "\nYou are in the main menu now!!!\n"
                "What do you want to do?\n"
                "Type 1,2,3,4, or to get a submenu.\n"
                "or q to exti >> "
              )

main_dispatch= { "1": fun1,
                 "2": fun2,
                 "3": fun3,
                 "4": fun4,
                 "5": sub_menu,
                 "q": quit,
                }

sub_prompt = ( "\nYou are in the sub menu now!!!\n"
                "What do you want to do?\n"
                "Type 1,2,3,4 or q to exti >> "
              )



sub_dispatch= {"1": fun1,
                "2": fun2,
                "3": fun3,
                "4": fun4,
                "q": quit,
               }



def file_process():
    print ("Current Dir",os.getcwd())
    print ("Abs path: ", os.path.abspath(os.getcwd()))
    print ("Rel path: ", os.path.relpath(os.getcwd()))
    
        
    names = os.path.split(os.getcwd())
    print("Split :", '===='.join(names))
    names2 = os.path.splitext(os.getcwd())
    print("split text :", '++++'.join(names2))

    print("Base name: ", os.path.basename(os.getcwd()))
    print("Dirname: ", os.path.dirname(os.getcwd()))
  #  os.path.join()

    print( "listdir: ", os.listdir(os.getcwd()))
    #os.mkdir()
    #os.walk()

# Get a little bit of practice with handling files and parsing simple text.
# 
# Paths and File Processing
# 
    # Write a program which prints the full path for all files in the current directory, one per line
    for file in os.listdir(os.getcwd()):print (os.path.abspath(file))

    # Write a program which copies a file from a source, to a destination (without using shutil, or the OS copy command).
    for file in os.listdir( os.getcwd()):
        #source = os.path.join( os.getcwd(), file)
        source = os.path.abspath(file)
        print (source)
        dest   = os.path.join( os.getcwd(), file + "copy")
        with open(source, 'rb') as infile, open(dest, 'wb') as outfile:
            outfile.write(infile.read())
        print()
# 
# Advanced: make it work for any size file: i.e. don’t read the entire contents of the file into memory at once.
# This should work for any kind of file, so you need to open the files in binary mode: open(filename, 'rb') (or 'wb' for writing). Note that for binary files, you can’t use readline() – lines don’t have any meaning for binary files.
# Test it with both text and binary files (maybe jpeg or something of your chosing).
# 





if __name__=='__main__':
    print ("MAIN")
    dict_1()
    dict_2()
    set1()
    set2()

    menu_selection(main_prompt, main_dispatch)

    file_process()



from rnadom import SystemRandom
from string import ascii_letters as letters

bigstring = ''.join(SystemRandom().choice
