A likely answer
---------------

**What we will learn:** Understanding probabilities and likelihoods. Why we measure proportions the way we do. Logarithms and log-likelihoods. Find the maximum (log-)likelihood estimate and prove it is indeed maximum.

**Pre-requisits:** [Basic probability](https://www.khanacademy.org/math/cc-seventh-grade-math/cc-7th-probability-statistics#cc-7th-basic-prob) [Logarithms](https://www.bbc.co.uk/bitesize/guides/zn3ty9q/revision/1)

Before starting, it is worth pausing to emphaise what I am trying to do here. Maximum likelihood estimation is usually taught in university maths and statsitics courses, often in the second or third years. It is thus an advanced topic, and (in my experience) very few students fully understand it. In this page, I show step-by-step what maximum likelihood is, using high school mathematics. This serves two purposes. Firstly, it shows that a concept in advanced mathematics can be understood using a reasonably basic understanding of probability. Secondly, it should help students studying more advanced mathematics gain intuition into what is going on when we calculate log-likelihoods. 

### The data

In the last lesson we looked at the ‘Yes’ and ‘No’ answers to the gherkin question as $1$ for ‘Yes’ and $0$ for ‘No’. This gave us a table with a 1 if a person likes gherkins, a 0 if they don’t.
 

Anthony | Aisha |Charlie | Becky| Jennifer| Hassan| Nia	|John | Sofie	| Suki
--- |--- |--- | --- |--- |--- |--- | --- |--- |--- 
1|	0|	1 |	0	| 1|	0| 0	|1	|0	| 0|


Intuitively, it feels like the best estimate, from this data, of the frequency of Millennial Londoners who like pickled gherkins is 4/10 or 40%.  If we take the average of all the 1’s’ and 0’s in the table above, we get exactly this answer:

$$ \frac{1+0+1+0+1+0+0+1+0+0}{10}=\frac{4}{10}$$

How do we know this is the correct answer? Imagine, for instance, that some of the friends objected to using the average using some, admittedly, quite dubious arguments. Antony might claim we should give extra weighting to the answers of those you asked first because ‘they are the originals’. He adds up $2 + 0 + 2 + 2 + 0 = 6$ for the first five and $0 + 0 + 1 + 0 + 0 = 1$ for the last five, and estimates the proportion be $(6+ 1)/15 = 7/15$. 

On hearing Antony’s argument, Aisha counter claims that it’s better to ask 5 people and ignore all the others. She just looks at the answer of every second person and finds that, out of this group, only one person (John, as it turns out) likes pickled gherkins and concludes that the proper proportion is $1/5$. Finally, Charlie says, ‘Hey guys. Let’s just listen to the first person and accept what he says is true. It will save us from arguments later on.’ 

Charlie proclaims that ‘Antony loves pickled gherkins, so everyone loves pickled gherkins!’

How do we convince Antony, Aisha and Charlie that they are all wrong and that there is only one correct way of measuring the proportion who like pickled gherkins and it is 40%? 


### Enter Ronald Fisher

In *Four Ways* I take you back in time to visit Ronald Fisher and look how he would have answered the question.

Fisher made the argument as follows. Imagine for now that we don’t know the exact proportion of people that will answer ‘yes’ to the Gherkin question– but we can be sure it has some value between zero and 100%. He would then ask Antony (who suggested $7/15$), Aisha (who proposed $1/5$), Charlie (who thinks 100% of people like gherkins) to calculate the likelihood of their suggestions given the data on gherkin preferences.

Let’s start with Aisha’s suggestion that the probability that a person likes a gherkin is $1/5$ or 20%. If she is correct then the likelihood that we got the answer we got from Charlie is $1/5$, since he said he liked gherkins. Similarly, again assuming, as Antony does, that 80% of people don’t like gherkins, then the likelihood of Sue’s answer is $4/5$. We can now write out a table of the likelihood of each person’s answer, as follows,


Anthony | Aisha |Charlie | Becky| Jennifer| Hassan| Nia	|John | Sofie	| Suki
--- |--- |--- | --- |--- |--- |--- | --- |--- |--- 
1/5|	4/5|	1/5 |	4/5	| 1/5|	4/5| 4/5	|1/5	|4/5	| 4/5|


The combined likelihood of all the answers is found by multiplying the likelihoods of all the answers together,  i.e. 

$$
1/5 \cdot 4/5 \cdot 1/5 \cdot 4/5 \cdot 1/5 \cdot 4/5 \cdot 4/5 \cdot 1/5 \cdot 4/5 \cdot 4/5=0.000419
$$

where we use a dot ($\cdot$) to represent multiplication. 

Clearly, the probability of this particular sequence of answers is very small, because it is the probability of us getting a very specific sequence of answers. This does not in itself prove that Aisha is wrong: the probability of any sequence of answers is necessarily going to be quite small. Instead, what is useful about this calculation is that it allows us to compare the likelihood of Aisha’s proposal to the other proposals.

To see how, let’s start by comparing the likelihood of Aisha’s estimate to that of Charlie, who claimed that 100% of people liked gherkins. This gives a likelihood of

$$
1 \cdot 0 \cdot 1 \cdot 0 \cdot 0 \cdot 0 \cdot 0 \cdot 1 \cdot 0 \cdot 0=0
$$

There is literally zero likelihood of getting the answers we did given his suggestion. He is proven wrong as soon as Aisha gives her answer. So, Aisha wins that one. For Antony, we get,

$$
7/15 \cdot 8/15 \cdot 7/15 \cdot 8/15 \cdot 7/15 \cdot 8/15 \cdot 8/15 \cdot 7/15 \cdot 8/15 \cdot 8/15=0.00109
$$

Antony is less wrong than Aisha, because 0.00109 is larger than 0.000419. But neither of them are as good as the correct estimate, of 4/10, for which we get a likelihood

$$
4/10 \cdot 6/10 \cdot 4/10 \cdot 6/10 \cdot 4/10 \cdot 6/10 \cdot 6/10 \cdot 4/10 \cdot 6/10 \cdot 6/10=0.00119
$$

We have a winner! Our value of 40% has the largest likelihood out of those we tested. 


### Likelihoods and Logarithms

In the above example we compare tried out different proportions and calculated their likelihood. Let's now the same exercise, but use the letter $p$ to denate the probability that a person likes
gerkhins, and the letter $L$ to denate the likelihood of the answers. For these particular answers,
$$
L = p \cdot (1-p) \cdot p \cdot (1-p) \cdot p \cdot (1-p) \cdot (1-p) \cdot p \cdot (1-p) \cdot (1-p)
$$ 
where $(1-p)$ is the probability that a person doesn't like gherkins. 

We can rewrite this equation using exponents, which are used to denote multiplying numbers together. For example, if we multiply three twos together ($2\cdot 2\cdot 2=8), a short hand is to write 2^3. So, $2^3=2\cdot 2\cdot 2=8$ and I say ‘$2$ to the power of $3$ is $8$’. The number $3$ is known as the *exponent*. Similarly, $2^6=2\cdot 2\cdot 2\cdot 2\cdot 2\cdot 2=64$. Now $6$ is the exponent. 
Multiplying numbers by themselves makes them very large, very quickly. For example, $2^20=1,048,576 and 2^100=1,267,650,600,228,229,401,496,703,205,376$. The number of atoms in the Universe is (very) roughly equal to $2^266$.



$$
L= p^4 \cdot (1-p)^6
$$
The probability of the particular set of preferences expressed by these 10 people. When p=0.4 then this becomes 
L= (4/10)^4 \cdot (1-4/10)^6=(4^4 〖\cdot 6〗^6)/10^10 =11664/9765625≈0.00119
as we also saw above. 

When dealing with independent events, such as dice throws or coin tosses or people liking gherkins, we multiply the probabilities of each event in order to find the probability of them occurring. Just like repeatedly multiplying by a number greater than 1 (such 2) makes them large very quickly, multiplying probabilities makes them small very quickly. For example, the probability of getting 10 sixes in a row is $(1/6)^{10}$, which is less than one in in 60 million. The fact that multiplying makes numbers small (or large) very fast is one of the reasons for using logarithms, which I will now introduce.

Logarithms are the opposite of powers. If I ask ‘what is $\log_2(8)$?’ then I am asking how many times I need to multiply $1$ by $2$ in order to get 8. The answer is that $\log_2(8)$=3, since as we just saw, I need to multiply three times to get 8 (i.e. $2^3=2\cdot 2\cdot 2=8$). Similarly, $\log_2(64)=6$, since $2$ multiplied $6$ times is $64$.  The logarithm of $8$ and $64$ can be thus thought of as undoing the power of $2$ to give us $3$ and $6$, respectively. 

The value $2$ written in the subscript in $\log_2$ is know as the base of the logarithm. We can have other bases. So for example, if I ask ‘what is $\log_10(10000)$?’ then I am asking how many times I need to multiply $1$ by $10$ in order to get $10,000$. The answer is \log_10(10000)=4.

Logarithms turn multiplication in to addition. Notice that, for powers, $2^3 \cdot 2^3=2^6$, we add the exponents when we multiply. This means that, for example, 

$$
\log_2(64)= \log_2(8 \cdot 8) =\log_2(8)+\log_2(8)=2∙\log_2(8)=6
$$

Notice also that, because the logarithm has the opposite effect to taking a power,

$$
\log_2(p^4)= \log_2(p \cdot p \cdot p \cdot p)= \log_2(8 \cdot 8) =\log_2(8)+\log_2(8)=2∙\log_2(8)=6
$$



It is this property we now use for likelihoods, using the letter $p$ instead of numbers. So when we have,

$$
L= p^4 \cdot (1-p)^6
$$

we can take the logarithm to get 

$$
\log_2\left(p^4∙(1-p)^6\right) = \log_2\left(p^4\right) + \log_2\left((1-p)^6\right) 
$$

Then we can take the exponenets out of the logarithm to get



Notice 

This is known  as the *log-likelihood*. It was the log-likelihood which Fisher then used 





### The Maximum Likelihood

Let's 






You can see how to apply the rule for derivatives of logarithms in this [video](https://www.khanacademy.org/math/ap-calculus-ab/ab-differentiation-2-new/ab-3-1b/v/logarithmic-functions-differentiation-intro). I have tried through this presentation to explain the reason for each rule we use. but I am skipping doing this here, because it drifts slightly too far off topic. If you are interested, a good starting point can be found [here](https://www.cuemath.com/calculus/derivative-of-log-x/).