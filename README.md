Hier is de bijgewerkte README met de toevoegingen:

```markdown
# Data Processing and Visualization Script for Q-Blade Simulations

Dit Git-repository bevat een Python-script voor het verwerken en visualiseren van gegevens uit Q-Blade simulaties. Het script is primair bedoeld voor het opschonen van cP- en cT-gegevens en het genereren van de cP/cT-prestatiegrafiek voor een turbinebladontwerp.

Dit script is ontwikkeld in opdracht van Cleanmobility HvA voor turbinebladontwerp en is bedoeld om de volgende taken uit te voeren:

1. Het inlezen van gegevens vanuit CSV-bestanden ('Data\Cp.csv' en 'Data\Ct.csv').
2. Het verwerken van de gegevens door kolommen te verwijderen en te sorteren.
3. Het genereren van grafieken op basis van de verwerkte gegevens.
4. Het opslaan van de resultaten in nieuwe CSV-bestanden ('Results\Cp_clean.csv', 'Results\Ct_clean.csv', 'Results\Cp_Ct_clean.csv').

## Inhoudsopgave

- [Instructies](#instructies)
- [Vereisten](#vereisten)
- [Gebruik](#gebruik)
- [Aanpassen](#aanpassen)
- [Licentie](#licentie)

## Instructies

Volg de onderstaande instructies om het script uit te voeren:

## Vereisten

- Python 3.x
- Numpy
- Pandas
- Matplotlib

Installeer deze bibliotheken als je ze nog niet hebt geïnstalleerd.

## Gebruik

1. Clone deze Git-repository naar je lokale machine:

   ```bash
   git clone https://github.com/jouw-gebruikersnaam/data-processing-repo.git
   ```

2. Navigeer naar de gekloonde repository:

   ```bash
   cd data-processing-repo
   ```

3. Voer het script uit:

   ```bash
   python data_processing_script.py
   ```

Het script zal de gegevens verwerken en grafieken genereren. De resultaten worden opgeslagen in de "Results" map.

## Aanpassen

Je kunt de scriptparameters in de `data_processing_script.py`-bestanden aanpassen om de invoerbestanden, x-asnaam en andere instellingen aan te passen.

## Licentie

Dit project is gelicentieerd onder de MIT-licentie. Zie het [LICENSE](LICENSE) bestand voor meer informatie.

---

Dit script is ontwikkeld door [Jouw Naam] in opdracht van Cleanmobility HvA voor turbinebladontwerp. Voor vragen of opmerkingen, neem contact op via stefvandermeer@outlook.com.
```
