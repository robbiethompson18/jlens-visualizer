# chain9: J-lens by layer and token, gemma-4-31B-it

Lens: `solarkyle/jspace-lenses/gemma-4-31b-it/lens.pt`. Rank here is rank among the 9 possible answers (1, 2, 3, 4, 5, 6, 7, 8, 9), 1 = the lens prefers it to all the others. Each item's graph shows, on top, the rank
of every tracked word at the token before the answer by layer (thin = raw, thick = EWMA with a
2-layer halflife). Below it, one heatmap per word: rank at every layer (y) and prompt token
(x), darker = higher rank. Dashed boxes outline the prompt line each step reads, in the colour of the
step it produces. A word lighting up on its own token in early layers is the token echoing itself, not
computation. Correct items first.

| depth | correct |
| --- | --- |
| 1 | 19/20 |
| 2 | 7/20 |
| 3 | 2/20 |

## Summary: median rank over correct items

![summary](summary.png)

## Answered correctly (28)

---

![chain9-d1-00](chain9-d1-00.png)

Start with the number 1 and apply the steps in order. After every step, if the number is bigger than 9, subtract 9; if it is smaller than 1, add 9.  
If it is even, halve it; if it is odd, add 6.  
What is the final number?

**Answer:** **7** · **Hidden trajectory:** 1 → 7

**gemma-4-31B-it:** ✅ top 5: `7`, `1`, `3`, `2`, `4`
---

![chain9-d1-01](chain9-d1-01.png)

Start with the number 9 and apply the steps in order. After every step, if the number is bigger than 9, subtract 9; if it is smaller than 1, add 9.  
Halve it, rounding up.  
What is the final number?

**Answer:** **5** · **Hidden trajectory:** 9 → 5

**gemma-4-31B-it:** ✅ top 5: `5`, `1`, `4`, `2`, `3`
---

![chain9-d1-02](chain9-d1-02.png)

Start with the number 7 and apply the steps in order. After every step, if the number is bigger than 9, subtract 9; if it is smaller than 1, add 9.  
If it is bigger than 5, subtract 3; otherwise double it.  
What is the final number?

**Answer:** **4** · **Hidden trajectory:** 7 → 4

**gemma-4-31B-it:** ✅ top 5: `4`, `1`, `8`, `5`, `6`
---

![chain9-d1-03](chain9-d1-03.png)

Start with the number 4 and apply the steps in order. After every step, if the number is bigger than 9, subtract 9; if it is smaller than 1, add 9.  
If it is even, halve it; if it is odd, add 8.  
What is the final number?

**Answer:** **2** · **Hidden trajectory:** 4 → 2

**gemma-4-31B-it:** ✅ top 5: `2`, `1`, `3`, `6`, `7`
---

![chain9-d1-04](chain9-d1-04.png)

Start with the number 6 and apply the steps in order. After every step, if the number is bigger than 9, subtract 9; if it is smaller than 1, add 9.  
If it is bigger than 5, subtract 2; otherwise double it.  
What is the final number?

**Answer:** **4** · **Hidden trajectory:** 6 → 4

**gemma-4-31B-it:** ✅ top 5: `4`, `1`, `8`, `6`, `5`
---

![chain9-d1-05](chain9-d1-05.png)

Start with the number 7 and apply the steps in order. After every step, if the number is bigger than 9, subtract 9; if it is smaller than 1, add 9.  
If it is bigger than 5, subtract 2; otherwise double it.  
What is the final number?

**Answer:** **5** · **Hidden trajectory:** 7 → 5

**gemma-4-31B-it:** ✅ top 5: `5`, `4`, `1`, `8`, `2`
---

![chain9-d1-07](chain9-d1-07.png)

Start with the number 2 and apply the steps in order. After every step, if the number is bigger than 9, subtract 9; if it is smaller than 1, add 9.  
If it is even, halve it; if it is odd, add 8.  
What is the final number?

