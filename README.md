# Morphing
*A demo linear morphing program, written in Python 3.6.*

Though this is my homework of Animation Design and Application(Professor Jin), I do spend a lot of energy to finish it. Here I will share you the usage and the project.

### Goal
> **Morphing** is a special effect in motion pictures and animations that changes (or morphs) one image or shape into another through a seamless transition.(From [wikipedia](https://en.wikipedia.org/wiki/Morphing))


It might be a little abstract. So look at the picture below, it depicts  three frames form a morph from George W. Bush to Arnold Schwarzenegger showing the midpoint between the two extremes.
Therefore, the goal of this program is to provide an user interface with which people can interact by just clicking buttons, selecting depending lines and show the results.
![MorphingExplaination](/AnimationReadMe_Picture/GeorgeW_to_Arnold_Schwarzenegger.jpg)

### Algorithm Principle
The algorithm principle lies in the paper:
Beier T, Neely S. Feature-based image metamorphosis. Computer Graphics, 1992, 26(2): 35~42

### Programming Environment
Operating System: Win7, 64bit
Language: Python 3.6, Qt5.8, 
IDE: Visual Studio 2015
### UI
User interface can be divided into 4 parts, they are source image area, target image area, result area and parameter tuning area respectively. 
![initialUI](/AnimationReadMe_Picture/initialUI.PNG)

### Usage
1. Run the project and then the initial interface shows up.
![initialUI](/AnimationReadMe_Picture/initialUI.PNG)
2. Load source and target image in source and target image area respectively by clicking Load button. Then select the image in file dialog.
![load](/AnimationReadMe_Picture/load.PNG)
3. After loading two pictures, user can draw depending lines both on source and target image area. There will be a number lying near the start point of the line as a prompt indicating the drawing order. **Please note the number of lines on source and target image should be equal.**
4. Tune the parameters of algorithm. For getting their specific meanings, please refer to the paper I list in **Algorithm Principle** part.
5. Click Generate button in parameter tuning area to generate the result. The process will be time consuming, please be patient :).
6. When the results are generated completely, click Play button, then the result will be shown in result area. Only one morphing result image will be showed by clicking once. If you want to see a video-like effect, please click Play button constantly (¤Å£þ 3£þ)¤Å.
![UI](/AnimationReadMe_Picture/UI.PNG)
7. During the process, some operators are not allowed, like playing images before generating them. At that time, the python console will give hints on what is wrong.
![error](/AnimationReadMe_Picture/error.PNG)
### Result
![result](/AnimationReadMe_Picture/result(2).png)
### Lessons

