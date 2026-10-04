# lens-eval-multihop: J-lens by layer and token, Qwen3.6-27B

Lens: `neuronpedia/jacobian-lens/qwen3.6-27b/jlens/Salesforce-wikitext/Qwen3.6-27B_jacobian_lens_n1000.pt`. Each item's graph shows, on top, the J-lens rank of every tracked word at the
token before the answer (log scale, rank 1 at the top; thin = raw, thick = EWMA with a 2-layer
halflife). Below it, one heatmap per word: rank at every layer (y) and each of the last prompt tokens (x),
darker = closer to the lens's top token. Correct items first.

| depth | correct |
| --- | --- |
| all | 60/93 |

## Summary: median rank over correct items

![summary](summary.png)

## Answered correctly (60)

---

![carnival-ocean](carnival-ocean.png)

Fact: The ocean on the coast of the country where Carnival is most famously celebrated is the

**Answer:** **Atlantic** · **Hidden trajectory:** Brazil → Atlantic

**Qwen3.6-27B:** ✅ top 5: `Atlantic`, `Pacific`, `Caribbean`, ``, `South`
---

![amazon-language](amazon-language.png)

Fact: The language spoken in the country where the Amazon River ends is

**Answer:** **Portuguese** · **Hidden trajectory:** Brazil → Portuguese

**Qwen3.6-27B:** ✅ top 5: `Portuguese`, `the`, ``, `Brazil`, `Brazilian`
---

![mars-color](mars-color.png)

Fact: The color of the planet fourth from the Sun is

**Answer:** **red** · **Hidden trajectory:** Mars → red

**Qwen3.6-27B:** ✅ top 5: `red`, `orange`, `redd`, `yellow`, `blue`
---

![spider-legs](spider-legs.png)

Fact: The number of legs on the animal that spins webs is

**Answer:** **8** · **Hidden trajectory:** spider → 8

**Qwen3.6-27B:** ✅ top 5: `8`, `0`, `4`, `2`, `6`
---

![basketball-players](basketball-players.png)

Fact: The number of players per side in the sport invented in Springfield, Massachusetts is

**Answer:** **5** · **Hidden trajectory:** basketball → 5

**Qwen3.6-27B:** ✅ top 5: `5`, `1`, `2`, `9`, `6`
---

![paper-continent](paper-continent.png)

Fact: The continent where the country that invented paper is located is

**Answer:** **Asia** · **Hidden trajectory:** China → Asia

**Qwen3.6-27B:** ✅ top 5: `Asia`, `the`, `also`, `called`, `China`
---

![christmas-season](christmas-season.png)

Fact: The season when the holiday with a decorated tree occurs is

**Answer:** **winter** · **Hidden trajectory:** Christmas → winter

**Qwen3.6-27B:** ✅ top 5: `winter`, `the`, `a`, `called`, `also`
---

![atomic-79-symbol](atomic-79-symbol.png)

Fact: The chemical symbol for the element with atomic number 79 is

**Answer:** **Au** · **Hidden trajectory:** gold → Au

**Qwen3.6-27B:** ✅ top 5: `Au`, `:`, `**`, `'`, `"`
---

![atomic-26-symbol](atomic-26-symbol.png)

Fact: The chemical symbol for the element with atomic number 26 is

**Answer:** **Fe** · **Hidden trajectory:** iron → Fe

**Qwen3.6-27B:** ✅ top 5: `Fe`, `**`, `$`, ``, `:`
---

![atomic-29-symbol](atomic-29-symbol.png)

Fact: The chemical symbol for the element with atomic number 29 is

**Answer:** **Cu** · **Hidden trajectory:** copper → Cu

**Qwen3.6-27B:** ✅ top 5: `Cu`, `:`, `**`, `$`, ``
---

![atomic-29-flame](atomic-29-flame.png)

Fact: The flame color produced by burning the element with atomic number 29 is

**Answer:** **green** · **Hidden trajectory:** copper → green

**Qwen3.6-27B:** ✅ top 5: `green`, `red`, `brick`, `yellow`, `:`
---

![month-3-godof](month-3-godof.png)

Fact: The third month of the year is named after the Roman god of

**Answer:** **war** · **Hidden trajectory:** March → war

**Qwen3.6-27B:** ✅ top 5: `war`, `the`, `agriculture`, `spring`, `gates`
---

![spaceneedle-border](spaceneedle-border.png)

