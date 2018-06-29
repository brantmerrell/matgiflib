# Matgiflib: Creating GIFs with matplotlib 

Given the popularity of GIFs for online graphics, and the popularity of matplotlib among python programmers, it seems natural to want a pyplot-like interface for making GIFs.

The idea is that
* You write a cool python program that you want to visualize;
* You specify _when_ and _how_ you want to visualize the program's state;
* Matgiflib generates a GIF as the program executes.

This is NOT fancy GPU-powered or real-time visualization. 
But it can be practical for python users who are familiar with matplotlib and want to make neat little GIFs for blog posts, social media, presentations, etc.

