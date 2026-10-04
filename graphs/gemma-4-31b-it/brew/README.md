# brew: J-lens by layer and token, gemma-4-31B-it

Lens: `solarkyle/jspace-lenses/gemma-4-31b-it/lens.pt`. Rank here is rank among the 10 possible answers (red, blue, green, gold, black, white, pink, gray, purple, brown), 1 = the lens prefers it to all the others. Each item's graph shows, on top, the rank
of every tracked word at the token before the answer by layer (thin = raw, thick = EWMA with a
2-layer halflife). Below it, one heatmap per word: rank at every layer (y) and prompt token
(x), darker = higher rank. Dashed boxes outline the prompt line each step reads, in the colour of the
step it produces. A word lighting up on its own token in early layers is the token echoing itself, not
computation. Correct items first.

| depth | correct |
| --- | --- |
| 1 | 20/20 |
| 2 | 16/20 |
| 3 | 1/20 |

## Summary: median rank over correct items

![summary](summary.png)

## Answered correctly (37)

---

![brew-d1-00](brew-d1-00.png)

A potion changes color each time an ingredient is stirred in. The rules:  
A red potion turns black with bark, brown with chalk, and gold with salt.  
A brown potion turns green with bark, blue with chalk, and gold with salt.  
A blue potion turns pink with bark, red with chalk, and gold with salt.  
A pink potion turns black with bark, green with chalk, and white with salt.  
A black potion turns purple with bark, gray with chalk, and gray with salt.  
A white potion turns gold with bark, pink with chalk, and red with salt.  
A gold potion turns pink with bark, red with chalk, and gray with salt.  
A green potion turns blue with bark, red with chalk, and black with salt.  
A purple potion turns green with bark, gray with chalk, and gray with salt.  
A gray potion turns brown with bark, red with chalk, and purple with salt.  
The potion starts out gold. You stir in, one at a time: bark.  
What color is the potion at the end?

**Answer:** **pink** · **Hidden trajectory:** gold → pink

**gemma-4-31B-it:** ✅ top 5: `pink`, `own`, `Pink`, `PINK`, `pink`
---

![brew-d1-01](brew-d1-01.png)

A potion changes color each time an ingredient is stirred in. The rules:  
A white potion turns pink with ash, gold with moss, and gray with salt.  
A purple potion turns white with ash, white with moss, and red with salt.  
A gray potion turns white with ash, red with moss, and gold with salt.  
A brown potion turns purple with ash, pink with moss, and black with salt.  
A red potion turns green with ash, brown with moss, and gray with salt.  
A green potion turns red with ash, purple with moss, and white with salt.  
A gold potion turns purple with ash, black with moss, and purple with salt.  
A blue potion turns red with ash, white with moss, and green with salt.  
A black potion turns blue with ash, white with moss, and purple with salt.  
A pink potion turns gold with ash, gray with moss, and brown with salt.  
The potion starts out white. You stir in, one at a time: ash.  
What color is the potion at the end?

**Answer:** **pink** · **Hidden trajectory:** white → pink

**gemma-4-31B-it:** ✅ top 5: `pink`, `own`, `gold`, `pink`, `[`
---

![brew-d1-02](brew-d1-02.png)

A potion changes color each time an ingredient is stirred in. The rules:  
A gray potion turns red with bark, red with chalk, and pink with clay.  
A gold potion turns brown with bark, red with chalk, and blue with clay.  
A white potion turns red with bark, gold with chalk, and gray with clay.  
A blue potion turns purple with bark, white with chalk, and white with clay.  
A brown potion turns black with bark, pink with chalk, and purple with clay.  
A purple potion turns blue with bark, blue with chalk, and red with clay.  
A red potion turns blue with bark, purple with chalk, and gray with clay.  
A black potion turns green with bark, gray with chalk, and green with clay.  
A green potion turns gray with bark, purple with chalk, and gray with clay.  
A pink potion turns blue with bark, gray with chalk, and white with clay.  
The potion starts out white. You stir in, one at a time: clay.  
What color is the potion at the end?

**Answer:** **gray** · **Hidden trajectory:** white → gray

**gemma-4-31B-it:** ✅ top 5: `gray`, `grey`, `Gray`, `[`, `own`
---

![brew-d1-03](brew-d1-03.png)

A potion changes color each time an ingredient is stirred in. The rules:  
A gold potion turns blue with chalk, white with clay, and green with moss.  
A green potion turns gold with chalk, red with clay, and white with moss.  
A purple potion turns green with chalk, gold with clay, and brown with moss.  
A black potion turns purple with chalk, red with clay, and gold with moss.  
A brown potion turns gray with chalk, blue with clay, and red with moss.  
A white potion turns red with chalk, green with clay, and brown with moss.  
A blue potion turns purple with chalk, gold with clay, and purple with moss.  
A red potion turns blue with chalk, black with clay, and blue with moss.  
A gray potion turns brown with chalk, purple with clay, and purple with moss.  
A pink potion turns white with chalk, purple with clay, and brown with moss.  
The potion starts out white. You stir in, one at a time: moss.  
What color is the potion at the end?

**Answer:** **brown** · **Hidden trajectory:** white → brown

**gemma-4-31B-it:** ✅ top 5: `brown`, `own`, `brown`, `Brown`, `blue`
---

![brew-d1-04](brew-d1-04.png)

A potion changes color each time an ingredient is stirred in. The rules:  
A green potion turns blue with ash, gold with clay, and red with moss.  
A blue potion turns pink with ash, brown with clay, and gold with moss.  
A white potion turns gray with ash, purple with clay, and gold with moss.  
A red potion turns green with ash, gray with clay, and pink with moss.  
A purple potion turns white with ash, gray with clay, and white with moss.  
A black potion turns gold with ash, red with clay, and red with moss.  
A gray potion turns brown with ash, brown with clay, and gold with moss.  
A pink potion turns gold with ash, gray with clay, and green with moss.  
A brown potion turns purple with ash, red with clay, and white with moss.  
A gold potion turns brown with ash, blue with clay, and green with moss.  
The potion starts out brown. You stir in, one at a time: clay.  
What color is the potion at the end?

**Answer:** **red** · **Hidden trajectory:** brown → red

**gemma-4-31B-it:** ✅ top 5: `red`, `Red`, `红`, `purple`, `紅`
---

![brew-d1-05](brew-d1-05.png)

A potion changes color each time an ingredient is stirred in. The rules:  
A white potion turns blue with ash, black with bark, and gray with moss.  
A green potion turns red with ash, black with bark, and white with moss.  
A pink potion turns green with ash, green with bark, and green with moss.  
A black potion turns red with ash, white with bark, and purple with moss.  
A brown potion turns white with ash, black with bark, and pink with moss.  
A purple potion turns brown with ash, white with bark, and brown with moss.  
A red potion turns white with ash, black with bark, and gray with moss.  
A blue potion turns gold with ash, purple with bark, and red with moss.  
A gold potion turns white with ash, red with bark, and gray with moss.  
A gray potion turns green with ash, red with bark, and purple with moss.  
The potion starts out brown. You stir in, one at a time: moss.  
What color is the potion at the end?

**Answer:** **pink** · **Hidden trajectory:** brown → pink

**gemma-4-31B-it:** ✅ top 5: `pink`, `Pink`, `own`, `pink`, `PINK`
---

![brew-d1-06](brew-d1-06.png)

A potion changes color each time an ingredient is stirred in. The rules:  
A purple potion turns red with bark, gold with chalk, and black with salt.  
A white potion turns gray with bark, black with chalk, and gold with salt.  
A blue potion turns gray with bark, red with chalk, and gray with salt.  
A gold potion turns red with bark, purple with chalk, and brown with salt.  
A gray potion turns purple with bark, purple with chalk, and purple with salt.  
A black potion turns purple with bark, white with chalk, and brown with salt.  
A red potion turns black with bark, purple with chalk, and gray with salt.  
A pink potion turns gray with bark, brown with chalk, and blue with salt.  
A green potion turns gray with bark, brown with chalk, and black with salt.  
A brown potion turns pink with bark, gray with chalk, and black with salt.  
The potion starts out black. You stir in, one at a time: bark.  
What color is the potion at the end?