**Answer:** **1** · **Hidden trajectory:** 2 → 1

**gemma-4-31B-it:** ✅ top 5: `1`, `2`, `4`, `8`, `6`
---

![chain9-d1-08](chain9-d1-08.png)

Start with the number 2 and apply the steps in order. After every step, if the number is bigger than 9, subtract 9; if it is smaller than 1, add 9.  
If it is even, halve it; if it is odd, add 7.  
What is the final number?

**Answer:** **1** · **Hidden trajectory:** 2 → 1

**gemma-4-31B-it:** ✅ top 5: `1`, `8`, `4`, `7`, `2`
---

![chain9-d1-09](chain9-d1-09.png)

Start with the number 8 and apply the steps in order. After every step, if the number is bigger than 9, subtract 9; if it is smaller than 1, add 9.  
If it is bigger than 5, subtract 1; otherwise double it.  
What is the final number?

**Answer:** **7** · **Hidden trajectory:** 8 → 7

**gemma-4-31B-it:** ✅ top 5: `7`, `1`, `4`, `2`, `6`
---

![chain9-d1-10](chain9-d1-10.png)

Start with the number 8 and apply the steps in order. After every step, if the number is bigger than 9, subtract 9; if it is smaller than 1, add 9.  
If it is even, halve it; if it is odd, add 6.  
What is the final number?

**Answer:** **4** · **Hidden trajectory:** 8 → 4

**gemma-4-31B-it:** ✅ top 5: `4`, `1`, `2`, `5`, `7`
---

![chain9-d1-11](chain9-d1-11.png)

Start with the number 1 and apply the steps in order. After every step, if the number is bigger than 9, subtract 9; if it is smaller than 1, add 9.  
If it is even, halve it; if it is odd, add 3.  
What is the final number?

**Answer:** **4** · **Hidden trajectory:** 1 → 4

**gemma-4-31B-it:** ✅ top 5: `4`, `2`, `1`, `3`, `0`
---

![chain9-d1-12](chain9-d1-12.png)

Start with the number 8 and apply the steps in order. After every step, if the number is bigger than 9, subtract 9; if it is smaller than 1, add 9.  
Halve it, rounding up.  
What is the final number?

**Answer:** **4** · **Hidden trajectory:** 8 → 4

**gemma-4-31B-it:** ✅ top 5: `4`, `5`, `3`, `2`, `1`
---

![chain9-d1-13](chain9-d1-13.png)

Start with the number 4 and apply the steps in order. After every step, if the number is bigger than 9, subtract 9; if it is smaller than 1, add 9.  
Halve it, rounding up.  
What is the final number?

**Answer:** **2** · **Hidden trajectory:** 4 → 2

**gemma-4-31B-it:** ✅ top 5: `2`, `3`, `4`, ``, `1`
---

![chain9-d1-14](chain9-d1-14.png)

Start with the number 4 and apply the steps in order. After every step, if the number is bigger than 9, subtract 9; if it is smaller than 1, add 9.  
If it is even, halve it; if it is odd, add 1.  
What is the final number?

**Answer:** **2** · **Hidden trajectory:** 4 → 2

**gemma-4-31B-it:** ✅ top 5: `2`, `3`, `5`, `1`, `4`
---

![chain9-d1-15](chain9-d1-15.png)

Start with the number 1 and apply the steps in order. After every step, if the number is bigger than 9, subtract 9; if it is smaller than 1, add 9.  
If it is even, halve it; if it is odd, add 8.  
What is the final number?

**Answer:** **9** · **Hidden trajectory:** 1 → 9

**gemma-4-31B-it:** ✅ top 5: `9`, `1`, `0`, `4`, `2`
---

![chain9-d1-16](chain9-d1-16.png)

Start with the number 7 and apply the steps in order. After every step, if the number is bigger than 9, subtract 9; if it is smaller than 1, add 9.  
If it is bigger than 5, subtract 2; otherwise double it.  
What is the final number?

