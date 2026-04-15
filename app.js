
const tytul = document.createElement('h2');
tytul.innerText = 'Kalkulator Funkcji Logicznych';

const poleTekstowe = document.createElement('input');
poleTekstowe.type = 'text';
poleTekstowe.placeholder = 'Wpisz funkcję, np. A AND B';

const przycisk = document.createElement('button');
przycisk.innerText = 'Oblicz';

const miejsceNaWynik = document.createElement('p');
miejsceNaWynik.innerText = 'Tutaj pojawi się wynik...';


document.body.appendChild(tytul);
document.body.appendChild(poleTekstowe);
document.body.appendChild(przycisk);
document.body.appendChild(miejsceNaWynik);


przycisk.addEventListener('click', () => {
    const wpisanaWartosc = poleTekstowe.value;
    miejsceNaWynik.innerText = 'Przygotowuję do wysłania: ' + wpisanaWartosc;
    
});