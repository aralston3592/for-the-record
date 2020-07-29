# For The Record...

Discover new, classic and ultimately delightful sounds through vinyl sharing service For The Record. Show off your record collection
to friends, family and also complete strangers and let thrm know where they can find them. 

## Purpose

For The Record is built for my Data Centric Development Milestone Project as part of Code Institute's Full Stack Web Developer 
course. Looking through my record collection at home I was thinking of the best way to share these with as many people as possible
and what I've come up with is a record sharing app that allows all users to share, discuss and discover music from all genres and
backgrounds. Via the app users can be add, edited and remove records for other users perusal. I feel this could develop into a Record 
CLub with members, records of the week and record listening parties.

## Wireframe Mockups

Before starting the project I put together a few wireframe mockups so I had an idea of what I was trying to 
create and what I should include. It also allowed me to see how the features would be scaled and incorporated 
over various device sizes. These were created using [Balsamiq](https://balsamiq.com/ "Balsamiq"):

[Wireframe Mockups](/assets/wireframes/home-pub-quiz.bmpr "Home Pub Quiz")

These wireframe mockups show how I intended the site design and layout to look on various devices, the streamline 
design does not vary too much between device sizes to bring a familiarity to revisiting users. 

## Theme



## UX

The [Materialize CSS](https://materializecss.com/ "Materialize") standard 12 column fluid responsive grid system 
allowed for an easily structured mobile-first design. It also made sure that Home Pub Quiz is responsive over 
varying screen sizes and devices. Images below show how the design and layout scales to suit each device size:

* Mobile Designs: [Mobile Home Page](/assets/img/HPQ-mobile-home.png "Mobile Home Page"), [Mobile Quiz Page](/assets/img/HPQ-mobile-quiz.png "Mobile Quiz Page"), [Mobile Score Page](/assets/img/HPQ-mobile-score.png "Mobile Score Page") 
* Tablet Designs: [Tablet Home Page](/assets/img/HPQ-tablet-home.png "Tablet Home Page"), [Tablet Quiz Page](/assets/img/HPQ-tablet-quiz.png "Tablet Quiz Page"), [Tablet Score Page](/assets/img/HPQ-tablet-score.png "Tablet Score Page")
* Desktop Designs: [Desktop Home Page](/assets/img/HPQ-desktop-home.png "Desktop Home Page"), [Desktop Quiz Page](/assets/img/HPQ-desktop-quiz.png "Desktop Quiz Page"), [Desktop Score Page](/assets/img/HPQ-desktop-score.png "Desktop Score Page")


## Features & Layout

### Welcome Page

Welcomes the user to For the Record and invites existing users to sign in and newcomers to register via two buttons that are centre page.
For The Record heading is located in the bottom left of screen and the background image created

### Quiz Rounds

Each of the six quiz rounds have a round specific category and are made up of five trivia questions. The categories for each round are: 

* Food & Drink
* Science & Nature
* Movies
* Music
* Sport
* General Knowledge

In each round the user may choose one of a possible three answers for each question and their score will be calculated depending on their input. A correct answer will add one point to the user's score, however an incorrect answer will result in a one point deduction, meaning it may be a better idea to leave an question unanswered if the user is not certain of the answer. 

The Home button at the bottom of each quiz round allows the user to restart the quiz by taking them back to the langing page. The next button allows the user to access the next round of the quiz. The complete button at the foot of round 6 totals the user's score and takes them to the score page.

### Score Page

The score page is where the user is taken upon completion of the quiz and aloows the user to see their total score. It also allows them to challenge their friends and family to take the quiz by sharing on social media. The social media share buttons have been added using [Share This](https://platform.sharethis.com/ "Share This Platform").

## Future Improvements

### Split Rounds Into Individual Quizzes
Add more questions to each round and make them individual quizzes that can be accessed by a category button on the landing page.
### High Scores Page
Allow users to input details and keep a leaderboard of all participants to build mor competition between users and drive up usage.
### Add More Categories 
Bring in more categories to fit in with above suggestion to create an individual quiz from each category. This could involve bringing in more specific categories and sub-categories that would make the quiz more accessible for all ages including but not limited to: Children's Trivia; Decade Specific Music and Movies; TV Shows; History; Geography; Specific Sports(e.g. Football, Rugby, Badminton etc.).

## Testing

All basic style and layout testing for each device size during development was done using Chrome's developer tools while previewing the site.

To validate my HTML I used [W3C HTML Validator](https://validator.w3.org/ "W3C HTML Validator").

To validate my CSS I used [W3C CSS Validator](https://jigsaw.w3.org/css-validator/ "W3C CSS Validator").

I passed my JS through [JSHint](https://jshint.com/ "JSHint") linter without any issues.

Used family and friends to perform small beta test before deployment. 

## Deployment

Site was deployed using [GitHub](https://github.com/ "GitHub"):

1. Open [GitHub Repository](https://github.com/aralston3592/pub-quiz "Home Pub Quiz").
2. Click on SETTINGS then scroll down to GitHub PAGES.
3. Select master branch as the SOURCE.
4. 'Your site is published at https://aralston3592.github.io/pub-quiz/' will appear on screen.
5. Site deployed, click link to access.

## Technology Used

* Wireframes: [Balsamiq](https://balsamiq.com/ "Balsamiq")
* Programming Languages: HTML, CSS, Javascript
* Fonts & Icons: [Google Fonts](https://fonts.google.com/ "Google Fonts"), [Materialize CSS](https://materializecss.com/ "Materialize"), [Share This](https://platform.sharethis.com/ "Share This Platform"). 
* Javascript: [JQuery](https://jquery.com/ "JQuery")
* Responsive Design: [Materialize CSS](https://materializecss.com/ "Materialize")
* IDE: [Gitpod](https://gitpod.io/ "GitPod")
* Version Control: [Git](https://git-scm.com/ "Git")
* Repository Host/Deployment: [GitHub](https://github.com/ "GitHub")