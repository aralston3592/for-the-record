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

[Wireframe Mockups](/assets/wireframes/ftr-wireframes.bmpr "For the Record")

These wireframe mockups show how I intended the site design and layout to look on various devices, the streamline 
design does not vary too much between device sizes to bring a familiarity to revisiting users. 

## UX

The [Materialize CSS](https://materializecss.com/ "Materialize") standard 12 column fluid responsive grid system 
allowed for an easily structured mobile-first design. It also made sure that Home Pub Quiz is responsive over 
varying screen sizes and devices. Images below show how the design and layout scales to suit each device size:

* Mobile Designs: [Mobile Welcome Page](/assets/img/ftr-welcome-mobile.png "Mobile Welcome Page"), [Mobile Records Page](/assets/img/ftr-records-mobile.png "Mobile Records Page"), [Mobile Login Page](/assets/img/ftr-login-mobile.png "Mobile Login Page"), [Mobile Add a Record Page](/assets/img/ftr-add-mobile.png "Mobile Add a Record Page"), [Mobile Genres Page](/assets/img/ftr-genres-mobile.png "Mobile Genres Page") 
* Desktop Designs: [Desktop Welcome Page](/assets/img/ftr-welcome-desktop.png "Desktop Welcome Page"), [Desktop Records Page](/assets/img/ftr-records-desktop.png "Desktop Records Page"), [Desktop Login Page](/assets/img/ftr-login-desktop.png "Desktop Login Page"), [Desktop Add a Record Page](/assets/img/ftr-add-desktop.png "Desktop Add a Record Page"), [Desktop Genres Page](/assets/img/ftr-genres-desktop.png "Desktop Genres Page")


## Features & Layout

### Welcome Page

Welcomes the user to For the Record, invites existing users to sign in and newcomers to register via two buttons that are centre page.
'For The Record' heading is located in the bottom left with the background image filling the screen behind.

### NavBar/Footer

#### NavBar
Logo and 'For the Record' title to the left with site navigation to the right. The NavBar allows the user to easily access the Record Collection, Add a Record, Browse by Genre and Login/Logout. 
Displayed on all pages below.
#### Footer
A small intro for users to the site along with a few links to online record stores. Copyright declaration visible here. Displayed at the bottom of all pages below.

### Register Page

New users are invited to register their details and choose a password to use when returning to the site.

### Login Page

Existing user can use their saved details and access the collection.

### Record Collection

Each record's artwork and title is displayed within a card with a link to purchase the record at the foot.
The record artwork image is a link to the record information page.
Each card has an information section hidden containing:

* Artist Name
* Label
* Genre
* Year
* Star Rating
* Review

When a user is active an update and delete button will be displayed below the record information.

### Record Page

Displayed after clicking on the album artwork of any record in the collection. This page shows the
record information along with options to update, delete or find out where to buy it.

### Genres Page

The Genres page provides a list of all genres currently stored in the database. Each of these listed genres provide
a link to the genre specific page showing each record in that genre.

For active users there is an option to add a genre at the foot of the list. 

### Genre Page

After selecting a genre from the list each record from that genre will be displayed here in the same cards as in the Record Collection Page.

### Add/Edit a Record/Genre Page 

Users can input the information via forms and easily add/edit the collections.

## Future Improvements

### Add a Record of the Month 
Give users a glimpse at the hottest record of the month.
### Record Club Listening Parties
Virtual listening parties organised by users would be streamed via the site.
### Search Record Collection
Add a search bar to the navbar allowing users to search keywords to find a specific record.

## Testing

All basic style and layout testing for each device size during development was done using Chrome's developer tools while previewing the site.

To validate my HTML I used [W3C HTML Validator](https://validator.w3.org/ "W3C HTML Validator").

To validate my CSS I used [W3C CSS Validator](https://jigsaw.w3.org/css-validator/ "W3C CSS Validator").


## Deployment

Site was deployed using [Heroku](https://www.heroku.com/ "Heroku"):

1. Log in to Heroku Dashboard.
2. Click on New dropdown menu on the right a choose Create New App.
3. Complete form then submit to create app.
4. Select App(for-the-record) from Dashboard.
5. Click on the Settings tab then find Reveal Config Vars in the Config Vars section.
6. Add Config Vars.
7. Click on the Deploy tab then Click on GitHub in the Deployment Method section.
8. Then Connect app to [GitHub Repository](https://github.com/aralston3592/for-the-record/ "GitHub Repository")
9. Deploy the app via Heroku using the Master Branch via the Manual Deploy Section.
10. Once completed Click View App button to begin using the app.

## Technology Used

* Wireframes: [Balsamiq](https://balsamiq.com/ "Balsamiq")
* Database: [Mongo DB](https://www.mongodb.com/ "MongoDB")
* Programming Languages: HTML, CSS, Javascript, Python
* Fonts & Icons: [Google Fonts](https://fonts.google.com/ "Google Fonts"), [Font Awesome](https://fontawesome.com/ "Font Awesome"), [Materialize CSS](https://materializecss.com/ "Materialize"). 
* Javascript: [JQuery](https://jquery.com/ "JQuery")
* Responsive Design: [Materialize CSS](https://materializecss.com/ "Materialize")
* IDE: [Gitpod](https://gitpod.io/ "GitPod")
* Version Control: [Git](https://git-scm.com/ "Git")
* Repository Host/Deployment: [Heroku](https://www.heroku.com/ "Heroku")