**Answer:** **purple** · **Hidden trajectory:** black → purple

**gemma-4-31B-it:** ✅ top 5: `purple`, `own`, `purchase`, `[`, `紫色`
---

![brew-d1-07](brew-d1-07.png)

A potion changes color each time an ingredient is stirred in. The rules:  
A pink potion turns red with ash, black with clay, and purple with salt.  
A white potion turns pink with ash, black with clay, and purple with salt.  
A blue potion turns white with ash, purple with clay, and pink with salt.  
A brown potion turns red with ash, pink with clay, and purple with salt.  
A purple potion turns gold with ash, blue with clay, and black with salt.  
A gray potion turns black with ash, pink with clay, and red with salt.  
A gold potion turns pink with ash, purple with clay, and pink with salt.  
A red potion turns purple with ash, gray with clay, and gray with salt.  
A green potion turns brown with ash, white with clay, and white with salt.  
A black potion turns white with ash, brown with clay, and white with salt.  
The potion starts out brown. You stir in, one at a time: salt.  
What color is the potion at the end?

**Answer:** **purple** · **Hidden trajectory:** brown → purple

**gemma-4-31B-it:** ✅ top 5: `purple`, `own`, `[`, `Purple`, `purchase`
---

![brew-d1-08](brew-d1-08.png)

A potion changes color each time an ingredient is stirred in. The rules:  
A gold potion turns red with ash, blue with bark, and green with clay.  
A purple potion turns brown with ash, green with bark, and pink with clay.  
A brown potion turns gray with ash, purple with bark, and purple with clay.  
A gray potion turns white with ash, gold with bark, and pink with clay.  
A white potion turns gray with ash, blue with bark, and red with clay.  
A green potion turns gray with ash, blue with bark, and brown with clay.  
A black potion turns brown with ash, white with bark, and gray with clay.  
A pink potion turns gray with ash, black with bark, and green with clay.  
A blue potion turns gray with ash, purple with bark, and purple with clay.  
A red potion turns green with ash, purple with bark, and brown with clay.  
The potion starts out green. You stir in, one at a time: clay.  
What color is the potion at the end?

**Answer:** **brown** · **Hidden trajectory:** green → brown

**gemma-4-31B-it:** ✅ top 5: `brown`, `purple`, `own`, `blue`, `brown`
---

![brew-d1-09](brew-d1-09.png)

A potion changes color each time an ingredient is stirred in. The rules:  
A gray potion turns pink with ash, blue with chalk, and white with salt.  
A brown potion turns black with ash, purple with chalk, and green with salt.  
A pink potion turns brown with ash, gold with chalk, and green with salt.  
A green potion turns purple with ash, black with chalk, and gray with salt.  
A white potion turns brown with ash, pink with chalk, and blue with salt.  
A blue potion turns black with ash, brown with chalk, and purple with salt.  
A black potion turns white with ash, blue with chalk, and brown with salt.  
A purple potion turns white with ash, green with chalk, and gray with salt.  
A gold potion turns red with ash, white with chalk, and blue with salt.  
A red potion turns blue with ash, black with chalk, and black with salt.  
The potion starts out blue. You stir in, one at a time: salt.  
What color is the potion at the end?

**Answer:** **purple** · **Hidden trajectory:** blue → purple

**gemma-4-31B-it:** ✅ top 5: `purple`, `purchase`, `Purple`, `紫色`, `purple`
---

![brew-d1-10](brew-d1-10.png)

A potion changes color each time an ingredient is stirred in. The rules:  
A purple potion turns brown with clay, white with moss, and gray with salt.  
A blue potion turns purple with clay, black with moss, and gray with salt.  
A gray potion turns black with clay, white with moss, and green with salt.  
A white potion turns gold with clay, green with moss, and purple with salt.  
A green potion turns purple with clay, white with moss, and pink with salt.  
A pink potion turns gold with clay, red with moss, and gold with salt.  
A brown potion turns gold with clay, white with moss, and gray with salt.  
A red potion turns blue with clay, gold with moss, and gold with salt.  
A black potion turns pink with clay, purple with moss, and gold with salt.  
A gold potion turns blue with clay, pink with moss, and blue with salt.  
The potion starts out brown. You stir in, one at a time: clay.  
What color is the potion at the end?

**Answer:** **gold** · **Hidden trajectory:** brown → gold

**gemma-4-31B-it:** ✅ top 5: `gold`, `Gold`, `[`, `own`, `Answer`
---

![brew-d1-11](brew-d1-11.png)

A potion changes color each time an ingredient is stirred in. The rules:  
A gold potion turns brown with chalk, red with moss, and gray with salt.  
A black potion turns white with chalk, brown with moss, and gray with salt.  
A brown potion turns purple with chalk, black with moss, and gold with salt.  
A red potion turns white with chalk, pink with moss, and pink with salt.  
A purple potion turns red with chalk, blue with moss, and gold with salt.  
A pink potion turns gray with chalk, red with moss, and gray with salt.  
A white potion turns gold with chalk, gold with moss, and black with salt.  
A gray potion turns gold with chalk, red with moss, and brown with salt.  
A blue potion turns red with chalk, red with moss, and red with salt.  
A green potion turns blue with chalk, blue with moss, and pink with salt.  
The potion starts out pink. You stir in, one at a time: moss.  
What color is the potion at the end?

**Answer:** **red** · **Hidden trajectory:** pink → red

**gemma-4-31B-it:** ✅ top 5: `red`, `红`, `Red`, `own`, `紅`
---

![brew-d1-12](brew-d1-12.png)

A potion changes color each time an ingredient is stirred in. The rules:  
A black potion turns green with ash, white with bark, and green with moss.  
A gray potion turns black with ash, brown with bark, and brown with moss.  
A blue potion turns black with ash, black with bark, and gray with moss.  
A red potion turns purple with ash, white with bark, and gray with moss.  
A white potion turns gray with ash, black with bark, and red with moss.  
A purple potion turns gold with ash, black with bark, and white with moss.  
A gold potion turns brown with ash, white with bark, and white with moss.  
A pink potion turns brown with ash, purple with bark, and red with moss.  
A green potion turns pink with ash, purple with bark, and pink with moss.  
A brown potion turns black with ash, green with bark, and red with moss.  
The potion starts out gray. You stir in, one at a time: ash.  
What color is the potion at the end?

**Answer:** **black** · **Hidden trajectory:** gray → black

**gemma-4-31B-it:** ✅ top 5: `black`, `黑`, `own`, `Black`, `black`
---

![brew-d1-13](brew-d1-13.png)

A potion changes color each time an ingredient is stirred in. The rules:  
A pink potion turns green with chalk, purple with clay, and purple with salt.  
A green potion turns brown with chalk, brown with clay, and purple with salt.  
A red potion turns brown with chalk, green with clay, and pink with salt.  
A white potion turns brown with chalk, gray with clay, and black with salt.  
A gray potion turns black with chalk, pink with clay, and pink with salt.  
A purple potion turns gray with chalk, gold with clay, and red with salt.  
A black potion turns pink with chalk, green with clay, and pink with salt.  
A gold potion turns purple with chalk, blue with clay, and red with salt.  
A brown potion turns gold with chalk, white with clay, and red with salt.  
A blue potion turns gray with chalk, purple with clay, and gray with salt.  
The potion starts out pink. You stir in, one at a time: chalk.  
What color is the potion at the end?

**Answer:** **green** · **Hidden trajectory:** pink → green

**gemma-4-31B-it:** ✅ top 5: `green`, `own`, `grün`, `[`, `绿`
---

![brew-d1-14](brew-d1-14.png)

A potion changes color each time an ingredient is stirred in. The rules:  
A purple potion turns red with ash, red with moss, and black with salt.  
A gold potion turns gray with ash, white with moss, and black with salt.  
A blue potion turns green with ash, red with moss, and white with salt.  
A green potion turns red with ash, white with moss, and brown with salt.  
A white potion turns brown with ash, gray with moss, and brown with salt.  
A black potion turns green with ash, gold with moss, and purple with salt.  
A red potion turns brown with ash, gray with moss, and brown with salt.  
A pink potion turns brown with ash, red with moss, and white with salt.  
A brown potion turns green with ash, gold with moss, and black with salt.  
A gray potion turns blue with ash, green with moss, and gold with salt.  
The potion starts out pink. You stir in, one at a time: moss.  
What color is the potion at the end?

