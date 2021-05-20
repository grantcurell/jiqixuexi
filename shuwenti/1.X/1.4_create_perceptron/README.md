# Perceptron

## How Perceptron Program Works

1. Create data set (it must be labeled)
2. Pick some function which splits the data into two sections
3. Generate some function that represents perceptron running which classifies the data
4. Run the perceptron function
5. Run the update function $w(t+1)=w(t)+y(t)x(t)$ on some given incorrect point. If there are none we're done
   1. Increment the repitition counter
6. Rerun 4 and 5 until complete