A likely answer
---------------

### The data

In the last lesson we looked at the ‘Yes’ and ‘No’ answers to the gherkin question as $1$ for ‘Yes’ and $0$ for ‘No’. This gave us a table with a 1 if a person likes gherkins, a 0 if they don’t.
 

Anthony | Aisha |Charlie | Becky| Jennifer| Hassan| Nia	|John | Sofie	| Suki
--- |--- |--- | --- |--- |--- |--- | --- |--- |--- 
1|	0|	1 |	0	| 1|	0| 0	|1	|0	| 0|


Intuitively, it feels like the best estimate, from this data, of the frequency of Millennial Londoners who like pickled gherkins is 4/10 or 40%.  If we take the average of all the 1’s’ and 0’s in the table above, we get exactly this answer:

$$\bar{x} = \frac{1+0+1+0+1+0+0+1+0+0}{10}=\frac{4}{10}$$

How do we know this is the correct answer? Imagine, for instance, that some of the friends objected to using the average using some, admittedly, quite dubious arguments. Antony might claim we should give extra weighting to the answers of those you asked first because ‘they are the originals’. He adds up 2 + 0 + 2 + 2 + 0 = 6 for the first five and 0 + 0 + 1 + 0 + 0 = 1 for the last five, and estimates the proportion be (6+ 1)/15 = 7/15. 

On hearing Antony’s argument, Aisha counter claims that it’s better to ask 5 people and ignore all the others. She just looks at the answer of every second person and finds that, out of this group, only one person (John, as it turns out) likes pickled gherkins and concludes that the proper proportion is 1/5. Finally, Charlie says, ‘Hey guys. Let’s just listen to the first person and accept what he says is true. It will save us from arguments later on.’ 

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

1/5×4/5×1/5×4/5×1/5×4/5×4/5×1/5×4/5×4/5=0.000419

Clearly, the probability of this particular sequence of answers is very small, because it is the probability of us getting a very specific sequence of answers. This does not in itself prove that Aisha is wrong: the probability of any sequence of answers is necessarily going to be quite small. Instead, what is useful about this calculation is that it allows us to compare the likelihood of Aisha’s proposal to the other proposals.

To see how, let’s start by comparing the likelihood of Aisha’s estimate to that of Charlie, who claimed that 100% of people liked gherkins. This gives a likelihood of

1×0×1×0×0×0×0×1×0×0=0

There is literally zero likelihood of getting the answers we did given his suggestion. He is proven wrong as soon as Aisha gives her answer. So, Aisha wins that one. For Antony, we get,

7/15×8/15×7/15×8/15×7/15×8/15×8/15×7/15×8/15×8/15=0.00109

Antony is less wrong than Aisha, because 0.00109 is larger than 0.000419. But neither of them are as good as the correct estimate, of 4/10, for which we get a likelihood

4/10×6/10×4/10×6/10×7/15×8/15×8/15×7/15×8/15×8/15=0.00119

We have a winner! Our value of 40% has the largest likelihood and is thus the estimate we should use. 


<div class="warning" style='padding:0.1em; background-color:#E9D8FD; color:#69337A'>
<span>
<p style='margin-top:1em; text-align:center'>
<b>Challenge I:4</b></p>
<p style='margin-left:1em;'>

**What is the likelihood for an estimate of 3 out 10 people liking gherkins?**

</p>
</p></span>
</div>


### The Maximum Likelihood

DERIVATION HERE