**Answer:** **red** · **Hidden trajectory:** pink → red

**gemma-4-31B-it:** ✅ top 5: `red`, `红`, `Red`, `own`, `[`
---

![brew-d1-15](brew-d1-15.png)

A potion changes color each time an ingredient is stirred in. The rules:  
A pink potion turns purple with ash, blue with bark, and purple with clay.  
A brown potion turns red with ash, black with bark, and white with clay.  
A blue potion turns green with ash, gray with bark, and gray with clay.  
A green potion turns black with ash, blue with bark, and blue with clay.  
A gold potion turns white with ash, green with bark, and blue with clay.  
A black potion turns green with ash, gray with bark, and brown with clay.  
A red potion turns blue with ash, pink with bark, and gold with clay.  
A white potion turns gold with ash, gray with bark, and brown with clay.  
A purple potion turns green with ash, pink with bark, and brown with clay.  
A gray potion turns blue with ash, red with bark, and gold with clay.  
The potion starts out blue. You stir in, one at a time: bark.  
What color is the potion at the end?

**Answer:** **gray** · **Hidden trajectory:** blue → gray

**gemma-4-31B-it:** ✅ top 5: `gray`, `grey`, `Gray`, `GRAY`, `gray`
---

![brew-d1-16](brew-d1-16.png)

A potion changes color each time an ingredient is stirred in. The rules:  
A black potion turns blue with ash, pink with bark, and white with chalk.  
A red potion turns gray with ash, green with bark, and purple with chalk.  
A gold potion turns pink with ash, gray with bark, and red with chalk.  
A brown potion turns white with ash, white with bark, and gray with chalk.  
A white potion turns green with ash, gray with bark, and red with chalk.  
A green potion turns blue with ash, pink with bark, and purple with chalk.  
A gray potion turns purple with ash, pink with bark, and blue with chalk.  
A pink potion turns gray with ash, black with bark, and white with chalk.  
A blue potion turns brown with ash, gold with bark, and pink with chalk.  
A purple potion turns white with ash, gray with bark, and brown with chalk.  
The potion starts out black. You stir in, one at a time: bark.  
What color is the potion at the end?

**Answer:** **pink** · **Hidden trajectory:** black → pink

**gemma-4-31B-it:** ✅ top 5: `pink`, `own`, `Pink`, `PINK`, `pink`
---

![brew-d1-17](brew-d1-17.png)

A potion changes color each time an ingredient is stirred in. The rules:  
A blue potion turns red with bark, gray with chalk, and white with moss.  
A pink potion turns purple with bark, purple with chalk, and white with moss.  
A white potion turns blue with bark, blue with chalk, and blue with moss.  
A brown potion turns black with bark, blue with chalk, and purple with moss.  
A gold potion turns blue with bark, red with chalk, and gray with moss.  
A gray potion turns pink with bark, green with chalk, and blue with moss.  
A black potion turns gray with bark, green with chalk, and gold with moss.  
A green potion turns red with bark, pink with chalk, and black with moss.  
A purple potion turns gold with bark, gold with chalk, and red with moss.  
A red potion turns blue with bark, black with chalk, and pink with moss.  
The potion starts out white. You stir in, one at a time: chalk.  
What color is the potion at the end?

**Answer:** **blue** · **Hidden trajectory:** white → blue

**gemma-4-31B-it:** ✅ top 5: `blue`, `Blue`, `bleue`, `biru`, `own`
---

![brew-d1-18](brew-d1-18.png)

A potion changes color each time an ingredient is stirred in. The rules:  
A white potion turns red with chalk, black with clay, and gold with moss.  
A purple potion turns brown with chalk, brown with clay, and green with moss.  
A brown potion turns purple with chalk, white with clay, and green with moss.  
A blue potion turns green with chalk, brown with clay, and pink with moss.  
A red potion turns brown with chalk, blue with clay, and green with moss.  
A gray potion turns red with chalk, white with clay, and brown with moss.  
A gold potion turns brown with chalk, white with clay, and purple with moss.  
A green potion turns black with chalk, gold with clay, and blue with moss.  
A black potion turns purple with chalk, brown with clay, and purple with moss.  
A pink potion turns black with chalk, blue with clay, and gold with moss.  
The potion starts out pink. You stir in, one at a time: chalk.  
What color is the potion at the end?

**Answer:** **black** · **Hidden trajectory:** pink → black

**gemma-4-31B-it:** ✅ top 5: `black`, `黑`, `own`, `[`, `黒`
---

![brew-d1-19](brew-d1-19.png)

A potion changes color each time an ingredient is stirred in. The rules:  
A blue potion turns gray with bark, green with moss, and gold with salt.  
A pink potion turns green with bark, blue with moss, and blue with salt.  
A black potion turns green with bark, purple with moss, and brown with salt.  
A gold potion turns green with bark, pink with moss, and gray with salt.  
A brown potion turns black with bark, gray with moss, and black with salt.  
A white potion turns gray with bark, black with moss, and pink with salt.  
A gray potion turns pink with bark, white with moss, and brown with salt.  
A purple potion turns white with bark, brown with moss, and brown with salt.  
A green potion turns brown with bark, blue with moss, and white with salt.  
A red potion turns blue with bark, black with moss, and gold with salt.  
The potion starts out white. You stir in, one at a time: salt.  
What color is the potion at the end?

**Answer:** **pink** · **Hidden trajectory:** white → pink

**gemma-4-31B-it:** ✅ top 5: `pink`, `own`, `Pink`, `pink`, `PINK`
---

![brew-d2-01](brew-d2-01.png)

A potion changes color each time an ingredient is stirred in. The rules:  
A purple potion turns gray with ash, gray with bark, and pink with chalk.  
A green potion turns black with ash, brown with bark, and black with chalk.  
A blue potion turns pink with ash, purple with bark, and gold with chalk.  
A red potion turns green with ash, gray with bark, and pink with chalk.  
A brown potion turns purple with ash, green with bark, and red with chalk.  
A black potion turns gold with ash, blue with bark, and red with chalk.  
A gold potion turns gray with ash, white with bark, and gray with chalk.  
A gray potion turns red with ash, green with bark, and pink with chalk.  
A pink potion turns purple with ash, white with bark, and black with chalk.  
A white potion turns gold with ash, blue with bark, and black with chalk.  
The potion starts out brown. You stir in, one at a time: bark, then chalk.  
What color is the potion at the end?

**Answer:** **black** · **Hidden trajectory:** brown → green → black

**gemma-4-31B-it:** ✅ top 5: `black`, `red`, `pink`, `purple`, `blue`
---

![brew-d2-02](brew-d2-02.png)

A potion changes color each time an ingredient is stirred in. The rules:  
A brown potion turns green with bark, green with chalk, and black with salt.  
A black potion turns brown with bark, white with chalk, and pink with salt.  
A gray potion turns blue with bark, white with chalk, and pink with salt.  
A green potion turns pink with bark, brown with chalk, and black with salt.  
A gold potion turns purple with bark, black with chalk, and purple with salt.  
A white potion turns purple with bark, gold with chalk, and blue with salt.  
A purple potion turns gray with bark, white with chalk, and white with salt.  
A blue potion turns black with bark, white with chalk, and green with salt.  
A pink potion turns purple with bark, purple with chalk, and white with salt.  
A red potion turns purple with bark, gold with chalk, and blue with salt.  
The potion starts out green. You stir in, one at a time: chalk, then salt.  
What color is the potion at the end?

**Answer:** **black** · **Hidden trajectory:** green → brown → black

**gemma-4-31B-it:** ✅ top 5: `black`, `黑`, `blue`, `own`, `[`
---

![brew-d2-03](brew-d2-03.png)

