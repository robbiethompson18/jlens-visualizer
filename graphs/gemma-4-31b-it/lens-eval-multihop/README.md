# lens-eval-multihop: J-lens by layer and token, gemma-4-31B-it

Lens: `solarkyle/jspace-lenses/gemma-4-31b-it/lens.pt`. Rank here is rank in the whole vocabulary (log scale), 1 = the lens's top token. Each item's graph shows, on top, the rank
of every tracked word at the token before the answer by layer (thin = raw, thick = EWMA with a
2-layer halflife). Below it, one heatmap per word: rank at every layer (y) and prompt token
(x), darker = higher rank. Dashed boxes outline the prompt line each step reads, in the colour of the
step it produces. A word lighting up on its own token in early layers is the token echoing itself, not
computation. Correct items first.

| depth | correct |
| --- | --- |
| all | 45/93 |

## Summary: median rank over correct items

![summary](summary.png)

## Answered correctly (45)

---

![amazon-language](amazon-language.png)

Fact: The language spoken in the country where the Amazon River ends is

**Answer:** **Portuguese** · **Hidden trajectory:** Brazil → Portuguese

**gemma-4-31B-it:** ✅ top 5: `Portuguese`, `either`, `**`, `called`, `Portug`
---

![mars-color](mars-color.png)

Fact: The color of the planet fourth from the Sun is

**Answer:** **red** · **Hidden trajectory:** Mars → red

**gemma-4-31B-it:** ✅ top 5: `red`, `reddish`, `similar`, `the`, `called`
---

![paper-continent](paper-continent.png)

Fact: The continent where the country that invented paper is located is

**Answer:** **Asia** · **Hidden trajectory:** China → Asia

**gemma-4-31B-it:** ✅ top 5: `Asia`, `the`, `located`, `also`, `**`
---

![christmas-season](christmas-season.png)

Fact: The season when the holiday with a decorated tree occurs is

**Answer:** **winter** · **Hidden trajectory:** Christmas → winter

**gemma-4-31B-it:** ✅ top 5: `winter`, `**`, `Winter`, `the`, `*`
---

![planet-3-moons](planet-3-moons.png)

Fact: The number of natural moons orbiting the planet third from the Sun is

**Answer:** **1** · **Hidden trajectory:** Earth → 1

**gemma-4-31B-it:** ✅ top 5: `1`, `5`, `<b>`, `2`, `0`
---

![spaceneedle-border](spaceneedle-border.png)

Fact: The US state where the Space Needle is located shares its northern border with

**Answer:** **Canada** · **Hidden trajectory:** Seattle → Canada

**gemma-4-31B-it:** ✅ top 5: `Canada`, `British`, `**`, `the`, `neighboring`
---

![rhyme-door-doubled](rhyme-door-doubled.png)

Fact: Take the number whose name rhymes with the word door. Doubling it gives the number

**Answer:** **8** · **Hidden trajectory:** four → 8

**gemma-4-31B-it:** ✅ top 5: `8`, `1`, `4`, `2`, `6`
---

![etym-wargod-month](etym-wargod-month.png)

Fact: The month named after the Roman god of war is month number

**Answer:** **3** · **Hidden trajectory:** March → 3

**gemma-4-31B-it:** ✅ top 5: `3`, `4`, `2`, `6`, `0`
---

![chem-atmosphere-Z](chem-atmosphere-Z.png)

Fact: The atomic number of the gas that makes up about 78 percent of the atmosphere is

**Answer:** **7** · **Hidden trajectory:** nitrogen → 7

**gemma-4-31B-it:** ✅ top 5: `7`, `2`, `6`, `8`, `0`
---

![chem-organic-Z](chem-organic-Z.png)

Fact: The atomic number of the element present in all organic compounds by definition is

**Answer:** **6** · **Hidden trajectory:** carbon → 6

**gemma-4-31B-it:** ✅ top 5: `6`, `0`, `3`, `1`, `2`
---

