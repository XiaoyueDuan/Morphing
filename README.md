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
![initialUI](/AnimationReadMe_Picture/Initlialize.PNG)
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
Though the algorithm is not difficult to understand, I do spend a lot of time on making an user interface. 

At the beginning of the algorithm implementing , I thought the calculation can be parallel so I choose to write the program in Python for its well-known matrix calculation library, including numpy and scipy lib which can reduce the time of  matrix calculation dramatically. It was not until the moment I made it manually that I realized the algorithm is not parallel unless largely occupying memory spaces. Though I used the parallel idea and reduced the inner loop of the algorithm, there are still 2 outer loops. Hence, the calculation speed is even slower than 3 nested loops written by C++. And the final calculating speed cannot attain real-time effect, which is totally opposite to my expectation.

I spent even more time on the UI implementation. Many friends of mine recommend me Qt library to make UI, saying that Qt is easy to manipulate and the UI effects look better than traditional UI lib, like MFC. Therefore, I adopt this idea immediately without hesitation. But I underestimate the difficulty of Qt learning, and I find that my friends recommend Qt to me have never used it too-they just heard it from others. The latest Qt version is Qt5, that's also the version I choose, but most Qt tutorials online were written in Qt4. And I don't want to compromise to use an older version, so it takes me some time to solve the compatibility problem. What's more, the official documentation of PyQt5 is not complete. All function description is the same: please refer to its C++ document, then a link following. And moreover, as a beginner, I didn't have enough time to fully understand the relationships of various widgets before coding, so the program still has many errors. For example, I hope the program can play a video when clicking Play button initially, but the video generating function in OpenCV cannot work properly. Then I want to make a GIF file, but the Image2gif function online are all in Python2, incompatible with Python3. I try the method combining matplotlib and imagemagick to make a video, but I just cannot install imagemagick. Finally, I compromise to use the Plan D- showing one image by clicking the Play button once- which is not an elegant solution at all. And I also hope to utilize the designing pattern idea at first, but the only thing I hope is there's no bugs during coding, which breach my original idea.

But generally speaking, I have learned a lot through this assignment. This experience remind me that I need to understand the algorithm better before coding, then select a lib with complete official document. Furthermore, I get some experience of designing pattern though I'm not that skillful about it. And also I get some knowledge of Qt designing. I think those experiences would be helpful for my future studying.

吐槽还是得用中文来才行啊~总的来说，这个程序写的真不容易。算法本身很好理解，原本真的可以像老师所说的“你们用半天就完成了”，但其实是实打实写了一周时间。在算法解决和图形界面构建方面都遇到了不少问题。

在实现算法的时候，理解算法初期以为会涉及一些可以并行的东西，因而也没有仔细想就选用了Python中的numpy进行计算。但真正实现起来发现并不能很好的并行计算，除非占用极大的内存空间。所以虽然用并行思想减少了一次循环，使得这个Python程序变为2层循环，但事实上处理速度还不如套了三层循环的C++程序。

在实现UI时更是一把辛酸泪。听同学说Qt界面使用起来很方便，也觉得这个作业在画线条时使用用户鼠标输入处理会更方便，就敲定使用Qt。然而我低估了学习Qt的难度，网上的教程都是针对Qt4的，模仿它们代码的时候总是遇到不兼容问题，但就是不想迁就用旧的版本。而且Qt5的Python版本还没有完整的官方文档，所有的描述都是一句话：请参照对应的C++文档（呃呃呃）。再者作为初学，很多Widget之间的关系都搞不清楚。程序还是有很多问题，比如说结果显示区本来是希望点击Play的时候根据时间和帧频以动画方式播放，但opencv不知为何就是生成不了视频文件；想做GIF动图，但网上的Python版本的Image2gif函数都是Python2的，再次不兼容Python3；想用matplotlib + imagemagick方法画图，imagemagick就是安装不对。无奈才选择按一下Play按钮显示下一幅画面的Plan D。并且起初也没预料到处理图片的速度会很慢，所以想使用用户交互的方式，实时根据算法的结果，调整参数得到更好的效果。但生成一个中间文件就要费很多时间，我还是用的实验室的32G内存的台式机。以及想应用一下设计结构中的思想，分离显示和算法，而其实等写代码的时候就顾不上了，想着代码无错就行。因而要再向里面加入功能也就是一种动一发而牵全身。

但总的来说通过这次作业学到了不少，提醒了我在提笔写程序前应该对算法了解的更为清楚，选择使用的库函数不仅要评估它的功能是否完善，还要考虑学习成本和文档的完整程度。再者虽然设计结构的思想没有很好的应用起来，但总算积累了一些经验。加之这个程序是我对Qt的初体验，相信对以后的学习也大有帮助。