A potion changes color each time an ingredient is stirred in. The rules:  
A purple potion turns black with ash, black with chalk, and black with salt.  
A brown potion turns pink with ash, red with chalk, and white with salt.  
A blue potion turns black with ash, white with chalk, and white with salt.  
A black potion turns pink with ash, white with chalk, and brown with salt.  
A gold potion turns pink with ash, brown with chalk, and black with salt.  
A white potion turns brown with ash, pink with chalk, and green with salt.  
A gray potion turns purple with ash, white with chalk, and black with salt.  
A pink potion turns white with ash, gray with chalk, and white with salt.  
A red potion turns gold with ash, pink with chalk, and gray with salt.  
A green potion turns gray with ash, blue with chalk, and blue with salt.  
The potion starts out brown. You stir in, one at a time: chalk, then ash.  
What color is the potion at the end?

**Answer:** **gold** · **Hidden trajectory:** brown → red → gold

**gemma-4-31B-it:** ✅ top 5: `gold`, `pink`, `Gold`, `purple`, `red`
---

![brew-d2-05](brew-d2-05.png)

A potion changes color each time an ingredient is stirred in. The rules:  
A blue potion turns gray with ash, red with clay, and black with salt.  
A white potion turns purple with ash, gold with clay, and red with salt.  
A brown potion turns pink with ash, blue with clay, and gold with salt.  
A green potion turns blue with ash, gray with clay, and gray with salt.  
A gray potion turns black with ash, brown with clay, and purple with salt.  
A gold potion turns green with ash, black with clay, and purple with salt.  
A pink potion turns gold with ash, gray with clay, and white with salt.  
A black potion turns green with ash, gray with clay, and purple with salt.  
A purple potion turns red with ash, brown with clay, and brown with salt.  
A red potion turns brown with ash, purple with clay, and gray with salt.  
The potion starts out white. You stir in, one at a time: clay, then clay.  
What color is the potion at the end?

**Answer:** **black** · **Hidden trajectory:** white → gold → black

**gemma-4-31B-it:** ✅ top 5: `black`, `gray`, `gold`, `purple`, `brown`
---

![brew-d2-06](brew-d2-06.png)

A potion changes color each time an ingredient is stirred in. The rules:  
A white potion turns pink with bark, green with moss, and purple with salt.  
A black potion turns blue with bark, red with moss, and gold with salt.  
A pink potion turns gold with bark, red with moss, and gold with salt.  
A purple potion turns blue with bark, pink with moss, and gold with salt.  
A brown potion turns white with bark, pink with moss, and red with salt.  
A gray potion turns brown with bark, blue with moss, and brown with salt.  
A blue potion turns gray with bark, pink with moss, and black with salt.  
A red potion turns purple with bark, brown with moss, and green with salt.  
A gold potion turns purple with bark, red with moss, and pink with salt.  
A green potion turns gray with bark, gold with moss, and gold with salt.  
The potion starts out purple. You stir in, one at a time: salt, then moss.  
What color is the potion at the end?

**Answer:** **red** · **Hidden trajectory:** purple → gold → red

**gemma-4-31B-it:** ✅ top 5: `red`, `gold`, `Red`, `红`, `pink`
---

![brew-d2-07](brew-d2-07.png)

A potion changes color each time an ingredient is stirred in. The rules:  
A brown potion turns white with ash, pink with bark, and purple with chalk.  
A purple potion turns black with ash, green with bark, and black with chalk.  
A pink potion turns red with ash, gold with bark, and brown with chalk.  
A blue potion turns white with ash, gray with bark, and brown with chalk.  
A green potion turns gold with ash, black with bark, and white with chalk.  
A gray potion turns white with ash, gold with bark, and pink with chalk.  
A red potion turns pink with ash, gray with bark, and purple with chalk.  
A gold potion turns gray with ash, red with bark, and blue with chalk.  
A white potion turns gold with ash, pink with bark, and gold with chalk.  
A black potion turns pink with ash, brown with bark, and blue with chalk.  
The potion starts out blue. You stir in, one at a time: bark, then ash.  
What color is the potion at the end?

**Answer:** **white** · **Hidden trajectory:** blue → gray → white

**gemma-4-31B-it:** ✅ top 5: `white`, `pink`, `gold`, `gray`, `black`
---

![brew-d2-09](brew-d2-09.png)

A potion changes color each time an ingredient is stirred in. The rules:  
A purple potion turns black with ash, brown with moss, and brown with salt.  
A red potion turns black with ash, black with moss, and gold with salt.  
A black potion turns brown with ash, red with moss, and gray with salt.  
A gray potion turns blue with ash, green with moss, and black with salt.  
A blue potion turns black with ash, purple with moss, and gold with salt.  
A gold potion turns pink with ash, purple with moss, and blue with salt.  
A green potion turns pink with ash, gray with moss, and gold with salt.  
A white potion turns gray with ash, red with moss, and red with salt.  
A pink potion turns blue with ash, green with moss, and red with salt.  
A brown potion turns purple with ash, green with moss, and green with salt.  
The potion starts out pink. You stir in, one at a time: moss, then moss.  
What color is the potion at the end?

**Answer:** **gray** · **Hidden trajectory:** pink → green → gray

**gemma-4-31B-it:** ✅ top 5: `gray`, `grey`, `red`, `Gray`, `blue`
---

![brew-d2-10](brew-d2-10.png)

A potion changes color each time an ingredient is stirred in. The rules:  
A blue potion turns pink with ash, gold with bark, and purple with salt.  
A brown potion turns red with ash, pink with bark, and purple with salt.  
A gray potion turns white with ash, green with bark, and white with salt.  
A purple potion turns white with ash, pink with bark, and green with salt.  
A gold potion turns green with ash, red with bark, and purple with salt.  
A white potion turns brown with ash, purple with bark, and purple with salt.  
A red potion turns gold with ash, brown with bark, and pink with salt.  
A green potion turns gray with ash, gray with bark, and black with salt.  
A pink potion turns green with ash, red with bark, and gold with salt.  
A black potion turns green with ash, red with bark, and brown with salt.  
The potion starts out pink. You stir in, one at a time: salt, then ash.  
What color is the potion at the end?

**Answer:** **green** · **Hidden trajectory:** pink → gold → green

**gemma-4-31B-it:** ✅ top 5: `green`, `gray`, `purple`, `grey`, `red`
---

![brew-d2-11](brew-d2-11.png)

A potion changes color each time an ingredient is stirred in. The rules:  
A gold potion turns blue with ash, red with bark, and green with chalk.  
A blue potion turns red with ash, gray with bark, and gray with chalk.  
A green potion turns gray with ash, gray with bark, and gray with chalk.  
A pink potion turns red with ash, brown with bark, and brown with chalk.  
A white potion turns black with ash, gold with bark, and pink with chalk.  
A brown potion turns gold with ash, black with bark, and white with chalk.  
A gray potion turns red with ash, red with bark, and brown with chalk.  
A black potion turns brown with ash, blue with bark, and pink with chalk.  
A red potion turns purple with ash, blue with bark, and pink with chalk.  
A purple potion turns pink with ash, red with bark, and gold with chalk.  
The potion starts out gray. You stir in, one at a time: chalk, then ash.  
What color is the potion at the end?

**Answer:** **gold** · **Hidden trajectory:** gray → brown → gold

**gemma-4-31B-it:** ✅ top 5: `gold`, `red`, `Gold`, `blue`, `black`
---

![brew-d2-12](brew-d2-12.png)

A potion changes color each time an ingredient is stirred in. The rules:  
A gray potion turns purple with ash, brown with clay, and black with moss.  
A red potion turns white with ash, green with clay, and gold with moss.  
A purple potion turns blue with ash, black with clay, and brown with moss.  
A gold potion turns red with ash, red with clay, and gray with moss.  
A blue potion turns pink with ash, gray with clay, and white with moss.  
A black potion turns blue with ash, gold with clay, and purple with moss.  
A green potion turns pink with ash, brown with clay, and blue with moss.  
A white potion turns brown with ash, purple with clay, and black with moss.  
A brown potion turns gold with ash, gray with clay, and red with moss.  
A pink potion turns brown with ash, brown with clay, and green with moss.  
The potion starts out blue. You stir in, one at a time: clay, then ash.  
What color is the potion at the end?