![func-pumps-chambers](func-pumps-chambers.png)

Fact: In humans, the organ that pumps blood through the body has this many chambers:

**Answer:** **4** · **Hidden trajectory:** heart → 4

**gemma-4-31B-it:** ✅ top 5: `4`, ``, ``, `2`, `0`
---

![func-filters-count](func-filters-count.png)

Fact: In humans, the number of organs that filter blood to make urine is

**Answer:** **2** · **Hidden trajectory:** kidney → 2

**gemma-4-31B-it:** ✅ top 5: `2`, `0`, `1`, `3`, ``
---

![birthstone-emerald-month](birthstone-emerald-month.png)

Fact: Emerald is the birthstone for month number

**Answer:** **5** · **Hidden trajectory:** May → 5

**gemma-4-31B-it:** ✅ top 5: `5`, `1`, `2`, `3`, `4`
---

![violin-strings](violin-strings.png)

Fact: The number of strings on the instrument that fiddlers play is

**Answer:** **4** · **Hidden trajectory:** violin → 4

**gemma-4-31B-it:** ✅ top 5: `4`, `2`, `6`, `�`, `5`
---

![nhop-guitar-planet](nhop-guitar-planet.png)

Count the legs on a spider. The planet at that position from the Sun is Neptune. Count the strings on a standard guitar. The planet at that position from the Sun is

**Answer:** **Saturn** · **Hidden trajectory:** 6 → six → Saturn

**gemma-4-31B-it:** ✅ top 5: `Saturn`, `own`, `Uranus`, `Neptune`, `Pluto`
---

![nhop-compass-planet](nhop-compass-planet.png)

Count the legs on a spider. The planet at that position from the Sun is Neptune. Count the cardinal directions on a compass. The planet at that position from the Sun is

**Answer:** **Mars** · **Hidden trajectory:** 4 → four → Mars

**gemma-4-31B-it:** ✅ top 5: `Mars`, `own`, `Uranus`, `Venus`, `Neptune`
---

![nhop-cube-element](nhop-cube-element.png)

Count the items in a dozen. The element at that position on the periodic table is magnesium. Count the faces on a cube. The element at that position on the periodic table is

**Answer:** **carbon** · **Hidden trajectory:** 6 → six → carbon

**gemma-4-31B-it:** ✅ top 5: `carbon`, `own`, `carbono`, `carbone`, `الكربون`
---

![nhop-rainbow-element](nhop-rainbow-element.png)

Count the items in a dozen. The element at that position on the periodic table is magnesium. Count the colors in a rainbow. The element at that position on the periodic table is

**Answer:** **nitrogen** · **Hidden trajectory:** 7 → nitrogen

**gemma-4-31B-it:** ✅ top 5: `nitrogen`, `Nitrogen`, `nitrog`, `own`, `nitro`
---

![nhop-spider-element](nhop-spider-element.png)

Count the items in a dozen. The element at that position on the periodic table is magnesium. Count the legs on a spider. The element at that position on the periodic table is

**Answer:** **oxygen** · **Hidden trajectory:** 8 → oxygen

**gemma-4-31B-it:** ✅ top 5: `oxygen`, `own`, `’`, `oxígeno`, `and`
---

![nhop-insect-element](nhop-insect-element.png)

Count the items in a dozen. The element at that position on the periodic table is magnesium. Count the legs on an insect. The element at that position on the periodic table is

**Answer:** **carbon** · **Hidden trajectory:** 6 → six → carbon

**gemma-4-31B-it:** ✅ top 5: `carbon`, `own`, `carbono`, `carbone`, `karbon`
---

![nhop-week-element](nhop-week-element.png)

Count the items in a dozen. The element at that position on the periodic table is magnesium. Count the days in a week. The element at that position on the periodic table is

**Answer:** **nitrogen** · **Hidden trajectory:** 7 → nitrogen

