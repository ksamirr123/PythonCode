Dict={
    "Name":"Sameer",
     "Year":2,
     "Room no":309,
     "Marks":{
         "phy":99,
         "chem":98,
         "maths":97,
     }

}
print(Dict.keys())#return all the keys
print(Dict.values())#return all the values
print(Dict.items())#return all items in the dictionary
print(Dict.get("Year"))#return specific value in dict
Dict.update({"na":"same"})#to update the key,val in dictionary
print(Dict.update({"Year":"4"}))
print(Dict)