def create(name):
    file=open(f"{name}.txt","w")
    file.close()
def read(name):
    file=open(f"{name}.txt","r")
    content = file.read()
    file.close()
    return content
    
def write(text,filename):
    file=open(f"{filename}.txt", "w")
    charlen= file.write(text)
    print(f"You have successfully written in file, total character Length: {charlen}")
    file.close()
def add(text, filename):
    file=open(f"{filename}.txt","a")
    charlen=file.write(f"\n{text}")
    print(f"You have successfully written in file, Total Character length: {charlen}")
    file.close()
def dataf(data):
    file=open("database.txt","a")
    for i,n,a,l in data:
        file.write(f"{i:5} {n:20} {a:6} {l:14}\n")
        print(f"{i:5} {n:20} {a:6} {l:14}")
    file.close()

while True:
    print("File handling".center(50))
    print("\n1.Create file\n2.Text file\n3.Structured data file\n4.Quit")
    c=input("Enter your selection: ")
    if(c=="1"):
        name=input("Enter your file name: ")
        create(name)
        continue
    if(c=="2"):
        print("Text file:\n1.Read file\n2.Write file\n3.Add data into file\n4.quit")
        a=input("Enter your selection: ")
        if(a=="1"):
            name=input("Enter your file name: ")
            content=read(name)
            print(f"{content}")
            continue
        if(a=="2"):
            text=input("Enter your text: ")
            name=input("Enter your file name: ")
            write(text,name)
            continue
        if(a=="3"):
            text=input("Enter your text: ")
            name=input("Enter your file name: ")
            add(text,name)
            continue
        if(a=="4"):
            break

    if(c=="3"):
        print("Structured file:\n1.Read file\n2.Add data into file\n3.Quit")
        r=input("Enter your selection: ")
        if(r=="1"):
            name=input("Enter your file name: ")
            content=read(name)
            print(f"{content}")
            continue

        if(r=="2"):
            ids=int(input("Enter id: "))
            name=input("Enter name: ")
            age=int(input("Enter age: "))
            place=input("Enter place: ")
            data=[ids,name,age,place]
            dataf(data)
            continue
        if(r=="3"):
            break
    if(c=="4"):
        print("Invalid selection")
        break
        
          

    
        

        
        
        
        
        
