Třetí projekt na Python Akademii od Engeta

## Popis projektu
Tento projekt slouží k extrahování výsledků z parlamentních voleb v roce 2017. Odkaz k prohlednutí [zde](https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101)

### Instalace knihoven
Knihovny, které jsou použitý v kódu jsou uložené v souboru requirements.txt. Pro instalaci doporučuju použit nové virtuální prostředí a s nainstalovaným manažerem spustit následovně:
```
$ pip --version                       #overim verzi manazeru
$ pip install -r requirements.txt     #nainstaluje knihovny
```
### Spuštění projektu
Spuštění souboru main.py v rámci přikazového řádku požaduje dva povinné argumenty.
```
python main.py <odkaz-uzemniho-celku> <vysledny-soubor>
```
Následně se vám stáhnou výsledky jako soubor s príponou .csv

### Ukázka projektu
Výsledký hlasování pro okres Benešov:
1. Argument: https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101
2. Argument: vysledky_benesov.csv

**Spuštění programu**
```
python main.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101" "vysledky_benesov.csv"
```

Průběh stahování v konzoli:
> ......

**Částečný výstup**
>....