**Answer:** **purple** · **Hidden trajectory:** blue → gray → purple

**gemma-4-31B-it:** ✅ top 5: `purple`, `pink`, `brown`, `blue`, `red`
---

![brew-d2-13](brew-d2-13.png)

A potion changes color each time an ingredient is stirred in. The rules:  
A red potion turns black with chalk, black with clay, and purple with moss.  
A gold potion turns green with chalk, white with clay, and green with moss.  
A gray potion turns brown with chalk, green with clay, and black with moss.  
A green potion turns gray with chalk, red with clay, and gray with moss.  
A black potion turns pink with chalk, blue with clay, and blue with moss.  
A pink potion turns blue with chalk, black with clay, and green with moss.  
A white potion turns pink with chalk, purple with clay, and blue with moss.  
A brown potion turns green with chalk, gold with clay, and gray with moss.  
A blue potion turns pink with chalk, purple with clay, and brown with moss.  
A purple potion turns white with chalk, brown with clay, and black with moss.  
The potion starts out white. You stir in, one at a time: chalk, then moss.  
What color is the potion at the end?

**Answer:** **green** · **Hidden trajectory:** white → pink → green

**gemma-4-31B-it:** ✅ top 5: `green`, `blue`, `gray`, `black`, `pink`
---

![brew-d2-15](brew-d2-15.png)

A potion changes color each time an ingredient is stirred in. The rules:  
A white potion turns purple with ash, pink with chalk, and purple with salt.  
A green potion turns red with ash, white with chalk, and purple with salt.  
A blue potion turns brown with ash, black with chalk, and purple with salt.  
A pink potion turns green with ash, blue with chalk, and black with salt.  
A gray potion turns green with ash, black with chalk, and blue with salt.  
A brown potion turns red with ash, red with chalk, and white with salt.  
A red potion turns gold with ash, blue with chalk, and gold with salt.  
A gold potion turns purple with ash, red with chalk, and white with salt.  
A purple potion turns red with ash, red with chalk, and pink with salt.  
A black potion turns blue with ash, gold with chalk, and gray with salt.  
The potion starts out green. You stir in, one at a time: ash, then salt.  
What color is the potion at the end?

**Answer:** **gold** · **Hidden trajectory:** green → red → gold

**gemma-4-31B-it:** ✅ top 5: `gold`, `pink`, `purple`, `Gold`, `red`
---

![brew-d2-16](brew-d2-16.png)

A potion changes color each time an ingredient is stirred in. The rules:  
A white potion turns gray with ash, black with bark, and pink with clay.  
A black potion turns pink with ash, brown with bark, and gold with clay.  
A gold potion turns blue with ash, red with bark, and green with clay.  
A gray potion turns blue with ash, red with bark, and brown with clay.  
A green potion turns white with ash, white with bark, and purple with clay.  
A blue potion turns black with ash, pink with bark, and brown with clay.  
A brown potion turns green with ash, gold with bark, and pink with clay.  
A pink potion turns gold with ash, purple with bark, and blue with clay.  
A purple potion turns green with ash, gray with bark, and gold with clay.  
A red potion turns brown with ash, white with bark, and pink with clay.  
The potion starts out brown. You stir in, one at a time: clay, then bark.  
What color is the potion at the end?

**Answer:** **purple** · **Hidden trajectory:** brown → pink → purple

**gemma-4-31B-it:** ✅ top 5: `purple`, `gray`, `pink`, `gold`, `red`
---

![brew-d2-17](brew-d2-17.png)

A potion changes color each time an ingredient is stirred in. The rules:  
A black potion turns pink with ash, gray with chalk, and green with salt.  
A gray potion turns gold with ash, brown with chalk, and pink with salt.  
A red potion turns pink with ash, gray with chalk, and green with salt.  
A brown potion turns green with ash, black with chalk, and red with salt.  
A white potion turns blue with ash, red with chalk, and green with salt.  
A pink potion turns gold with ash, purple with chalk, and black with salt.  
A purple potion turns white with ash, black with chalk, and red with salt.  
A gold potion turns brown with ash, blue with chalk, and green with salt.  
A green potion turns pink with ash, gold with chalk, and gray with salt.  
A blue potion turns red with ash, gray with chalk, and pink with salt.  
The potion starts out gold. You stir in, one at a time: chalk, then salt.  
What color is the potion at the end?

**Answer:** **pink** · **Hidden trajectory:** gold → blue → pink

**gemma-4-31B-it:** ✅ top 5: `pink`, `green`, `gray`, `black`, `blue`
---

![brew-d2-18](brew-d2-18.png)

A potion changes color each time an ingredient is stirred in. The rules:  
A gray potion turns green with bark, gold with clay, and red with salt.  
A white potion turns red with bark, gray with clay, and blue with salt.  
A pink potion turns brown with bark, purple with clay, and gold with salt.  
A brown potion turns purple with bark, green with clay, and green with salt.  
A red potion turns purple with bark, pink with clay, and brown with salt.  
A purple potion turns brown with bark, black with clay, and white with salt.  
A blue potion turns brown with bark, gray with clay, and red with salt.  
A gold potion turns brown with bark, white with clay, and purple with salt.  
A black potion turns pink with bark, brown with clay, and purple with salt.  
A green potion turns purple with bark, red with clay, and white with salt.  
The potion starts out gray. You stir in, one at a time: bark, then bark.  
What color is the potion at the end?

**Answer:** **purple** · **Hidden trajectory:** gray → green → purple

**gemma-4-31B-it:** ✅ top 5: `purple`, `brown`, `black`, `pink`, `Answer`
---

![brew-d2-19](brew-d2-19.png)

A potion changes color each time an ingredient is stirred in. The rules:  
A pink potion turns gray with bark, brown with chalk, and blue with clay.  
A red potion turns blue with bark, black with chalk, and purple with clay.  
A brown potion turns gray with bark, red with chalk, and gold with clay.  
A blue potion turns white with bark, red with chalk, and purple with clay.  
A white potion turns gray with bark, pink with chalk, and gold with clay.  
A gold potion turns green with bark, brown with chalk, and pink with clay.  
A black potion turns white with bark, green with chalk, and gold with clay.  
A green potion turns gold with bark, gray with chalk, and black with clay.  
A purple potion turns red with bark, gray with chalk, and gray with clay.  
A gray potion turns white with bark, red with chalk, and white with clay.  
The potion starts out black. You stir in, one at a time: chalk, then chalk.  
What color is the potion at the end?

**Answer:** **gray** · **Hidden trajectory:** black → green → gray

**gemma-4-31B-it:** ✅ top 5: `gray`, `red`, `grey`, `gold`, `black`
---

![brew-d3-11](brew-d3-11.png)

A potion changes color each time an ingredient is stirred in. The rules:  
A red potion turns pink with ash, gold with bark, and pink with clay.  
A gray potion turns white with ash, brown with bark, and green with clay.  
A gold potion turns white with ash, blue with bark, and white with clay.  
A black potion turns gray with ash, gold with bark, and gold with clay.  
A white potion turns gold with ash, brown with bark, and brown with clay.  
A brown potion turns red with ash, blue with bark, and pink with clay.  
A green potion turns blue with ash, white with bark, and pink with clay.  
A purple potion turns gold with ash, blue with bark, and brown with clay.  
A blue potion turns green with ash, red with bark, and pink with clay.  
A pink potion turns gray with ash, purple with bark, and gray with clay.  
The potion starts out red. You stir in, one at a time: clay, then bark, then clay.  
What color is the potion at the end?

**Answer:** **brown** · **Hidden trajectory:** red → pink → purple → brown

**gemma-4-31B-it:** ✅ top 5: `brown`, `purple`, `pink`, `gold`, `blue`

## Answered wrong (23)

---

![brew-d2-00](brew-d2-00.png)

