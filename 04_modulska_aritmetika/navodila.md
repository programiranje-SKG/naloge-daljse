# Modulska aritmetika

## Uvod
Za podano praštevilo $p$, imenovano modul, definirajmo množico $Z_p = \{0, 1, ... , p-1\}$. Za
števila iz te množice sta operaciji *modulskega seštevanja* ($\oplus$) in modulskega množenja ($\otimes$)
definirani takole: 

$$a \oplus b = (a + b) \; mod \; p \\
a \otimes b = a b \; mod \; p$$

Zapis $s \; mod \; t$ predstavlja ostanek pri deljenju števila $s$ s številom $t$.
Modulska *nasprotna vrednost* števila $a$ je število $\bar{a}$, za katero velja $a \oplus \bar{a} = 0$. Modulska *obratna vrednost* števila $a \neq 0$ je število $a^*$, za katero velja $a \otimes a^* = 1$. Sedaj lahko definiramo tudi operaciji *modulskega odštevanja* ($ \ominus $) in modulskega deljenja ($\oslash$):

$$a \ominus b = a \oplus \bar{b} \\
a \oslash b = a \otimes b^*  \; (pri \; pogoju \; b \neq 0) $$



Na primer, elementi množice $Z_7$ se med sabo modulsko seštevajo, odštevajo, množijo in
delijo takole:

<table>
<tr><td><center> Modulska vsota </center> </td> <td>    </td><td><center> Modulska razlika </center></td></tr>
<tr><td>

| $\oplus$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 |          
|---|---|---|---|---|---|---|---|
| **0** | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
| **1** | 1 | 2 | 3 | 4 | 5 | 6 | 0 |
| **2** | 2 | 3 | 4 | 5 | 6 | 0 | 1 |
| **3** | 3 | 4 | 5 | 6 | 0 | 1 | 2 |
| **4** | 4 | 5 | 6 | 0 | 1 | 2 | 3 |
| **5** | 5 | 6 | 0 | 1 | 2 | 3 | 4 |
| **6** | 6 | 0 | 1 | 2 | 3 | 4 | 5 |

</td><td>
</td><td>

| $\ominus$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 |          
|---|---|---|---|---|---|---|---|
| **0** | 0 | 6 | 5 | 4 | 3 | 2 | 1 |
| **1** | 1 | 0 | 6 | 5 | 4 | 3 | 2 |
| **2** | 2 | 1 | 0 | 6 | 5 | 4 | 3 |
| **3** | 3 | 2 | 1 | 0 | 6 | 5 | 4 |
| **4** | 4 | 3 | 2 | 1 | 0 | 6 | 5 |
| **5** | 5 | 4 | 3 | 2 | 1 | 0 | 6 |
| **6** | 6 | 5 | 4 | 3 | 2 | 1 | 0 |


</td></tr>

<tr> </tr>
<tr><td><center> Modulski zmnožek </center></td> <td>    </td><td><center> Modulski količnik </center></td></tr>
<tr><td>

| $\otimes$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 |          
|---|---|---|---|---|---|---|---|
| **0** | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **1** | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
| **2** | 0 | 2 | 4 | 6 | 1 | 3 | 5 |
| **3** | 0 | 3 | 6 | 2 | 5 | 1 | 4 |
| **4** | 0 | 4 | 1 | 5 | 2 | 6 | 3 |
| **5** | 0 | 5 | 3 | 1 | 6 | 4 | 2 |
| **6** | 0 | 6 | 5 | 4 | 3 | 2 | 1 |



</td><td>
</td><td>

| $\oslash$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 |          
|---|---|---|---|---|---|---|---|
| **0** | - | 0 | 0 | 0 | 0 | 0 | 0 |
| **1** | - | 1 | 4 | 5 | 2 | 3 | 6 |
| **2** | - | 2 | 1 | 3 | 4 | 6 | 5 |
| **3** | - | 3 | 5 | 1 | 6 | 2 | 4 |
| **4** | - | 4 | 2 | 6 | 1 | 5 | 3 |
| **5** | - | 5 | 6 | 4 | 3 | 1 | 2 |
| **6** | - | 6 | 3 | 2 | 5 | 4 | 1 |

</td></tr>
 </table>

*Modulska potenca* $mpow(a, t)$, pri čemer je $a \in Z_p$, $t$ pa je lahko *poljubno* celo število, je deﬁnirana takole:

$$mpow(a, t) = 
    \begin{cases}
    1 & pri \; t=0 \\
    a \otimes mpow(a,t-1) & pri \; t > 0 \\
    mpow(a, -t)^* & pri \; t < 0 \\
    \end{cases}

$$

