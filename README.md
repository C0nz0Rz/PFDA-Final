# Generative Pixel Pattern

## Demo
Demo Video: <https://youtu.be/i9H_nA9jM98>

## GitHub Repository
GitHub Repo: <https://github.com/C0nz0Rz/PFDA-Final.git>

## Description
Hello! My name is Connor Goodrich, and this is my final project called, “Generative Pixel Pattern”. Essentially, my program uses Pygame to create a group of squares that are scaled by the user’s input. For instance, if the user typed 3 into the terminal, it would generate a 3 square by 3 square artwork. (if 4, then 4 square by four square, and so on.) Additionally, each square will be a randomly generated color. 

## Other cool features:
--As stated earlier, this code allows the user to input the scale of the artwork that is generated. This adds a variable of interaction with the user, and makes them able to customize and have more “control” (if you will) over the artwork they make. The requested input from the user is: "Pick a number between 2 and 5, which will be the scale of the art." When the user responds to the message in the terminal, the program only accepts int values 2, 3, 4, and 5.
--The pop-up pygame window has the capability to go full screen!
--The png screenshot that is saved when the code is run will not overwrite the previously saved image, since each one is time stamped with the year, month, and day; as well as the hour, min and second when it was saved. 
So each time the code is run, you’ll get a unique design, different from the previous run.
--Also, having the ability to save an image of the pop-up window is cool, because the user can capture and keep the creation they made. Instead of it just going away after they close the program.

## Libraries used:
--pygame - this is the main library I accessed, which allows me to create a pop-up display window and "draw" in it.
--random - allows me to randomize the colors generated, so that I get a different artwork each time I run the code. It uses sudo-random algorithms to choose a number from the range listed by me.
--time - allows me to set the clock needed for the framerate/refresh rate of the display window that shows the artwork.
--from datetime, datetime - I used this library to make a timestamp for each png file (timestamp found in the file name) saved when the program is run.

## Additional code debugging explaination
Initially, the code would make each square generate a new color as many times a second as set by the framerate. So in my case, 60 times a second. But, to fix this and just have it generate only one color for each square, I made an empty list and a for loop that generated tuples containing the color values and had it repeat for the total amount of squares. (To calculate this, I took the scale int value imputed by the user and squared it) 
This would later be called on line 48 where I plug in the tuple of random color values, which here is called in the numerical order of the list I made. (The program knows which number of the list it’s on by this counter I incorporated here on line 44 and 51!)

I used a nested loop starting on line 45, which creates surfaces for each vertical collum and each horizontal row in the large square group. It is dependant on the int value stored in <range> inputed by the user in the terminal when prompted.