**Answer:** **5** · **Hidden trajectory:** 7 → 5

**gemma-4-31B-it:** ✅ top 5: `5`, `4`, `1`, `8`, `2`
---

![chain9-d1-17](chain9-d1-17.png)

Start with the number 5 and apply the steps in order. After every step, if the number is bigger than 9, subtract 9; if it is smaller than 1, add 9.  
Halve it, rounding up.  
What is the final number?

**Answer:** **3** · **Hidden trajectory:** 5 → 3

**gemma-4-31B-it:** ✅ top 5: `3`, `2`, `4`, `1`, `0`
---

![chain9-d1-18](chain9-d1-18.png)

Start with the number 2 and apply the steps in order. After every step, if the number is bigger than 9, subtract 9; if it is smaller than 1, add 9.  
Halve it, rounding up.  
What is the final number?

**Answer:** **1** · **Hidden trajectory:** 2 → 1

**gemma-4-31B-it:** ✅ top 5: `1`, `2`, `4`, `3`, `8`
---

![chain9-d1-19](chain9-d1-19.png)

Start with the number 7 and apply the steps in order. After every step, if the number is bigger than 9, subtract 9; if it is smaller than 1, add 9.  
If it is bigger than 5, subtract 3; otherwise double it.  
What is the final number?

**Answer:** **4** · **Hidden trajectory:** 7 → 4

**gemma-4-31B-it:** ✅ top 5: `4`, `1`, `8`, `5`, `6`
---

![chain9-d2-01](chain9-d2-01.png)

Start with the number 5 and apply the steps in order. After every step, if the number is bigger than 9, subtract 9; if it is smaller than 1, add 9.  
If it is bigger than 5, subtract 3; otherwise double it.  
If it is even, halve it; if it is odd, add 3.  
What is the final number?

**Answer:** **4** · **Hidden trajectory:** 5 → 1 → 4

**gemma-4-31B-it:** ✅ top 5: `4`, `8`, `1`, `2`, `5`
---

![chain9-d2-02](chain9-d2-02.png)

Start with the number 9 and apply the steps in order. After every step, if the number is bigger than 9, subtract 9; if it is smaller than 1, add 9.  
If it is bigger than 5, subtract 4; otherwise double it.  
If it is bigger than 5, subtract 4; otherwise double it.  
What is the final number?

**Answer:** **1** · **Hidden trajectory:** 9 → 5 → 1

**gemma-4-31B-it:** ✅ top 5: `1`, `5`, `4`, `2`, `8`
---

![chain9-d2-06](chain9-d2-06.png)

Start with the number 5 and apply the steps in order. After every step, if the number is bigger than 9, subtract 9; if it is smaller than 1, add 9.  
Halve it, rounding up.  
If it is bigger than 5, subtract 4; otherwise double it.  
What is the final number?

**Answer:** **6** · **Hidden trajectory:** 5 → 3 → 6

**gemma-4-31B-it:** ✅ top 5: `6`, `4`, `5`, `3`, `1`
---

![chain9-d2-08](chain9-d2-08.png)

Start with the number 6 and apply the steps in order. After every step, if the number is bigger than 9, subtract 9; if it is smaller than 1, add 9.  
If it is even, halve it; if it is odd, add 1.  
Halve it, rounding up.  
What is the final number?

**Answer:** **2** · **Hidden trajectory:** 6 → 3 → 2

**gemma-4-31B-it:** ✅ top 5: `2`, `4`, `3`, `1`, `5`
---

![chain9-d2-10](chain9-d2-10.png)

Start with the number 3 and apply the steps in order. After every step, if the number is bigger than 9, subtract 9; if it is smaller than 1, add 9.  
Halve it, rounding up.  
Halve it, rounding up.  
What is the final number?

**Answer:** **1** · **Hidden trajectory:** 3 → 2 → 1

