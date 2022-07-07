# Jr Data Scientist Evaluation 1
Hello, my name is Chandra Kiran. Iam sharing my solutions for all the questions in the evaluation1. I have executed each question in a seperate python file and attached the same here. 
## Part 1
### Qsn no-1 : Write a regex to extract all the numbers with orange color background from the below text in italics.
### {"orders":[{"id":1},{"id":2},{"id":3},{"id":4},{"id":5},{"id":6},{"id":7},{"id":8},{"id":9},{"id":10},{"id":11},{"id":648},{"id":649},{"id":650},{"id":651},{"id":652},{"id":653}],"errors":[{"code":3,"message":"[PHP Warning #2] count(): Parameter must be an array or an object that implements Countable (153)"}]}
Solution : I have pasted the text in tha text file. Then imported the text file into the python.Applied the regex to the text to extract the numbers. Also i have split the text  to extract only orange colour words
![image](https://user-images.githubusercontent.com/108783651/177749280-f1b82efd-e003-4d09-93d2-0299727ca73d.png)

### Qsn no-2 : Here’s the list of reviews of Chrome apps - scraped from Playstore.  DataSet Link
### Problem statement - There are times when a user writes Good, Nice App or any other positive text, in the review and gives 1-star rating. Your goal is to identify the reviews where the semantics of review text does not match rating. Your goal is to identify such ratings where review text is good, but rating is negative- so that the support team can point this to users. Deploy it using - Flask/Streamlit etc and share the live link. 
Solution : 



### Qsn no-3 : Ranking Data - Understanding the co-relation between keyword rankings with description or any other attribute. Here’s the dataset. 
Solution : Imported the file into python using pandas. The dataset contains 9 Attributes and 3065 columns. Rank attritube has 16 null values and same dealtwith using dropna.I have encoded the object type attributes using Labelencoder from sklearn.preprocessing. 
Now applied correlation to the dataset and visualised using seaborns heatmap. 
![image](https://user-images.githubusercontent.com/108783651/177752624-90be5472-bcea-4f74-b722-472f6a35f438.png)

#### Answered Suggested questions
#### 1.	Is there any co-relation between short description, long description and ranking? Does the placement of keyword (for example - using a keyword in the first 10 words - have any co-relation with the ranking)?
Answr : Yes there is a negative corrrelation betwen short and long descriptions as indicated from the correlation matrix.
#### 2.	Does APP ID (Also known as package name) play any role in ranking?  
The App package has a postive correlation with the rank which indicates customers favoured interests to specific apps
#### 3.	Any other pattern or good questions that you can think of and answer?
Answr : Based on App ID, Vivaldi browser was the lowest rated. It was not even among top 16 in the ranks
        Based on keyword, Android browser was the best rated.Also fast browser was least rated. 