Na primer, pri $p = 7$ velja $mpow(5,0) = 1$, $mpow(5,1) = 5$, $mpow(5,2) = 5 \otimes 5 = 4$, $mpow(5,3) = 5 \otimes 5 \otimes 5 = 6$, $mpow(5,-1) = 5^* = 3$, $mpow(5,-2) = (5 \otimes 5)^* = 4^* = 2$ itd.

Deﬁnirajmo še modulski *kvadratni koren* (msqrt): 

$$ msqrt(a) = \{b \in Z_p \; | \; b \otimes b = a\}$$

Za razliko od običajnega kvadratnega korena modulski ni enolično določen, zato ga deﬁniramo kot množico vseh števil, ki pri modulskem množenju s samim seboj dajo podano
število. Na primer, pri $p=7$ velja $msqrt(0)=\{0\}$, $msqrt(1)=\{1,6\}$, $msqrt(2)=\{3,4\}$, $msqrt(3)= \emptyset$, $msqrt(4)=\{2,5\}$, $msqrt(5)= \emptyset$, $msqrt(6)= \emptyset$.

Število $n \in  Z_p$ je *multiplikativni generator* množice $Z_p$ , če je množica

$$
P(n) = \{mpow(n,i) \; | \; i \in \{0,1, \dots, p-1 \}\}
$$

enaka množici $Z_p\ \{0\} = \{1,2, \dots,p-1 \}$. Na primer, pri $p=7$ velja $P(0) = \{0\}$, $P(1) = \{1\}$, $P(2) = \{1,2,4\}$, $P(3) = \{1,2,3,4,5,6\}$, $P(4) = \{1,2,4\}$, $P(5) = \{1,2,3,4,5,6\}$ in $P(6) = \{1,6\}$. Multiplikativna generatorja množice $Z_7$ sta torej števili 3 in 5.

## Naloge

V razredu Zp, čigar objekt predstavlja množico $Z_p$ za podani modul $p$ implementirajte sledeče metode:

### Vsota

Definiratje metodo `vsota(self, prvo, drugo)`, ki vrne modulsko vsoto števil `prvo` in `drugo` v okviru množice, ki jo predstavlja trenutni objekt. Obe števili sta iz intervala $[0, p-1]$, kjer je $p$ modul množice trenutnega objekta.

### Zmnožek
Metoda `zmnozek(self, prvo, drugo)` vrne modulski zmnožek števil `prvo` in `drugo` v okviru množice, ki jo predstavlja trenutni objekt. Obe števili sta iz intervala $[0, p-1]$, kjer je $p$ modul množice trenutnega objekta.

### Nasprotno
Metoda `nasprotno(self, stevilo)` vrne modulsko nasprotno vrednost števila `stevilo`.Število je iz intervala $[0, p-1]$, kjer je $p$ modul množice trenutnega objekta.

### Razlika
Metoda `razlika(self, prvo, drugo)` vrne modulsko razliko števil `prvo` in `drugo` v okviru množice, ki jo predstavlja trenutni objekt. Obe števili sta iz intervala $[0, p-1]$, kjer je $p$ modul množice trenutnega objekta.

### Obratno
Metoda `obratno(self, stevilo)` vrne modulsko obratno vrednost števila `stevilo`. Število se nahaja na intervalu $[1, p - 1]$, kjer je $p$ modul množice trenutnega objekta.

### Količnik
Metoda `kolicnik(self, prvo, drugo)` vrne modulski količnik števil `prvo` in `drugo`. Parameter `prvo` se nahaja v intervalu $[0, p  - 1]$, parameter `drugo` pa v intervalu $[1, p  - 1]$.

### Potenca
Metoda `potenca(self, stevilo, eksponent)` vrne modulsko potenco števila `stevilo` na število `eksponent`. Parameter `eksponent` se nahaja v intervalu $[-10^3, 10^3]$. Parameter 'stevilo' se nahaja v intervalu $[1, p-1]$.

### Število kvadratnih korenov

Metoda `stevilo_kvadratnih_korenov(self, stevilo)` vrne moč množice (število elementov) modulskih kvadratnih korenov števila `stevilo`, torej število števil $b$ iz intervala $[0, p-1]$, za katera je produkt $b \otimes b$  enak številu $stevilo$.

### Je potenca

Pomožna metoda. `je_potenca(self, osnova, iskani_rezultat)` preveri, če je `iskani_rezultat` potenca števila `osnova` v množici, ki jo predstavlja trenutni objekt.

### Je multiplikativni generator

Metoda `je_multiplikativni_generator(self, stevilo)` vrne `True` natanko v primeru, če je število `stevilo` multiplikativni generator množice, ki jo predstavlja trenutni objekt. Parameter `stevilo` se nahaja v intervalu $[1, p  - 1]$.

Pri implementaciji si lahko pomagaš s funkcijo `je_potenca(osnova, iskani_rezultat)`.
