from textblob import TextBlob

blob= TextBlob(input("enter what you want to translate from English to French: "))
print(blob.detect_language())
b=(blob.correct()) 
print (b)
print (b.translate(to='fr')) 