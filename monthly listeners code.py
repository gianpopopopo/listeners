import json

with open('C:/Users/54911/Desktop/Codigos python/Monthly Listeners/kworb.net.json', encoding = "UTF-8") as json_file:
    elements = json.load(json_file)

del elements[0:4]

n = 0

def cut (elements,n):
    if len(elements[-1]) < 4:
        return elements
        
    else:  
        del elements[n]['Cities']
        del elements[n]['Column4']
        
        return cut(elements, n+1)


def listeners (elements):
    artist = str(input("Type the name of an artist to know the monthly listeners: "))
    for i in range(len(elements)):
        if artist == elements[i]['Column2']:
            return (print(f"The artist {artist} has {elements[i]['Column3']} monthly listeners and is {i+1} in the charts on the 17/3/2023."))
    else:
        print("The artist you entered is no in the top 2500 or there was a grammatical error.")
        

cut (elements,n)
listeners (elements)