**gemma-4-31B-it:** ✅ top 5: `nitrogen`, `nitrog`, `Nitrogen`, `own`, `nitro`
---

![super-smallest-continent](super-smallest-continent.png)

Fact: The smallest country in the world is located on the continent of

**Answer:** **Europe** · **Hidden trajectory:** Vatican → Europe

**gemma-4-31B-it:** ✅ top 5: `Europe`, `Asia`, `Africa`, `**`, `Antarctica`
---

![colosseum-currency](colosseum-currency.png)

Fact: The currency used in the country where the Colosseum stands is the

**Answer:** **Euro** · **Hidden trajectory:** Italy → Euro

**gemma-4-31B-it:** ✅ top 5: `Euro`, `**`, `euro`, `own`, `same`
---

![holiday-independence-monthnum](holiday-independence-monthnum.png)

Fact: The US Independence Day holiday is celebrated in month number

**Answer:** **7** · **Hidden trajectory:** July → 7

**gemma-4-31B-it:** ✅ top 5: `7`, `0`, `6`, `4`, `2`
---

![holiday-valentines-monthnum](holiday-valentines-monthnum.png)

Fact: Valentine's Day is celebrated in month number

**Answer:** **2** · **Hidden trajectory:** February → 2

**gemma-4-31B-it:** ✅ top 5: `2`, `0`, `3`, `1`, `4`
---

![month-1-godof](month-1-godof.png)

Fact: The first month of the year is named after the Roman god of

**Answer:** **beginnings** · **Hidden trajectory:** January → beginnings

**gemma-4-31B-it:** ✅ top 5: `beginnings`, `own`, `new`, `doorways`, `doors`
---

![etym-janus-monthnum](etym-janus-monthnum.png)

Fact: The month named after the two-faced Roman god of doorways is month number

**Answer:** **1** · **Hidden trajectory:** January → 1

**gemma-4-31B-it:** ✅ top 5: `1`, `2`, `6`, `3`, `4`
---

![month-7-namedafter](month-7-namedafter.png)

Fact: The seventh month of the year is named after the Roman leader Julius

**Answer:** **Caesar** · **Hidden trajectory:** July → Caesar

**gemma-4-31B-it:** ✅ top 5: `Caesar`, `own`, `Caesars`, `caesar`, `’`
---

![etym-caesar-monthnum](etym-caesar-monthnum.png)

Fact: The month named after Julius Caesar is month number

**Answer:** **7** · **Hidden trajectory:** July → 7

**gemma-4-31B-it:** ✅ top 5: `7`, `2`, `4`, `3`, `6`
---

![inv-balloon-opposite](inv-balloon-opposite.png)

Fact: The direction opposite to the one a helium balloon floats toward is "

**Answer:** **down** · **Hidden trajectory:** up → down

**gemma-4-31B-it:** ✅ top 5: `down`, `Down`, `up`, `DOWN`, `bottom`
---

![inv-roots-opposite](inv-roots-opposite.png)

Fact: The direction opposite to the one tree roots grow is "

**Answer:** **up** · **Hidden trajectory:** down → up

**gemma-4-31B-it:** ✅ top 5: `up`, `Up`, `down`, `UP`, `above`
---

![rhyme-tree-squared](rhyme-tree-squared.png)

Fact: The square of the number whose name rhymes with tree is

**Answer:** **9** · **Hidden trajectory:** three → 9

**gemma-4-31B-it:** ✅ top 5: `9`, `3`, `2`, `4`, `0`
---

![rhyme-hive-plusone](rhyme-hive-plusone.png)

Fact: One more than the number whose name rhymes with hive is

**Answer:** **6** · **Hidden trajectory:** five → 6

**gemma-4-31B-it:** ✅ top 5: `6`, ``, `5`, `<u>`, `4`
---

![tajmahal-continent](tajmahal-continent.png)

Fact: The continent where the country that built the Taj Mahal is located is

