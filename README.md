<p align="center"> 
<img src="https://github.com/cfaulkner985/hollywood-reviews/blob/master/static/img/hollywood-reviews-logo.png">
</p>

# ReadMe

Link to view the website - https://hollywood-reviews.herokuapp.com/

I am creating a moved based website called Hollywood reviews. This website will be for movie lover who want to share their views on the latest or other movies they have seen. Also the website will include a movie database so if the user wants to find out information about the movie eg. Directors, actors then they will find it here. If there is a chance that the movie is not here then they will be able to add it as there is an add movie function on the site.
# UX
This website is based for people of all ages as movies are something that everyone no matter what age can enjoy. It is also for people who like to give their thoughts on a movie either if its good or bad.
Ideal user of this site would be:
* People who enjoy watching movies.
* People who enjoy giving their thoughts on a movie
* People who are interested to see what other people thought of a particular movie
* People who want information on particular movies
* People who want to add new movies to the site to keep it updated for other.
In this website I have a home page which is the page that will load up when you enter the site. This is where the user will be able leave a review. They will fill in the fields listed below:
  * First name
  * Last name
  * Country
  * Date of Review
  * E-Mail
  * Movie Reviewed
  * Rating
  * Thoughts

Once they have filled in this information then they click on the ‘Submit Review’ button to leave their review.

