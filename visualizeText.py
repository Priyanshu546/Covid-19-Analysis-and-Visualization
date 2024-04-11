dataset3= pd.read_csv("covid+death.csv") 
dataset3.head()
dataset3.tail()
dataset3.groupby(["Condition"]).count()
# import word cloud 
from wordcloud import WordCloud 

sentences = dataset3["Condition"].tolist() 
sentences_as_a_string = ' '.join(sentences) 


# Convert the string into WordCloud 
plt.figure(figsize=(20, 20)) 
plt.imshow(WordCloud().generate(sentences_as_a_string)) 
column2_tolist= dataset3["Condition Group"].tolist() 

# Convert the list to one single string 
column_to_string= " ".join(column2_tolist) 

# Convert the string into WordCloud 
plt.figure(figsize=(20,20)) 
plt.imshow(WordCloud().generate(column_to_string)) 
