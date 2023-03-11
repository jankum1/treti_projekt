## Engeto - 3. projekt

Třetí projekt na Python Akademii od Engeta.

## Popis projektu:
Tento projekt slouží k extrahování výsledků parlamentních voleb v roce 2017. Odkaz: https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=11&xnumnuts=6207

## Instalace knihoven
Knihovny, které jsou použity v kódu jsou uložené v souboru requirements.txt. Pro instalaci doporučuji použít nové virtuální prostředí a s nainstalovaným manažerem spustit následovně
```
  $ pip3 --version                      # overim verzi manazeru
  $ pi3 install -r requirements.txt     # nainstalujeme knihovny
```
## Spuštění projektu:
Spuštění souboru ```election_scraper.py``` v rámci příkazového řádku požaduje dva povinné argumenty.
```
python electin_scraper <odkaz-uzemniho-celku> <vysledny-soubor>
```
Následně se vám stáhnou výsledky jako soubor s přílohou ```.csv```
    
## Ukázka projektu
Výsledky hlasování pro okres Znojmo:
1. argument: ```https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=11&xnumnuts=6207```
2. argument: ```vysledky_znojmo.csv```

Spuštění programu:

```python election_scraper.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=11&xnumnuts=6207" "vysledky_znojmo.csv"```

Průběh stahování:
```
LET'S GO!
DOWNLOADING DATA FROM THE SELECTED URL: https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=11&xnumnuts=6207
ELECTION RESULTS WAS SAVED TO FILE: vysledky_znojmo.csv
EXITING election_scraper...
```
Částečný výstup:
```
Code,Location,Registered,Envelopes,Valid,Občanská demokratická strana,Řád národa - Vlastenecká unie,CESTA ODPOVĚDNÉ SPOLEČNOSTI,Česká str.sociálně demokrat.,Radostné Česko,STAROSTOVÉ A NEZÁVISLÍ,Komunistická str.Čech a Moravy,Strana zelených,"ROZUMNÍ-stop migraci,diktát.EU",Strana svobodných občanů,Blok proti islam.-Obran.domova,Občanská demokratická aliance,Česká pirátská strana,Referendum o Evropské unii,TOP 09,ANO 2011,Dobrá volba 2016,SPR-Republ.str.Čsl. M.Sládka,Křesť.demokr.unie-Čs.str.lid.,Česká strana národně sociální,REALISTÉ,SPORTOVCI,Dělnic.str.sociální spravedl.,Svob.a př.dem.-T.Okamura (SPD),Strana Práv Občanů,Národ Sobě
593729,Bantice,228,153,151,8,0,0,13,0,4,12,4,4,4,0,0,9,0,1,34,0,0,32,0,0,0,1,23,1,1
593737,Běhařovice,318,209,208,5,0,0,20,1,3,16,1,2,0,0,1,12,0,0,101,0,0,28,0,0,0,1,17,0,0
593745,Bezkov,157,110,110,0,0,0,9,0,4,12,2,1,3,0,0,6,0,6,25,0,0,26,0,0,0,0,14,2,0
...
```
