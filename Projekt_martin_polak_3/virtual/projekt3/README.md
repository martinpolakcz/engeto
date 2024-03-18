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
```
Processing: 529303 : Benešov
Processing: 532568 : Bernartice
Processing: 530743 : Bílkovice
Processing: 532380 : Blažejovice
Processing: 532096 : Borovnice
Processing: 532924 : Bukovany
Processing: 529451 : Bystřice
Processing: 532690 : Ctiboř
Processing: 529478 : Čakov
```
**Částečný výstup**
| kód_obce | název_obce | Voličiv seznamu | Vydanéobálky | Platnéhlasy |Občanská demokratická strana |Řád národa - Vlastenecká unie | CESTA ODPOVĚDNÉ SPOLEČNOSTI |
|-------|-------|-------|---|---|---|---|---|
|29303|Benešov|13104|8485|8437|1052|10|2|
|532568|Bernartice|191|148|148|4|0|0|
|530743|Bílkovice|170|121|118|7|0|0|
|532380|Blažejovice|96|80|77|6|0|0|
|532096|Borovnice|73|54|53|2|0|0|
|532924|Bukovany|598|393|393|50|0|0|
|529451|Bystřice|3490|2206|2200|204|6|2|
|532690|Ctiboř|106|83|83|3|0|0|
|529478|Čakov|93|71|71|7|0|0|




