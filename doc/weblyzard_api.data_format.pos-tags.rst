POS tags
========
This file contains the used part-of-speech (POS)-tagsets for English, French and German. All used tags can also be found in `usedPosTags.csv <https://github.com/weblyzard/weblyzard_api/tree/master/doc/usedPosTags.csv>`_ .

English
-------

The English tagger uses the Penn Treebank POS tag set.
::

	1.  CC  Coordinating conjunction
	2.  CD  Cardinal number
	3.  DT  Determiner
	4.  EX  Existential there
	5.  FW  Foreign word
	6.  IN  Preposition or subordinating conjunction
	7.  JJ  Adjective
	8.  JJR     Adjective, comparative
	9.  JJS     Adjective, superlative
	10.     LS  List item marker
	11.     MD  Modal
	12.     NN  Noun, singular or mass
	13.     NNS     Noun, plural
	14.     NNP     Proper noun, singular
	15.     NNPS    Proper noun, plural
	16.     PDT     Predeterminer
	17.     POS     Possessive ending
	18.     PRP     Personal pronoun
	19.     PRP$    Possessive pronoun
	20.     RB  Adverb
	21.     RBR     Adverb, comparative
	22.     RBS     Adverb, superlative
	23.     RP  Particle
	24.     SYM     Symbol
	25.     TO  to
	26.     UH  Interjection
	27.     VB  Verb, base form
	28.     VBD     Verb, past tense
	29.     VBG     Verb, gerund or present participle
	30.     VBN     Verb, past participle
	31.     VBP     Verb, non-3rd person singular present
	32.     VBZ     Verb, 3rd person singular present
	33.     WDT     Wh-determiner
	34.     WP  Wh-pronoun
	35.     WP$     Possessive wh-pronoun
	36.     WRB     Wh-adverb

French
------

The French Tagger has been trained with the French Treebank corpus.
::

	A (adjective)
	Adv (adverb)
	CC (coordinating conjunction)
	Cl (weak clitic pronoun)
	CS (subordinating conjunction)
	D (determiner)
	ET (foreign word)
	I (interjection)
	NC (common noun)
	NP (proper noun)
	P (preposition)
	PREF (prefix)
	PRO (strong pronoun)
	V (verb)
	PONCT (punctuation mark)


German
------

