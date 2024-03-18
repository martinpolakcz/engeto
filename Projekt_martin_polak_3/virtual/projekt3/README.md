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
kód_obce,název_obce,Voličiv seznamu,Vydanéobálky,Platnéhlasy,Občanská demokratická strana,Řád národa - Vlastenecká unie,CESTA ODPOVĚDNÉ SPOLEČNOSTI,Česká str.sociálně demokrat.,Radostné Česko,STAROSTOVÉ A NEZÁVISLÍ,Komunistická str.Čech a Moravy,Strana zelených,ROZUMNÍ-stop migraci,diktát.EU,Strana svobodných občanů,Blok proti islam.-Obran.domova,Občanská demokratická aliance,Česká pirátská strana,Unie H.A.V.E.L.,Referendum o Evropské unii,TOP 09,ANO 2011,Dobrá volba 2016,SPR-Republ.str.Čsl. M.Sládka,Křesť.demokr.unie-Čs.str.lid.,Česká strana národně sociální,REALISTÉ,SPORTOVCI,Dělnic.str.sociální spravedl.,Svob.a př.dem.-T.Okamura (SPD),Strana Práv Občanů
529303,Benešov,13104,8485,8437,1052,10,2,624,3,802,597,109,35,112,6,11,948,3,6,414,2577,3,21,314,5,58,17,16,682,10
532568,Bernartice,191,148,148,4,0,0,17,0,6,7,1,4,0,0,0,7,0,0,3,39,0,0,37,0,3,0,0,20,0
