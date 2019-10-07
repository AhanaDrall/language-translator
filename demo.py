from textblob import TextBlob

blob= TextBlob(input("enter what you want to translate: "))
print(blob.detect_language())
 
print (blob.translate(to='fr'))