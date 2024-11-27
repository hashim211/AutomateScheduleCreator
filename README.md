Welcome to AutomateScheduleCreator project. The idea of this project is to create a schedule in the Excel filled automatically with this information : The day of the interview, which time interview will start,
duration of the interview, name and phone number of the person.
I programed this idea using a simple web page to help me faciliate filling the information.
I used Flask with HTML && JS.

![image](https://github.com/user-attachments/assets/92355977-fe84-4063-99f0-d7c9e468df34)
This is the page looks like, you can select the following :
-The time the interviews will start from.
-The time where last interview can be on in a day.
-Duration time for each candidate.
-Break time between each candidate if neede.
-Number of interviews in each day.
-Which day to start the interviews.
-Number of weeks of the interview.
-The name and phone of person("You can add phone number by putting - after the name i.e Hashim - 054000000").
-Note that you can put multi names by putting the comma(,) and it will split names. i.e Hashim - 0555552, Ma -00.
If no - is there the number will be null.
--------------------------------------------------------------------------------------------------
By clicking Generate Schedule button, You will get the result as JSON format and will be a button to download.
![image](https://github.com/user-attachments/assets/8e25ab51-05f2-49f7-806d-1c201bf4663e)