**gemma-4-31B-it:** ✅ top 5: `1`, `2`, `3`, `4`, `5`
---

![chain9-d2-16](chain9-d2-16.png)

Start with the number 8 and apply the steps in order. After every step, if the number is bigger than 9, subtract 9; if it is smaller than 1, add 9.  
Halve it, rounding up.  
Halve it, rounding up.  
What is the final number?

**Answer:** **2** · **Hidden trajectory:** 8 → 4 → 2

**gemma-4-31B-it:** ✅ top 5: `2`, `3`, `1`, `4`, `5`
---

![chain9-d2-17](chain9-d2-17.png)

Start with the number 4 and apply the steps in order. After every step, if the number is bigger than 9, subtract 9; if it is smaller than 1, add 9.  
Halve it, rounding up.  
Halve it, rounding up.  
What is the final number?

**Answer:** **1** · **Hidden trajectory:** 4 → 2 → 1

**gemma-4-31B-it:** ✅ top 5: `1`, `2`, `3`, `4`, `5`
---

![chain9-d3-15](chain9-d3-15.png)

Start with the number 4 and apply the steps in order. After every step, if the number is bigger than 9, subtract 9; if it is smaller than 1, add 9.  
If it is even, halve it; if it is odd, add 3.  
If it is even, halve it; if it is odd, add 1.  
If it is even, halve it; if it is odd, add 2.  
What is the final number?

**Answer:** **3** · **Hidden trajectory:** 4 → 2 → 1 → 3

**gemma-4-31B-it:** ✅ top 5: `3`, `2`, `4`, `1`, `5`
---

![chain9-d3-19](chain9-d3-19.png)

Start with the number 7 and apply the steps in order. After every step, if the number is bigger than 9, subtract 9; if it is smaller than 1, add 9.  
If it is bigger than 5, subtract 2; otherwise double it.  
If it is even, halve it; if it is odd, add 7.  
If it is bigger than 5, subtract 2; otherwise double it.  
What is the final number?

**Answer:** **6** · **Hidden trajectory:** 7 → 5 → 3 → 6

**gemma-4-31B-it:** ✅ top 5: `6`, `4`, `5`, `8`, `3`

## Answered wrong (32)

---

![chain9-d1-06](chain9-d1-06.png)

Start with the number 3 and apply the steps in order. After every step, if the number is bigger than 9, subtract 9; if it is smaller than 1, add 9.  
If it is even, halve it; if it is odd, add 2.  
What is the final number?

**Answer:** **5** · **Hidden trajectory:** 3 → 5

**gemma-4-31B-it:** ❌ top 5: `2`, `5`, `1`, `3`, `4`
---

![chain9-d2-00](chain9-d2-00.png)

Start with the number 8 and apply the steps in order. After every step, if the number is bigger than 9, subtract 9; if it is smaller than 1, add 9.  
If it is bigger than 5, subtract 3; otherwise double it.  
If it is even, halve it; if it is odd, add 1.  
What is the final number?

**Answer:** **6** · **Hidden trajectory:** 8 → 5 → 6

**gemma-4-31B-it:** ❌ top 5: `3`, `2`, `5`, `4`, `6`
---

![chain9-d2-03](chain9-d2-03.png)

Start with the number 1 and apply the steps in order. After every step, if the number is bigger than 9, subtract 9; if it is smaller than 1, add 9.  
If it is even, halve it; if it is odd, add 8.  
If it is bigger than 5, subtract 3; otherwise double it.  
What is the final number?

**Answer:** **6** · **Hidden trajectory:** 1 → 9 → 6

**gemma-4-31B-it:** ❌ top 5: `2`, `3`, `1`, `5`, `4`
---

![chain9-d2-04](chain9-d2-04.png)

Start with the number 8 and apply the steps in order. After every step, if the number is bigger than 9, subtract 9; if it is smaller than 1, add 9.  
If it is even, halve it; if it is odd, add 5.  
If it is even, halve it; if it is odd, add 5.  
What is the final number?