**Answer:** **Asia** · **Hidden trajectory:** India → Asia

**gemma-4-31B-it:** ✅ top 5: `Asia`, `located`, `the`, `**`, `...`
---

![louvre-language](louvre-language.png)

Fact: The primary language spoken in the country where the Louvre museum is located is

**Answer:** **French** · **Hidden trajectory:** France → French

**gemma-4-31B-it:** ✅ top 5: `French`, `**`, `own`, `the`, `official`
---

![firstletter-halloween-month](firstletter-halloween-month.png)

Fact: The first letter of the month containing Halloween is "

**Answer:** **O** · **Hidden trajectory:** October → O

**gemma-4-31B-it:** ✅ top 5: `O`, `o`, `S`, `C`, `T`
---

![firstletter-valentines-month](firstletter-valentines-month.png)

Fact: The first letter of the month containing Valentine's Day is "

**Answer:** **F** · **Hidden trajectory:** February → F

**gemma-4-31B-it:** ✅ top 5: `F`, `V`, `f`, `//`, `F`
---

![succ-halloween-nextmonth](succ-halloween-nextmonth.png)

Fact: The month immediately after the one containing Halloween is

**Answer:** **November** · **Hidden trajectory:** October → November

**gemma-4-31B-it:** ✅ top 5: `November`, `**`, `the`, `...`, `October`
---

![pred-valentines-prevmonth](pred-valentines-prevmonth.png)

Fact: The month immediately before the one containing Valentine's Day is "

**Answer:** **January** · **Hidden trajectory:** February → January

**gemma-4-31B-it:** ✅ top 5: `January`, `February`, `JAN`, `la`, `**.`
---

![dual-stars-visible-opposite](dual-stars-visible-opposite.png)

Fact: The opposite of the time of day when stars are visible is "

**Answer:** **day** · **Hidden trajectory:** night → day

**gemma-4-31B-it:** ✅ top 5: `day`, `Day`, `the`, `daytime`, `dawn`
---

![dual-photosynthesis-opposite](dual-photosynthesis-opposite.png)

Fact: The opposite of the time of day when plants photosynthesize is "

**Answer:** **night** · **Hidden trajectory:** day → night

**gemma-4-31B-it:** ✅ top 5: `night`, `Night`, `the`, `at`, `midnight`
---

![half-clock-hours](half-clock-hours.png)

Fact: Half the number of hours shown on a standard clock face is

**Answer:** **6** · **Hidden trajectory:** 12 → 6

**gemma-4-31B-it:** ✅ top 5: `6`, `1`, `3`, `7`, `2`
---

![letterpos-carbon-symbol](letterpos-carbon-symbol.png)

Fact: The position in the alphabet of the chemical symbol for carbon is

**Answer:** **3** · **Hidden trajectory:** C → 3

**gemma-4-31B-it:** ✅ top 5: `3`, `1`, `2`, `5`, `4`
---

![dbl-obituary-antonym](dbl-obituary-antonym.png)

Fact: The antonym of what an obituary announces is "

**Answer:** **birth** · **Hidden trajectory:** death → birth

**gemma-4-31B-it:** ✅ top 5: `birth`, `life`, `living`, `Birth`, `coming`
---

![dbl-altitude-antonym](dbl-altitude-antonym.png)

Fact: The antonym of how you would describe an airplane's cruising altitude is "

**Answer:** **low** · **Hidden trajectory:** high → low

**gemma-4-31B-it:** ✅ top 5: `low`, `Low`, `down`, `lo`, `high`

## Answered wrong (48)

---

![carnival-ocean](carnival-ocean.png)

Fact: The ocean on the coast of the country where Carnival is most famously celebrated is the

**Answer:** **Atlantic** · **Hidden trajectory:** Brazil → Atlantic

**gemma-4-31B-it:** ❌ top 5: `ocean`, `Atlantic`, `atlantic`, `Atlantic`, `world`
---

