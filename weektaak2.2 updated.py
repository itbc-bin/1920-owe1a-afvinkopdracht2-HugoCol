# het aantal nucleotiden van een sequentie tellen
# het gc% van een sequentie berekenen
# In de variabele file wordt de sequentie opgeslagen
file = input("kopie paste hier het file path of gehele fasta tekst ")

# sequentie open functie om gemakkelijker verschillende sequenties te testen
# het ingevoerde bestand wordt geopend
sequentie = open(file)

# De eerste regel, dus de header in het fasta bestand, wordt genegeerd
sequentie = sequentie.readlines()[1:]
# Een lege variabele wordt aangemaakt
seq = ""
# de inhoudt van het fasta bestand wordt aan de variabele toegevoegd zonder regel 1 (header)
for lines in sequentie:
    seq += lines

# variabelen met getelde nucleotiden
# V2_variabelen veranderd naar volledige namen van de nucleotiden. Dit was een tip van een ICT student de reden is om later makkelijker te zien wat de variabele is
# ipv met de hand typen het ik alle variabelen renamed met de refactor tool
aantal_adenosine = seq.count("A")  # Adenosine
aantal_cytidine = seq.count("C")  # Cytidine
aantal_guanine = seq.count("G")  # Gunanine
aantal_thymine = seq.count("T")  # Thymine

# optellen van de variabelen voor gebruik in gcpercentage berekening
totaleLengteSequentie = aantal_adenosine + aantal_cytidine + aantal_guanine + aantal_thymine

# aantal gc optellen
GCopgeteld = aantal_cytidine + aantal_guanine

# gc percentage berekenen, V2_ik kreeg de tip om 100 ook in een variabele te zetten. Nu was het niet zo belangrijk
GCpercentage = gc / totaleLengteSequentie * 100

# print alle aantallen het het percentage gc, eerst had ik een aparte print command voor het gcpercentage maar heb er een command van gemaakt.
# na gcperc heb ik met het commando round(var, *aantal getallen achter de komma*) het percentage afgerond tot twee getallen na de komma

print(
"Adenosine: ", aantal_adenosine, "\n" "Cytidine: ", aantal_cytidine, "\n" "Guanine: ", aantal_guanine, "\n" "Thymine: ",
aantal_thymine,
"\n" "totale lengte: ", totaleLengteSequentie, "\n" "Percentage GC nucleotiden in de string = ", round(GCpercentage, 2),
"%")
# print(totaal)
