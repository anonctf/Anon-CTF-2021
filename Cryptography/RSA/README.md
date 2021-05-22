# RSA_test

[RSA algorithm](https://simple.wikipedia.org/wiki/RSA_algorithm).<br><br>

**Question 1:**<br>
p = 993319; q = 939391<br>
n = p * q<br>
n = 933114928729<br>
This is feasible beacause both p & q are pime numbers.<br><br>

**Question 2:**<br>
p = 84673; n = 5414753677<br>
q = n / p<br>
q = 63949<br>
This is feasible beacause both p & q are pime numbers.<br><br>

**Question 3:**<br>
e = 4; n = 15788162802910546503821920886905393316386362759567480839428456525224226445173031635306683726182522494910808518920409019414034814409330094245825749680913204566832337704700165993198897029795786969124232138869784626202501366135975223827287812326250577148625360887698930625504334325804587329905617936581116392784684334664204309771430814449606147221349888320403451637882447709796221706470239625292297988766493746209684880843111138170600039888112404411310974758532603998608057008811836384597579147244737606088756299939654265086899096359070667266167754944587948695842171915048619846282873769413489072243477764350071787327574<br>
This is not feasible beacause factors of n are not pime numbers.<br><br>

**Question 4:**<br>
p = 28813; q = 37633<br>
φ(n) = (p - 1) * (q - 1)<br>
φ(n) = 1084253184<br>
This is feasible beacause both p & q are different pime numbers.<br><br>

**Question 5:**<br>
plaintext = 132752155257635; e = 3; n = 526143710132827117<br>
ciphertext = (plaintext)<sup>e</sup> mod n<br>
```Python
# Python3 interpreter
>>> pow(132752155257635, 3, 526143710132827117)
408020833339943651
```
ciphertext = 408020833339943651<br>
This is feasible beacause factors of n are pime numbers.<br><br>

**Question 6:**<br>
p = 755230417; e = 65537; ciphertext = 179678541211980372; n = 593028658204570843<br>
de = 1 mod φ(n)<br>
plaintext = (ciphertext)<sup>d</sup> mod n<br>
```Python
# Python3 interpreter
>>> p = 755230417
>>> e = 65537
>>> c = 179678541211980372
>>> n = 593028658204570843
>>> q = int(n / p)
>>> q
785228779
>>> tot = (p - 1) * (q - 1)
>>> tot
593028656664111648
>>> from Crypto.Util.number import inverse
>>> d = inverse(e, tot) # or d = pow(e, -1, tot)
>>> d
464319078679304225
>>> pow(c, d, n)
172042158527139
```
plaintext = 172042158527139<br>
This is feasible beacause both p & q are pime numbers and e is greater than 1 and coprime to φ(n).<br><br>

After solving this quiz you'll be a string. You need to decrypt this string to get the flag.<br>
B64 > brainfuck > flag
