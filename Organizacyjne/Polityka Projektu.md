# Struktura branchy

##  **Main**

Tutaj mergujemy z brancha [Integracja](###Integracja), [Frontend](###Frontend), i  [Backend](###Backend), gdy funkcjonalność jest gotowa do dodania do aplikacji *(Jeżeli funkcjonalność Backendu wpływa na działanie frontendu, lub odwrotnie, wtedy mergujemy za pośrednictwem integracji, nie bezpośrednio)*. 
    
>Bezpośrednio ją w niej edytujemy tylko pliki .md. 
    
>Z niej hostowana jest strona

### Integracja
Tutaj mergujemy z brancha [Frontend](###Frontend) i [Backend](###Backend) po dokonaniu testów i dokumentacji. Jeżeli aktualizacje funkcjonalność w jednym wymagają zmiany drugiego, z tąd należy pullować do branchy [Backend](###Backend) i [Frontend](###Frontend)
### Backend
Tutaj mergujemy z i pullujemy do branchy osobistych.

 Jeżeli członek zespołu dokona merge'a dodającego nową funkcjonalność, drugi z tąd pulluje do swojego brancha osobistego, a następnie dokonuje testów. Po wykonaniu testów, branch może być zmergowany do [Integracja](###Integracja)

Każdy członek zespołu ma swoje branche osobiste:
#### Backend P
#### Backend W
### Frontend 
Tutaj mergujemy z i pullujemy do branchy osobistych.

 Jeżeli członek zespołu dokona merge'a dodającego nową funkcjonalność, drugi z tąd pulluje do swojego brancha osobistego, a następnie dokonuje testów. Po wykonaniu testów, branch może być zmergowany do [Integracja](###Integracja)

Każdy członek ma swoje branche osobiste
#### Frontend J
#### Frontend M
    
# Dodawanie funkcjonalności

1. Utwórz issue mówiący o funkcjonalności (albo zobacz, że ktoś inny go utwrorzył i przypisał ciebie)
2. Spulluj do swojego brancha osobistego z odpowiedniego brancha aktualną wersję kodu
3. Zmodyfikuj kod tak, by dodał funkcjonalność. Przetestuj wstępnie jego działanie
4. Najlepiej jest pisać dokumentację na beirząco
4. Zmerguj swój kod do brancha z którego pullowałeś
5. Stwórz subissue dotyczącym testu i przypisz do niego drugieo członka zespołu

# Testowanie funkjconalności
1. Zobacz, że ktoś przypisał ci issue dotyczące testu funkcjonalności
2. Spulluj do swojego brancha osobistego z odpowiedniego brancha aktualną wersję kodu 
3. Utwórz **Osobny plik** który importuje kog programu testowanego, a następnie sprawdza, czy zwracana jest poprawna wartość
.
Alternatywnie: Dokonaj testu ręcznego/wizualnego (szczególnie dla testó frontendu)
4. Jeżeli kod przeszedł testy, zmerguj go do odpowiednio wyższego brancha ( zwykle [Integracja](###Integracja) lub [Main](##Main))
5. Jeżeli kod nie przeszedł testów, w issue przekaż informację o tym autorowi. Możesz zapropononować jak naprawić, jednak sam go nie naprawiaj.

# Tworzenie issue
## Tytuł 
Tytuł powinien zawierać kilka słów o tematyce problemu
## Opis 
W opisie powinno być stosunkowo szczegółowo opisane, co powinno być zrobione 
*W przyszłości dodać przykłady*
## Przypisanie
Zależnie od rodzaju zadania, należy przypisać jedną lub kilka osób do zadania, by wiedziały, że mają się nim zająć. Powinno się respektować podział na zespoły.
Można do zadania przypisać samego siebie
> Niedopuszczalne jest tworzenie issue a następnie nie przypsanie nikogo
## Tag
Należy dodać jeden tag zespołu i jeden tag typu zadania
### Tagi zespołu
#### Frontend
Zadanie dotyczy interakcji użytkownika z programem, wyświetlania itp.
#### Backend
Zadanie dotyczy działania kodu, obliczeń, przekształceń itp.
#### Integration
Zadanie dotyczny interakcji między forntendem i backendem, albo obu na raz
#### Organisational
Zadanie dotyczny struktury projektu, tworzenia retrospektyw, sprawozdań itp.
### Tagi typu zadania
#### Enchancement
Dodanie nowej funkcjonalnośći 
#### Test
Nowa funkcjonalność wymaga sprawdzenia
#### Documentation
Funkcjonalność lub projekt wymagają utworzenia/poprawy jakości/ restrukturyzacji dokumentacji
#### Bug
Jakiś błąd został wykryty na testach, lub je przeszedłi został wykryty w późniejsyzm terminie

## Typ
Nieobowiązkowe, pokrywa się funkcjonalnością z tagiem
## Projekt
Tutaj zawsze dajemy **@Boolutil V2** Powinno dodawać się automatycznie
## Milestone
Nie dodajemy
*temat do poprawek optymalizacynych na przyszłość*
## Priority
**To niestety trzeba dodać po utworzeniu issue, za pomocą panelu *Priority board*, *Team items*, lub *My items*.**
### P0
Należy to zrobić jak najszybciej, najlepiej na drugi dzień
### P1
Powinien zostać zagospodarowany czas na wypełnienie zadania w tym samym tygodniu
### P2
Zadanie może czekać na dogodny moment

# Otrzymywanie issue
Po otrzymaniu issue przypisanego do ciebie, należy:
1. Określić rozmiar
2. Bezpośrednio przed rozpoczęciem pracy nad nim zmienić status na **In progress**
3. Po zakończeniu pracy zamknąć issue, dodając komentarz krótko podsumowywujący progress.
## Rozmiary
Rozmiary są określeniem złożoności/trudności/czasochłonności zadania
### XS
Szybciej byłoby to zrobić niż tworzyć issue
### S
Kwestia paru- parunastu minut
### M 
Zadanie na całą małą lub połowę dłuższej sesji 
### L
Zadanie na kilka sesji
### XL
"Nawet nie wiem jak się za to zabrać" wymaga conajmniej kilku sesji i podziału na subissue