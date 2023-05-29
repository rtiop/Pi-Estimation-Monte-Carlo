# Pi-Estimation-Monte-Carlo

## Introduction
This script works by plotting *n* points on a square and using the Monte-Carlo statistical method to aproximate Pi.

## Running
To run the code use the command **python pi.py**. You will then be prompted (in Spanish) for a number. That will be the number of points plotted. The program outputs a float which is the aproximation.

## Monte-Carlo
The idea is that if you scatter dots at random locations on a square in which a quarter of a circle is inscribed, you can estimate Pi. You divide the number of dots that fall within the circle by the total number of dots (*n*) and multiply that number by 4. The result optained is **non deterministiuc**. so each time you rerun the program you will probably get a diferent result, but it will tend to be more accurate as *n* grows.
