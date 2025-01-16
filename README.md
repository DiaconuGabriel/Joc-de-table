# Joc-de-table

Pentru acest proiect au fost utilizate librariile: pygame, random, sys, os, time, socket, pickle si contine 3 fisiere: server.py, table_player.py si table_player1.py.
	
Serverul este unul iterativ si tine cont de tura fiecarui jucator. El asteapta o conexiune, 
iar in momentul in care a primit prima conexiune, o accepta, si ii trimite acesteia numarul de
jucatori, apoi asteapta cea de a doua conexiune. Dupa ce a acceptat si cea de a doua conexiune,
trimite ambelor conexiuni numarul de jucatori care este 2 si intra intr-o bucla while. Dar 
inainte de a intra in bucla while se verifica daca primul jucator intrat in server are acelasi
IP cu serverul, deoarece el este cel care trebuie sa faca prima mutare. In bucla while daca
este tura primului jucator serverul primeste date de la acesta si le despacheteaza pentru a
modifica tura jucatorilor in cazul in care unul dintre ei a terminat de mutat, iar apoi le trimite
jucatorilor datele primite. In acest fel este tratat si cel de al doilea jucator.

Celelalte 2 fisiere sunt la fel, doar ca fisierul table_player1.py contine si cod 
capabil de a muta piese maro care este folosit in cazul in care se doreste a juca cu altcineva.
Proiectul contine 2 clase denumite Zar si Piesa. Algoritmul dupa care functioneaza jocul este 
urmatorul: fiecare zona in care exista sau vor exista piese este o lista. Fiecare piesa si 
zar din joc reprezinta un obiect. Cele 6 zaruri se gasesc intr-o alta lista. In momentul in care
utilizatorul apasa tasta "SPACE" sunt generate 2 numere random si astfel cu functia de draw a 
fiecarui zar acestea sunt desenate pe tabla. De asemena se salveaza in alte 2 liste pentru
zaruri numarul zarului si numarul de mutari disponibile cu acel zar. In cazul in care zarurile 
sunt egale numarul de mutari disponibile va fi 2. Cu ajutorul tastelor 'n' si 'm' se vor selecta
unul dintre cele 2 zaruri. Dupa aceasta daca utilizatorul apasa pe una din piesele pe care doreste
sa le mute, daca piesa poate fi mutata, se va muta si se va decrementa numarul de mutari si de
asemenea piesa va fi mutata dintr-o lista in alta corespunzator zonei din care face parte.
Dupa ce utilizatorul a consumat mutarile cu cele 2 zaruri, automat celalat jucator va putea muta.
De asemenea in cazul in care unul din jucatori arunca cu zarul si nu exista piese
care pot fi mutate, numarul de mutari cu cele 2 zaruri pe care le-a primit va deveni 0 pentru
fiecare zar, si astfel celalat jucator va putea sa arunce cu zarul si apoi sa mute. In final 
dupa ce unul din jucatori a castigat pe ecranele fiecaruia se va afisa un mesaj in functie daca 
a castigat sau nu.

# Cum Joci?
Cu space dai cu zarul, iar cu m și n selectezi fiecare zar în parte. Faci clic pe piesa pe care dorești să o muți.

# Cateva imagini

![image](https://github.com/user-attachments/assets/367961cd-12b7-4746-ae33-1fbb2e36f27d)

![image](https://github.com/user-attachments/assets/8687e3f7-d4ea-4da8-a2d9-2cb0c3230aed)

![image](https://github.com/user-attachments/assets/8f157d69-08b7-462b-9b92-13c33a991cc1)

![image](https://github.com/user-attachments/assets/1126dfd5-90d7-4c3c-9308-a2e2eb11b7d5)