Wireframe mock-up for [Home Page](https://github.com/cfaulkner985/hollywood-reviews/blob/master/Wireframes/Wireframe%20-%20Home%20Page.pdf)

The next page is the reviews page where they can see the review they have left. They click on the collapsible tab and they will see all the information they provided. They have two options if they are not happy with the review. They could edit or delete using the ‘Edit’ and ‘Delete’ buttons provided to the right of the review

Wireframe mock-up for [Reviews Page](https://github.com/cfaulkner985/hollywood-reviews/blob/master/Wireframes/Wireframe%20-%20Reviews.pdf)

If the user decides to click on the ‘Edit’ button then it will bring them to a page that is similar to the Home Page. They will be able to edit any choices they make previously. Once they are happy with their changes then they can click on ‘Edit Review’ button to update the changes. The changes will then appear updated on the Reviews page.

Wireframe mock-up for [Edit Reviews Page](https://github.com/cfaulkner985/hollywood-reviews/blob/master/Wireframes/Wireframe%20-%20Edit%20Reviews.pdf)

The movie page is a database of over 2000 movies and is viewed on a collapsible menu similar to the reviews page. The main heading will show the movie’s title, IMDB rating and rotten tomatoes rating. Once the user clicks to expand it then they will see:

* Year Released
* Run Time
* Actors
* Director
* Genres
* Plot

If the user cannot find the movie they are looking for then they have the option of clicking on the ‘Add Movie’ button to add a new movie to the site

Wireframe mock-up for [Movies Page](https://github.com/cfaulkner985/hollywood-reviews/blob/master/Wireframes/Wireframe%20-%20Movies.pdf)

If the user does click on the ‘Add Movie’ button then it will bring them to the add movie page. This page will let the user add a movie and will be able to be seen by anyone else who visits the site. The user will have the same information as the movies page to fill out to insert the movie. Once they are happy they click on the ‘Insert Movie’ button and the movie will be added to the Movies page.

Wireframe mock-up for [Add Movies Page](https://github.com/cfaulkner985/hollywood-reviews/blob/master/Wireframes/Wireframe%20-%20Add%20Movie.pdf)

# Features
## Existing Features
### All Pages
* Logo appears on the top right of every page and brings the user back to the home page by clicking on it.
* Navigation bar allows user to navigate through the site by clicking on the word of the page they want to go to.
*  Side navigation bar is used when the screen gets smaller to a mobile size view. It allows the user to navigate through the site by clicking on the word of the page they want to go to


### Home Page
* Slider showing 3 images which are on a constant loop but can be changed between by clicking on the little circles below the image.
* There is a form for the user to fill out to leave a review. All of the input boxes are text boxes apart from the country and date of review. The user will have to choose their country from a list using a dropdown box with all countries listed. The date of review will bring up a date picker box where the user can select the exact date that they left the review.
* The page also has a submit button where the user will press to submit the review that have left will be brought to the reviews page

### Reviews Page
* This will display the list of reviews in a Collapsible. The heading of the collapsible will display movie reviewed and date review and when the user clicks on this it will display the rest of the information that the user left.
* There is an edit button that when the user clicks it will bring them to an edit review page where they will be able to edit the review they have left.
* There is also a delete button that when the user clicks it will delete the review that they have left. This cannot be undone when pressed.

### Edit Reviews Page
* There is a form for the user to fill out to edit a review. All of the input boxes are text boxes apart from the country and date of review. The user will have to choose their country from a list using a dropdown box with all countries listed. The date of review will bring up a date picker box where the user can select the exact date that they left the review. The user will see the information they have previously left to edit.
* The page also has an edit review button where the user will press to submit the review that have left which will update in the reviews page.

### Movies Page
* This will display the list of movies in a Collapsible. The heading of the collapsible will display the move title and when the user clicks on this it will display the rest of the information about the movie.
* The page also has an add movie button where the user will press to add movie to the movies page. It will bring them to the add movies page
* This page also has a search funtion where the user can search for a movie on the list of movies by typing it in and clicking on the submit button

### Add Movies Page
* There is a form for the user to fill out to add a movie. All of the input boxes are text boxes. This information will be saved on the Movies Page once the user has submitted the new movie
* The page also has an ‘Add Movie’ button where the user will press to add the movie that have inputted which will update in the movies page.

## Features to implement in the future
* I want to be able to see the poster of the movies on the site so the user can see what the movie what the movie poster is. I should be able to get most if not all of them online.
* I would want to link the movie reviewed to the actually movie in the database. So when the user types in a movie they want to review a list of them will appear which will be linked to the movie database.

## Technologies Used
* I have used HTML, CSS and JavaScript programming languages.
* I used MongoDB to store the information for the sites including the movie database and reviews database.
* I used Gitpod (https://gitpod.io/) to build the website.
* I used Materaize (https://materializecss.com/) get HTML, jQuery and CSS code for my project.
* I used JQuery (https://jquery.com/) for the JavaScript in the website
* I used Material Icons (https://material.io/resources/icons/to add the icons for the buttons
* Block templates were used so I don’t have to repeat my code to save time
* I used autopep8 (https://github.com/hhatto/autopep8) to tidy up my python code
* Other rechnologies used can be found in my [Requirements](https://github.com/cfaulkner985/hollywood-reviews/blob/master/requirements.txt) file.
* The project also uses AutoPrefixer (https://autoprefixer.github.io/) and makes sure the CSS is valid for all web browsers

## Committing files to GitHub
When I make changes to each file I push them from GitHub from GitPod and below are the steps I do to do this. This is essential as to not losing any of the work I have done.
1.	On my GitPod project scroll down and click on the command prompt at the bottom
2. Check status by typing in ‘git status’
3.	Type ‘git add’ to add the files for staging
4.	Type ‘git commit -m "Add all files" to commit the files
5.	Type ‘git push’ to push the files to GitHub

## Testing
Testing was done on a seperate document which is: [Testing.md](https://github.com/cfaulkner985/hollywood-reviews/blob/master/Testing.md)

## Flask and Heroku
1. The first this I did when creating my project was install flask. I did this my typing in ‘pip install flask’ into my project’s Gitpod terminal. Once I created the python file I ran a test to make sure that it was linked correctly and assigned it a port which I would then link to Heroku.
2. Before I go any further with Heroku I have to create a requirements file. So In my terminal I type ‘pip3 freeze --local > requirements.txt and this will create the requirements file on Gitpod.
3. I also have to create a Profile before I push the files over to Heroku. To do this I type ‘echo web: python app.py > Procfile’ into the terminal and this will add the Profile to my list of files.
4. I signed into heroku using ‘heroku login’ and once I was logged in I added the files to heroku. I created a new Git repository and then deployed it to the Heroku repository by typing ‘git push heroku master’ into the terminal.
5. In Heroku I then linked the IP and port which I created in the python file. I set the IP to ‘0.0.0.0’ and the Port to ‘5000’. I also linked MONGO_URI, MONGO_DBNAME which were created in Mongo DB. I also set the SECRET_KEY which was created on (https://randomkeygen.com/) then I opened the app in Heroku and it opened up as expected.

## Deployment
This project was developed using the GitPod (https://gitpod.io/) and was committed to git and pushed to GitHub using the built in function within GitPod.
In GitHub the repository is cfaulkner985/Hollywood-reviews (https://github.com/cfaulkner985/hollywood-reviews). Below is the way to deploy the files to Heroku:
1. From by GitPod terminal I loginto my Heroku account by typing in 'heroku login' and press return 
2. I then press any key on the keyboard to continue and it will log me into my heroku account
3. Also from the GitPod terminal I push the files to Heroku by typing in 'git push heroku master'
4. From heroku I click on my project which is 'hollywood reviews'
5. I then click on Deploy which is a tab along the top
6. From this page I scroll down to the bottom and click on 'Deploy Branch' and make sure 'master' is selected.
7. After this is then lets me know it is seccessfully deployed and can be found at 'https://hollywood-reviews.herokuapp.com/'


## How to run this project locally
1. To locally start all of the process types that are defined in your Procfile:
2. I type in 'heroku local' into the terminal (heroku local is a shorter alternative to heroku local:start which does the same thing.)
3. To locally start I then type in 'heroku local web'
4. I can now the app locally.
5. I then press Ctrl+C to shut it down when I am done.

## Credits
### Images
Image in my logo - https://dcassetcdn.com/design_img/3304282/613725/613725_18135564_3304282_5a635a25_image.jpg the rest was done on ‘Paint’

Image for favicon - https://i.pinimg.com/originals/7f/d3/2b/7fd32b6ebfa4d4fdb363eaff298c2e08.jpg

Images for the slider
Image 1 – https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQRpBgcQPzFKor3qT8lJNGBhJW3EJS-PhIVcw&usqp=CAU

Image 2 – https://d12dkjq56sjcos.cloudfront.net/pub/media/wysiwyg/losangeles/06-route-detail/View-Of-Hollywood-Street-Neon-Signs-Big-Bus-Tours-Los-Angeles-Hollywood-Loop.jpg

Image 3 -  https://www.shortlist.com/media/imager/202002/46036-original.jpg

### Other
I got help for the ratings slider bar from https://css-tricks.com/styling-cross-browser-compatible-range-inputs-css// which can be viewed in my Reviwes and Edit Reviews page

I got help with the search for a movie funtion from https://stackoverflow.com/questions/49937047/alert-notification-not-found-after-search-string-on-page-html/49937156

My mentor Rohit Sharma was a great help guided me through this project.
