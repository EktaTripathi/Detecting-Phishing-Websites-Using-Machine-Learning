# Detecting-Phishing-Websites-Using-Machine-Learning
# Introduction
There are number of users who purchase products online and make payment through 
various websites.There are some fake websites which ask user to enter their username, 
passwords and bank credentials etc. for malicious reasons. This type of websites is known 
as phishing website.
This project will help to detect phishing websites with the help of Machine Learning Algorithms. By entering the website URL, it will detect whether the website is malicious or not.  Predicted class is 1 means website is phishing. It contains malicious code. Predicted class is -1 means website is not phishing. It’s safe


The phishing website can be 
detected based on some important characteristics like URL and Domain Identity, and 
security and encryption criteria in the final phishing detection rate. Python modules will 
be used to extract features from URL to detect phishing websites like Presence of IP 
address in URL, Presence of @ symbol in URL, Number of dots in hostname, Length of 
hostname etc.



## Proposed System
### Admin Login
**1. Login**                    
**2. View Users**                 
**3. Add to Blacklist**           
**4. View List**                  
**5. Log out**  

### User Login
**1. Login**

**2. Preprocess**

**3. Random Forest**

**4. SVM**

**5. LogisticRegression**

**6. Prediction**

**7. Quit**

Admin Login
1. Login: In the login section, once the admin will enter the login credential then admin 
page will open.
2. View users: Here admin can see how many users have registered in the application.
3. Add to blacklist: Here admin can add any blacklisted website which is phishing.
4. View list: Here admin can see the blacklisted websites.
5. Log out: after clicking on the logout, it will back to the login page.



User Login
1. Preprocess: after clicking on Preprocess button, it will show the histogram of the 
extracted feature.
2. Random Forest: It will show the variable importance which describes which features 
are relevant and also random forest metrics value 
3. SVM: It will show the bar chart of MSE, MAE, R-Squared parameter, RMSE and 
accuracy.
4. LogisticRegression: It will also show the bar chart of MSE, MAE, R-Squared 
parameter, RMSE and accuracy.
5. Prediction: After entering the URL on the textbox once we clicked on the prediction 
button it will print the message that predicted class is 1 or -1. If the predicted class 
is 1 it means the website is phishing and if the predicted class is -1 it means the 
website is non-phishing.
 6. Quit: after clicking on the quit button, it will close the application.


Implementation Approaches
The proposed work is implemented in PyChram with libraries scikit-learn, pandas, 
matplotlib and other mandatory libraries. We downloaded dataset from Kaggle.com The 
data downloaded contains train set and test set separately with two different classes +1 and 
-1. The train dataset considered as train set and test dataset considered as test set. Machine 
learning algorithm is applied such as logistic regression and random forest. 

Implemented three machine learning algorithms on the given dataset for phishing website 
detection shows that Logistics regression model outperforms other models. The accuracy 
of Random Forest is high compared to other machine learning algorithms.

### SVM 96.74
### Logistic Regression 92.29
### Random Forest 96.85

## Predicted class is 1 means website is phishing. It contains malicious code.

## Predicted class is -1 means website is not phishing. It’s safe.

## Limitations of the System
• Since the accuracy rate of random forest is 96.85% so sometimes it failed to detect 
phishing sites.


• Sometimes after entering the phishing URL, it detects as non-phishing and vice-versa

