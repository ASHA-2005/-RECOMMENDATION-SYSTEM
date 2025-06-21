# -RECOMMENDATION-SYSTEM

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: KONGARAPU ASHA 

*INTERN ID*: CT04DF84

*DOMAIN*: MACHINE LEARNING

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTOSH

#📌 Project Description – Recommendation System

🔍 Overview of the Task

As part of my internship at CODTECH IT SOLUTIONS, I was assigned Task 4, which involved building a Recommendation System. The main goal of this project was to create a system capable of suggesting relevant items (in this case, movies) to users based on their preferences. This task falls under the domain of machine learning and data science and is widely used in real-world platforms such as Netflix, Amazon, and YouTube.

The objective was to implement either Collaborative Filtering or Matrix Factorization techniques to build a system that understands user behavior and provides personalized recommendations. The project also required showcasing the final recommendations along with supporting evaluation metrics and a visual representation of the similarity between users.

 Technology and Tools Used

For this project, I utilized the following tools and technologies:

Platform: Visual Studio Code (VS Code)

Programming Language: Python

Libraries Used: NumPy, Pandas, Scikit-learn (for similarity computation)

Data Structure: User-item matrix with ratings

Algorithm: User-based Collaborative Filtering

All the code was written and executed in VS Code using Jupyter Notebook or Python script execution via terminal.

 Steps Performed:
 
Data Preparation:

I started by creating a user-item ratings matrix where rows represented users and columns represented movies. The values in the matrix were the ratings that users had given to specific movies.

User Similarity Calculation:

I used cosine similarity to compute the similarity between users based on their rating patterns. This generated a User Similarity Matrix that shows how closely the preferences of two users align.

Recommendation Generation:

Once the similarity matrix was built, I predicted the ratings for movies that the user had not rated. Based on these predictions, I recommended movies that were likely to be of interest to the target user. For instance, User 1 was recommended Movie 3 with a predicted rating score.

Output Interpretation:

The final output displayed:


Ratings matrix

User similarity matrix

Top recommended movie(s) for the target user

This output confirms that the collaborative filtering system was functioning correctly.

 Evaluation and Results:
 
The results were evaluated by checking the similarity scores between users and validating if the recommended movie made sense based on the ratings of similar users. The predicted score for the recommended movie was also considered a performance indicator. In this case, Movie 3 was recommended to User 1 with a predicted rating of 0.44, which was a reasonable suggestion given the data provided.

 Conclusion:
 
This project helped me understand how real-world recommendation systems are built and implemented. I learned how to:

Handle sparse data

Apply collaborative filtering techniques

Measure similarity between users

Generate meaningful recommendations based on data patterns

It also enhanced my practical skills in Python and data science libraries, and gave me hands-on experience in building an end-to-end recommendation system from scratch.

 Platform Used:
 
All the development work was done in Visual Studio Code (VS Code), which provided a smooth coding and debugging environment. I used the built-in terminal to run my scripts and check the outputs, and I managed all my files under a local project folder structure.

#OUTPUT

![Image](https://github.com/user-attachments/assets/8dc0e0ae-2c88-4f25-ac65-db4214811623)

