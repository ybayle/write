- [Installation de l'environnement de travail](#Installation-de-l'environnement-de-travail)
- [Rapport de stage](#Rapport-de-stage)
    - [Rédaction](#rédaction)
    - [Plan](#Plan)
    - [Page de titre](#Page-de-titre)
    - [À lire](#À-lire)
    - [Outils](#Outils)
- [Soutenance](#Soutenance)
- [Fiche d'évaluation du stage par le tuteur en entreprise](#fiche-dévaluation-du-stage-par-le-tuteur-en-entreprise)
- [Après le stage](#après-le-stage)

# Installation de l'environnement de travail

1. https://strawberryperl.com/
2. https://miktex.org/download
3. https://github.com/VSCodium/vscodium/releases
4. https://github.com/James-Yu/LaTeX-Workshop
5. https://www.sumatrapdfreader.org/download-free-pdf-viewer

Now you should be able to compile this [example latex](https://github.com/bayle42/write/blob/master/RapportHebdomadaire/crh.tex) in VScodium and see the PDF with SumatraPDF that should be identical to [this generated PDF](https://github.com/bayle42/write/blob/master/RapportHebdomadaire/crh.pdf).

# Rapport de stage

## Rédaction

- Lire les consignes fournies par les écoles et universités ([Source 1](ConsignesRapport/ConsignesRapport1.pdf) et [Source 2](ConsignesRapport/ConsignesRapport2.pdf)).
- Il faut 3 semaines à temps plein pour rédiger un rapport de stage de 6 mois de 40-50 pages et 3 mois pour rédiger un mémoire de thèse de 200 pages, ce qui représente entre 3 et 5 pages par jour. /!\ Attention c'est une moyenne et il faut le considérer comme telle.
- Un schéma, une figure, un tableau, une équation, un dessin, un graphique, doivent être introduits et commentés dans le texte. Cela n'empêche pas qu'ils puissent être lus et compris en dehors de leur contexte grâce à un titre et des légendes concis et complets.
- Si un schéma, une figure, un tableau, une équation, un dessin ou un graphique est cité, il doit y la source dans la légende.  
- Il est possible de générer automatiquement le code latex à partir d'équation en python https://github.com/google/latexify_py.
- Les nombres inférieurs à 10 doivent être écrit en toutes lettres et non en chiffres (un, deux, trois, quatre, cinq, six, sept, huit, neuf, 10, 11, ...).
- Utiliser le présent pour rédiger plutôt que le passé ou le mélange du présent et du passé.
- Citer une source dès qu'il y a une information qui est affirmée ou pour justifier un choix technique.
- Ne pas mettre de virgule avant `et`.
- Il doit y avoir en français une virgule pas un point pour écrire les chiffres après la virgule.
- Ne pas commencer les phrases par `en effet`, `car`, `donc`, `parallèlement`, `bien que`, ...
- Ne pas commencer une phrase par du participe présent (`Étudiant en Master, je`, ...).
- Ne pas utiliser le langage oral en évitant (`clairement`, `garder à l'esprit`, ...).
- Éviter les mots subjectifs (`meilleur`, `intéressant`, `gênant`, ...).
- Être le plus précis possible et éviter `généralement`, `de tout temps`, `à l'heure où`, `intéressant`, `longtemps`, ...
- Éviter d'utiliser les parenthèses dans une phrase.
- Ne pas utiliser `:` au milieu d'une phrase. Les `:` peuvent être utilisés pour introduire une énumération avec des tirets.
- Ne pas faire d'anglicisme. Il faut utiliser des mots français ou mettre en italique les mots provenant de langues étrangères sauf s'ils ont été spécifiquement francisés (certains cas en latin notamment).
- Pour faciliter la relecture, la correction et le travail à plusieurs lors d'une rédaction avec latex, il faut respecter la contrainte d'une phrase par ligne.
- Ne pas utiliser le première personne, excepté dans la section sur les remerciements.
- Pour les images, [draw.io](https://app.diagrams.net/) fournit une intégration dans [Microsoft Visual Studio Code](https://code.visualstudio.com/).
- Pour les fautes, [LanguageTool](https://marketplace.visualstudio.com/items?itemName=adamvoss.vscode-languagetool) a une intégration dans [Microsoft Visual Studio Code](https://code.visualstudio.com/).
- Mettre un espace avant l'unité qu'on utilise : `20 ms` (et non `20ms`).
- Les notes de bas de pages servent principalement à indiquer la source d'une idée qui est étayée et non à essayer de réduire la taille des phrases dans le texte principal.
- `La méthode est basée sur` : `basée` est un anglicisme dans ce sens, il faut utiliser `fondée sur`. `Basé` ne peut s'utiliser en français qu'avec une localisation  (`L'entreprise est basée à Montpellier`, ...)
- Réutiliser les informations mises au propre dans les [Comptes Rendus Hebdomadaires](RapportHebdomadaire/crh.pdf).
- Chaque phrase doit être concise. Le mot `respectivement` permet facilement de condenser de l'information. On peut par exemple remplacer `Ces comparaisons sont faites avec deux signaux d'entrée différents : i) une sinusoïde de 500 Hz et de 50 mV d'amplitude. Pour comparer les réponses de la diode en régime linéaire et ii) une sinusoïde de 500 Hz et de 950mV d'amplitude. Pour comparer les réponses de la diode en régime de saturation.` par `Ces comparaisons en régime linéaire et saturé sont effectuées avec une sinusoïde de 500 Hz affichant une amplitude de 50 mV et 950 mV respectivement.`
- Il faut éviter d'avoir deux fois le même mots dans une phrase. Il faut soit reformuler la phrase pour la rendre plus concise, soit la diviser en deux, soit trouver un synonyme. 
- Il faut être cohérent dans tout le rapport sur l'utilisation des mots. Il est par exemple possible d'utiliser `étude` ou `test` mais la lecture est plus ardue si les deux sont utilisés tour à tour plutôt que si un seul des deux mots est utilisé tout au long du rapport.
- Ne pas écrire `La figure 2 compare ...` car ce n'est pas la figure qui compare. La figure représente plusieurs y en fonction d'un x et c'est un être humain qui compare.
- Il faut éviter de commencer les phrases par un verbe. Au lieu de `Obtenir ce résultat`, il est préférable d'avoir `L'obtention de ce résultat`.
- Vérifier l'utilisation des unités avec cette checklist : https://physics.nist.gov/cuu/Units/checklist.html
- Si le PDF est trop volumineux, il est possible de le compresser en utilisant la commande suivante :

```
"C:\Program Files\gs\gs9.53.1\bin\gswin64.exe" -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/printer -dNOPAUSE -dQUIET -dBATCH -sOutputFile=output.pdf input.pdf
```

avec comme option de compression `-dPDFSETTINGS` :

```
0: '/default',
1: '/prepress',
2: '/printer',
3: '/ebook',
4: '/screen'
```

## Plan

- Page de garde
- Summary (Résumé en anglais sur une demi-page environ)
- Préambule (ou l'Avant-propos est une section facultative)
- Remerciements
- Table des matières
- Introduction
  - Enjeux, motivations, contexte
  - Problématiques
  - Objectifs et jalons
  - Annonce du plan
- Matériels
- Méthodes
- Résultats
- Discussions
- Conclusion
- Ouverture et perspectives
- Références
- Liste des figures
- Liste des tableaux
- Liste des acronymes
- Glossaire
- Annexes (facultatif)

## Page de titre

- Nom des structures et logos des universités, des écoles, des laboratoires, d'[Orosys](img/logo_orosys.png) et de [Two notes Audio Engineering](img/logo_twonotes.png)
- Type de rapport
- Titre du rapport
- Prénom et nom de l'auteur
- Prénoms, noms et rôles des encadrants et partenaires
- Date
- Mention ou filigrane confidentiel

## À lire

- [Règles typographiques de base](http://www4.ac-nancy-metz.fr/ien-vittel/docs%20site/outils%20pour%20le%20maitre/regles_typo_version2012.pdf)

## Outils

- [Shape Catcher](http://shapecatcher.com/) Unicode character recognition for Latex
- [Detexify](http://detexify.kirelabs.org/classify.html) Draw a symbol and latex will give you the code to use it
- [Latex 4 Technics](https://www.latex4technics.com/) Helper for displaying latex equation

# Soutenance

- Lire les consignes fournies par les écoles et universités ([Source 1](ConsignesSoutenance/ConsignesSoutenance1.pdf)).

# Fiche d'évaluation du stage par le tuteur en entreprise

- Lire les éléments qui sont évalués par le tuteur et pris en considération par les enseignants ([Source 1](FicheEvaluationStageParTuteurEntreprise/FicheEvaluationStageParTuteurEntreprise1.pdf) et [Source 2](FicheEvaluationStageParTuteurEntreprise/FicheEvaluationStageParTuteurEntreprise2.pdf)).

# Après le stage

[Après le stage](ApresStage.md)
