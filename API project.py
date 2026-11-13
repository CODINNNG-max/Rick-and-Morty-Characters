import requests

url="https://rickandmortyapi.com/api/character"
def check(user):
    if user=="":
        print("Cannot leave empty !")
        return False
    else:
        return True
    
while True:
    try:
        user_input=int(input("1.Would you like to search a character from the show rick and morty \n2.Exit program\n"))
    except ValueError:
        print('Enter a number please')
        continue
    if user_input==1:    
        try:
            que_params={}
            nm=input("What character from the rick and morty franchasie would you like to find : ").lower().strip()
            que_params["name"]=nm
            print(f"You can filter {nm} by :\n1.Status : Alive|Dead|Unknown \n2.Species : Human|Alien|... \n3.Both above \n4.None")
            while True:
                ch=input(f'Enter filters for {nm} : ')
                if check(ch): 
                    if ch =="1":
                        st=input(f"Enter {nm}\'s status : ").lower().strip()
                        if check(st):
                            que_params["status"]=st
                            break
                        else:
                            continue
                    elif ch=="2":
                        sp=input("Enter specified species : ").lower().strip()
                        if check(sp):
                            que_params["species"]=sp
                            break
                        else:
                            continue
                    elif ch=="3":
                        st=input(f"Enter {nm}\'s status : ").lower().strip()
                        sp=input("Enter specified species : ").lower().strip()
                        if check(st) and check(sp):
                            que_params["status"]=st
                            que_params["species"]=sp
                            break
                        
                    elif ch=="4":
                        print("No filters applied")
                        break
                    else:
                        print("Please enter a number from the ones listed above")
                        continue
            try:    
                response = requests.get(url,params=que_params)
            except requests.exceptions.RequestException:
                print("Failed to connect to server")
                continue
            if response.status_code==404:
                print(f"No characters found matching {nm} with those filters")
            else:
                ram=response.json()
                if ram['info']['count'] <=20:
                    print(f"There's {ram['info']['count']} {nm}'s that match your filter")
                else:
                    print(f"There are {ram['info']['count']} {nm}'s that match your filter the first 20 are :")
                for index,i in enumerate(ram['results'],1):
                    print(f"{index}. Name : {i['name']} | Status {i['status']} | Species {i['species']}")
                    
                while True:
                    try:
                        explore=int(input("Would you like to explore a variant in greater detail ? \n1.Enter to continue \n2.To exit :\n"))
                    except ValueError:
                        print("Please enter a number")
                        continue
                    if explore==1:
                        try:
                            search=int(input("Enter the number of the variant you would like to explore :"))
                            if search>=1 and search <=len(ram['results']):
                                chosen=ram['results'][search-1]
                                print(f"Name : {chosen['name']} | Origin : {chosen['origin']['name']} | Type : {chosen['type']} | Location : {chosen['location']['name']}")
                            else:
                                print('Not found')
                        except KeyError:
                            print("Failed to find key")
                            
                    elif explore==2:
                        print("Exited successfully")
                        break
                    else:
                        print("Please enter a number from above")
                        continue

        except Exception as e :
            print(f"Error found : {e}")
    elif user_input==2:
        print("Program exited successfully")
        break
    else:
        print("Please pick a value provided above !")
        continue