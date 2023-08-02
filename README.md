# GPT2 Mental Health Advice Chatbot
## Introduction
Mental and physical health are crucial components of overall well-being, with mental health significantly impacting physical health and behaviors. To address this, an AI-based chatbot can serve as a primary tool to improve general well-being and provide support to those hesitant to seek professional help due to stigma and prejudice surrounding mental illness. The objective of this project is to build a model capable of receiving user questions and providing sensible, relevant, and human-like answers with strong grammar and spelling.
## Data
The data for this project was scraped from Reddit's r/mentalhealth and r/mentalillness subreddits using the Python Pushshift API Wrapper (PSAW). The data included both posts and comments, which were stored in separate Pandas DataFrames. The Submissions DataFrame contained the following columns:
* **Id**: Unique identification number for each submission.
* **Title**: The title of the submission, is often a question.
* **Selftext**: Additional content provided by the submission author.
* **Created**: The submission's creation date.
<br>The Comments DataFrame also had 'id' and 'created' columns, along with the following columns:
* **Link_id**: ID matching each submission with its associated comments.
* **Body**: The content of the comment.
<br>After cleaning and processing the data, duplicate comments and irrelevant entries were removed, resulting in 415,290 rows in the Submissions DataFrame and 1,556,846 rows in the Comments DataFrame.
## Exploratory Data Analysis
During the exploratory data analysis, I examined the most popular words in titles and comments, identified polarity and subjectivity, and calculated readability scores. The analysis revealed differences between titles and comments, with titles often having a negative connotation and comments having a neutral or positive connotation. The majority of sentences in both titles and comments showed neutral polarity, indicating a lack of emotional expression. Additionally, I used LDA (Latent Dirichlet Allocation) modeling to investigate topics, but the low coherence scores suggested challenges in revealing specific topics beyond the general theme of mental health.
![Alt Top 10 words in titles](https://github.com/yuliyaselevich/GPT2_mental_health_advice_chatbot/blob/main/Images/1.png)
![Alt Top 10 words in comments](https://github.com/yuliyaselevich/GPT2_mental_health_advice_chatbot/blob/main/Images/2.png)
## Modeling
For this project, I utilized the GPT-2 pre-trained model and the gpt-2-simple package. GPT-2 is an unsupervised deep learning transformer-based language model developed by OpenAI. The model was fine-tuned using 2,100 steps, with output samples generated every 500 steps. Although parameters like 'temperature' and 'top_k' were meant to control randomness and diversity in output, the model often produced seemingly random and nonsensical results regardless of these settings.
## Results
The results of the GPT-2 model demonstrated mixed performance. Some outputs were sensible and relevant, while others were nonsensical and repetitive. Despite these limitations, the model generally grasped the theme of mental health, producing outputs related to mental health issues.
## Conclusion
In conclusion, the GPT-2 model was utilized to explore its efficacy in providing mental health advice. Although the model showed some understanding of the theme, it often generated inaccurate and confusing outputs. To improve performance, potential steps include fine-tuning GPT-3, increasing data and training steps, and performing additional text cleaning. Ensuring effective filtering of output before model deployment is crucial to deliver reliable and meaningful mental health support.
### Methods Used
* Web Scraping
* EDA
* Natural Language Processing
* Sentiment Analysis
* Deep Learning
* Model Finetuning
### Technologies
* Python
* Pandas
* Seaborn
* Matplotlib
* Scikit-learn
* NLTK
* Gensim
* pyLDAvis
* GPT-2-simple
* Flask
* Starlette
* Tensorflow
## Featured Notebooks/Reports
* [Data Wrangling/Exploratory Data Analysis](https://github.com/yuliyaselevich/GPT2_mental_health_advice_chatbot/blob/main/Notebooks/data_wrangling_eda.ipynb)
* [Preprocessing/Modeling](https://github.com/yuliyaselevich/GPT2_mental_health_advice_chatbot/blob/main/Notebooks/preprocessing_modeling.ipynb)
* [Project Report](https://github.com/yuliyaselevich/Capstone-3-GPT2-Mental-Health-Advice/blob/main/Documents/Capstone3_ProjectReport.pdf)
## Contact
* [LinkedIn](https://www.linkedin.com/in/yuliyaselevich/)