Fact: The US state where the Space Needle is located shares its northern border with

**Answer:** **Canada** · **Hidden trajectory:** Seattle → Canada

**Qwen3.6-27B:** ✅ top 5: `Canada`, `the`, `a`, `which`, `another`
---

![rhyme-chair-flag](rhyme-chair-flag.png)

Fact: The large mammal whose name rhymes with 'chair' appears on the state flag of

**Answer:** **California** · **Hidden trajectory:** bear → California

**Qwen3.6-27B:** ✅ top 5: `California`, `Tennessee`, `Texas`, `Montana`, `New`
---

![rhyme-spoon-orbit](rhyme-spoon-orbit.png)

Fact: The celestial body whose name rhymes with 'spoon' orbits the planet called

**Answer:** **Earth** · **Hidden trajectory:** moon → Earth

**Qwen3.6-27B:** ✅ top 5: `Earth`, `'`, `Saturn`, `the`, `Jupiter`
---

![etym-wargod-month](etym-wargod-month.png)

Fact: The month named after the Roman god of war is month number

**Answer:** **3** · **Hidden trajectory:** March → 3

**Qwen3.6-27B:** ✅ top 5: `3`, `7`, `8`, `5`, `4`
---

![etym-saturn-position](etym-saturn-position.png)

Fact: The planet named after the Roman god of agriculture and time is planet number

**Answer:** **6** · **Hidden trajectory:** Saturn → 6

**Qwen3.6-27B:** ✅ top 5: `6`, `5`, `4`, `8`, `7`
---

![chem-photosynthesis-Z](chem-photosynthesis-Z.png)

Fact: The atomic number of the gas that plants release during photosynthesis is

**Answer:** **8** · **Hidden trajectory:** oxygen → 8

**Qwen3.6-27B:** ✅ top 5: `8`, `1`, `3`, `6`, `2`
---

![chem-atmosphere-Z](chem-atmosphere-Z.png)

Fact: The atomic number of the gas that makes up about 78 percent of the atmosphere is

**Answer:** **7** · **Hidden trajectory:** nitrogen → 7

**Qwen3.6-27B:** ✅ top 5: `7`, `2`, `1`, `6`, `4`
---

![chem-organic-Z](chem-organic-Z.png)

Fact: The atomic number of the element present in all organic compounds by definition is

**Answer:** **6** · **Hidden trajectory:** carbon → 6

**Qwen3.6-27B:** ✅ top 5: `6`, `1`, `4`, `2`, `0`
---

![func-pumps-chambers](func-pumps-chambers.png)

Fact: In humans, the organ that pumps blood through the body has this many chambers:

**Answer:** **4** · **Hidden trajectory:** heart → 4

**Qwen3.6-27B:** ✅ top 5: `4`, `1`, `2`, `3`, `0`
---

![func-filters-count](func-filters-count.png)

Fact: In humans, the number of organs that filter blood to make urine is

**Answer:** **2** · **Hidden trajectory:** kidney → 2

**Qwen3.6-27B:** ✅ top 5: `2`, `1`, `0`, `3`, `4`
---

![birthstone-emerald-month](birthstone-emerald-month.png)

Fact: Emerald is the birthstone for month number

**Answer:** **5** · **Hidden trajectory:** May → 5

**Qwen3.6-27B:** ✅ top 5: `5`, `0`, `4`, `3`, `1`
---

![violin-strings](violin-strings.png)

Fact: The number of strings on the instrument that fiddlers play is

**Answer:** **4** · **Hidden trajectory:** violin → 4

**Qwen3.6-27B:** ✅ top 5: `4`, `3`, `1`, `0`, `2`
---

![nhop-guitar-planet](nhop-guitar-planet.png)

Count the legs on a spider. The planet at that position from the Sun is Neptune. Count the strings on a standard guitar. The planet at that position from the Sun is

**Answer:** **Saturn** · **Hidden trajectory:** 6 → six → Saturn

**Qwen3.6-27B:** ✅ top 5: `Saturn`, `Uran`, `Jupiter`, `Mercury`, `Earth`
---

![nhop-volleyball-planet](nhop-volleyball-planet.png)

Count the legs on a spider. The planet at that position from the Sun is Neptune. Count the players on a volleyball court per team. The planet at that position from the Sun is

**Answer:** **Saturn** · **Hidden trajectory:** 6 → six → Saturn

**Qwen3.6-27B:** ✅ top 5: `Saturn`, `Uran`, `Earth`, `Mars`, `Venus`
---

