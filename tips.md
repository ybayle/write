# Tips

## Comment collaborer avec une nouvelle personne ?

Il y a des grandes idées mais rien de fixé, il faut adapter en fonction.
Il y a des points évidents mais des fois c'est bien de le rappeller.
Tout ne s'applique pas forcément à tout les domaines (info vs élec).

- dire à l'oral dès le début que s'il y a un problème ou une question, il faut en parler tout de suite. Si toi ou quelqu'un de l'équipe à la réponse ça prend moins de temps plutôt que de galérer 15 ans à chercher dans son coin. Pour certaines personnes c'est évident mais pour d'autres non à cause de leur fierté et il ne faut pas hésiter à le rappeller. Vaut mieux recevoir un "Va googler" tout de suite qu'un "pourquoi tu ne nous as pas demandé" 2 jours plus tard.
- code review (ou revue de schéma) régulière sur des petis bouts incrémentaux à chaque fois surtout au début pour mettre en place les échanges, les conventions et le type de travail attendu.
- standup 5-10 mn max quotidien le matin
- établir jalon/deadline rendu + RDV sur tout le long du projet même si ça dévie, car ça va dévier.
- liste de la pipeline de travail avec tous les outils utilisés et ce qui est fait à la main ou pas
- des conseils et templates pour rédiger les documents techniques (surtout le rapport) https://github.com/bayle42/write/
- template pour le compte rendu hebdomadaire https://github.com/bayle42/write/tree/master/RapportHebdomadaire
- 1 seul endroit où gérer les tâches, bugs, commentaires, ... (Trello ou YouTrack ou Github/Issues&Projects, ...)
- 1 seul mode de communication (pas slack + sms + mail sur plusieurs boîtes de réception + skype + GMeet + signal + ... )
- éviter les implicites : quand fais PR code review c'est tentant de mettre juste "rm" ou "missing eol", mais faut le dire clairement au début qu'il y aura des abbréviations pour aller plus vite. et faut pas oublier de dire bonjour/au revoir.
- 1 seul dossier partagé de travail (dossier sur VPN, GDrive, repo Github, ...) avec une structure fixe à définir au départ par exemple :

    - cahier des charges/
    - état de l'art/
    - documentation/
    - img/
    - sous-projet 1/
    - sous-projet 2/
    - ...
    - sous-projet N/
        - src/
        - schémas/
        - scripts/
        - 

- surtout pour éviter les dossier "misc" fourre-tout et de ne pas s'y retrouver si on n'est pas revenu sur le projet depuis 10 jours.
- Ne pas hésiter à compléter ce document.

## Comment corriger un bug ?

Conseils c'est comme un sport de combat ou un cours sur les premiers secours, il faut souvent répéter les bonnes pratiques pour qu'un jour quand on en a besoin on sache quoi faire.
Sinon ce qu'il se passe c'est qu'on se retrouve la tête dans le guidon et quand quelqu'un d'autre nous fait remarquer notre erreur on se dit "purée je le savais qu'il fallait le faire comme ça, pourquoi je ne l'ai pas fais ?" On trouve une [excuse générique] alors que ça devrait être une bonne pratique/habitude

Comment corriger un code ?

1. Reproduire le bug
2. Isoler le plus possible ce qui produit le bug. Dans un workflow/pipeline (code vertical) c'est enlever des étapes de manières dichotomique p(pour aller plus vite) pour savoir quelle étape produit le bug. Dans un code horizontal, c'est trouver le moment où ça se produit. Dans une machine à état, il faut trouver l'état ou la combinaison qui produit le bug
3. Une fois que les conditions minimum ont été établies, on peut commencer à lire du code pour préciser ou il se trouve. Une fois que le bug est trouvé :
4. Le corriger. 90 %  du temps corriger un bug consiste à modifier un caractère ou une ligne. LE reste du temps ça implique des choses plus complexes comme du code supplémentaire ou du refactoring.
5. une fois que c'est corrigé, il faut vérifier que dans la condition qui produisait le bug de manière systématique, le bug n'apparaît plus.
6. Ajouter un test (unitaire ou d'intégration) afin que dans un futur refactoring malencontreux, le bug ne réaparaisse pas.
7. Pusher, PR, code review et vérifier avec une tierce personne (idéalement la personne qui a soulevé le bug) que celui ci est bien réglé.

Tête dans le guidon/prendre du recul/être efficace

parfois on
en sortant de l'école info/math, on a appris à faire des choses from scratch (réinventer une roue). Dans le monde du travail, on demandera plus souvent de construire une voiture et pour cela de ne pas réinventer la roue. Mais à l'école on n'a pas appris à (i) trouver les gens qui font des roues et (ii) comparer les différentes roues ni (iii) à utiliser/intégreR/mettre en place la roue dans la voiture. et pourtant c'est de ça que sera constitué la majorité de votre travail dans le futur.