![spider-legs](spider-legs.png)

Fact: The number of legs on the animal that spins webs is

**Answer:** **8** · **Hidden trajectory:** spider → 8

**gemma-4-31B-it:** ❌ top 5: `1`, `0`, `8`, `2`, `�`
---

![basketball-players](basketball-players.png)

Fact: The number of players per side in the sport invented in Springfield, Massachusetts is

**Answer:** **5** · **Hidden trajectory:** basketball → 5

**gemma-4-31B-it:** ❌ top 5: `6`, `9`, `1`, `5`, `2`
---

![osu-rival-mascot](osu-rival-mascot.png)

Fact: The mascot of the college football rival of Ohio State is a

**Answer:** **wolverine** · **Hidden trajectory:** Michigan → wolverine

**gemma-4-31B-it:** ❌ top 5: `chip`, `buck`, `bunny`, `bear`, `chipped`
---

![topeka-west](topeka-west.png)

Fact: The state west of the state with Topeka as its capital is

**Answer:** **Colorado** · **Hidden trajectory:** Kansas → Colorado

**gemma-4-31B-it:** ❌ top 5: `Nevada`, `**`, `Arizona`, `either`, `actually`
---

![atomic-79-symbol](atomic-79-symbol.png)

Fact: The chemical symbol for the element with atomic number 79 is

**Answer:** **Au** · **Hidden trajectory:** gold → Au

**gemma-4-31B-it:** ❌ top 5: `**`, `Au`, `"`, `'`, `$\`
---

![atomic-26-symbol](atomic-26-symbol.png)

Fact: The chemical symbol for the element with atomic number 26 is

**Answer:** **Fe** · **Hidden trajectory:** iron → Fe

**gemma-4-31B-it:** ❌ top 5: `**`, `Fe`, `"`, `$\`, `'`
---

![atomic-29-symbol](atomic-29-symbol.png)

Fact: The chemical symbol for the element with atomic number 29 is

**Answer:** **Cu** · **Hidden trajectory:** copper → Cu

**gemma-4-31B-it:** ❌ top 5: `**`, `Cu`, `"`, `$\`, `"**`
---

![atomic-80-state](atomic-80-state.png)

Fact: The state of matter at room temperature of the element with atomic number 80 is

**Answer:** **liquid** · **Hidden trajectory:** mercury → liquid

**gemma-4-31B-it:** ❌ top 5: `Mercury`, `mercury`, `own`, `Hg`, `**`
---

![atomic-29-flame](atomic-29-flame.png)

Fact: The flame color produced by burning the element with atomic number 29 is

**Answer:** **green** · **Hidden trajectory:** copper → green

**gemma-4-31B-it:** ❌ top 5: `the`, `’`, `set`, `associated`, `element`
---

![month-3-godof](month-3-godof.png)

Fact: The third month of the year is named after the Roman god of

**Answer:** **war** · **Hidden trajectory:** March → war

**gemma-4-31B-it:** ❌ top 5: `beginnings`, `own`, `beginning`, `new`, `the`
---

![rhyme-rain-neighbor](rhyme-rain-neighbor.png)

Fact: The European country whose name rhymes with 'rain' shares its western border with

**Answer:** **Portugal** · **Hidden trajectory:** Spain → Portugal

**gemma-4-31B-it:** ❌ top 5: `the`, `France`, `Spain`, `its`, `only`
---

![rhyme-chair-flag](rhyme-chair-flag.png)

Fact: The large mammal whose name rhymes with 'chair' appears on the state flag of

**Answer:** **California** · **Hidden trajectory:** bear → California

**gemma-4-31B-it:** ❌ top 5: `the`, `own`, `Wyoming`, `Louisiana`, `Georgia`
---

![rhyme-spoon-orbit](rhyme-spoon-orbit.png)

Fact: The celestial body whose name rhymes with 'spoon' orbits the planet called