A potion changes color each time an ingredient is stirred in. The rules:  
A purple potion turns gold with ash, white with bark, and green with salt.  
A gold potion turns gray with ash, brown with bark, and red with salt.  
A black potion turns brown with ash, purple with bark, and purple with salt.  
A pink potion turns white with ash, gold with bark, and green with salt.  
A red potion turns gold with ash, gold with bark, and green with salt.  
A blue potion turns gray with ash, gold with bark, and brown with salt.  
A white potion turns blue with ash, gray with bark, and gray with salt.  
A green potion turns pink with ash, purple with bark, and white with salt.  
A brown potion turns white with ash, white with bark, and red with salt.  
A gray potion turns purple with ash, green with bark, and brown with salt.  
The potion starts out brown. You stir in, one at a time: salt, then bark.  
What color is the potion at the end?

**Answer:** **gold** · **Hidden trajectory:** brown → red → gold

**gemma-4-31B-it:** ❌ top 5: `purple`, `gold`, `gray`, `brown`, `white`
---

![brew-d2-04](brew-d2-04.png)

A potion changes color each time an ingredient is stirred in. The rules:  
A blue potion turns brown with bark, black with chalk, and pink with moss.  
A pink potion turns black with bark, blue with chalk, and brown with moss.  
A white potion turns purple with bark, purple with chalk, and gold with moss.  
A black potion turns gray with bark, pink with chalk, and green with moss.  
A green potion turns purple with bark, black with chalk, and pink with moss.  
A brown potion turns green with bark, red with chalk, and blue with moss.  
A purple potion turns white with bark, green with chalk, and brown with moss.  
A red potion turns black with bark, gold with chalk, and pink with moss.  
A gold potion turns black with bark, purple with chalk, and blue with moss.  
A gray potion turns pink with bark, white with chalk, and gold with moss.  
The potion starts out purple. You stir in, one at a time: chalk, then moss.  
What color is the potion at the end?

**Answer:** **pink** · **Hidden trajectory:** purple → green → pink

**gemma-4-31B-it:** ❌ top 5: `brown`, `blue`, `purple`, `gray`, `gold`
---

![brew-d2-08](brew-d2-08.png)

A potion changes color each time an ingredient is stirred in. The rules:  
A brown potion turns gray with ash, green with bark, and green with clay.  
A red potion turns gray with ash, blue with bark, and blue with clay.  
A pink potion turns black with ash, red with bark, and white with clay.  
A blue potion turns gold with ash, green with bark, and red with clay.  
A black potion turns blue with ash, brown with bark, and red with clay.  
A white potion turns green with ash, red with bark, and pink with clay.  
A gray potion turns white with ash, pink with bark, and gold with clay.  
A green potion turns gray with ash, black with bark, and black with clay.  
A gold potion turns brown with ash, gray with bark, and brown with clay.  
A purple potion turns gold with ash, red with bark, and pink with clay.  
The potion starts out green. You stir in, one at a time: clay, then ash.  
What color is the potion at the end?

**Answer:** **blue** · **Hidden trajectory:** green → black → blue

**gemma-4-31B-it:** ❌ top 5: `gray`, `blue`, `grey`, `red`, `black`
---

![brew-d2-14](brew-d2-14.png)

A potion changes color each time an ingredient is stirred in. The rules:  
A red potion turns brown with bark, brown with clay, and black with moss.  
A white potion turns gray with bark, brown with clay, and blue with moss.  
A purple potion turns white with bark, blue with clay, and brown with moss.  
A blue potion turns gold with bark, red with clay, and gray with moss.  
A green potion turns pink with bark, red with clay, and gray with moss.  
A brown potion turns pink with bark, blue with clay, and black with moss.  
A gold potion turns white with bark, blue with clay, and blue with moss.  
A pink potion turns blue with bark, blue with clay, and red with moss.  
A black potion turns gray with bark, green with clay, and gold with moss.  
A gray potion turns blue with bark, brown with clay, and red with moss.  
The potion starts out black. You stir in, one at a time: moss, then moss.  
What color is the potion at the end?

**Answer:** **blue** · **Hidden trajectory:** black → gold → blue

**gemma-4-31B-it:** ❌ top 5: `gold`, `red`, `blue`, `gray`, `black`
---

![brew-d3-00](brew-d3-00.png)

A potion changes color each time an ingredient is stirred in. The rules:  
A purple potion turns black with ash, red with bark, and pink with clay.  
A blue potion turns gold with ash, pink with bark, and gold with clay.  
A white potion turns brown with ash, gold with bark, and gray with clay.  
A pink potion turns black with ash, gray with bark, and white with clay.  
A gray potion turns green with ash, gold with bark, and gold with clay.  
A brown potion turns green with ash, gray with bark, and pink with clay.  
A green potion turns purple with ash, blue with bark, and white with clay.  
A gold potion turns red with ash, gray with bark, and pink with clay.  
A red potion turns white with ash, green with bark, and purple with clay.  
A black potion turns gray with ash, white with bark, and brown with clay.  
The potion starts out green. You stir in, one at a time: bark, then ash, then clay.  
What color is the potion at the end?

**Answer:** **pink** · **Hidden trajectory:** green → blue → gold → pink

**gemma-4-31B-it:** ❌ top 5: `gold`, `pink`, `white`, `purple`, `gray`
---

![brew-d3-01](brew-d3-01.png)

A potion changes color each time an ingredient is stirred in. The rules:  
A black potion turns red with ash, blue with chalk, and gray with clay.  
A blue potion turns red with ash, white with chalk, and purple with clay.  
A purple potion turns white with ash, pink with chalk, and pink with clay.  
A gray potion turns purple with ash, pink with chalk, and gold with clay.  
A green potion turns red with ash, red with chalk, and red with clay.  
A brown potion turns blue with ash, red with chalk, and gray with clay.  
A red potion turns gold with ash, gold with chalk, and white with clay.  
A gold potion turns brown with ash, purple with chalk, and green with clay.  
A white potion turns brown with ash, gray with chalk, and gold with clay.  
A pink potion turns gray with ash, gray with chalk, and blue with clay.  
The potion starts out green. You stir in, one at a time: ash, then ash, then ash.  
What color is the potion at the end?

**Answer:** **brown** · **Hidden trajectory:** green → red → gold → brown

**gemma-4-31B-it:** ❌ top 5: `gold`, `brown`, `red`, `Gold`, `purple`
---

![brew-d3-02](brew-d3-02.png)

A potion changes color each time an ingredient is stirred in. The rules:  
A green potion turns gray with bark, white with chalk, and gray with clay.  
A white potion turns purple with bark, red with chalk, and gray with clay.  
A gold potion turns blue with bark, blue with chalk, and white with clay.  
A red potion turns brown with bark, purple with chalk, and white with clay.  
A blue potion turns white with bark, gray with chalk, and black with clay.  
A pink potion turns green with bark, white with chalk, and red with clay.  
A gray potion turns purple with bark, blue with chalk, and green with clay.  
A brown potion turns white with bark, gold with chalk, and gray with clay.  
A purple potion turns brown with bark, brown with chalk, and white with clay.  
A black potion turns purple with bark, gray with chalk, and white with clay.  
The potion starts out blue. You stir in, one at a time: clay, then chalk, then bark.  
What color is the potion at the end?

**Answer:** **purple** · **Hidden trajectory:** blue → black → gray → purple

**gemma-4-31B-it:** ❌ top 5: `gray`, `purple`, `grey`, `red`, `black`
---

![brew-d3-03](brew-d3-03.png)

A potion changes color each time an ingredient is stirred in. The rules:  
A gray potion turns red with ash, green with bark, and purple with clay.  
A green potion turns red with ash, pink with bark, and brown with clay.  
A purple potion turns blue with ash, blue with bark, and black with clay.  
A white potion turns gray with ash, brown with bark, and gold with clay.  
A black potion turns blue with ash, white with bark, and brown with clay.  
A brown potion turns red with ash, purple with bark, and blue with clay.  
A blue potion turns black with ash, white with bark, and white with clay.  
A gold potion turns purple with ash, purple with bark, and red with clay.  
A red potion turns blue with ash, gold with bark, and gold with clay.  
A pink potion turns purple with ash, brown with bark, and blue with clay.  
The potion starts out green. You stir in, one at a time: ash, then bark, then ash.  
What color is the potion at the end?

**Answer:** **purple** · **Hidden trajectory:** green → red → gold → purple

**gemma-4-31B-it:** ❌ top 5: `black`, `blue`, `purple`, `white`, `gold`
---