![nhop-cube-element](nhop-cube-element.png)

Count the items in a dozen. The element at that position on the periodic table is magnesium. Count the faces on a cube. The element at that position on the periodic table is

**Answer:** **carbon** · **Hidden trajectory:** 6 → six → carbon

**Qwen3.6-27B:** ✅ top 5: `carbon`, `oxygen`, `Carbon`, `b`, `sulfur`
---

![nhop-rainbow-element](nhop-rainbow-element.png)

Count the items in a dozen. The element at that position on the periodic table is magnesium. Count the colors in a rainbow. The element at that position on the periodic table is

**Answer:** **nitrogen** · **Hidden trajectory:** 7 → nitrogen

**Qwen3.6-27B:** ✅ top 5: `nitrogen`, `Nit`, `oxygen`, `chlorine`, `...`
---

![nhop-spider-element](nhop-spider-element.png)

Count the items in a dozen. The element at that position on the periodic table is magnesium. Count the legs on a spider. The element at that position on the periodic table is

**Answer:** **oxygen** · **Hidden trajectory:** 8 → oxygen

**Qwen3.6-27B:** ✅ top 5: `oxygen`, `b`, `Oxygen`, `carbon`, `sulfur`
---

![nhop-insect-element](nhop-insect-element.png)

Count the items in a dozen. The element at that position on the periodic table is magnesium. Count the legs on an insect. The element at that position on the periodic table is

**Answer:** **carbon** · **Hidden trajectory:** 6 → six → carbon

**Qwen3.6-27B:** ✅ top 5: `carbon`, `oxygen`, `Carbon`, `b`, `silicon`
---

![nhop-week-element](nhop-week-element.png)

Count the items in a dozen. The element at that position on the periodic table is magnesium. Count the days in a week. The element at that position on the periodic table is

**Answer:** **nitrogen** · **Hidden trajectory:** 7 → nitrogen

**Qwen3.6-27B:** ✅ top 5: `nitrogen`, `Nit`, `lithium`, `...`, `oxygen`
---

![super-largest-country-capital](super-largest-country-capital.png)

Fact: The capital city of the largest country by area is

**Answer:** **Moscow** · **Hidden trajectory:** Russia → Moscow

**Qwen3.6-27B:** ✅ top 5: `Moscow`, `Ottawa`, ``, `located`, `not`
---

![super-smallest-continent](super-smallest-continent.png)

Fact: The smallest country in the world is located on the continent of

**Answer:** **Europe** · **Hidden trajectory:** Vatican → Europe

**Qwen3.6-27B:** ✅ top 5: `Europe`, ``, `__`, `Africa`, `...`
---

![super-populous-capital](super-populous-capital.png)

Fact: The capital city of the most populous country in the world is

**Answer:** **Beijing** · **Hidden trajectory:** China → Beijing

**Qwen3.6-27B:** ✅ top 5: `Beijing`, `New`, ``, `located`, `not`
---

![super-largest-island-nation](super-largest-island-nation.png)

Fact: The country that is the largest island nation by area has its capital at

**Answer:** **Jakarta** · **Hidden trajectory:** Indonesia → Jakarta

**Qwen3.6-27B:** ✅ top 5: `Jakarta`, `Port`, `Canberra`, `the`, `a`
---

![colosseum-currency](colosseum-currency.png)

Fact: The currency used in the country where the Colosseum stands is the

**Answer:** **Euro** · **Hidden trajectory:** Italy → Euro

**Qwen3.6-27B:** ✅ top 5: `Euro`, `euro`, ``, `__`, `______`
---

![holiday-independence-monthnum](holiday-independence-monthnum.png)

Fact: The US Independence Day holiday is celebrated in month number

**Answer:** **7** · **Hidden trajectory:** July → 7

**Qwen3.6-27B:** ✅ top 5: `7`, `6`, `1`, `0`, `8`
---

![holiday-valentines-monthnum](holiday-valentines-monthnum.png)

Fact: Valentine's Day is celebrated in month number

**Answer:** **2** · **Hidden trajectory:** February → 2

**Qwen3.6-27B:** ✅ top 5: `2`, `1`, `0`, `3`, `4`
---

![month-1-godof](month-1-godof.png)

Fact: The first month of the year is named after the Roman god of

**Answer:** **beginnings** · **Hidden trajectory:** January → beginnings

