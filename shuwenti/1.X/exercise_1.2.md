# Exercise 1.2

Suppose that we  use  a perceptron to  detect spam  messages. Let's say that  each email message is represented by the frequency of occurrence  of keywords, and the output is if the message is considered spam.

- Can you think of some keywords that will end up with a large positive weight in  the perceptron?

Anything related to porn. Nigeria.

- How about keywords that will get a  negative weight?

The names of people in your list of work contacts or friends. Words in your signature block. 

- What parameter in the perceptron directly affects how many border­line messages end up being classified as spam?

$b$ - the bias. If the bias is a larger positive number it requires more negative numbers to make the overall sum negative.