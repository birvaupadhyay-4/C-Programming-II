sentence=input("enter sentence:")
def rev(sentence):
     words=sentence.split()
     rev=""
     for word in words:
        rev=rev + word[::-1] + " "
     print("reverse sentence:",rev)
          
rev(sentence)
