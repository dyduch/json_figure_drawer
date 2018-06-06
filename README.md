# json_figure_drawer


NapisaÄ program, ktĂłry odczytuje plik w formacie JSON z opisem grafiki, wyĹwietla tÄ grafikÄ na ekranie i zapisuje w pliku PNG.

Plik moĹźe zawieraÄ:

    punkty
    wielokÄty (podana lista punktĂłw)
    prostokÄty (wspĂłĹrzÄdne Ĺrodka, wysokoĹÄ, szerokoĹÄ) - rĂłwnolegle do osi ukĹadu wspĂłĹrzÄdnych
    kwadraty (Ĺrodek i dĹugoĹÄ boku)
    koĹa (Ĺrodek i promieĹ)

KaĹźda figura moĹźe mieÄ okreĹlony kolor w postaci sĹownej (z zadanej palety, np. red), trĂłjki liczb dziesiÄtnych (np. (255, 0, 0) lub notacji HTML (#ff0000).

PrzykĹadowy plik zawierajÄcy wszystkie dopuszczalne elementy: http://home.agh.edu.pl/~zkaleta/python/sample.json

Program ma przyjmowaÄ nazwÄ pliku wejĹciowego z linii komend. JeĹźeli zostanie podana flaga -o (lub --output) to po niej ma byÄ nazwa pliku, do ktĂłrego grafikÄ naleĹźy zapisaÄ. JeĹli flaga -o nie zostanie podana, to naleĹźy tylko wyĹwietliÄ na ekranie.
