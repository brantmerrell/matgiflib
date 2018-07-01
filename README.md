# Matgiflib: Creating GIFs with Matplotlib 

## Intended purpose
Given the popularity of GIFs for online graphics, and the popularity of Matplotlib among python programmers, it seems natural to marry the two phenomena. This python package does just that: Matplotlib users can use their powers to create animations! 

The idea is that
* You write a cool python program that you want to visualize;
* You specify _when_ and _how_ you want to visualize the program's state;
* As the program executes, Matgiflib generates the frames of a GIF. When the program finishes, a GIF is compiled from the frames.

We try to introduce as little additional baggage as possible---basic familiarity with Matplotlib's pyplot interface gets you 99% of the way to making beautiful GIFs. Contrast this with Matplotlib's native animation API, which is relatively complicated IMHO.
 
I expect that this package will be most practical for python users who are familiar with Matplotlib and want to make neat little GIFs for blog posts, social media, presentations, etc.

## Installation
Make sure you satisfy the following requirements:
* The Matplotlib python package (naturally). Easily installed via pip or anaconda.
* [ImageMagick](https://www.imagemagick.org/script/index.php) must be installed---we assume you can run the ``convert`` command on your terminal. This is available from most package managers (e.g., apt for Ubuntu).
* Some of the examples require additional python packages (e.g., numpy). Nothing exotic.

Then install the Matgiflib package:
* Clone or download this repository
* move into this directory
* run ``python setup.py install``

Try running some of the examples! 
For instance, executing
``python examples/gameoflife/gameoflife.py`` 
produces the following GIF: 

<img src="https://github.com/dpmerrell/matgiflib/blob/master/examples/gameoflife/conway.gif?raw=true" alt="conway.gif" width="400px" />
