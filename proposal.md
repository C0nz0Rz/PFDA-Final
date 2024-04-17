Generative Pixel Pattern

Repository: https://github.com/C0nz0Rz/PFDA-Final.git
For helpful tips when using my code, check the README.md shown below!


Description: For this project, I would like to create a program that would create a 6 x 6 square "pixel art" based on a randomly colored 3 by 3 square, which would be the pattern.
Being able to create a fun little design at a press of a button is pretty cool to think about, and I think just like the rorschach test, artists can look at the artwork
made and perhaps see something (perhaps a form) out of it that inspires them to create their own artwork.


Features: 
-A cool feature would be that it is almost always going to provide a unique pattern, since it randomizes the color that is painted on each square (of the 3 by 3).
My only knowledge of how this would be possible is through the Pygame library, using the random method. I maybe could use Turtle, but I think that would be unnessisarily complicated.

-It will be able to generate a 3 by 3 square artwork, then will translate and flip copies of said artwork over the X and Y axis. Which, when combined, will create a 6 by 6 artwork.
The idea is that with the essentially "mirrored" image generated, it would appear to have order, composition, and ultimately, an artistic design.
[(I think that it is incredible that python is capable of creating generative art, and I want to harness that ability here to make a simple artwork.)]

-I would like the program to save each generated artwork into an image file, so that it wouldn't just appear on the monitor, but be able to be accessed or printed by the user later. I might have to use the pillow library for this as well.

-I want to have the option to execute the command multiple times with a keyword. Like after the program generates one, it should prompt the user with a question asking to render another design.


Challenges:
-I am very new to Pygame, as well as applying the simple rules of Python. So brushing up on the doccumentation for the Pygame library as well as rewatching the chapter videos we've gone over would be helpful.
-Another library that would be good to read up on might be the Pillow doccumentation.


Outcomes:
-Ideal Outcome: Ideally, (like stated before) I would like the program to be able to generate a 6 by 6 square artwork, utilizing and correctly ajusting the random 3 x 3 square mini-art as a pattern. Additionally, I think it would be cool if it could save it as an image on my computer.

-Minimal Viable Outcome: I would like to at least be able to generate a random 3x3 square artwork, and have it visable to the viewer.


Milestones:
1. Finish def variable: <main():> and <def randomize():>
2. Finish def variable: <def translate():>
3. Finish def variable: <def coloring():>