**Answer:** **2** · **Hidden trajectory:** 8 → 4 → 2

**gemma-4-31B-it:** ❌ top 5: `4`, `6`, `5`, `3`, `1`
---

![chain9-d2-05](chain9-d2-05.png)

Start with the number 8 and apply the steps in order. After every step, if the number is bigger than 9, subtract 9; if it is smaller than 1, add 9.  
If it is bigger than 5, subtract 1; otherwise double it.  
If it is even, halve it; if it is odd, add 3.  
What is the final number?

**Answer:** **1** · **Hidden trajectory:** 8 → 7 → 1

**gemma-4-31B-it:** ❌ top 5: `7`, `4`, `3`, `8`, `6`
---

![chain9-d2-07](chain9-d2-07.png)

Start with the number 1 and apply the steps in order. After every step, if the number is bigger than 9, subtract 9; if it is smaller than 1, add 9.  
If it is even, halve it; if it is odd, add 7.  
If it is bigger than 5, subtract 4; otherwise double it.  
What is the final number?

**Answer:** **4** · **Hidden trajectory:** 1 → 8 → 4

**gemma-4-31B-it:** ❌ top 5: `6`, `2`, `4`, `1`, `3`
---

![chain9-d2-09](chain9-d2-09.png)

Start with the number 7 and apply the steps in order. After every step, if the number is bigger than 9, subtract 9; if it is smaller than 1, add 9.  
If it is bigger than 5, subtract 1; otherwise double it.  
If it is bigger than 5, subtract 1; otherwise double it.  
What is the final number?

**Answer:** **5** · **Hidden trajectory:** 7 → 6 → 5

**gemma-4-31B-it:** ❌ top 5: `6`, `1`, `8`, `5`, `4`
---

![chain9-d2-11](chain9-d2-11.png)

Start with the number 8 and apply the steps in order. After every step, if the number is bigger than 9, subtract 9; if it is smaller than 1, add 9.  
If it is bigger than 5, subtract 1; otherwise double it.  
If it is even, halve it; if it is odd, add 6.  
What is the final number?

**Answer:** **4** · **Hidden trajectory:** 8 → 7 → 4

**gemma-4-31B-it:** ❌ top 5: `7`, `3`, `4`, `8`, `1`
---

![chain9-d2-12](chain9-d2-12.png)

Start with the number 4 and apply the steps in order. After every step, if the number is bigger than 9, subtract 9; if it is smaller than 1, add 9.  
Halve it, rounding up.  
If it is even, halve it; if it is odd, add 6.  
What is the final number?

**Answer:** **1** · **Hidden trajectory:** 4 → 2 → 1

**gemma-4-31B-it:** ❌ top 5: `8`, `4`, `3`, `5`, `2`
---

![chain9-d2-13](chain9-d2-13.png)

Start with the number 7 and apply the steps in order. After every step, if the number is bigger than 9, subtract 9; if it is smaller than 1, add 9.  
Halve it, rounding up.  
If it is even, halve it; if it is odd, add 7.  
What is the final number?

**Answer:** **2** · **Hidden trajectory:** 7 → 4 → 2

**gemma-4-31B-it:** ❌ top 5: `5`, `6`, `7`, `1`, `2`
---

![chain9-d2-14](chain9-d2-14.png)

Start with the number 7 and apply the steps in order. After every step, if the number is bigger than 9, subtract 9; if it is smaller than 1, add 9.  
If it is even, halve it; if it is odd, add 6.  
If it is even, halve it; if it is odd, add 1.  
What is the final number?

**Answer:** **2** · **Hidden trajectory:** 7 → 4 → 2

**gemma-4-31B-it:** ❌ top 5: `7`, `4`, `3`, `6`, `2`
---

![chain9-d2-15](chain9-d2-15.png)