**Answer:** **Earth** · **Hidden trajectory:** moon → Earth

**gemma-4-31B-it:** ❌ top 5: `'`, `the`, `Jupiter`, `called`, `own`
---

![etym-frigg-position](etym-frigg-position.png)

Fact: Counting Monday as day 1, the day of the week named after the Norse goddess Frigg is day number

**Answer:** **5** · **Hidden trajectory:** Friday → 5

**gemma-4-31B-it:** ❌ top 5: `1`, `3`, `6`, `4`, `2`
---

![etym-saturn-position](etym-saturn-position.png)

Fact: The planet named after the Roman god of agriculture and time is planet number

**Answer:** **6** · **Hidden trajectory:** Saturn → 6

**gemma-4-31B-it:** ❌ top 5: `4`, `7`, `1`, `6`, `2`
---

![chem-photosynthesis-Z](chem-photosynthesis-Z.png)

Fact: The atomic number of the gas that plants release during photosynthesis is

**Answer:** **8** · **Hidden trajectory:** oxygen → 8

**gemma-4-31B-it:** ❌ top 5: `2`, `8`, `7`, `1`, `6`
---

![chem-bones-Z](chem-bones-Z.png)

Fact: The atomic number of the metal most abundant in human bones is

**Answer:** **20** · **Hidden trajectory:** calcium → 20

**gemma-4-31B-it:** ❌ top 5: `2`, `4`, `3`, `1`, `5`
---

![nhop-primary-planet](nhop-primary-planet.png)

Count the legs on a spider. The planet at that position from the Sun is Neptune. Count the primary colors of light. The planet at that position from the Sun is

**Answer:** **Earth** · **Hidden trajectory:** 3 → three → third → Earth

**gemma-4-31B-it:** ❌ top 5: `own`, `Earth`, `Neptune`, `Saturn`, `Mars`
---

![nhop-rings-planet](nhop-rings-planet.png)

Count the legs on a spider. The planet at that position from the Sun is Neptune. Count the Olympic rings. The planet at that position from the Sun is

**Answer:** **Jupiter** · **Hidden trajectory:** 5 → five → Jupiter

**gemma-4-31B-it:** ❌ top 5: `own`, `Saturn`, `Jupiter`, `Neptune`, `Uranus`
---

![nhop-volleyball-planet](nhop-volleyball-planet.png)

Count the legs on a spider. The planet at that position from the Sun is Neptune. Count the players on a volleyball court per team. The planet at that position from the Sun is

**Answer:** **Saturn** · **Hidden trajectory:** 6 → six → Saturn

**gemma-4-31B-it:** ❌ top 5: `own`, `Saturn`, `Uranus`, `Pluto`, `Jupiter`
---

![nhop-alphabet-element](nhop-alphabet-element.png)

Count the items in a dozen. The element at that position on the periodic table is magnesium. Count the letters in the English alphabet. The element at that position on the periodic table is

**Answer:** **iron** · **Hidden trajectory:** 26 → iron

**gemma-4-31B-it:** ❌ top 5: `own`, `the`, `magnesium`, `neon`, `nickel`
---

![nhop-fortnight-element](nhop-fortnight-element.png)

Count the items in a dozen. The element at that position on the periodic table is magnesium. Count the days in a fortnight. The element at that position on the periodic table is

**Answer:** **silicon** · **Hidden trajectory:** 14 → silicon

**gemma-4-31B-it:** ❌ top 5: `sulfur`, `selenium`, `phosphorus`, `silicon`, `sulphur`
---

![super-largest-country-capital](super-largest-country-capital.png)

Fact: The capital city of the largest country by area is

**Answer:** **Moscow** · **Hidden trajectory:** Russia → Moscow

**gemma-4-31B-it:** ❌ top 5: `**`, `Moscow`, `the`, `{`, `located`
---

![super-populous-capital](super-populous-capital.png)

