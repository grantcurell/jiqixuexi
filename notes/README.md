- [Asymptotic](#asymptotic)
- [Central Limit Theorem](#central-limit-theorem)
  - [Idea](#idea)
  - [Intuition](#intuition)
  - [Setup](#setup)
  - [Required Understanding of Variance](#required-understanding-of-variance)
    - [Constants in Variance](#constants-in-variance)
  - [Strategy - Use Standardization of Mean and Variance](#strategy---use-standardization-of-mean-and-variance)
    - [Get Mean 0](#get-mean-0)
    - [Get var 1](#get-var-1)
  - [An Example](#an-example)
    - [Standardize](#standardize)
  - [Central Limit Theorem Stated](#central-limit-theorem-stated)
- [Fundamental Theorem of Algebra](#fundamental-theorem-of-algebra)

# Asymptotic

A line whose distance to a given curve tends to zero. An asymptote may or may not intersect its associated curve.

![](images/2021-06-14-17-16-35.png)

# Central Limit Theorem

[Central Limit Theorem Lecture](https://www.youtube.com/watch?v=r9S2fMQiP2E&list=PLm3J0oaFux3ZYpFLwwrlv_EHH9wtH6pnX&index=11)

## Idea
You have some algorithm which succeeds with probability P and you run it a bunch of times independently and you want to
 understand something about the total number of times it succeeds.

## Intuition

![](images/2021-06-14-18-01-49.png)

Let's say we have a really strange dice that follows the above discrete probability distribution. We are going to take samples of it, then average the samples, and look at the frequency of the averages (mean) we get.

Say we have sample size of $n=4$. Then $S_1=[1,1,3,6]$ which gives you $\bar{x_1}=2.75$. Note: This would be the first sample. It is a sample of samples!

$S_2=[3,4,3,1] \rightarrow \bar{x_2}=2.75$

$S_3=[1,1,6,6] \rightarrow \bar{x_3}=3.5$

$\vdots$

$S_{10,000}$

Now we need to plot the frequency of the sample means.

![](images/2021-06-14-18-09-32.png)

Each dot represents a sample mean which had 4 data points. Notice as we take increasingly more, it looks increasingly like a normal distribution. If you were to take a larger sample size, the graph would be taller around the original mean.

## Setup
Let $X_1, X_2, ... , X_N$ be iid random variables independently/identically distributed. Identically
distributed means that they come from the same probability distribution. The variables have $Pr[X_i=1]=p$ and
$Pr[x_i=0]=1-p=q$ probability. You could say each $X_i$ is a bernoulli random variable with probability of success $p$.
Let $S_n=X_1+X_2+...+X_n$.

## Required Understanding of Variance

We want to understand the expectation/mean. $E[S_n]=np=E[X_1]+...+E[X_n]$. We know this from the rule *linearity of
expectation* which says the expectation of a sum is equal to the sum of the expectations. Each of the random variables
has expectation $p$ beacuse the probabilyt of $X_i=1$ we defined as $p$.

$Var[S_n]=npq=np(1-p)$
Remember the variance is $Var[Y]=E[(Y-\mu)^2]$ where $\mu=E[Y]$. Which is all equal to $E[Y^2]-E[Y]^2$. You also need
this rule: $Var[Y+Y']=Var[Y]+Var[Y']$ where $Y,Y'$ are iid.

This means the sum S_n is the sum of the independent variances $E[Y^2]-E[Y]^2 -> Var[X_i]=p-p^2=p(1-p)=pq$.

### Constants in Variance

$Var[Y+c]=Var[Y]$. A constant is just a value that is independent of everything else and subsequently does not affect
the value of the variance.

$Var[cY] = c^2Var[Y]$ <br>
$stddev[Y]=\sqrt(Var[Y])$

We frequently work with standard deviation because the units are more intuitive. You could use the variance but consider
that variance is $\sigma^2$ which means our units would be squared. We square everything to make sure it is positive.
However remember that when we do $\sqrt \sigma^2$ now there are two possible answers - one negative one positive.
See [Fundamental Theorem of Algebra](#Fundamental-Theorem-of-Algebra)

## Strategy - Use Standardization of Mean and Variance

If you have some random variable it is helpful to start by finding it's mean and variance first. If you can do both of
these things you should standardize your random variable which means make it have mean 0 and variance 1. You can
arrange for that by performing some operations which we call standardizing the variable.

### Get Mean 0

$S_n-np$ Remember $np=E[S_n]$ which is the same as the mean. That is to say, to get $S_n=0$ you subtract the mean from
it. This operation is sometimes called *centering*

### Get var 1

**TODO**: I don't really understand why these tricks work.

Multiply $1/stddev$. Remember the stddev is the square root of the variance. So you get
$np=\dfrac{S_n-np}{\sqrt(npq)}=\sigma$. That makes a random variable with mean 0 and variance 1 and therefore standard
 deviation 1.

In general if you have any random variable you could define the standardized version as
$Z=\dfrac{S-\mu}{\sigma}$ where $\mu$ is the mean and $\sigma$ is the standard deviation of $S$.

$Pr[S\le\mu]=Pr[\mu+\sigma Z\le u]=Pr[Z\le\dfrac{u-\mu}{\sigma}]$

If you understand the distribution of $S$ then you also understand the distribution of $Z$ and vice versa.

## An Example

Flipping coins.

$p=\dfrac{1}{2} , q=\dfrac{1}{2} , S_n=X_1+...+...X_n$

$\mu=E[S_n]=\dfrac{n}{2} , Var[S_n]=\dfrac{n}{4}  \sigma=\dfrac{\sqrt(n)}{2}$

This makes intuitive sense. If you flip a coin, the expectation should be 1/2 but it may vary a bit by $\sqrt(n)$

### Standardize

$\mathbb{Z_n}=\dfrac{S_n-\dfrac{n}{2}}{\dfrac{\sqrt(n)}{2}}$

Multiply top and bottom by 2 and factor out $1/\sqrt(n)$

=$\dfrac{1}{\sqrt(n)}(2S_n-n)=\dfrac{1}{\sqrt(n)}(2X_1-1+2X_2-1+...+2X_n-1)$

Notice, because the probability of $X_n$ being 1 is 1/2, in the equation $\dfrac{1}{\sqrt(n)}(2X_1-1+2X_2-1+...+2X_n-1)$
the terms $2X_1-1+2X_2-1$ are each half the time -1 or +1 because the value of $X$ is either 0 or 1. These are called *Radamacher Random Variables*.

$Pr[S_n=\dfrac{n}{2}]=Pr[Z_n=0] \asymp \sqrt(\dfrac{2}{\pi})*\dfrac{1}{\sqrt(n)}$
where $\asymp$ means asymptotic to.

Histogram of $Z_n$'s probabilities as $n$ becomes increasingly large:

![](images/2021-06-14-17-29-22.png)

$\dfrac{2}{\sqrt(n)}$ is the width of a single bar.

## Central Limit Theorem Stated

C.L.T Let $X_1, X_2, ...$ be i.i.d random variables that have a mean and a non-zero variance then the associated random variable $\lim_{n \to \infin} Z_n \rightarrow Z$ where $Z_n$ is standardized with mean 0 and variance 1 and $Z$ is a standard gaussian random variable. $\forall u \in \reals Pr[Z_n \le u]=Pr[Z \le u]\plusmn o(1)$ The little $o(1)$ is with respect to $\lim_{n \to \infin}$.

This theorem by itself is not useful in computer science because it does not give any information about the rate of the error. Furthermore this rate  could actually depend on $u$ which is problamatic. To add bounds see the Berry-Esseen Theorem.


# Fundamental Theorem of Algebra

Every polynomial eg. $x^n+ax^n-1+a_n=0$ has $n$ roots if $x \in \mathbb{C}$. The quadratic formula answers $ax^2+bx+c=0$ for $x$. The power, two here, is the number of roots."
