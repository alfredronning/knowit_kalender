# Julenisse valg

Julenissen har vært sjefen på nordpolen så lenge alle kan huske.
Etter en del politisk press, og mye kritikk, har han blitt tvuget til å gjøre nordpolen om til et demokrati og stille til åpent valg.

Nordpolen har fortsatt lang vei å gå på når det kommer til likestilling, for nå er det kun snille barn som får stemmene.
Julenissen har fått mye kritikk for dette, så han har måttet inngå et kompromiss der stemmen blir vektet av hvor slemme barna har vært.

På alle stemmene står det hvilke handlinger barnet har gjort, og hvem de vil stemme på.
Og det er kun den slemmeste handlingen barnet har gjort som avgjør hvor mye stemmen skal telle.

Det er selvfølgelig ingen tvil om at julenissen kommer til å vinne.
Spørsmålet er hvor hardt han kommer til å vinne.
Det har likevel ikke skremt hans to motstandere Sneglulf og Alvekongen fra å stille til valg.

## Oppgave

Man får en liste med slemme handlinger, og hvordan de er vektet.
Med en slem handling per linje som ligger [her](slemmehandlinger.txt).

```
tagging:0.5
gå på rød mann:0.8
lugge:0.3
```

Hvis slemme handlinger er som listet over, og et barn har begått alle disse tre handlingene, vil stemmen telle 0.3, siden å lugge er verst.
Handlinger som ikke ligger i slemmelista, vil telle som 1.0, altså null slemt.

Inputen på alle stemmene som ligger [her](stemmer.txt), innerholder handlinger og navnet som stemmes på.
Der er handlingene komma-separert, og navnet på personen de stemmer på separert med kolon.

Oppgaven er å si med hvor mange stemmer julenissen slo andreplassen med, rundet til nærmeste heltall.

## Eksempel

Med slemme handlinger:
```
tagging:0.8
banne i kirka:0.1
bite:0.2
```

Og stemmer:
```
tagging,aking,julebollebaking:julenissen
tegning,banne i kirka,julegavepakking:sneglulf
bite,lage julepynt,tagging:alvekongen
```

Så ville julenissen fått 0.8 stemmer, sneglulf 0.1 og alvekongen 0.2. Stemmen på alvekongen har to slemme handlinger, både biting og tagging. Siden biting er den verste av disse to, så teller stemmen 0.2.

Resultatet blir da `0.8-0.2 = 0.6` som blir rundet opp til `1`.