Start with the number 7 and apply the steps in order. After every step, if the number is bigger than 9, subtract 9; if it is smaller than 1, add 9.  
If it is even, halve it; if it is odd, add 6.  
If it is even, halve it; if it is odd, add 2.  
What is the final number?

**Answer:** **2** · **Hidden trajectory:** 7 → 4 → 2

**gemma-4-31B-it:** ❌ top 5: `6`, `4`, `3`, `5`, `7`
---

![chain9-d2-18](chain9-d2-18.png)

Start with the number 3 and apply the steps in order. After every step, if the number is bigger than 9, subtract 9; if it is smaller than 1, add 9.  
If it is bigger than 5, subtract 2; otherwise double it.  
If it is bigger than 5, subtract 2; otherwise double it.  
What is the final number?

**Answer:** **4** · **Hidden trajectory:** 3 → 6 → 4

**gemma-4-31B-it:** ❌ top 5: `6`, `8`, `4`, `2`, `1`
---

![chain9-d2-19](chain9-d2-19.png)

Start with the number 5 and apply the steps in order. After every step, if the number is bigger than 9, subtract 9; if it is smaller than 1, add 9.  
If it is even, halve it; if it is odd, add 5.  
If it is bigger than 5, subtract 3; otherwise double it.  
What is the final number?

**Answer:** **2** · **Hidden trajectory:** 5 → 1 → 2

**gemma-4-31B-it:** ❌ top 5: `1`, `8`, `4`, `6`, `2`
---

![chain9-d3-00](chain9-d3-00.png)

Start with the number 8 and apply the steps in order. After every step, if the number is bigger than 9, subtract 9; if it is smaller than 1, add 9.  
If it is even, halve it; if it is odd, add 3.  
Halve it, rounding up.  
If it is even, halve it; if it is odd, add 7.  
What is the final number?

**Answer:** **1** · **Hidden trajectory:** 8 → 4 → 2 → 1

**gemma-4-31B-it:** ❌ top 5: `5`, `6`, `4`, `7`, `8`
---

![chain9-d3-01](chain9-d3-01.png)

Start with the number 7 and apply the steps in order. After every step, if the number is bigger than 9, subtract 9; if it is smaller than 1, add 9.  
If it is even, halve it; if it is odd, add 7.  
If it is bigger than 5, subtract 4; otherwise double it.  
If it is bigger than 5, subtract 3; otherwise double it.  
What is the final number?

**Answer:** **2** · **Hidden trajectory:** 7 → 5 → 1 → 2

**gemma-4-31B-it:** ❌ top 5: `8`, `6`, `4`, `2`, `1`
---

![chain9-d3-02](chain9-d3-02.png)

Start with the number 7 and apply the steps in order. After every step, if the number is bigger than 9, subtract 9; if it is smaller than 1, add 9.  
If it is bigger than 5, subtract 3; otherwise double it.  
If it is even, halve it; if it is odd, add 8.  
Halve it, rounding up.  
What is the final number?

**Answer:** **1** · **Hidden trajectory:** 7 → 4 → 2 → 1

**gemma-4-31B-it:** ❌ top 5: `6`, `5`, `7`, `4`, `8`
---

![chain9-d3-03](chain9-d3-03.png)

Start with the number 7 and apply the steps in order. After every step, if the number is bigger than 9, subtract 9; if it is smaller than 1, add 9.  
If it is bigger than 5, subtract 3; otherwise double it.  
If it is bigger than 5, subtract 2; otherwise double it.  
If it is bigger than 5, subtract 3; otherwise double it.  
What is the final number?

**Answer:** **5** · **Hidden trajectory:** 7 → 4 → 8 → 5

**gemma-4-31B-it:** ❌ top 5: `8`, `4`, `6`, `2`, `1`
---

![chain9-d3-04](chain9-d3-04.png)

