# Pi-Estimation-Monte-Carlo

## Explanation
This repository only contains one file: "pi.py". The sole purpose of this repository is the publication of this script.

## Pi.py 📄 
This file interacts with the user through the terminal (command-line interface). Run the command **python pi.py** in your terminal to use. You will the be prompted for a number (see the section **Monte-Carlo method**).

## Monte-Carlo method 📖 
The Monte-Carlo method is a mathematical statistics tool used for many stuff (including at its origins nuke-making). One of its most well-known applications is aproximating Pi. This is how it works: imagine you have a square with lengths of length one. To be precise, here are the coordinates of its four vertexes, named in order A, B, C, D: {(0, 0), (0, 1), (1, 0), (1, 1)}. Now imagine a circle with radius of length one and its centre at (0, 0). There is a section of the plane where the circle and the square are superimposed. I won't go into detail about why this is, but Pi is equal to the area of that section times four divided by one (the area of the square).

The catch is that we can't just use Pi to discover the area of that sector (ABC). We're trying to estimate Pi, so we can't just use it! But we can estimate the ration between the area of the sector and the area of the square, which we can then multiply by 4 to get our estimation. To do so we scatter points randomly in the square and keep track of how many are within the sector, which gives us a proxy for the ratio sector/square.

## Contributing 👥 
Why would you want to contribute to this?? Anyway, if you really think this is actually worthwhile, follow the following steps:

1. Create an issue ([here](https://github.com/rtiop/Pi-Estimation-Monte-Carlo/issues/new)), explaining what you will do (if you know it)
2. Fork the repository and do what you want to do
3. Creat a pull request and wait for me to approve it, give you feedback, refuse it ... or not notice it.

Don't be afraid to experiment and play around with the code! 
