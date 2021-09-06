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