Start with the number 6 and apply the steps in order. After every step, if the number is bigger than 9, subtract 9; if it is smaller than 1, add 9.  
If it is bigger than 5, subtract 1; otherwise double it.  
If it is even, halve it; if it is odd, add 8.  
If it is even, halve it; if it is odd, add 6.  
What is the final number?

**Answer:** **2** · **Hidden trajectory:** 6 → 5 → 4 → 2

**gemma-4-31B-it:** ❌ top 5: `7`, `6`, `8`, `5`, `4`
---

![chain9-d3-05](chain9-d3-05.png)

Start with the number 2 and apply the steps in order. After every step, if the number is bigger than 9, subtract 9; if it is smaller than 1, add 9.  
Halve it, rounding up.  
If it is even, halve it; if it is odd, add 5.  
If it is even, halve it; if it is odd, add 8.  
What is the final number?

**Answer:** **3** · **Hidden trajectory:** 2 → 1 → 6 → 3

**gemma-4-31B-it:** ❌ top 5: `6`, `7`, `4`, `5`, `8`
---

![chain9-d3-06](chain9-d3-06.png)

Start with the number 5 and apply the steps in order. After every step, if the number is bigger than 9, subtract 9; if it is smaller than 1, add 9.  
If it is even, halve it; if it is odd, add 2.  
If it is bigger than 5, subtract 4; otherwise double it.  
Halve it, rounding up.  
What is the final number?

**Answer:** **2** · **Hidden trajectory:** 5 → 7 → 3 → 2

**gemma-4-31B-it:** ❌ top 5: `3`, `2`, `4`, `1`, `7`
---

![chain9-d3-07](chain9-d3-07.png)

Start with the number 8 and apply the steps in order. After every step, if the number is bigger than 9, subtract 9; if it is smaller than 1, add 9.  
If it is bigger than 5, subtract 3; otherwise double it.  
If it is bigger than 5, subtract 4; otherwise double it.  
If it is even, halve it; if it is odd, add 2.  
What is the final number?

**Answer:** **3** · **Hidden trajectory:** 8 → 5 → 1 → 3

**gemma-4-31B-it:** ❌ top 5: `4`, `5`, `3`, `2`, `1`
---

![chain9-d3-08](chain9-d3-08.png)

Start with the number 3 and apply the steps in order. After every step, if the number is bigger than 9, subtract 9; if it is smaller than 1, add 9.  
If it is bigger than 5, subtract 3; otherwise double it.  
If it is bigger than 5, subtract 4; otherwise double it.  
Halve it, rounding up.  
What is the final number?

**Answer:** **1** · **Hidden trajectory:** 3 → 6 → 2 → 1

**gemma-4-31B-it:** ❌ top 5: `3`, `2`, `4`, `1`, `6`
---

![chain9-d3-09](chain9-d3-09.png)

Start with the number 7 and apply the steps in order. After every step, if the number is bigger than 9, subtract 9; if it is smaller than 1, add 9.  
If it is bigger than 5, subtract 4; otherwise double it.  
If it is even, halve it; if it is odd, add 8.  
Halve it, rounding up.  
What is the final number?

**Answer:** **1** · **Hidden trajectory:** 7 → 3 → 2 → 1

**gemma-4-31B-it:** ❌ top 5: `6`, `5`, `7`, `8`, `4`
---

![chain9-d3-10](chain9-d3-10.png)

Start with the number 7 and apply the steps in order. After every step, if the number is bigger than 9, subtract 9; if it is smaller than 1, add 9.  
If it is bigger than 5, subtract 1; otherwise double it.  
If it is even, halve it; if it is odd, add 2.  
Halve it, rounding up.  
What is the final number?

**Answer:** **2** · **Hidden trajectory:** 7 → 6 → 3 → 2

**gemma-4-31B-it:** ❌ top 5: `3`, `2`, `4`, `1`, `5`
---

![chain9-d3-11](chain9-d3-11.png)