**Qwen3.6-27B:** ✅ top 5: `beginnings`, `doors`, `door`, `gates`, `the`
---

![month-7-namedafter](month-7-namedafter.png)

Fact: The seventh month of the year is named after the Roman leader Julius

**Answer:** **Caesar** · **Hidden trajectory:** July → Caesar

**Qwen3.6-27B:** ✅ top 5: `Caesar`, `C`, `.`, `Ca`, `Ce`
---

![etym-caesar-monthnum](etym-caesar-monthnum.png)

Fact: The month named after Julius Caesar is month number

**Answer:** **7** · **Hidden trajectory:** July → 7

**Qwen3.6-27B:** ✅ top 5: `7`, `1`, `6`, `8`, `2`
---

![nhop-soccer-element](nhop-soccer-element.png)

Count the items in a dozen. The element at that position on the periodic table is magnesium. Count the players on a soccer team on the field. The element at that position on the periodic table is

**Answer:** **sodium** · **Hidden trajectory:** 11 → sodium

**Qwen3.6-27B:** ✅ top 5: `sodium`, `aluminum`, `fluor`, `titanium`, `bor`
---

![inv-balloon-opposite](inv-balloon-opposite.png)

Fact: The direction opposite to the one a helium balloon floats toward is "

**Answer:** **down** · **Hidden trajectory:** up → down

**Qwen3.6-27B:** ✅ top 5: `down`, `t`, `down`, `south`, `Down`
---

![inv-roots-opposite](inv-roots-opposite.png)

Fact: The direction opposite to the one tree roots grow is "

**Answer:** **up** · **Hidden trajectory:** down → up

**Qwen3.6-27B:** ✅ top 5: `up`, `down`, `up`, `t`, `away`
---

![inv-antarctica-opposite](inv-antarctica-opposite.png)

Fact: The cardinal direction opposite to where Antarctica lies from the equator is

**Answer:** **north** · **Hidden trajectory:** south → north

**Qwen3.6-27B:** ✅ top 5: `north`, `North`, `the`, `where`, `to`
---

![rhyme-tree-squared](rhyme-tree-squared.png)

Fact: The square of the number whose name rhymes with tree is

**Answer:** **9** · **Hidden trajectory:** three → 9

**Qwen3.6-27B:** ✅ top 5: `9`, `1`, `4`, `3`, `2`
---

![rhyme-fix-halved](rhyme-fix-halved.png)

Fact: Half of the number whose name rhymes with fix is

**Answer:** **3** · **Hidden trajectory:** six → 3

**Qwen3.6-27B:** ✅ top 5: `3`, `2`, `5`, `1`, `4`
---

![tajmahal-continent](tajmahal-continent.png)

Fact: The continent where the country that built the Taj Mahal is located is

**Answer:** **Asia** · **Hidden trajectory:** India → Asia

**Qwen3.6-27B:** ✅ top 5: `Asia`, `the`, `India`, `also`, `in`
---

![louvre-language](louvre-language.png)

Fact: The primary language spoken in the country where the Louvre museum is located is

**Answer:** **French** · **Hidden trajectory:** France → French

**Qwen3.6-27B:** ✅ top 5: `French`, `the`, ``, `not`, `:`
---

![firstletter-halloween-month](firstletter-halloween-month.png)

Fact: The first letter of the month containing Halloween is "

**Answer:** **O** · **Hidden trajectory:** October → O

**Qwen3.6-27B:** ✅ top 5: `O`, `H`, `N`, `o`, `0`
---

![firstletter-valentines-month](firstletter-valentines-month.png)

Fact: The first letter of the month containing Valentine's Day is "

**Answer:** **F** · **Hidden trajectory:** February → F

**Qwen3.6-27B:** ✅ top 5: `F`, `J`, `f`, `V`, `February`
---

![succ-halloween-nextmonth](succ-halloween-nextmonth.png)

Fact: The month immediately after the one containing Halloween is

**Answer:** **November** · **Hidden trajectory:** October → November

**Qwen3.6-27B:** ✅ top 5: `November`, `December`, `the`, `January`, `a`
---

![pred-valentines-prevmonth](pred-valentines-prevmonth.png)

Fact: The month immediately before the one containing Valentine's Day is "

**Answer:** **January** · **Hidden trajectory:** February → January

**Qwen3.6-27B:** ✅ top 5: `January`, `December`, `February`, `the`, `November`
---