Fact: The capital city of the most populous country in the world is

**Answer:** **Beijing** · **Hidden trajectory:** China → Beijing

**gemma-4-31B-it:** ❌ top 5: `**`, `Beijing`, `the`, `located`, `something`
---

![super-largest-island-nation](super-largest-island-nation.png)

Fact: The country that is the largest island nation by area has its capital at

**Answer:** **Jakarta** · **Hidden trajectory:** Indonesia → Jakarta

**gemma-4-31B-it:** ❌ top 5: `own`, ``, `coordinates`, `longitude`, `**`
---

![greatwall-ocean](greatwall-ocean.png)

Fact: The ocean east of the country that built the Great Wall is the

**Answer:** **Pacific** · **Hidden trajectory:** China → Pacific

**gemma-4-31B-it:** ❌ top 5: `same`, `Pacific`, `East`, `Philippines`, `ocean`
---

![holiday-christmas-monthnum](holiday-christmas-monthnum.png)

Fact: Christmas Day is celebrated in month number

**Answer:** **12** · **Hidden trajectory:** December → 12

**gemma-4-31B-it:** ❌ top 5: `1`, `2`, `6`, `7`, `5`
---

![holiday-halloween-monthnum](holiday-halloween-monthnum.png)

Fact: Halloween is celebrated in month number

**Answer:** **10** · **Hidden trajectory:** October → 10

**gemma-4-31B-it:** ❌ top 5: `1`, `7`, `8`, `2`, `6`
---

![nhop-soccer-element](nhop-soccer-element.png)

Count the items in a dozen. The element at that position on the periodic table is magnesium. Count the players on a soccer team on the field. The element at that position on the periodic table is

**Answer:** **sodium** · **Hidden trajectory:** 11 → sodium

**gemma-4-31B-it:** ❌ top 5: `phosphorus`, `phosphorous`, `aluminum`, `Phosphorus`, `phosphor`
---

![nhop-chess-element](nhop-chess-element.png)

Count the items in a dozen. The element at that position on the periodic table is magnesium. Count the pieces each player starts with in chess. The element at that position on the periodic table is

**Answer:** **sulfur** · **Hidden trajectory:** 16 → sulfur

**gemma-4-31B-it:** ❌ top 5: `cobalt`, `gad`, `selenium`, `potassium`, `strontium`
---

![nhop-suit-element](nhop-suit-element.png)

Count the items in a dozen. The element at that position on the periodic table is magnesium. Count the cards in one suit of a standard deck. The element at that position on the periodic table is

**Answer:** **aluminum** · **Hidden trajectory:** 13 → aluminum

**gemma-4-31B-it:** ❌ top 5: `iodine`, `palladium`, `the`, `’`, `tell`
---

![nhop-clock-element](nhop-clock-element.png)

Count the items in a dozen. The element at that position on the periodic table is magnesium. Count the hours marked on a standard clock face. The element at that position on the periodic table is

**Answer:** **magnesium** · **Hidden trajectory:** 12 → magnesium

**gemma-4-31B-it:** ❌ top 5: `aluminum`, `aluminium`, `own`, `aluminio`, `alumnus`
---

![nhop-deck-element](nhop-deck-element.png)

Count the items in a dozen. The element at that position on the periodic table is magnesium. Count the cards in a standard deck without jokers. The element at that position on the periodic table is

**Answer:** **tellurium** · **Hidden trajectory:** 52 → tellurium

**gemma-4-31B-it:** ❌ top 5: `tell`, `not`, `selenium`, `iodine`, `{`
---

![inv-sunrise-opposite](inv-sunrise-opposite.png)

Fact: The cardinal direction opposite to the one where the sun rises is

**Answer:** **west** · **Hidden trajectory:** east → west

**gemma-4-31B-it:** ❌ top 5: `West`, `west`, `the`, `own`, `**`
---

