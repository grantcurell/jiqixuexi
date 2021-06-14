# Exercise 1.1

Express each of the following tasks in the framework of learning from data by specifying the input space $X$, output space $Y$, target function $f: X->Y$, and the specifics of the data set that we will learn from.

- Medical diagnosis: A patient walks in with a medical history and some symptoms, and you want to identify the problem.

$X$: {Symptoms} <br>
$Y$: {Medical history} <br>
$f: X->Y$: Doctor

Assuming that there is a relationship between the symptoms and the medical history. This problem is a bit weird because you wouldn't necessarily assume that. For example: Someone might have a history of cancer but come in with a stab wound.

- Handwritten digit recognition (for example postal zip code recognition for mail sorting)

$X$: {Inbound postcard} <br>
$Y$: {Correct address} <br>
$f: X->Y$: Someone sorting the mail

- Determining if an email is spam or not

$X$: {Some e-mail} <br>
$Y$: {A box of correctly identified Spam} <br>
$f: X->Y$: Users clicking spam

- Predicting how an electric load varies with price, temperature, and day of the week

$X$: {temperature, day of the week} <br>
$Y$: {price} <br>
$f: X->Y$: Some equation at the power company determining the load and calculating price

- A  problem of interest to you for which there  is  no analytic solution, but you have data from which to construct  an empirical  solution.

$X$: data <br>
$Y$: some Y answer that depended on $X$ data <br>
$f: X->Y$: Some learning algorithm $A$