We use the Stuttgart-Tübingen-Tagset (STTS) that is used for the NEGRA Corpus.
::

	ADJA    attributives Adjektiv                   [das] große [Haus]
	ADJD    adverbiales oder                        [er fährt] schnell
			prädikatives Adjektiv                   [er ist] schnell
	 
	ADV     Adverb                                  schon, bald, doch
	 
	APPR    Präposition; Zirkumposition links       in [der Stadt], ohne [mich]
	APPRART Präposition mit Artikel                 im [Haus], zur [Sache]
	APPO    Postposition                            [ihm] zufolge, [der Sache] wegen
	APZR    Zirkumposition rechts                   [von jetzt] an
	 
	ART     bestimmter oder                         der, die, das,
			unbestimmter Artikel                    ein, eine, ...
	 
	CARD    Kardinalzahl                            zwei [Männer], [im Jahre] 1994
	 
	FM      Fremdsprachliches Material              [Er hat das mit ``]
													A big fish ['' übersetzt]
	 
	ITJ     Interjektion                            mhm, ach, tja
	 
	ORD     Ordinalzahl                             [der] neunte [August]
	 
	KOUI    unterordnende Konjunktion               um [zu leben],
			mit ``zu'' und Infinitiv                anstatt [zu fragen]
	KOUS    unterordnende Konjunktion               weil, daß, damit,
			mit Satz                                wenn, ob
	KON     nebenordnende Konjunktion               und, oder, aber
	KOKOM   Vergleichskonjunktion                   als, wie
	 
	NN      normales Nomen                          Tisch, Herr, [das] Reisen
	NE      Eigennamen                              Hans, Hamburg, HSV
	 
	PDS     substituierendes Demonstrativ-          dieser, jener
			pronomen
	PDAT    attribuierendes Demonstrativ-           jener [Mensch]
			pronomen
	 
	PIS     substituierendes Indefinit-             keiner, viele, man, niemand
			pronomen
	PIAT    attribuierendes Indefinit-              kein [Mensch],
			pronomen ohne Determiner                irgendein [Glas]
	PIDAT   attribuierendes Indefinit-              [ein] wenig [Wasser],
			pronomen mit Determiner                 [die] beiden [Brüder]
	 
	PPER    irreflexives Personalpronomen           ich, er, ihm, mich, dir
	 
	PPOSS   substituierendes Possessiv-             meins, deiner
			pronomen
	PPOSAT  attribuierendes Possessivpronomen       mein [Buch], deine [Mutter]
	 
	PRELS   substituierendes Relativpronomen        [der Hund ,] der
	PRELAT  attribuierendes Relativpronomen         [der Mann ,] dessen [Hund]
	 
	PRF     reflexives Personalpronomen             sich, einander, dich, mir
	 
	PWS     substituierendes                        wer, was
			Interrogativpronomen
	PWAT    attribuierendes                         welche [Farbe],
			Interrogativpronomen                    wessen [Hut]
	PWAV    adverbiales Interrogativ-               warum, wo, wann,
			oder Relativpronomen                    worüber, wobei
	 
	PAV     Pronominaladverb                        dafür, dabei, deswegen, trotzdem
	 
	PTKZU   ``zu'' vor Infinitiv                    zu [gehen]
	PTKNEG  Negationspartikel                       nicht
	PTKVZ   abgetrennter Verbzusatz                 [er kommt] an, [er fährt] rad
	PTKANT  Antwortpartikel                         ja, nein, danke, bitte
	PTKA    Partikel bei Adjektiv                   am [schönsten],
			oder Adverb                             zu [schnell]
	 
	SGML    SGML Markup
	 
	SPELL   Buchstabierfolge                        S-C-H-W-E-I-K-L
	 
	TRUNC   Kompositions-Erstglied                  An- [und Abreise]
	 
	VVFIN   finites Verb, voll                      [du] gehst, [wir] kommen [an]
	VVIMP   Imperativ, voll                         komm [!]
	VVINF   Infinitiv, voll                         gehen, ankommen
	VVIZU   Infinitiv mit ``zu'', voll              anzukommen, loszulassen
	VVPP    Partizip Perfekt, voll                  gegangen, angekommen
	VAFIN   finites Verb, aux                       [du] bist, [wir] werden
	VAIMP   Imperativ, aux                          sei [ruhig !]
	VAINF   Infinitiv, aux                          werden, sein
	VAPP    Partizip Perfekt, aux                   gewesen
	VMFIN   finites Verb, modal                     dürfen
	VMINF   Infinitiv, modal                        wollen
	VMPP    Partizip Perfekt, modal                 gekonnt, [er hat gehen] können
	 
	XY      Nichtwort, Sonderzeichen                3:7, H2O,
			enthaltend                              D2XW3
	 
	\$,     Komma                                   ,
	\$.     Satzbeendende Interpunktion             . ? ! ; :
	\$(     sonstige Satzzeichen; satzintern        - [,]()


Spanish
--------

We use the simplified version of the tagset used in the AnCora treebank. The original AnCora part-of-speech tags were modeled after the EAGLES Spanish tagset: http://nlp.lsi.upc.edu/freeling/doc/tagsets/tagset-es.html The "simplification" consists of nulling out many of the final fields which don't strictly belong in a part-of-speech tag. Therefore, the fields in the POS tags produced by the tagger correspond exactly to AnCora POS fields, but a lot of those fields will be null. For most practical purposes you'll only need to look at the first 2–4 characters of the tag. The first character always indicates the broad POS category, and the second character indicates some kind of subtype.

::

    a   adjective
    c   conjunction
    d   determiner
    f   punctuation
    i   interjection
    n   noun    (c common  f feminine m masculine p plural s singular)   
    p   pronoun
    r   adverb  (general negative)
    s   preposition (c common p plural s singular)
    v   verb
    w   date    31_de_julio
    z   number  2,74_por_ciento


Examples:
::

    pd000000    esta           
    vsip000 es 
    di0000  una 
    nc0s000 oracion, prueba, escándalo
    sp000   de
    dd0000  Ese
    vmis000 provocó
    aq0000  amplios
    nc0p000 cambios
    np00000 Chris_Woodruff, El_Periódico_de_Cataluña
    rg  no_obstante
    nc00000 stock_options
    
Documentation:

http://clic.ub.edu/corpus/webfm_send/18

https://docs.google.com/document/d/1lI-ie4-GGx2IA6RJNc0PMb3CHDoNQMUa0gj0eQEDYQ0/