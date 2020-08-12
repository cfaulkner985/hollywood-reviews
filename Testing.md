<p align="center"> 
<img src="https://github.com/cfaulkner985/hollywood-reviews/blob/master/static/img/hollywood-reviews-logo.png">
</p>

# Testing

## All Pages
* Logo appears on the top right of every page and brings the user back to the home page by clicking on it.
* Navigation bar allows user to navigate through the site by clicking on the word of the page they want to go to.
<p align="center"> 
<img src="https://github.com/cfaulkner985/hollywood-reviews/blob/master/testing/logo-and-nav-bar.png">
</p>
* Side navigation bar is used when the screen gets smaller to a mobile size view. It allows the user to navigate through the site by clicking on the word of the page they want to go to
<p align="center"> 
<img src="https://github.com/cfaulkner985/hollywood-reviews/blob/master/testing/side-bar.png">
</p>
The navigation bar, logo and side bar load up on all pages as expected. Also, all of the links are working and are being directed to the corrected page including the logo link.

## Home Page
* Slider showing 3 images which are on a constant loop but can be changed between by clicking on the little circles below the image.
<p align="center"> 
<img src="https://github.com/cfaulkner985/hollywood-reviews/blob/master/testing/slider-images.png">
</p>

* There is a form for the user to fill out to leave a review. All of the input boxes are text boxes apart from the country and date of review. The user will have to choose their country from a list using a dropdown box with all countries listed. The date of review will bring up a date picker box where the user can select the exact date that they left the review.
* The page also has a submit button where the user will press to submit the review that have left will be brought to the reviews page
<p align="center"> 
<img src="https://github.com/cfaulkner985/hollywood-reviews/blob/master/testing/add-review.png">
</p>
The slider images go through on a loop as expected and can be moved quicker by clicking the little circle as expected. Typing in the input boxes are working as well as the country which brings up and list of countries as expected. Also, the date picker for date of review is working as expected. Also the ‘Submit Review’ button works as expected.

## Reviews Page
* This will display the list of reviews in a Collapsible. The heading of the collapsible will display movie reviewed and date review and when the user clicks on this it will display the rest of the information that the user left.
* There is an edit button that when the user clicks it will bring them to an edit review page where they will be able to edit the review they have left.
* There is also a delete button that when the user clicks it will delete the review that they have left. This cannot be undone when pressed.
<p align="center"> 
<img src="https://github.com/cfaulkner985/hollywood-reviews/blob/master/testing/reviews.png">
</p>
The reviews load up correctly and the new review and others display in a collapsible as expected. The Edit button brings me to the edit reviews page as expected and the delete button removes the review which is also as expected. 

## Edit Reviews Page
* There is a form for the user to fill out to edit a review. All of the input boxes are text boxes apart from the country and date of review. The user will have to choose their country from a list using a dropdown box with all countries listed. The date of review will bring up a date picker box where the user can select the exact date that they left the review. The user will see the information they have previously left to edit.
* The page also has an edit review button where the user will press to submit the review that have left which will update in the reviews page.
<p align="center"> 
<img src="https://github.com/cfaulkner985/hollywood-reviews/blob/master/testing/edit-reviews.png">
</p>
The Edit Review page load up correctly and displays the form to edit the reviews similar to the add reviews page. The old inputs appear so I can edit them which is what is supposed to happen. The field can be inputted the same way as reviews including the date picker and country option. The user then clicks on the Edit Review button and the reviews page updates as expected.
<p align="center"> 
<img src="https://github.com/cfaulkner985/hollywood-reviews/blob/master/testing/updated-reviews.png">
</p>

## Movies Page
* This will display the list of movies in a collapsible. The heading of the collapsible will displays movie title and when the user clicks on this it will display the rest of the information about the movie.
* The page also has an add movie button where the user will press to add movie to the movies page. It will bring them to the add movies page
* This page also has a search funtion where the user can search for a movie on the list of movies by typing it in and clicking on the submit button
<p align="center"> 
<img src="https://github.com/cfaulkner985/hollywood-reviews/blob/master/testing/movies.png">
</p>
<p align="center"> 
<img src="https://github.com/cfaulkner985/hollywood-reviews/blob/master/testing/search-bar.png">
</p>

The movies page loads up correctly when the link is clicked. The movies display in a collapsible and when you click on the heading it displays the rest of the information as expected. The user then can click on the Add Movie button which will bring the user to the add movies page as expected. Also when the user searches for the movie and clicks 'Submit'. It will bring them to the movie they want and if they keep pressing 'Submit' it will bring them to other matches. If the movie there are searching for is not there then nothing will happen when they hit the 'Submit' button

## Add Movies Page
* There is a form for the user to fill out to add a movie. All of the input boxes are text boxes. This information will be saved on the Movies Page once the user has submitted the new movie
* The page also has an ‘Add Movie’ button where the user will press to add the movie that have inputted which will update in the movies page.
<p align="center"> 
<img src="https://github.com/cfaulkner985/hollywood-reviews/blob/master/testing/add-movie.png">
</p>
The Add Movies page load up correctly and displays the form to add the movie. The input boxes appear to add the information all the information of the movie the user wishes to add. Once all inputted the user then clicks on the Insert Movie button and the movie page updates as expected.
<p align="center"> 
<img src="https://github.com/cfaulkner985/hollywood-reviews/blob/master/testing/updated-movies.png">
</p>

## Validation
I have used the W3C validators to make sure my HTML and CSS codes have no major errors. The links for these can be found below:
- W3C CSS validation (https://jigsaw.w3.org/css-validator/) 
- W3C Markup Validation (https://validator.w3.org/)
- I also used JSHint (https://jshint.com/) to validate there was no errors on the JavaScript file.

## Further Testing
*	I checked the website on different devices and from different locations and looks good.
*	I asked friend and family to check the website and let me know if there was anything they would to improve. They suggested added movie posters would be a good idea.
*	I have tested all pages on the following devices:
    * Desktop - Chrome (Version 83.0.4103.61), Firefox Version 76.0.1), Internet Explorer (Version 11)
    * Galaxy S5
    * Pixel 2
    * IPhone X
    * IPad
    * IPad Pro

All pages are aligned and look good on all these devices.