![brew-d3-04](brew-d3-04.png)

A potion changes color each time an ingredient is stirred in. The rules:  
A white potion turns green with ash, green with clay, and green with salt.  
A red potion turns blue with ash, gray with clay, and brown with salt.  
A green potion turns blue with ash, white with clay, and purple with salt.  
A gray potion turns blue with ash, blue with clay, and brown with salt.  
A purple potion turns brown with ash, brown with clay, and white with salt.  
A blue potion turns pink with ash, brown with clay, and purple with salt.  
A black potion turns red with ash, pink with clay, and blue with salt.  
A gold potion turns black with ash, gray with clay, and purple with salt.  
A pink potion turns red with ash, purple with clay, and green with salt.  
A brown potion turns white with ash, pink with clay, and pink with salt.  
The potion starts out gold. You stir in, one at a time: salt, then salt, then clay.  
What color is the potion at the end?

**Answer:** **green** · **Hidden trajectory:** gold → purple → white → green

**gemma-4-31B-it:** ❌ top 5: `brown`, `pink`, `purple`, `gray`, `white`
---

![brew-d3-05](brew-d3-05.png)

A potion changes color each time an ingredient is stirred in. The rules:  
A white potion turns gray with bark, green with clay, and gold with salt.  
A blue potion turns gray with bark, gold with clay, and brown with salt.  
A pink potion turns brown with bark, red with clay, and green with salt.  
A gold potion turns pink with bark, purple with clay, and black with salt.  
A black potion turns pink with bark, gray with clay, and green with salt.  
A red potion turns purple with bark, pink with clay, and purple with salt.  
A green potion turns purple with bark, red with clay, and purple with salt.  
A brown potion turns red with bark, black with clay, and red with salt.  
A purple potion turns red with bark, gold with clay, and blue with salt.  
A gray potion turns red with bark, black with clay, and brown with salt.  
The potion starts out black. You stir in, one at a time: bark, then salt, then clay.  
What color is the potion at the end?

**Answer:** **red** · **Hidden trajectory:** black → pink → green → red

**gemma-4-31B-it:** ❌ top 5: `purple`, `gold`, `red`, `blue`, `black`
---

![brew-d3-06](brew-d3-06.png)

A potion changes color each time an ingredient is stirred in. The rules:  
A brown potion turns gray with clay, green with moss, and gold with salt.  
A pink potion turns white with clay, gold with moss, and purple with salt.  
A gold potion turns brown with clay, black with moss, and brown with salt.  
A purple potion turns gray with clay, gold with moss, and gray with salt.  
A blue potion turns gray with clay, gold with moss, and gray with salt.  
A black potion turns gold with clay, white with moss, and blue with salt.  
A green potion turns brown with clay, black with moss, and black with salt.  
A red potion turns pink with clay, purple with moss, and white with salt.  
A gray potion turns gold with clay, blue with moss, and purple with salt.  
A white potion turns blue with clay, brown with moss, and black with salt.  
The potion starts out green. You stir in, one at a time: salt, then salt, then clay.  
What color is the potion at the end?

**Answer:** **gray** · **Hidden trajectory:** green → black → blue → gray

**gemma-4-31B-it:** ❌ top 5: `gold`, `brown`, `blue`, `black`, `purple`
---

![brew-d3-07](brew-d3-07.png)

A potion changes color each time an ingredient is stirred in. The rules:  
A gold potion turns purple with ash, white with chalk, and blue with salt.  
A gray potion turns white with ash, red with chalk, and blue with salt.  
A pink potion turns green with ash, blue with chalk, and brown with salt.  
A black potion turns gold with ash, blue with chalk, and pink with salt.  
A white potion turns black with ash, brown with chalk, and purple with salt.  
A green potion turns gold with ash, red with chalk, and pink with salt.  
A blue potion turns pink with ash, gold with chalk, and black with salt.  
A purple potion turns black with ash, red with chalk, and white with salt.  
A red potion turns blue with ash, brown with chalk, and brown with salt.  
A brown potion turns gray with ash, gray with chalk, and red with salt.  
The potion starts out blue. You stir in, one at a time: ash, then ash, then chalk.  
What color is the potion at the end?

**Answer:** **red** · **Hidden trajectory:** blue → pink → green → red

**gemma-4-31B-it:** ❌ top 5: `black`, `gold`, `red`, `gray`, `white`
---

![brew-d3-08](brew-d3-08.png)

A potion changes color each time an ingredient is stirred in. The rules:  
A white potion turns blue with ash, purple with chalk, and blue with clay.  
A gold potion turns red with ash, pink with chalk, and red with clay.  
A gray potion turns red with ash, pink with chalk, and black with clay.  
A black potion turns brown with ash, gray with chalk, and white with clay.  
A blue potion turns gray with ash, gray with chalk, and gray with clay.  
A green potion turns white with ash, purple with chalk, and pink with clay.  
A pink potion turns purple with ash, black with chalk, and gold with clay.  
A purple potion turns gold with ash, gray with chalk, and gold with clay.  
A brown potion turns gold with ash, white with chalk, and red with clay.  
A red potion turns blue with ash, black with chalk, and green with clay.  
The potion starts out gray. You stir in, one at a time: clay, then clay, then clay.  
What color is the potion at the end?

**Answer:** **blue** · **Hidden trajectory:** gray → black → white → blue

**gemma-4-31B-it:** ❌ top 5: `white`, `gray`, `blue`, `black`, `red`
---

![brew-d3-09](brew-d3-09.png)

A potion changes color each time an ingredient is stirred in. The rules:  
A gold potion turns black with chalk, black with clay, and white with moss.  
A brown potion turns pink with chalk, purple with clay, and white with moss.  
A red potion turns gold with chalk, gray with clay, and green with moss.  
A white potion turns gray with chalk, red with clay, and purple with moss.  
A gray potion turns blue with chalk, white with clay, and purple with moss.  
A pink potion turns green with chalk, black with clay, and blue with moss.  
A black potion turns purple with chalk, white with clay, and red with moss.  
A purple potion turns white with chalk, gold with clay, and blue with moss.  
A blue potion turns red with chalk, green with clay, and brown with moss.  
A green potion turns white with chalk, black with clay, and black with moss.  
The potion starts out brown. You stir in, one at a time: moss, then chalk, then chalk.  
What color is the potion at the end?

**Answer:** **blue** · **Hidden trajectory:** brown → white → gray → blue

**gemma-4-31B-it:** ❌ top 5: `gray`, `red`, `grey`, `blue`, `gold`
---

![brew-d3-10](brew-d3-10.png)

A potion changes color each time an ingredient is stirred in. The rules:  
A pink potion turns white with bark, red with chalk, and gold with salt.  
A green potion turns pink with bark, gold with chalk, and gray with salt.  
A blue potion turns black with bark, pink with chalk, and purple with salt.  
A gray potion turns pink with bark, brown with chalk, and purple with salt.  
A white potion turns pink with bark, purple with chalk, and gold with salt.  
A black potion turns green with bark, green with chalk, and pink with salt.  
A brown potion turns red with bark, black with chalk, and pink with salt.  
A red potion turns green with bark, white with chalk, and pink with salt.  
A purple potion turns brown with bark, green with chalk, and red with salt.  
A gold potion turns gray with bark, pink with chalk, and gray with salt.  
The potion starts out white. You stir in, one at a time: chalk, then chalk, then salt.  
What color is the potion at the end?

**Answer:** **gray** · **Hidden trajectory:** white → purple → green → gray

**gemma-4-31B-it:** ❌ top 5: `red`, `gold`, `pink`, `green`, `gray`
---

![brew-d3-12](brew-d3-12.png)

A potion changes color each time an ingredient is stirred in. The rules:  
A green potion turns gray with bark, white with chalk, and white with salt.  
A red potion turns black with bark, purple with chalk, and white with salt.  
A purple potion turns blue with bark, brown with chalk, and gray with salt.  
A gold potion turns green with bark, blue with chalk, and brown with salt.  
A brown potion turns gold with bark, gold with chalk, and purple with salt.  
A blue potion turns pink with bark, red with chalk, and red with salt.  
A pink potion turns green with bark, gray with chalk, and blue with salt.  
A gray potion turns brown with bark, blue with chalk, and purple with salt.  
A white potion turns gray with bark, brown with chalk, and green with salt.  
A black potion turns gold with bark, red with chalk, and blue with salt.  
The potion starts out gray. You stir in, one at a time: bark, then chalk, then chalk.  
What color is the potion at the end?

