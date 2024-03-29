# Mandelbrot
A python script to represent a part of the Mandelbrot set for a given region of the complex plane.

The Mandelbrot set is made up of all complex numbers **c** for which the following iterative function remains bound:

![](https://latex.codecogs.com/svg.image?\large&space;z_{n&plus;1}&space;=&space;z^{2}_n&space;&plus;&space;c)

The code sets up an **N X N** matrix of equidistantly sampled points from a square region of the complex plane, with side length **L** centered around the point
**c0 = x + y * i**

The basic Mandelbrot iteration is then performed on each point T number of times. For all interesting regions of the Mandelbrot set, the value of the iteration becomes inf or nan within a few hundred steps, in which case they are considered to be out of the set.

The basic call from the command line is shown below. The first three positional arguments stand for **x,y,l** respectively
the last two flags are for resolution and number of iterations, with default values are 1024 and 1500

run this in your command line to produce an image:

```console
python Mandelbaecker.py 0.432539867562512  0.226118675951765 3.2e-6 -r 1024 -i 1000

```

here is a high resolution example of what the code produces

![alt text](Fi.png)
