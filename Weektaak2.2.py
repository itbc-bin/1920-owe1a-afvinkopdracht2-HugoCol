# het aantal nucleotiden van een sequentie tellen
# het gc% van een sequentie berekenen

# invoer van genenstring die je wilt sequencen drie " gebruikt omdat de string meerdere regels lang is

seq = """GAGGGGAAACCTTCATTTTACGGCGGGGAGAAGGAGAGTGACCACTGACAGATAACAGCATCAGGAATCTTCTAACCATTCTTGACAAAATATGCAACGAACAATAAAGTCCTTTTTTCAGCCCAAGCTAGGGGCTGAAGTAAAGACTAAAGAAGAGAAAGTGAAGAATGATGTTCAAAAGGAAAAAGAAGAGCCAGAGAAAAGTGTTCCTGAACGTCCTTTAAAAGAGAGAAATGGCAGAGCTTTATGTGGAGATACCGAGTCACCAGTCAAACGAGTTTCAAAGAAGTCTGCACGTGTGTTGGAAAGTGATAGTGAAGAGGAAGAGGAGAATTCAAAGGTACAAGCGACTCCTGAAAAAATGAACAATGAAAGCGATCCAAAGAATGATGTTAAAGAAACTCCTCCGAGTGCACGTAAAGAAACTCCTCCGAGTGCACGTAAAGAAACTCCTCCGAGTGCACGTAAAGAAACTCCTCAGAGTGCACGTAAAGAAACTCCTCCGAGTGCACGTAAGGACGCAAAATCTGAAGGAGCTTCAGAGATGAACACTTCCCAAGATTTTGTCTCTCCTTGCAGCAGCAAATCTATTGACAGCCCTTTATGTTCAGATTCTCCTGGCATATCTCCTTCCGGTATCCCCAAACGAAAGACAGCCCGTAAACAGCTACCAAAGCGTAAACTGGAAATATCTCCCAGTGAATCAAATCCACCAAAAGATGATTTTGATGTCAAAGGAGCAGTGAAGCGACAAAAGAAAGAGGCAGAGGGAGATATTCAACAAGAAGAACCCATGGAGACAAGTCACAATATCTCCATGGAAGAGGAATGCCCCATAAAGAAAGAGACAAATCCCGACGTTGTTCAAGAAACCATATCCAACGCGGATGATCCAAACATAGAACTTGTAGACCAAAAGGATGTTGTTTCAGGAGAAAAGCAATCTGAGCCTAAATGTCAAGAGCAACCACAGCCCAAACTTACCAGTCCTACTGTGGAGCCTAAAGCTTCAAAAGGGAAGGCAAGAAAGAAAAACAGTCCTCTGCCAAAGAAAGTGAAATTTAGCGATAAAGTTTCTTTTAAAGACAATGACAGTGAGGAAAAAAGTAATGAGGAAAAAAGCGACGAGGAGCCTCAGAAGAAAGCAGATTCTGCTAAACCTGTGAAACAAATAAGCAGTTTCTTTGCCCCAAGGAAACCTGCAATAAAGACTGAAAAGAGAGAGGAAAATCTGAATGAAAAGAATGTCACTGAGACCTCTTTAGAAGAATCCCCTAAGCCTAAAAAAAACGTTGGCAGTTTCTTTGGAGCATCCAAGCAAGAAGCAACAGAAGAACAGACAGAGTATAACCCATCCAAGAGTAAATATCACCCCATAGATGATGCTTGCTGGTGTAATGGACAGAAGGTACCTTATCTTGCTGTTGCACGAACTTTTGAAAGGATAGAAGAGGAATCTGCCCGACTGAAGAACGTAGAGACTCTGAGTAATTTTCTGCGCTCCGTCATTGCTCTTACTCCTGAGGATCTCTTGCCTTGCATCTATCTTTGTCTGAACCGCCTGGGACCGGCATATGAAGGACTGGAGCTAGGCATAGGAGAAACTATTCTAATGAAAGCAGTTGCCCAGGCTACAGGACGCCAGCTTGAGAAGATAAAGGCTGAGGCACAAGAGAAAGGAGACCTTGGCCTGGTTGCTGAGAGCAGTCGTAGCAACCAACGCACAATGTTTACACCCCCAAAGCTCATGGCATCAGGTGTTTTCGGCAAGCTGAAAGATATAGCCAGGATGACTGGCAATGCTTCTATGAATAAGAAAATTGACATTATTAAAGGACTGTTTGTAGCCTGCAGGCATTCTGAGGCACGTTATATTGCCAGATCTCTTGGAGGAAAACTTAGAATTGGTCTTGCAGAACAGTCAGTGTTATCATCCATTGCTCAGGCAGTGTGCCTTACTCCTCCTGGGCGAGATGCCCCTCCTACTGTGATGGATGCCGGAAAGGGAATGAGTGCAGATGCCAGGAAATCCTGGATTGAGGAGAAAGCAATGATCTTGAAACAAACTTTTTGTGAGTTGCCAAACTATGATGCCATAATTCCTATTCTTTTGGAACATGGTATTGATGACCTCCCAAAACACTGCCGACTTACTCCAGGTATCCCTCTGAAACCAATGTTGGCGCATCCTACCAAGGGTATTGGGGAAGTGTTGAAGCGATTTGATGAAGCTGCCTTTACTTGTGAATACAAATATGACGGGGAGCGTGCACAGATACATATTCTGGAAAATGGGGAAGTACATGTATACAGCAGAAACCAAGAAAACAACACCACAAAATACCCTGACATCATCAGCAGAATTCCTAAGATTAAAAAAGAAAGCGTCAAATCCTGTATCCTCGATACGGAAGCTGTAGCCGGGGATGCAGAAAAGAAACAAATTCAGCCATTTCAAGTACTGACTACTAGAAAGAGAAAGGATGTGGATGCATCAGAGATTAAAGTGCAAGTTTGTGTGTATGCCTTTGACATGCTTTACCTTAATGGAGAGTCCCTAGTGAAGGAGCCATTTGCTAAGCGACGACAGCTCTTGAGAGACTCGTTCCTGGAGACTGAAGGGCAGTTCATGTTTGCTACATATATGGATAAGTCAAATACAGATGAAATTTCTGAGTTTCTTGATCAGTCTATTAAAGATTCATGTGAAGGACTTATGGTGAAGACACTGGAGCAAGACGCTACATATGAAATTGCAAAGAGATCTCACAATTGGTTAAAATTAAAGAAGGATTACTTGGAAGGTGTGGGTGATACTCTGGATCTTGTTGTTATTGGAGCTTACCTTGGGAAAGGGAAAAGAACTGGTATCTATGGAGGCTTCTTACTTGCGTCATACGACGAAGAAAGTGAGGAATATCAGACCATCTGCAAGATTGGAACAGGTTTTACAGATGACGACTTAGAAAAGCATTACAACTTCCTGAAGGATCATGTGATTGAAAATCCACGGAGCTACTACCGCTGGGACAGTGCCACAGAGCCAGATCACTGGTTTGATCCTGTACAAGTCTGGGAAGTTAAGTGTGCTGATCTATCCATTTCTCCAGTACATAAGGCAGCTCTTGGATTGGTGGAGGACCAGAAAGGAATTTCTCTGCGATTTCCTCGTTTTCTTCGTATCAGAGACGATAAGAAACCAGAGGAATCCACAAACAGTTTTCAGGTTGCAGATCTTTATAGAAAGCAGCAGCAAATCCAAAACACAAGTTCAACAGAGAAGGCAGAGGAGGATTTTTACTAGAATTACACATCAGCACTTTTATTTTATTTTTTTTCTCTTCTTTGTAATGTCCACATTGAACAATTGTGTTTTCAAGTCCAGGGGATTCAATTGGTATGTAAAGCAGCCATCAATAAGAAAGCCTTAGCTTGTATCCTATATATTACCATTCATTCTCTGAAGCATTTCAGGAAACCCCTCGATTCTGTCTCTACTGTCCATTTCTATGTTGACCTGAGAAACAAAAGTCATTGCCTAACCTCCCCCCACCTATTGTGTTGCCTTGGAGTAGTGAAGACGATGGAATTGGGCCTTTTTTTTTTTTTTTTTTGCTACATTGCTGATGTTGTTCTCTTCTATTTTATAACAGCTATGTGAACTAGACTTGTGAAATACTTGAAAAGCAATGGTTCTTCTTTACAATATTGTGATATTAAAAGCCATAAGAAAATAAATACTAATTATATTGAAAAAAAAAAAAAAAACC"""


# variabelen met getelde nucleotiden

aantal_a = seq.count("A") # Adenosine
aantal_c = seq.count("C") # Cytidine
aantal_g = seq.count("G") # Gunanine
aantal_t = seq.count("T") # Thymine

# optellen van de variabelen voor gebruik in gcperc berekening
totaal = aantal_a + aantal_c + aantal_g + aantal_t

# aantal gc optellen
gc = aantal_c + aantal_g

# gc percentage berekenen
gcperc = gc / totaal * 100

# print alle aantallen het het percentage gc, eerst had ik een aparte print command voor het gcpercentage maar heb er een command van gemaakt.
# na gcperc heb ik met het commando round(var, *aantal getallen achter de komma*) het percentage afgerond tot twee getallen na de komma

print("Adenosine: ", aantal_a, "\n" "Cytidine: ", aantal_c, "\n" "Guanine: ",aantal_g,"\n" "Thymine: ",aantal_t,"\n", "Percentage GC nucleotiden in de string = ", round(gcperc, 2) ,"%")