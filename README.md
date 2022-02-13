Ever wonder about how well do you know about snakes? 
# Welcome to **[Snakequiz](https://snakequiz-pp3.herokuapp.com/)**, and test your knowledge!

<img src="assets/screenshots/mockup-final.png" width="800">

- [**Purpose of the game**](#--purpose-of-the-game--)
- [**Why This**](#--why-this--)
- [**Features**](#--features--)
  * [Existing Features:](#existing-features-)
    + [**Home page**:](#--home-page---)
    + [Menu Item 1 **Play**](#menu-item-1---play--)
    + [Menu Item 2 **Quit**](#menu-item-2---quit--)
    + [Menu Item 3 **Restart**](#menu-item-3---restart--)
    + [Menu Item 4 **Scoreboard**](#menu-item-4---scoreboard--)
  * [New Features In the Future Update:](#new-features-in-the-future-update-)
    + [Menu Item: **My Last 4 Scores**](#menu-item----my-last-4-scores--)
    + [Quiz: **Allow player to add more questions**](#quiz----allow-player-to-add-more-questions--)
    + [Game: **Chatbox**](#game----chatbox--)
- [**Game Logic**](#--game-logic--)
  * [Flowchart](#flowchart)
- [**Data Model**](#--data-model--)
- [**Technology Used**](#--technology-used--)
  * [**Language**](#--language--)
  * [**Tools**](#--tools--)
- [**Testing**](#--testing--)
  * [**Code Validation on PEP8**](#--code-validation-on-pep8--)
  * [**Bugs**](#--bugs--)
    + [*Fixed Bugs*](#-fixed-bugs-)
    + [*Unfixed Bugs*](#-unfixed-bugs-)
- [**Deployment**](#--deployment--)
- [**Credits**](#--credits--)
- [**Acknowledgments**](#--acknowledgments--)

## **Purpose of the game**
<p>This game is aimed to test as well as to entertain children and adults who are interested in snakes and want to know more about it. After each question, there is also an interesting fact related to the question that will be displayed, to give the player a bit more in depth information. Main objectives are:</p>

- to test the player's knowledge about snakes
- to challenge the players memory 
- to increase the players's interests and curiousity about snakes 
- and most importantly to LOVE NATURE

------

## **Why This**

<p>This snake quiz was inspired by my 8 year old who has a fascination about snakes, and strange insects. Personally, I was never a big fan of snakes, mainly scared of them. However, in my son’s eyes, they are cute and beautiful. I guess when you look at those pictures, you could say that:</p>

<img src="assets/screenshots/cutie1.jpg" width="300"> <img src="assets/screenshots/cutie2.jpg" width="300">
<img src="assets/screenshots/cutie3.jpg" width="300"> <img src="assets/screenshots/cutie4.jpg" width="300">
<img src="assets/screenshots/funny1.jpg" width="600">

<p>Being an encouraging mom I did try to gather all the information out there to satisfy his curious mind. In the process, I ended up learning a fair amount of interesting facts about the creature. He did ask for a snake as a pet, I couldn't agree with that, but I decided to build this quiz instead. Hoping other people could learn a thing or two about snakes by playing this quiz, to spark interest and dive deep into it, not only about snakes but about nature in general.</p>

------

## **Features**
### Existing Features:
#### **Home page**:
Once you are on the **[live site](https://snakequiz-pp3.herokuapp.com/)** first thing you will notice is the welcome message with the title of “SNAKEQUIZ” ASCII in star wars style, because it is cool. And some simple instructions of the game below.

<img src="assets/screenshots/live-site-final1.png" width="800">

<br>
<p>Followed by the game menu with 4 options, allowing the player to choose between start the quiz, quit, restart and display the Scoreboard. </p>

<img src="assets/screenshots/live-menu.png" width="800">

#### Menu Item 1 **Play**
<p>When the player chooses the Play option, the system will ask for an input of the chosen player name. With specified information about what you can use in the player name and the max number of characters. If any character is not a letter or digit, or the length is more than 8 characters, the system will detect it, and trigger an error message to be displayed. The system will keep requesting the player name until a valid answer is received, then the quiz will start.</p>

<img src="assets/screenshots/live-menu1.png" width="800">

Below are the Error Message Examples:

<img src="assets/screenshots/live-playername-validation.png" width="800">
<img src="assets/screenshots/live-playername-validation2.png" width="800">

<p>There are 10 questions in total as indicated at the beginning of the quiz. Mixed with Y/N and multiple choice questions, here will display an instruction about how to answer each type of question.</p>

<img src="assets/screenshots/live-instruction.png" width="800">

<p>Each question will provide the player with feedback whether their answer was correct or not. Followed by an interesting fact related to that particular question, to give the player a bit more information for “good to know” purposes.</p>

<img src="assets/screenshots/live-quiz.png" width="800">

<p>After completing all 10 questions, a final score will be displayed to the player, as well as the game menu, giving players the opportunity to choose their next move.</p>

<img src="assets/screenshots/live-final-score.png" width="800">

<p>Meanwhile, the final score along with the player's name and time stamp will be registered on the google sheet which is linked to the quiz game via API.</p>

<img src="assets/screenshots/gsheet.png" width="800">

#### Menu Item 2 **Quit**
<p>When the player chooses the Quit option, the system will display a goodbye message, and end. You need to click on the “Run Program” button on the top of the screen to reactivate the program.</p>

<img src="assets/screenshots/live-menu2.png" width="800">

#### Menu Item 3 **Restart**
<p>You would choose this option when you have already played your 1st game, and would like to play again. By choosing this option, the quiz will start straight away without asking you to input username. That is assuming you will not choose this option if you are playing for the first time.</p>

<img src="assets/screenshots/live-menu3.png" width="800">

#### Menu Item 4 **Scoreboard**
<p>By choosing this option, the system will request the information from the google sheet via API, and display the top 10 player scores of all time in the descending order, with their name and time stamp on the side. Followed by the game menu, so the player can choose their next move.
</p>

<img src="assets/screenshots/live-menu4.png" width="800">

<br>

### New Features In the Future Update:
#### Menu Item: **My Last 4 Scores**
<p>My mentor gave me this idea, so originally I planned for 5 options in the game menu, with the last one to display a single player’s last 4 scores. I thought this feature is nice, because it will allow the players to keep track of their own scores. Unfortunately, I didn’t manage to make it work, and it seems to add a lot of complexity to the game, which with my current skill set is a bit out of reach. Hopefully in the future, as I progress further in the coding journey, I will be able to make it work.</p>

#### Quiz: **Allow player to add more questions**
<p>It would be nice to have a feature that allows players to add more questions in the quiz section, to test / share the knowledge with others, to expand the scope. And also, it would be nice if the question can be rotated randomly each time it runs.</p>

#### Game: **Chatbox**
<p>Inspired by CI’s slack channel, why not have a place that will allow players to chat with each other, learn from each other and inspire one another. Afterall, they share a common interest in snakes.</p>

## **Game Logic**
### Flowchart

<img src="assets/flowchart-final.png" width="800">

<br>

## **Data Model**
[Google sheet](https://docs.google.com/spreadsheets/u/0/) was used to store information like score, player’s name and the time stamp. When the player chooses to see the Top 10 scores, the system will read the whole data from this sheet and display only the highest 10.

<img src="assets/screenshots/gsheet.png" width="800">

<br>

## **Technology Used**
### **Language**
This is a command-line application built purely using **python** as the main programming language

### **Tools**
- [Github](https://github.com/) for store and version control of the code

- [Gitpod](https://gitpod.io/workspaces) for editing code

- [Heroku](https://heroku.com/) for deployment

- [draw.io](https://app.diagrams.net/) for creating flowchart

- [Patorjk.com](https://patorjk.com/software/taag/#p=display&f=Star%20Wars&t=Type%20Something%20) for creating the cool looking game title at the beginning of the game

- [Lightshot](https://app.prntscr.com/en/index.html) for creating screenshots

- [GitHub Wiki TOC generator](https://ecotrust-canada.github.io/markdown-toc/) for generating table of content for README.md file

- [techsini.com](https://techsini.com/multi-mockup/index.php) for generating the mock up

- [Google Image](https://www.google.com/search?q=cute+snake&sxsrf=APq-WBtiN9NnHc8YW9Ugr5ZmfkmyOwTAjw:1644681215048&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjdp938wvr1AhUtlYsKHWDdDn8Q_AUoAXoECAIQAw&biw=1920&bih=937&dpr=1) for downloading the cute snakes pictures

- [Google sheet](https://docs.google.com/spreadsheets/u/0/) was used to store data

- [Google cloud platform](https://console.cloud.google.com/) for connecting google sheet via API

<br>

## **Testing**
### **Code Validation on PEP8**
Run.py

<img src="assets/screenshots/pep8-run.png" width="800">

Quiz.py

<img src="assets/screenshots/pep8-quiz.png" width="800">

### **Bugs**
#### *Fixed Bugs*
1 <p>When score is greater than 7, the print statement of "You did awesome job!" doesn’t work</p>
 <p>Solution: With my mentor’s help, turned out the word “and” was missing</p>

<img src="assets/screenshots/fixed-bug1.png" width="800">

2 <p>Once the quiz starts, it will go to the next question, even the error message displayed.</p>
<p>Solution: Turned out I forgot the while loop, added them to each question, and the problem was fixed.</p>

3 <p>The display_top_10 function was only displaying the records from 9 and below, even if there was a score of 10 in the google sheet.</p>
<p>Solution: I Joined a call in study_group channel on slack, and with the help of DaveHorrocks_5P, Daisy_mentor, Charlie, and Sensei Bim, it got solved. What I learned in the process was how they debug and look at the problem from different angles. Not to mention how much I admire the intelligence and the positive energy between them. They are always ready to offer help.</p>

#### *Unfixed Bugs*
1 <p>For menu item 3: **restart**, players can still access it from the beginning of the game. So they can skip the step of creating the player name and start the quiz right away. The system will have their score written in the google sheet, but without any player name as a result.</p>

2 <p>The player name is not unique at the moment, due to time limit, I didn't manage to fix it. It sure would be a nice thing to have.</p>

## **Deployment**
Heroku
  - Login on the [Heroku](https://id.heroku.com/login) website, [create](https://signup.heroku.com/login) your free account if you don’t have one already.
  
  <img src="assets/screenshots/heroku-signup.png" width="800">

- On your dashboard, click on the **New** button on the top right corner, and then click on **Create new app** as shown below

<img src="assets/screenshots/heroku-newapp.png" width="800">

- Next, type in your project name, it has to be unique, then choose your region and click on **Create App**

<img src="assets/screenshots/heroku-appname.png" width="800">

- You will come to the next screen, and we will set the **Settings** first and then **Deploy**

<img src="assets/screenshots/heroku-ds.png" width="800">

- In the **Settings**, first you will set two Config Vars, one is our CREDS.json file, and another is to set the PORT to 8000 as shown below

<img src="assets/screenshots/heroku-settings.png" width="800">

- Then you will scroll down and add two buildpacks in the **Settings**, first **python** and second **nodejs**. Be aware of the order of these two, it has to be exactly like this, otherwise it will cause problems when we deploy the project.

<img src="assets/screenshots/heroku-buildpacks.png" width="800">

- That's all the settings we need to do. Now let's go to the **Deploy** tab. In the deployment method, I connected my Github, for this project. 

<img src="assets/screenshots/heroku-deploy-method.png" width="800">

- At the bottom of the page, choose **Manual deploy** and then click on **Deploy Branch** button

<img src="assets/screenshots/heroku-manuald.png" width="800">

- The deployment process will start, and it will take a few minutes

<img src="assets/screenshots/heroku-deploying.png" width="800">

- When the deployment has completed, it will display **Your app was successfully deployed** with a **View** button below the message, that will take you to your deployed site.

<img src="assets/screenshots/heroku-d-success.png" width="800">

<br>

## **Credits**

- Code Institute's [Love Sandwiches project](https://github.com/Code-Institute-Solutions/love-sandwiches-p5-sourcecode/tree/master/05-deployment/01-deployment-part-1)

- Tutor support from Code Institute for helping me out when I got stuck. Special shout out to Ger, who helped me to solve multiple problems that was driving me nuts. 

- The display_top_10_scores function didn’t work properly, and I tried different things. In the end Mr Suffar’s [video](https://www.youtube.com/watch?v=HRJRq2r7eL8) gave me an idea and I took part of his code, and modified it to work in mine.

- [Stackoverflow](https://stackoverflow.com/) for researching a list of things, [this article](https://www.programiz.com/python-programming/methods/string/isalnum) to learn about isalnum() for checking any characters that are not letter or digit, that I used in the check_player_name function as one of the validator.

- The Interesting facts content came from the sources below:
  - Question 1 [reptilesmagazine.com](https://reptilesmagazine.com/snake-cardiovascular-system-anatomy/)
  - Question 2 [biomedicalsciences.unimelb.edu.au](https://biomedicalsciences.unimelb.edu.au/departments/department-of-biochemistry-and-pharmacology/engage/avru/blog/sneaky-snake-facts#:~:text=As%20snakes%20are%20so%20flexible,even%20more%20than%20us%20humans.&text=Snakes%20belong%20to%20the%20vertebrates,mammals%2C%20birds%2C%20and%20fish.)
  - Question 3-7 [nationalgeographic.com](https://www.nationalgeographic.com/animals/reptiles/facts/snakes-1)
  - Question 8 [elementalscience.com](https://elementalscience.com/blogs/science-activities/how-do-snakes-smell-the-jacobson-organ#:~:text=The%20Jacobson%20organ%20is%20found,the%20tips%20of%20the%20fork.)
  - Question 9 [safarisafricana.com](https://safarisafricana.com/most-venomous-snakes/)
  - Question 10 [guinnessworldrecords.com](https://www.guinnessworldrecords.com/world-records/70265-longest-venomous-snake)



## **Acknowledgments**
My mentor Mr. ADEGBENGA ADEYE for his continuous and structured feedback and support. My project won't be the same without his valuable advice. 

Tutor support at Code Institute. They are always there when I need help, I am really grateful for that.

Fellow students on the Slack community for their help and support, this amazing community constantly inspires me and it feels nice to learn and grow with them together.

Most importantly, I would like to thank my husband who supported me every step in my coding journey, and my son who inspired me to build this project. 

THANK YOU ALL!!!