![dual-stars-visible-opposite](dual-stars-visible-opposite.png)

Fact: The opposite of the time of day when stars are visible is "

**Answer:** **day** · **Hidden trajectory:** night → day

**Qwen3.6-27B:** ✅ top 5: `day`, `mor`, `night`, `noon`, `the`
---

![dual-photosynthesis-opposite](dual-photosynthesis-opposite.png)

Fact: The opposite of the time of day when plants photosynthesize is "

**Answer:** **night** · **Hidden trajectory:** day → night

**Qwen3.6-27B:** ✅ top 5: `night`, `not`, `dark`, `the`, `night`
---

![roman-rings-olympic](roman-rings-olympic.png)

Fact: Written as a Roman numeral, the number of Olympic rings is

**Answer:** **V** · **Hidden trajectory:** 5 → five → V

**Qwen3.6-27B:** ✅ top 5: `V`, `five`, ``, `equal`, `C`
---

![half-clock-hours](half-clock-hours.png)

Fact: Half the number of hours shown on a standard clock face is

**Answer:** **6** · **Hidden trajectory:** 12 → 6

**Qwen3.6-27B:** ✅ top 5: `6`, `1`, `3`, `2`, `5`
---

![dbl-armistice-antonym](dbl-armistice-antonym.png)

Fact: The antonym of what an armistice ends is "

**Answer:** **peace** · **Hidden trajectory:** war → peace

**Qwen3.6-27B:** ✅ top 5: `peace`, `ag`, `war`, `har`, `co`
---

![dbl-obituary-antonym](dbl-obituary-antonym.png)

Fact: The antonym of what an obituary announces is "

**Answer:** **birth** · **Hidden trajectory:** death → birth

**Qwen3.6-27B:** ✅ top 5: `birth`, `life`, `living`, `alive`, `live`
---

![dbl-altitude-antonym](dbl-altitude-antonym.png)

Fact: The antonym of how you would describe an airplane's cruising altitude is "

**Answer:** **low** · **Hidden trajectory:** high → low

**Qwen3.6-27B:** ✅ top 5: `low`, `short`, `close`, `very`, `ground`

## Answered wrong (33)

---

![osu-rival-mascot](osu-rival-mascot.png)

Fact: The mascot of the college football rival of Ohio State is a

**Answer:** **wolverine** · **Hidden trajectory:** Michigan → wolverine

**Qwen3.6-27B:** ❌ top 5: `buck`, `Buck`, `bob`, `bulld`, `wild`
---

![topeka-west](topeka-west.png)

Fact: The state west of the state with Topeka as its capital is

**Answer:** **Colorado** · **Hidden trajectory:** Kansas → Colorado

**Qwen3.6-27B:** ❌ top 5: `Kansas`, `Nebraska`, `Colorado`, `the`, `Iowa`
---

![atomic-80-state](atomic-80-state.png)

Fact: The state of matter at room temperature of the element with atomic number 80 is

**Answer:** **liquid** · **Hidden trajectory:** mercury → liquid

**Qwen3.6-27B:** ❌ top 5: `solid`, `a`, `liquid`, ``, `:`
---

![planet-3-moons](planet-3-moons.png)

Fact: The number of natural moons orbiting the planet third from the Sun is

**Answer:** **1** · **Hidden trajectory:** Earth → 1

**Qwen3.6-27B:** ❌ top 5: `0`, `2`, `1`, `3`, `6`
---

![rhyme-rain-neighbor](rhyme-rain-neighbor.png)

Fact: The European country whose name rhymes with 'rain' shares its western border with

**Answer:** **Portugal** · **Hidden trajectory:** Spain → Portugal

**Qwen3.6-27B:** ❌ top 5: `France`, `the`, `Germany`, `a`, `Belgium`
---

![rhyme-door-doubled](rhyme-door-doubled.png)

Fact: Take the number whose name rhymes with the word door. Doubling it gives the number

**Answer:** **8** · **Hidden trajectory:** four → 8

**Qwen3.6-27B:** ❌ top 5: `1`, `8`, `2`, `6`, `4`
---

![etym-frigg-position](etym-frigg-position.png)

Fact: Counting Monday as day 1, the day of the week named after the Norse goddess Frigg is day number

**Answer:** **5** · **Hidden trajectory:** Friday → 5

**Qwen3.6-27B:** ❌ top 5: `2`, `3`, `5`, `4`, `1`
---