![inv-antarctica-opposite](inv-antarctica-opposite.png)

Fact: The cardinal direction opposite to where Antarctica lies from the equator is

**Answer:** **north** · **Hidden trajectory:** south → north

**gemma-4-31B-it:** ❌ top 5: `North`, `north`, `**`, `own`, `...`
---

![rhyme-fix-halved](rhyme-fix-halved.png)

Fact: Half of the number whose name rhymes with fix is

**Answer:** **3** · **Hidden trajectory:** six → 3

**gemma-4-31B-it:** ❌ top 5: `2`, `1`, `3`, `4`, `5`
---

![rhyme-shoe-doubled](rhyme-shoe-doubled.png)

Fact: Double the number whose name rhymes with shoe is

**Answer:** **4** · **Hidden trajectory:** two → 4

**gemma-4-31B-it:** ❌ top 5: `2`, `4`, `1`, `3`, `6`
---

![firstletter-populous-country](firstletter-populous-country.png)

Fact: The first letter of the name of the world's most populous country is

**Answer:** **C** · **Hidden trajectory:** China → C

**gemma-4-31B-it:** ❌ top 5: `'`, `"`, `the`, `'`, `**`
---

![firstletter-paris-country](firstletter-paris-country.png)

Fact: The first letter of the name of the country whose capital is Paris is

**Answer:** **F** · **Hidden trajectory:** France → F

**gemma-4-31B-it:** ❌ top 5: `'`, `"`, `P`, `the`, `**`
---

![firstletter-greatwall-country](firstletter-greatwall-country.png)

Fact: The first letter of the name of the country that built the Great Wall is

**Answer:** **C** · **Hidden trajectory:** China → C

**gemma-4-31B-it:** ❌ top 5: `China`, `not`, `**`, `located`, `why`
---

![roman-rings-olympic](roman-rings-olympic.png)

Fact: Written as a Roman numeral, the number of Olympic rings is

**Answer:** **V** · **Hidden trajectory:** 5 → five → V

**gemma-4-31B-it:** ❌ top 5: `either`, `five`, `not`, ``, `**`
---

![roman-states-us](roman-states-us.png)

Fact: Written as a Roman numeral, the number of US states is

**Answer:** **L** · **Hidden trajectory:** 50 → L

**gemma-4-31B-it:** ❌ top 5: `written`, ``, `adage`, `stored`, `used`
---

![double-dice-faces](double-dice-faces.png)

Fact: Double the number of faces on a standard die is

**Answer:** **12** · **Hidden trajectory:** 6 → six → 12

**gemma-4-31B-it:** ❌ top 5: `1`, `6`, `2`, `5`, `3`
---

![letterpos-water-symbol](letterpos-water-symbol.png)

Fact: The position in the alphabet of the chemical symbol for hydrogen is

**Answer:** **8** · **Hidden trajectory:** H → 8

**gemma-4-31B-it:** ❌ top 5: `1`, `2`, `5`, `6`, `3`
---

![letterpos-oxygen-symbol](letterpos-oxygen-symbol.png)

Fact: The position in the alphabet of the chemical symbol for oxygen is

**Answer:** **15** · **Hidden trajectory:** O → 15

**gemma-4-31B-it:** ❌ top 5: `1`, `2`, `8`, `5`, `3`
---

![letterpos-nitrogen-symbol](letterpos-nitrogen-symbol.png)

Fact: The position in the alphabet of the chemical symbol for nitrogen is

**Answer:** **14** · **Hidden trajectory:** N → 14

**gemma-4-31B-it:** ❌ top 5: `1`, `7`, `2`, `5`, `3`
---

![dbl-armistice-antonym](dbl-armistice-antonym.png)

Fact: The antonym of what an armistice ends is "

**Answer:** **peace** · **Hidden trajectory:** war → peace

**gemma-4-31B-it:** ❌ top 5: `war`, `conflict`, `War`, `peace`, `Conflict`
