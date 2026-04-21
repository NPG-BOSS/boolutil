document.body.innerHTML = '';

// ==========================================
// SEKCJA 1: Wpisanie funkcji ręcznie
// ==========================================
const sekcjaTekstowa = document.createElement('div');
sekcjaTekstowa.style.marginBottom = '40px'; 

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

const kontenerNaTabele = document.createElement('div'); 

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
    
    // Nagłówki
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

    // Generowanie wierszy
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
        
        // Cykliczny przycisk
        const poleWyniku = document.createElement('button');
        poleWyniku.innerText = '0'; 
        poleWyniku.className = 'wynik-btn'; 
        poleWyniku.style.width = '40px';
        poleWyniku.style.height = '30px';
        poleWyniku.style.cursor = 'pointer';
        poleWyniku.style.fontWeight = 'bold';
        
        poleWyniku.addEventListener('click', (event) => {
            if (event.target.innerText === '0') {
                event.target.innerText = '1';
            } else if (event.target.innerText === '1') {
                event.target.innerText = '-';
            } else {
                event.target.innerText = '0';
            }
        });

        wynikTd.appendChild(poleWyniku);
        wiersz.appendChild(wynikTd);
        tabela.appendChild(wiersz);
    }
    
    kontenerNaTabele.appendChild(tabela);

    // PRZYWRÓCONY PRZYCISK WYSYŁANIA
    const przyciskWyslijTabele = document.createElement('button');
    przyciskWyslijTabele.innerText = 'Wyślij wyniki z tabeli';
    przyciskWyslijTabele.style.marginTop = '15px';
    kontenerNaTabele.appendChild(przyciskWyslijTabele);

    // LOGIKA ZBIERANIA DANYCH PODPIĘTA POD PRZYCISK WYSYŁANIA
    przyciskWyslijTabele.addEventListener('click', () => {
        const wszystkiePola = kontenerNaTabele.querySelectorAll('.wynik-btn');
        const zebraneWyniki = [];

        wszystkiePola.forEach(pole => {
            zebraneWyniki.push(pole.innerText);
        });

        console.log("Paczka dla backendu:", zebraneWyniki);
        alert("Zebrano dane! Zobacz konsolę (F12).");
    });
});

przyciskGeneruj.click();