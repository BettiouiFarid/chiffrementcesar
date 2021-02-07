



def cesar(text):

    original_tab = [['e', '0.159'], ['a', '0.094'], ['i', '0.084'], ['s', '0.079'], ['t', '0.073'], ['n', '0.072'], ['r', '0.065'], ['u', '0.062'], ['l', '0.053'], ['o', '0.051'], ['d', '0.034'], ['m', '0.032'], ['p', '0.029'], ['q', '0.029'], ['c', '0.026'], ['v', '0.021'], ['b', '0.01'], ['f', '0.01'], ['j', '0.009'], ['j', '0.009'], ['h', '0.008'], ['x', '0.003'], ['z', '0.003'], ['y', '0.002'], ['k', '0.00'], ['w', '0.00']]
    tab = []

    text = text.lower()

    alphabet = "abcdefjhijklmnopqrstuvwxyz"

    space = 0
    
    #####    Initialisation

    for i in alphabet : 

        position = ord(i) - 97
        element = []
        element.append(i)
        element.append("0")
        tab.append(element) 


    for caracter in text :
        
        if caracter == " " :

            space+=1
            continue
        
        if caracter == "," :

            space+=1
            continue
        
        if caracter == "’" :

            space+=1
            continue

        position = ord(caracter) - 97
        
        a = int(tab[position][1])
        a+=1
        tab[position][1] = a 

    #### Remplacer le nb de repetition vc % 
    
    len_net = len(text) - space

    for i in tab : 

            i[1]= format(int(i[1])/len_net,'.3f')
    print(tab)
    tab.sort(key=lambda x: x[1],reverse=True)

    
    print(tab)

    ##### lettre of original_tab to tab #####
    i = 0
    k = 0
    taille = 15
    while i < taille : 

        k+=ord(tab[i][0]) - ord(original_tab[i][0])
        i+=1

    k = int(k/taille)


    #### Decrypte
    
    for cle in range(k-1,k+2) : 
    
        message =""

        for caracter in text :
            
            if caracter == " " :
                
                message +=" "
                continue
            
            if caracter == "’" :
                
                message +=caracter
                continue
            
            if caracter == "," :
                
                message +=caracter
                continue
            
            a = ord(caracter)-cle
            
            if a < 79 : 

                message += chr(a+26)
            
            else : 
                message += chr(a)
        
        print(message)
        print()

text = input("entrer votre message chiffré: ")
cesar(text)
