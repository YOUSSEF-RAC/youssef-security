Dit is een eenvoudige command-line applicatie waarmee je tekst kunt versleutelen en ontsleutelen met behulp van symmetrische encryptie.

Functionaliteiten:
Versleutelen: Je kunt tekst invoeren en deze wordt versleuteld met een gegenereerde sleutel.
Ontsleutelen: Je kunt versleutelde tekst invoeren en deze weer ontsleutelen met de juiste sleutel.


Benodigdheden:
Python (versie 3.6 of hoger)
De cryptography library. Je kunt deze installeren met:
pip install cryptography


Encryptiemethode:
Deze app maakt gebruik van symmetrische encryptie via de Fernet-methode van de cryptography-library.
Bij symmetrische encryptie wordt dezelfde sleutel gebruikt voor zowel het versleutelen als het ontsleutelen van de tekst. 
Dit betekent dat je de sleutel moet bewaren om de versleutelde gegevens te kunnen terughalen.


Versleutelen:
Start het script.
Kies optie (1) voor versleutelen.
Voer de tekst in die je wilt versleutelen.
Je ontvangt een versleutelde tekst en een sleutel om deze later weer te ontsleutelen.


Ontsleutelen:
Start het script opnieuw.
Kies optie (2) voor ontsleutelen.
Voer de versleutelde tekst in.
Voer de sleutel in die je eerder hebt ontvangen.
Je ontvangt de originele tekst.