Start with the number 3 and apply the steps in order. After every step, if the number is bigger than 9, subtract 9; if it is smaller than 1, add 9.  
If it is even, halve it; if it is odd, add 5.  
If it is bigger than 5, subtract 1; otherwise double it.  
If it is even, halve it; if it is odd, add 7.  
What is the final number?

**Answer:** **5** · **Hidden trajectory:** 3 → 8 → 7 → 5

**gemma-4-31B-it:** ❌ top 5: `4`, `5`, `6`, `3`, `8`
---

![chain9-d3-12](chain9-d3-12.png)

Start with the number 9 and apply the steps in order. After every step, if the number is bigger than 9, subtract 9; if it is smaller than 1, add 9.  
If it is bigger than 5, subtract 1; otherwise double it.  
If it is even, halve it; if it is odd, add 5.  
Halve it, rounding up.  
What is the final number?

**Answer:** **2** · **Hidden trajectory:** 9 → 8 → 4 → 2

**gemma-4-31B-it:** ❌ top 5: `4`, `3`, `5`, `7`, `6`
---

![chain9-d3-13](chain9-d3-13.png)

Start with the number 3 and apply the steps in order. After every step, if the number is bigger than 9, subtract 9; if it is smaller than 1, add 9.  
If it is even, halve it; if it is odd, add 7.  
If it is bigger than 5, subtract 4; otherwise double it.  
If it is bigger than 5, subtract 1; otherwise double it.  
What is the final number?

**Answer:** **4** · **Hidden trajectory:** 3 → 1 → 2 → 4

**gemma-4-31B-it:** ❌ top 5: `6`, `8`, `4`, `2`, `1`
---

![chain9-d3-14](chain9-d3-14.png)

Start with the number 5 and apply the steps in order. After every step, if the number is bigger than 9, subtract 9; if it is smaller than 1, add 9.  
Halve it, rounding up.  
If it is bigger than 5, subtract 1; otherwise double it.  
If it is bigger than 5, subtract 4; otherwise double it.  
What is the final number?

**Answer:** **2** · **Hidden trajectory:** 5 → 3 → 6 → 2

**gemma-4-31B-it:** ❌ top 5: `8`, `4`, `6`, `1`, `5`
---

![chain9-d3-16](chain9-d3-16.png)

Start with the number 9 and apply the steps in order. After every step, if the number is bigger than 9, subtract 9; if it is smaller than 1, add 9.  
If it is even, halve it; if it is odd, add 7.  
Halve it, rounding up.  
If it is even, halve it; if it is odd, add 6.  
What is the final number?

**Answer:** **2** · **Hidden trajectory:** 9 → 7 → 4 → 2

**gemma-4-31B-it:** ❌ top 5: `7`, `5`, `4`, `6`, `8`
---

![chain9-d3-17](chain9-d3-17.png)

Start with the number 7 and apply the steps in order. After every step, if the number is bigger than 9, subtract 9; if it is smaller than 1, add 9.  
If it is even, halve it; if it is odd, add 2.  
If it is even, halve it; if it is odd, add 6.  
If it is bigger than 5, subtract 1; otherwise double it.  
What is the final number?

**Answer:** **5** · **Hidden trajectory:** 7 → 9 → 6 → 5

**gemma-4-31B-it:** ❌ top 5: `4`, `5`, `6`, `8`, `7`
---

![chain9-d3-18](chain9-d3-18.png)

Start with the number 2 and apply the steps in order. After every step, if the number is bigger than 9, subtract 9; if it is smaller than 1, add 9.  
If it is even, halve it; if it is odd, add 3.  
If it is even, halve it; if it is odd, add 3.  
If it is bigger than 5, subtract 2; otherwise double it.  
What is the final number?

**Answer:** **8** · **Hidden trajectory:** 2 → 1 → 4 → 8

**gemma-4-31B-it:** ❌ top 5: `4`, `3`, `2`, `5`, `1`
