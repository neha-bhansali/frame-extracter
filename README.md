# Frame-Extracter

## Process: 
- Capture the video
   cap = cv.VideoCapture("vid.mp4")

- Extract the frames from video
  ret , frame = cap.read()
  
- Save the frame         
  cv.imwrite(str(i) + "\\" + str(int(c)) + ".jpg"  , frame)

- Release cap


## Steps to perform when working with this file:

- Create a folder with the same name as your video
- Add the name of your video to the list


Example:
![image](https://user-images.githubusercontent.com/78554453/233797904-87eb8aa9-12eb-4a9a-a82d-22b8c11e392d.png)