**Answer:** **blue** · **Hidden trajectory:** gray → brown → gold → blue

**gemma-4-31B-it:** ❌ top 5: `gold`, `brown`, `blue`, `red`, `Gold`
---

![brew-d3-13](brew-d3-13.png)

A potion changes color each time an ingredient is stirred in. The rules:  
A blue potion turns brown with bark, black with chalk, and gold with moss.  
A green potion turns pink with bark, gray with chalk, and brown with moss.  
A white potion turns black with bark, brown with chalk, and pink with moss.  
A black potion turns gray with bark, green with chalk, and gray with moss.  
A gray potion turns brown with bark, black with chalk, and gold with moss.  
A pink potion turns gray with bark, purple with chalk, and brown with moss.  
A purple potion turns green with bark, white with chalk, and green with moss.  
A gold potion turns purple with bark, pink with chalk, and green with moss.  
A red potion turns white with bark, pink with chalk, and brown with moss.  
A brown potion turns blue with bark, white with chalk, and blue with moss.  
The potion starts out black. You stir in, one at a time: bark, then bark, then chalk.  
What color is the potion at the end?

**Answer:** **white** · **Hidden trajectory:** black → gray → brown → white

**gemma-4-31B-it:** ❌ top 5: `black`, `brown`, `purple`, `white`, `blue`
---

![brew-d3-14](brew-d3-14.png)

A potion changes color each time an ingredient is stirred in. The rules:  
A gold potion turns brown with ash, pink with bark, and gray with moss.  
A purple potion turns brown with ash, brown with bark, and gray with moss.  
A black potion turns brown with ash, gray with bark, and purple with moss.  
A white potion turns gold with ash, gold with bark, and blue with moss.  
A blue potion turns gray with ash, gray with bark, and green with moss.  
A pink potion turns gray with ash, gold with bark, and white with moss.  
A gray potion turns red with ash, white with bark, and blue with moss.  
A red potion turns gold with ash, green with bark, and green with moss.  
A green potion turns black with ash, brown with bark, and brown with moss.  
A brown potion turns blue with ash, blue with bark, and red with moss.  
The potion starts out purple. You stir in, one at a time: ash, then moss, then moss.  
What color is the potion at the end?

**Answer:** **green** · **Hidden trajectory:** purple → brown → red → green

**gemma-4-31B-it:** ❌ top 5: `gray`, `purple`, `grey`, `blue`, `red`
---

![brew-d3-15](brew-d3-15.png)

A potion changes color each time an ingredient is stirred in. The rules:  
A purple potion turns blue with ash, gray with bark, and red with clay.  
A gold potion turns blue with ash, green with bark, and red with clay.  
A green potion turns gold with ash, blue with bark, and brown with clay.  
A red potion turns black with ash, purple with bark, and blue with clay.  
A blue potion turns white with ash, black with bark, and red with clay.  
A black potion turns pink with ash, brown with bark, and gray with clay.  
A white potion turns pink with ash, green with bark, and green with clay.  
A gray potion turns brown with ash, blue with bark, and white with clay.  
A pink potion turns gold with ash, brown with bark, and gray with clay.  
A brown potion turns gray with ash, red with bark, and gray with clay.  
The potion starts out white. You stir in, one at a time: bark, then clay, then bark.  
What color is the potion at the end?

**Answer:** **red** · **Hidden trajectory:** white → green → brown → red

**gemma-4-31B-it:** ❌ top 5: `purple`, `red`, `blue`, `brown`, `gray`
---

![brew-d3-16](brew-d3-16.png)

A potion changes color each time an ingredient is stirred in. The rules:  
A red potion turns gold with ash, pink with moss, and gray with salt.  
A purple potion turns pink with ash, white with moss, and white with salt.  
A pink potion turns blue with ash, purple with moss, and red with salt.  
A brown potion turns red with ash, blue with moss, and blue with salt.  
A gold potion turns red with ash, green with moss, and purple with salt.  
A green potion turns gray with ash, brown with moss, and white with salt.  
A black potion turns white with ash, blue with moss, and green with salt.  
A white potion turns black with ash, black with moss, and blue with salt.  
A gray potion turns gold with ash, purple with moss, and white with salt.  
A blue potion turns black with ash, gray with moss, and red with salt.  
The potion starts out pink. You stir in, one at a time: ash, then ash, then salt.  
What color is the potion at the end?

**Answer:** **green** · **Hidden trajectory:** pink → blue → black → green

**gemma-4-31B-it:** ❌ top 5: `red`, `gray`, `black`, `gold`, `blue`
---

![brew-d3-17](brew-d3-17.png)

A potion changes color each time an ingredient is stirred in. The rules:  
A red potion turns gold with ash, green with bark, and pink with moss.  
A black potion turns green with ash, purple with bark, and pink with moss.  
A white potion turns gray with ash, red with bark, and pink with moss.  
A pink potion turns purple with ash, red with bark, and white with moss.  
A green potion turns blue with ash, pink with bark, and brown with moss.  
A blue potion turns green with ash, white with bark, and pink with moss.  
A gray potion turns brown with ash, pink with bark, and green with moss.  
A brown potion turns white with ash, purple with bark, and purple with moss.  
A purple potion turns white with ash, black with bark, and pink with moss.  
A gold potion turns pink with ash, white with bark, and purple with moss.  
The potion starts out gold. You stir in, one at a time: bark, then ash, then moss.  
What color is the potion at the end?

**Answer:** **green** · **Hidden trajectory:** gold → white → gray → green

**gemma-4-31B-it:** ❌ top 5: `pink`, `gray`, `red`, `purple`, `grey`
---

![brew-d3-18](brew-d3-18.png)

A potion changes color each time an ingredient is stirred in. The rules:  
A white potion turns gray with ash, purple with bark, and gold with clay.  
A black potion turns gold with ash, gray with bark, and purple with clay.  
A red potion turns gray with ash, brown with bark, and pink with clay.  
A green potion turns blue with ash, blue with bark, and gray with clay.  
A blue potion turns white with ash, gold with bark, and brown with clay.  
A gray potion turns white with ash, gold with bark, and blue with clay.  
A pink potion turns gold with ash, brown with bark, and red with clay.  
A brown potion turns pink with ash, pink with bark, and green with clay.  
A purple potion turns blue with ash, white with bark, and blue with clay.  
A gold potion turns gray with ash, gray with bark, and red with clay.  
The potion starts out pink. You stir in, one at a time: clay, then bark, then clay.  
What color is the potion at the end?

**Answer:** **green** · **Hidden trajectory:** pink → red → brown → green

**gemma-4-31B-it:** ❌ top 5: `pink`, `brown`, `purple`, `red`, `gray`
---

![brew-d3-19](brew-d3-19.png)

A potion changes color each time an ingredient is stirred in. The rules:  
A gray potion turns gold with ash, brown with chalk, and brown with moss.  
A brown potion turns purple with ash, purple with chalk, and gray with moss.  
A green potion turns red with ash, red with chalk, and brown with moss.  
A white potion turns brown with ash, red with chalk, and red with moss.  
A blue potion turns brown with ash, gray with chalk, and red with moss.  
A gold potion turns purple with ash, black with chalk, and red with moss.  
A black potion turns gold with ash, purple with chalk, and gold with moss.  
A pink potion turns brown with ash, blue with chalk, and green with moss.  
A red potion turns white with ash, green with chalk, and brown with moss.  
A purple potion turns black with ash, white with chalk, and gold with moss.  
The potion starts out black. You stir in, one at a time: chalk, then chalk, then moss.  
What color is the potion at the end?

**Answer:** **red** · **Hidden trajectory:** black → purple → white → red

**gemma-4-31B-it:** ❌ top 5: `gold`, `gray`, `purple`, `black`, `red`
