# Jr Data Scientist Evaluation 1
Hello, my name is Chandra Kiran. Iam sharing my solutions for all the questions in the evaluation1. I have executed each question in a seperate python file and attached the same here. 
## Part 1
### Qsn no-1 : Write a regex to extract all the numbers with orange color background from the below text in italics.
### {"orders":[{"id":1},{"id":2},{"id":3},{"id":4},{"id":5},{"id":6},{"id":7},{"id":8},{"id":9},{"id":10},{"id":11},{"id":648},{"id":649},{"id":650},{"id":651},{"id":652},{"id":653}],"errors":[{"code":3,"message":"[PHP Warning #2] count(): Parameter must be an array or an object that implements Countable (153)"}]}
Solution : I have pasted the text in tha text file. Then imported the text file into the python.Applied the regex to the text to extract the numbers. Also i have split the text  to extract only orange colour words
![image](https://user-images.githubusercontent.com/108783651/177749280-f1b82efd-e003-4d09-93d2-0299727ca73d.png)

### Qsn no-2 : Here’s the list of reviews of Chrome apps - scraped from Playstore.  DataSet Link
### Problem statement - There are times when a user writes Good, Nice App or any other positive text, in the review and gives 1-star rating. Your goal is to identify the reviews where the semantics of review text does not match rating. Your goal is to identify such ratings where review text is good, but rating is negative- so that the support team can point this to users. Deploy it using - Flask/Streamlit etc and share the live link. 
Solution : The dataset contains 10 features. Among that text and ranking was necessary. Used nltk and regex libraries to clean the text.Used sentiment intensity analyzer to identify the sentiment of the review to categorise it as positive or negative. I have taken both rating 1 and 2 as low ratings and extracted the positive comments from it.
![image](https://user-images.githubusercontent.com/108783651/178002231-4e462261-60d7-4305-a1c8-bec6183f54d2.png)
#### Model deployment
I have used streamlit to deploy it. Live link - https://chandrakirank-jr-data-scientist-evaulu-lowratinganalysis-fm6tnq.streamlitapp.com/
## Web App Screenshots
![image](https://user-images.githubusercontent.com/108783651/178009212-26a569a5-a830-485e-b9f0-783900dbd20d.png)
![image](https://user-images.githubusercontent.com/108783651/178009430-e6e8039f-3491-41c0-aef2-9298f352b4a0.png)

### Qsn no-3 : Ranking Data - Understanding the co-relation between keyword rankings with description or any other attribute. Here’s the dataset. 
Solution : Imported the file into python using pandas. The dataset contains 9 Attributes and 3065 columns. Rank attritube has 16 null values and same dealtwith using dropna.I have encoded the object type attributes using Labelencoder from sklearn.preprocessing. 
Now applied correlation to the dataset and visualised using seaborns heatmap. 
![image](https://user-images.githubusercontent.com/108783651/177752624-90be5472-bcea-4f74-b722-472f6a35f438.png)

#### Answered Suggested questions
#### 1.	Is there any co-relation between short description, long description and ranking? Does the placement of keyword (for example - using a keyword in the first 10 words - have any co-relation with the ranking)?
Answr : Yes there is a negative corrrelation betwen short and long descriptions as indicated from the correlation matrix.
#### 2.	Does APP ID (Also known as package name) play any role in ranking?  
Answr : The App package has a postive correlation with the rank which indicates customers favoured interests to specific apps
#### 3.	Any other pattern or good questions that you can think of and answer?
Answr : Based on App ID, Vivaldi browser was the lowest rated. It was not even among top 16 in the ranks
        Based on keyword, Android browser was the best rated.Also fast browser was least rated. 
## Part 2
### Qsn no-1 : Check if the sentence is Grammatically correct: Please use any pre-trained model or use text from open datasets. Once done, please evaluate the English Grammar in the text column of the below dataset. DataSet Link
### Optional - if you can indicate the grammatical accuracy of sentences in percentage or on number scale (1-10), that would be an added plus - but is not essential. 
Solution :  I used a fine-tuned version of Google's T5 model. T5 is a text-to-text model, meaning given text, it produces a standalone piece of text. After importing the data, i have applied the T5 model on it. It produced the correct grammatical text. Then calculated the similarity score between imput text and produced text.
![image](https://user-images.githubusercontent.com/108783651/178004073-c4c9d633-f051-4868-ad6c-e753b0a09848.png)

## Bonus point questions
### Qsn no-1 : Write about any difficult problem that you solved. (According to us difficult - is something which 90% of people would have only 10% probability in getting a similarly good solution). 
Answr : I was working in paper making industry. For improving surface appearance of pape board(gloss), we use pair of rolls known as softnip rolls through which the    paper passes. The rolls are loaded onto the paper board. When ever foriegn particles (about 2mm to 50 mm size) comes with paper board, they will get stick with the rools and generate impression on board which is called stamping. The paper board with stamping cannot be used by the customer and is defective.By the time workmen check and clean it we would loose more than 10 metric tons of paper which was huge loss. 
I have instlled an IOT sensor to the roll bearings so that whenever foriegn particle sticks to the roll, the roll bearing vibration increases. IOT sensor captures the amplification in the bearing vibration and starts a hooter which will laet the crew. Crew will clean it immediately which reduces the loss.
This is the incidence where i have adopted the emerging technology to identify issues and reduce loss. We are planning to implement computer vision technology to identify defects on paper Board.
### Qsn no-2 : Formally, a vector space V' is a subspace of a vector space V if
###  V' is a vector space
###  every element of V′ is also an element of V.
#### Note that ordered pairs of real numbers (a,b) a,b∈R form a vector space V. Which of the following is a subspace of V?
#### ● The set of pairs (a, a + 1) for all real a
#### ● The set of pairs (a, b) for all real a ≥ b
#### ● The set of pairs (a, 2a) for all real a
#### ● The set of pairs (a, b) for all non-negative real a,b
Answr : The set of paris (a, 2a) for all real a is the subspace of vector space V.
A Subspace is a vector space included in another large vector space. To find a spce is whether is a subspace or not, we need to test twothings
1) To find the whether the sum of the vectors is in the subspace
2) Scalar multiplied vector is in the subspace 
That is, we are checking whether it is closed under additiona and scalar multiplication.

