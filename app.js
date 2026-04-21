
document.body.innerHTML = '';

// ==========================================
// SEKCJA 1: Wpisanie funkcji ręcznie
// ==========================================
const sekcjaTekstowa = document.createElement('div');
sekcjaTekstowa.style.marginBottom = '40px'; // Odstęp od dołu

const tytul1 = document.createElement('h3');
tytul1.innerText = '1. Wpisz funkcję logiczną z klawiatury:';

const poleTekstowe = document.createElement('input');
poleTekstowe.type = 'text';
poleTekstowe.placeholder = 'np. A AND B';
poleTekstowe.style.marginRight = '10px';
poleTekstowe.style.padding = '5px';

const przyciskTekst = document.createElement('button');
przyciskTekst.innerText = 'Wyślij funkcję';

sekcjaTekstowa.appendChild(tytul1);
sekcjaTekstowa.appendChild(poleTekstowe);
sekcjaTekstowa.appendChild(przyciskTekst);
document.body.appendChild(sekcjaTekstowa);


// ==========================================
// SEKCJA 2: Generator Tabeli Prawdy
// ==========================================
const sekcjaTabeli = document.createElement('div');

const tytul2 = document.createElement('h3');
tytul2.innerText = '2. Lub wygeneruj tabelę prawdy:';

const etykieta = document.createElement('label');
etykieta.innerText = 'Liczba zmiennych (np. 3): ';


const poleIloscZmiennych = document.createElement('input');
poleIloscZmiennych.type = 'number';
poleIloscZmiennych.value = '3';
poleIloscZmiennych.min = '1';
poleIloscZmiennych.max = '5';
poleIloscZmiennych.style.width = '40px';
poleIloscZmiennych.style.marginRight = '10px';

const przyciskGeneruj = document.createElement('button');
przyciskGeneruj.innerText = 'Generuj tabelę';

const kontenerNaTabele = document.createElement('div'); // Tutaj wskoczy nasza tabela


sekcjaTabeli.appendChild(tytul2);
sekcjaTabeli.appendChild(etykieta);
sekcjaTabeli.appendChild(poleIloscZmiennych);
sekcjaTabeli.appendChild(przyciskGeneruj);
sekcjaTabeli.appendChild(kontenerNaTabele);
document.body.appendChild(sekcjaTabeli);



przyciskGeneruj.addEventListener('click', () => {
    
    kontenerNaTabele.innerHTML = ''; 
    
    const ileZmiennych = parseInt(poleIloscZmiennych.value);
    const tabela = document.createElement('table');
    tabela.style.borderCollapse = "collapse";
    tabela.style.marginTop = "20px";
    
    
    const wierszNaglowkowy = document.createElement('tr');
    for (let i = 0; i < ileZmiennych; i++) {
        const th = document.createElement('th');
        th.innerText = `X${i + 1}`;
        th.style.border = "1px solid black";
        th.style.padding = "8px";
        wierszNaglowkowy.appendChild(th);
    }
    const thWynik = document.createElement('th');
    thWynik.innerText = "Wynik (Y)";
    thWynik.style.border = "1px solid black";
    thWynik.style.padding = "8px";
    wierszNaglowkowy.appendChild(thWynik);
    tabela.appendChild(wierszNaglowkowy);

    
    const liczbaWierszy = Math.pow(2, ileZmiennych);
    for (let i = 0; i < liczbaWierszy; i++) {
        const wiersz = document.createElement('tr');
        const binarnie = i.toString(2).padStart(ileZmiennych, '0');
        
        for (let bit of binarnie) {
            const komorka = document.createElement('td');
            komorka.innerText = bit;
            komorka.style.border = "1px solid black";
            komorka.style.padding = "8px";
            komorka.style.textAlign = "center";
            wiersz.appendChild(komorka);
        }

    
        const wynikTd = document.createElement('td');
        wynikTd.style.border = "1px solid black";
        wynikTd.style.padding = "8px";
        
        
        const poleWyniku = document.createElement('input');
        poleWyniku.type = 'text';
        poleWyniku.maxLength = 1; // Zablokuj do 1 znaku
        poleWyniku.style.width = '30px';
        poleWyniku.style.textAlign = 'center';
        
        
        poleWyniku.addEventListener('input', (event) => {
            if (event.target.value !== '0' && event.target.value !== '1') {
                event.target.value = '';
            }
        });

        wynikTd.appendChild(poleWyniku);
        wiersz.appendChild(wynikTd);
        tabela.appendChild(wiersz);
    }
    
    kontenerNaTabele.appendChild(tabela);

    
    const przyciskWyslijTabele = document.createElement('button');
    przyciskWyslijTabele.innerText = 'Wyślij wyniki z tabeli';
    przyciskWyslijTabele.style.marginTop = '15px';
    kontenerNaTabele.appendChild(przyciskWyslijTabele);
});


przyciskGeneruj.click();