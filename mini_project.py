dictionary={}

while True:
    print("/n dictionary Management System")
    print("1.Add a Word")
    print("2.Search For Meaning")
    print("3.Display All Words")
    print("4.Update Meaning")
    print("5.Delete Word")
    print("6.Exit")

    choice = input("enter your choice: ")

    if choice=="1":
        word = input("Enter The Word: ").lower()
        meaning=input("Enter The Meaning: ")
        dictionary[word]= meaning
        print("word added successfully")

    elif choice=="2" :
        word=input("Enter the Word To Search: ")
        if word in dictionary:
            print("Meaning", dictionary[word])
        else:
            print("Word not found in dictionary. ")

    elif choice == "3" :
        print( " word and their meanings" )
        print(dictionary.items()) 

    elif choice == "4" :
         if word in dictionary:
             word=input("enter the word to update meaning :")
             meaning=input("enter the new meaning:")
             dictionary[word]= meaning
             print("Word-Meaning updated Successfully")
         else:
             print("Word is not found")
             
    elif choice == "5" :
        if word in dictionary:
            word=input("Enter the word to delete:")
            dictionary.pop(word)
            print(dictionary)
        else:
            print("Word is not found")
    else:
        break



        
        

