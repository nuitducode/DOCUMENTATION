---
hide:
  - footer
---

# RÈGLES ET CONSEILS

!!! note ""
    Les informations ci-dessous seront proposées au format PDF dans les prochains jours. Vous pourrez ainsi imprimer les documents et les distribuer aux élèves le jour de la NDC.

## SCRATCH

Durant la NDC, vous disposerez de 6 heures pour créer un jeu avec Scratch. Pour cela, vous devrez utiliser l'un des univers de jeu mis à votre disposition. Ces univers de jeu ne contiennent aucun script, mais possèdent de nombreux lutins, des scènes et des sons.


### LES RÈGLES

!!! danger "IMPORTANT"
    * Les univers de jeu et les liens fournis sont **confidentiels**. Ils ne doivent être partagés avec personne.
    * Le titre de votre jeu doit être le nom de votre équipe. Les mots suivants ne doivent apparaitre ni dans le titre ni dans les champs « Instructions » ou « Notes et Crédits » de votre jeu (ou des différentes versions de votre jeu): « nuit », « code », « c0de », « 2023 », « NdC », « ndc ».

* **Vous devez choisir un univers de jeu parmi ceux proposés**. Prenez le temps de bien étudier les différents univers de jeu (lutins, costumes, décors…) avant d'en choisir un. Une fois votre choix fait, cliquez sur « Remix ». Cet univers « remixé » devient le point de départ de votre jeu.
* **Vous devez écrire une courte documentation** (ou mode d'emploi) de votre jeu. Cette documentation doit être placée dans le champ « Instructions ». La documentation fait partie de l'évaluation du jeu.
* Vous êtes totalement libre de créer le jeu que vous voulez. Soyez créatif !
* Vous ne pouvez créer votre jeu qu'à partir des éléments que vous trouvez dans l'univers de jeu que vous avez choisi sans y ajouter aucun élément extérieur.
* Il n'est pas autorisé d'importer des lutins, scènes ou sons (de la bibliothèque Scratch ou depuis Internet) dans votre projet. Seuls ceux fournis dans l'univers de jeu « remixé » doivent être utilisés.
* Il n'est pas autorisé de regarder ou copier/coller des scripts d'autres projets de la plateforme Scratch ou de votre ordinateur.
* Il n'est pas autorisé d'aller chercher des tutoriels (vidéos ou autres) durant la NDC: les codes doivent venir de vous.
* Vous n'êtes absolument pas obligé d'utiliser tous les lutins, scènes ou sons de l'univers de jeu.
* Vous avez le droit de dupliquer des lutins si vous en avez besoin.
* Les éléments du jeu vous suggèrent peut-être de créer un jeu que vous connaissez déjà, mais vous êtes tout à fait libre de proposer autre chose.
* Vous avez le droit de demander de l'aide aux professeurs qui encadrent la NDC. Ils ne vous donneront pas un script complet, mais certainement de bons conseils pour avancer.
* Vous avez le droit de demander de l'aide à vos camarades des autres équipes participantes. La Nuit du c0de est un événement festif et l'entraide est fortement recommandée.
* Vous avez le droit de faire des « retouches » graphiques mineures sur les lutins ou les scènes: symétrie, rotation, changer une couleur, déformer, ajout de texte… mais attention à ne pas y passer trop de temps. Il est quand même conseillé d'éviter: il y a suffisamment de lutins (et certains ont beaucoup de costumes) pour trouver ce dont vous avez besoin.
* Vous avez le droit de créer des lutins qui servirait de « capteur » lors des déplacements (juste un rectangle ou un cercle) ou des lutins « texte ».


### QUELQUES CONSEILS
* Avant de vous lancer dans le code, prenez le temps d'imaginer votre jeu. Passez en revue tous les lutins, tous leurs costumes (qui sont parfois nombreux) et tous les sons. Prévoyez de réaliser rapidement une version simple, mais jouable de votre jeu. Puis, si vous en avez le temps, rajoutez au fur et à mesure des éléments de complexité: niveau de difficulté, scores, son, etc.
* Vous travaillez à deux ou trois: organisez-vous pour être les plus efficaces possible.
* **Pensez à sauvegarder** ! Et surtout, effectuez régulièrement des **copies incrémentées** (version 1, 2, 3…) de votre jeu à chaque amélioration majeure (qui marche). Scratch ne permet pas d'annuler des modifications…
* N'oubliez pas de faire des pauses, d'aller voir ce que font les autres, de boire et de manger !
* Et puis surtout, rappelez-vous: c'est un jeu ! **Amusez-vous !**

### IMPORTANT: À LA FIN DES 6h

#### Cas 1: si vous avez créé votre jeu en ligne avec un compte Scratch

* **Partagez votre jeu** en cliquant sur le bouton orange « Partager » (« Share » en anglais).
* **Enregistrez votre jeu** sur le site de la Nuit du c0de.

Pour enregistrer votre jeu sur le site de la Nuit du c0de, un lien vous sera fourni. Ce lien vous amènera sur la page d'enregistrement. Sur cette page, vous devrez indiquer le nom de votre équipe, votre catégorie et l'identifiant de votre projet. L'identifiant du projet est la suite de chiffres présente dans son adresse. Exemple: si l'adresse est `https://scratch.mit.edu/projects/6535`, l'identifiant est `6535`.

!!! danger ""
    Après avoir déposé votre jeu, vous n'aurez plus le droit de le modifier. Les jeux modifiés après le dépôt ne seront pas évalués.


#### Cas 2: si vous avez créé votre jeu sans connexion internet

Rendre le fichier `.sb3` en suivant les consignes fournies par votre enseignant.

###  CRITÈRES D'ÉVALUATION

Chaque critère est noté sur 5:

* Jouabilité
* Originalité / Créativité
* Richesse / Complexité
* Respect des consignes / Documentation


## PYTHON / PYXEL

Durant la NDC, vous disposerez de 6 heures pour créer un jeu avec Python / Pyxel. Pour cela, vous pouvez utiliser les ressources (fichiers <kbd>.pyxres</kbd>) mises à votre disposition ou partir de zéro.

### LES RÈGLES

!!! danger "IMPORTANT"
    * Les univers de jeu et les liens fournis sont **confidentiels**. Ils ne doivent être partagés avec personne.
    * Le titre de votre jeu doit être le nom de votre équipe.

* La taille de l'écran du jeu doit être de **128x128 pixels** (<kbd>pyxel.init(128, 128, title="Nuit du c0de 2023")</kbd>).
* Le code de votre jeu doit être dans <u>un seul fichier</u> <kbd>app.py</kbd>. Si vous utilisez des images, elles seront dans un deuxième fichier au format <kbd>.pyxres</kbd>.
* Plusieurs ressources graphiques (fichiers <kbd>.pyxres</kbd>) seront proposées. Cependant, vous n'êtes pas obligés de les utiliser. Vous pouvez créer vos propres images avec l'éditeur Pyxel. Vous pouvez aussi créer un jeu sans images, en utilisant seulement les formes géométriques.
* Il n'est pas autorisé de regarder ou copier/coller du code trouvé sur internet ou votre ordinateur.
* Il n'est pas autorisé d'aller chercher des tutoriels (vidéos ou autres) durant la NDC: le code doit venir de vous.
* **Vous devez écrire une courte documentation** (ou mode d'emploi) de votre jeu. La documentation fait partie de l'évaluation du jeu.
* Vous êtes totalement libre de créer le jeu que vous voulez. Soyez créatif !
* Vous avez le droit de demander de l'aide aux professeurs qui encadrent la NDC. Ils ne vous donneront pas un code complet, mais certainement de bons conseils pour avancer. Soyez patients: lorsque vous avez travaillé pendant plusieurs heures sur un projet, il est très difficile pour quelqu'un qui le découvre de répondre rapidement à une question.
* Vous avez le droit de demander de l'aide à vos camarades des autres équipes participantes. La Nuit du c0de est un événement festif et l'entraide est fortement recommandée.

### QUELQUES CONSEILS

* Avant de vous lancer dans le code, prenez le temps d'imaginer votre jeu. Passez en revue les ressources. Prévoyez de réaliser rapidement une version simple, mais jouable de votre jeu. Puis, si vous en avez le temps, rajoutez au fur et à mesure des éléments de complexité: niveau de difficulté, scores, son, etc.
* Vous travaillez à deux ou trois: organisez-vous pour être les plus efficaces possible.
* **Pensez à sauvegarder** ! Et surtout, effectuez régulièrement **des copies incrémentées** (version 1, 2, 3…) de votre jeu à chaque amélioration majeure (qui marche).
* N'oubliez pas de faire des pauses, d'aller voir ce que font les autres, de boire et de manger !
* Et puis surtout, rappelez-vous: c'est un jeu ! **Amusez-vous !**

### IMPORTANT: À LA FIN DES 6h

Avant la fin des 6h, déposez votre jeu sur le site de la Nuit du c0de.

#### Cas 1: si vous avez créé votre jeu en ligne sur le site de la Nuit du c0de

Vous n'avez rien à faire.

#### Cas 2: si vous avez créé votre jeu sans connexion internet

Déposez votre jeu sur le site de la Nuit du c0de en utilisant le lien fourni par votre enseignant. Ce lien vous amènera sur la page de dépôt. Sur cette page, vous devrez indiquer le nom de votre équipe, votre catégorie puis déposer votre fichier <kbd>app.py</kbd> et, s'il existe, le fichier <kbd>.pyxres</kbd>.

Si vous n'avez pas la possibilité de déposer vous-même ces fichiers sur le site, donnez-les à votre enseignant.

###  CRITÈRES D'ÉVALUATION

Chaque critère est noté sur 5:

* Jouabilité
* Originalité / Créativité
* Richesse / Complexité
* Respect des consignes / Documentation
