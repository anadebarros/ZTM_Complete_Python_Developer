#Exercise!
#Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!
picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

#I added a twist:
# I wanted to print the tree twice, so I mada a little counter
counter = 0 #

while counter < 2:
  for item in picture:
    for i in item:
        if i == 0:
          print(" ", end ="")
        else:
          print("*", end ="")
    print(" ") #need a new line after each row in list
  counter += 1