![chem-bones-Z](chem-bones-Z.png)

Fact: The atomic number of the metal most abundant in human bones is

**Answer:** **20** · **Hidden trajectory:** calcium → 20

**Qwen3.6-27B:** ❌ top 5: `2`, `1`, `4`, `8`, `3`
---

![nhop-primary-planet](nhop-primary-planet.png)

Count the legs on a spider. The planet at that position from the Sun is Neptune. Count the primary colors of light. The planet at that position from the Sun is

**Answer:** **Earth** · **Hidden trajectory:** 3 → three → third → Earth

**Qwen3.6-27B:** ❌ top 5: `Jupiter`, `Uran`, `Saturn`, `Mercury`, `Earth`
---

![nhop-rings-planet](nhop-rings-planet.png)

Count the legs on a spider. The planet at that position from the Sun is Neptune. Count the Olympic rings. The planet at that position from the Sun is

**Answer:** **Jupiter** · **Hidden trajectory:** 5 → five → Jupiter

**Qwen3.6-27B:** ❌ top 5: `Saturn`, `Earth`, `Uran`, `Jupiter`, `Mars`
---

![nhop-compass-planet](nhop-compass-planet.png)

Count the legs on a spider. The planet at that position from the Sun is Neptune. Count the cardinal directions on a compass. The planet at that position from the Sun is

**Answer:** **Mars** · **Hidden trajectory:** 4 → four → Mars

**Qwen3.6-27B:** ❌ top 5: `Uran`, `Saturn`, `Earth`, `Mercury`, `Jupiter`
---

![nhop-alphabet-element](nhop-alphabet-element.png)

Count the items in a dozen. The element at that position on the periodic table is magnesium. Count the letters in the English alphabet. The element at that position on the periodic table is

**Answer:** **iron** · **Hidden trajectory:** 26 → iron

**Qwen3.6-27B:** ❌ top 5: `zinc`, `iron`, `iod`, `copper`, `silver`
---

![nhop-fortnight-element](nhop-fortnight-element.png)

Count the items in a dozen. The element at that position on the periodic table is magnesium. Count the days in a fortnight. The element at that position on the periodic table is

**Answer:** **silicon** · **Hidden trajectory:** 14 → silicon

**Qwen3.6-27B:** ❌ top 5: `nitrogen`, `silicon`, `Nit`, `chlorine`, `oxygen`
---

![greatwall-ocean](greatwall-ocean.png)

Fact: The ocean east of the country that built the Great Wall is the

**Answer:** **Pacific** · **Hidden trajectory:** China → Pacific

**Qwen3.6-27B:** ❌ top 5: `Yellow`, `Pacific`, `East`, `Sea`, `yellow`
---

![holiday-christmas-monthnum](holiday-christmas-monthnum.png)

Fact: Christmas Day is celebrated in month number

**Answer:** **12** · **Hidden trajectory:** December → 12

**Qwen3.6-27B:** ❌ top 5: `1`, `2`, ``, `3`, `0`
---

![holiday-halloween-monthnum](holiday-halloween-monthnum.png)

Fact: Halloween is celebrated in month number

**Answer:** **10** · **Hidden trajectory:** October → 10

**Qwen3.6-27B:** ❌ top 5: `1`, `3`, ``, `9`, `2`
---

![etym-janus-monthnum](etym-janus-monthnum.png)

Fact: The month named after the two-faced Roman god of doorways is month number

**Answer:** **1** · **Hidden trajectory:** January → 1

**Qwen3.6-27B:** ❌ top 5: `2`, `6`, `1`, `8`, `7`
---

![nhop-chess-element](nhop-chess-element.png)

Count the items in a dozen. The element at that position on the periodic table is magnesium. Count the pieces each player starts with in chess. The element at that position on the periodic table is

**Answer:** **sulfur** · **Hidden trajectory:** 16 → sulfur

**Qwen3.6-27B:** ❌ top 5: `oxygen`, `silicon`, `sulfur`, `iron`, `titanium`
---

![nhop-suit-element](nhop-suit-element.png)

Count the items in a dozen. The element at that position on the periodic table is magnesium. Count the cards in one suit of a standard deck. The element at that position on the periodic table is

**Answer:** **aluminum** · **Hidden trajectory:** 13 → aluminum

**Qwen3.6-27B:** ❌ top 5: `silicon`, `nitrogen`, `chlorine`, `carbon`, `sulfur`
---

