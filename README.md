# Generative Pixel Pattern

## Demo
Demo Video: <https://youtu.be/i9H_nA9jM98>

## GitHub Repository
GitHub Repo: <https://github.com/C0nz0Rz/PFDA-Final.git>

## Description
Hello! My name is Connor Goodrich, and this is my final project called, “Generative Pixel Pattern”. Essentially, my program uses Pygame to create a group of squares that are scaled by the user’s input. For instance, if the user typed 3 into the terminal, it would generate a 3 square by 3 square artwork. (if 4, then 4 square by four square, and so on.) Additionally, each square will be a randomly generated color. 

Other cool features:
--As stated earlier, this code allows the user to input the scale of the artwork that is generated. This adds a variable of interaction with the user, and makes them able to customize and have more “control” (if you will) over the artwork they make.
--The pop-up pygame window has the capability to go full screen!
--The png screenshot that is saved when the code is run will not overwrite the previously saved image, since each one is time stamped with the year, month, and day; as well as the hour, min and second when it was saved. 
So each time the code is run, you’ll get a unique design, different from the previous run.
--Also, having the ability to save an image of the pop-up window is cool, because the user can capture and keep the creation they made. Instead of it just going away after they close the program.


Initially, the code would make each square generate a new color as many times a second as set by the framerate. So in my case, 60 times a second. But, to fix this and just have it generate only one color for each square, I made an empty list and a for loop that generated tuples containing the color values and had it repeat for the total amount of squares. (To calculate this, I took the scale int value imputed by the user and squared it) 
This would later be called on line 48 where I plug in the tuple of random color values, which here is called in the numerical order of the list I made. (The program knows which number of the list it’s on by this counter I incorporated here on line 44 and 51!)
