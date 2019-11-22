import matplotlib.pyplot as plt
import tkinter as tk
books={1:['half girlfriend','romance','1'],2:["Harry potter","fiction","1"],3:["Cindrella","fiction","2"],4:["Romeo Juliet","drama","4"],5:["The hunger games","sci-fi","3"],6:["Artemis Fowl","sci-fi","2"],7:["Diary of a wimpy kid","funny","5"],8:["Sherlock Holmes","mystery","1"],9:["The Dracula","fiction","6"],10:["RD Sharma","Knowledge","3"],11:["Twilight","fiction","3"],12:["2 states","drama","3"],13:["abcd","ansh","2"]}
def add():
    new=[]
    ISBN=int(input('enter ISBN number '))
    Book=input('enter Book name ')
    category=input('enter Book Category ')
    Volume=input('enter book volume ')
    i=books.keys()
    if ISBN not in i :
        new.append(Book)
        new.append(category)
        new.append(Volume)
        books[ISBN]=new
        print(books)
    else:
        print("\nBook already exists!! \n")
		
def delete():
    ISBN=int(input('enter ISBN number'))
    i=books.keys()
    if ISBN in i:
        del books[ISBN]
        print(books)
    else:
        print("Invalid input")
def replace():
    new=[]
    ISBN=int(input('enter ISBN number '))
    Book=input('enter Book name ')
    category=input('enter Book Category ')
    Volume=input('enter book volume ')
    i=books.keys()
    if ISBN in i :
        new.append(Book)
        new.append(category)
        new.append(Volume)
        books[ISBN]=new
        print(books)
    else:
        print("Book doesn't exist")
def category():
    global cat
    global co
    cat=[]
    co=[]
    for i in books.values():
        if i[1] not in cat:
            cat.append(i[1])
    
    l=list(books.values())
    for temp in cat:
        count=0
        for i in range(len(books)):
            if temp==l[i][1]:
                count=count+1
        co.append(count)
    print(co)        
    plt.bar(cat,co, width=0.5, align='center')
    plt.show()        

def volume():
    global vol
    global cv
    vol=[]
    cv=[]
    for i in books.values():
        if i[2] not in vol:
            vol.append(i[2])
    
    li=list(books.values())
    for temp in vol:
        count=0
        for i in range(len(books)):
            if temp==li[i][2]:
                count=count+1
        cv.append(count)
    print(cv)
    plt.bar(vol,cv, width=0.5, align='center')
    plt.show()
        
        

    
'''while(1):
    print('welcome to library')
    print("The current library is : \n")
    print(books)
    print(len(books))
    print('1. To add a book\n2. to remove a book\n3. To replace a book\n 4.Plotting the graph for categories \n5.Plotting the graph for volume\n0. To Exit ')
    n=int(input("enter your choice from 0 - 4"))
    if n==1:
        add()
    elif n==2:
        delete()
    elif n==3:
        replace()
    elif n==4:
        category()
        plt.bar(cat,co, width=0.5, align='center')
        plt.show()
    elif n==5:
        volume()
        plt.bar(vol,cv, width=0.5, align='center')
        plt.show()
        
    else:
        break
'''
root=tk.Tk()
root.title("Library system")
frame=tk.Frame(root)
frame.pack()
button = tk.Button(frame,text='Add a book',width=25,command= add)
button.pack()
button = tk.Button(frame,text='Remove a book',width=25,command= delete)
button.pack()
button = tk.Button(frame,text='Replace a book',width=25,command= replace)
button.pack()
button = tk.Button(frame,text='Graph for category',width=25,command= category)
button.pack()
button = tk.Button(frame,text='Graph for volume',width=25,command= volume)
button.pack()
button = tk.Button(frame,text='Quit',width=25,command= root.destroy)
button.pack()
root.mainloop()

		