![nhop-clock-element](nhop-clock-element.png)

Count the items in a dozen. The element at that position on the periodic table is magnesium. Count the hours marked on a standard clock face. The element at that position on the periodic table is

**Answer:** **magnesium** · **Hidden trajectory:** 12 → magnesium

**Qwen3.6-27B:** ❌ top 5: `carbon`, `nickel`, `copper`, `magnesium`, `neon`
---

![nhop-deck-element](nhop-deck-element.png)

Count the items in a dozen. The element at that position on the periodic table is magnesium. Count the cards in a standard deck without jokers. The element at that position on the periodic table is

**Answer:** **tellurium** · **Hidden trajectory:** 52 → tellurium

**Qwen3.6-27B:** ❌ top 5: `xen`, `silver`, `pall`, `bar`, `ruth`
---

![inv-sunrise-opposite](inv-sunrise-opposite.png)

Fact: The cardinal direction opposite to the one where the sun rises is

**Answer:** **west** · **Hidden trajectory:** east → west

**Qwen3.6-27B:** ❌ top 5: `the`, `west`, `West`, `called`, `where`
---

![rhyme-hive-plusone](rhyme-hive-plusone.png)

Fact: One more than the number whose name rhymes with hive is

**Answer:** **6** · **Hidden trajectory:** five → 6

**Qwen3.6-27B:** ❌ top 5: `7`, `6`, `8`, `1`, `5`
---

![rhyme-shoe-doubled](rhyme-shoe-doubled.png)

Fact: Double the number whose name rhymes with shoe is

**Answer:** **4** · **Hidden trajectory:** two → 4

**Qwen3.6-27B:** ❌ top 5: `1`, `2`, `8`, `6`, `4`
---

![firstletter-populous-country](firstletter-populous-country.png)

Fact: The first letter of the name of the world's most populous country is

**Answer:** **C** · **Hidden trajectory:** China → C

**Qwen3.6-27B:** ❌ top 5: `'`, `the`, `"`, `C`, `\"`
---

![firstletter-paris-country](firstletter-paris-country.png)

Fact: The first letter of the name of the country whose capital is Paris is

**Answer:** **F** · **Hidden trajectory:** France → F

**Qwen3.6-27B:** ❌ top 5: `P`, `'`, `the`, `F`, `"`
---

![firstletter-greatwall-country](firstletter-greatwall-country.png)

Fact: The first letter of the name of the country that built the Great Wall is

**Answer:** **C** · **Hidden trajectory:** China → C

**Qwen3.6-27B:** ❌ top 5: `the`, `'`, `China`, `G`, `C`
---

![roman-states-us](roman-states-us.png)

Fact: Written as a Roman numeral, the number of US states is

**Answer:** **L** · **Hidden trajectory:** 50 → L

**Qwen3.6-27B:** ❌ top 5: `XXX`, `L`, ``, `XX`, `XL`
---

![double-dice-faces](double-dice-faces.png)

Fact: Double the number of faces on a standard die is

**Answer:** **12** · **Hidden trajectory:** 6 → six → 12

**Qwen3.6-27B:** ❌ top 5: `1`, `6`, `2`, `8`, `4`
---

![letterpos-water-symbol](letterpos-water-symbol.png)

Fact: The position in the alphabet of the chemical symbol for hydrogen is

**Answer:** **8** · **Hidden trajectory:** H → 8

**Qwen3.6-27B:** ❌ top 5: `1`, `2`, `3`, `8`, `4`
---

![letterpos-oxygen-symbol](letterpos-oxygen-symbol.png)

Fact: The position in the alphabet of the chemical symbol for oxygen is

**Answer:** **15** · **Hidden trajectory:** O → 15

**Qwen3.6-27B:** ❌ top 5: `8`, `1`, `2`, `0`, `6`
---

![letterpos-carbon-symbol](letterpos-carbon-symbol.png)

Fact: The position in the alphabet of the chemical symbol for carbon is

**Answer:** **3** · **Hidden trajectory:** C → 3

**Qwen3.6-27B:** ❌ top 5: `6`, `1`, `2`, `4`, `3`
---

![letterpos-nitrogen-symbol](letterpos-nitrogen-symbol.png)

Fact: The position in the alphabet of the chemical symbol for nitrogen is

**Answer:** **14** · **Hidden trajectory:** N → 14

**Qwen3.6-27B:** ❌ top 5: `7`, `1`, `2`, `8`, `3`
