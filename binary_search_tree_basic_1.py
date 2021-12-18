#question: Alice has some cards with numbers written on them
#. She arranges the cards in decreasing order, and lays them out face
#down in a sequence on a table. She challenges Bob to pick out the
#card containing a given number by turning over as few cards
#as possible. Write a function to help Bob locate the card.
# return the value of cards position which matches the query

# binary search function
def binary_search(lowPos,highPos,outputMsg):
   while lowPos <= highPos:
      # get the mid position
      midPos = (lowPos + highPos) // 2
   
      getOutput = outputMsg(midPos)
      if getOutput == "found":
            return midPos
      elif getOutput == "left":
            highPos = midPos - 1
      elif getOutput == "right":
            lowPos = midPos + 1
         
      # if all going to be wrong then simply return -1 
   return -1


# function to get the output 
def locate_card(cards,query):
   
   def outputMsg(midPos):
      
      midEle = cards[midPos]
      
      if midEle == query:
         if midPos - 1 >= 0 and cards[midPos - 1] == query:
            return "left"
         else:
            return "found"
         
      elif midEle < query:
         return "left"
      else:
         return "right"
   
   return binary_search(0, len(cards)-1, outputMsg)
   
      
     



# an array for all possible cases for this above problem
cases = []

#listed the possible cases
case = {
   "inputs":{
      "cards" :[12,11,9,8,7,4,2,1],
      "query" :8
   },
   "output": 3
   }

# test case 1.Query may be placed middle in the list
cases.append(case)

# test case 2. Query is the first element of the list
cases.append({
   "inputs":{
      "cards":[17,14,13,11,10,9,7,5],
      "query": 17
   },
   "output":0
})

# test case 3. Query is the last element of the list
cases.append({
   "inputs":{
      "cards":[17,14,13,11,10,9,7,5],
      "query": 5
   },
   "output":7
})

# test case 4. There is no query in the list and output is -1
cases.append({
   "inputs":{
      "cards":[17,14,13,11,10,9,7,5],
      "query": 3
   },
   "output":-1
})


#test case 5. This is an empty list and output is -1
cases.append({
   "inputs":{
      "cards":[],
      "query": 5
   },
   "output":-1
})

# test case 6. One element in the list and it is the query.
cases.append({
   "inputs":{
      "cards":[12],
      "query": 12
   },
   "output":0
})


# test case 7. There is multiple repeatative element in the list.
cases.append({
   "inputs":{
      "cards":[17,14,14,13,11,11,11,10,9,7,7,7,5],
      "query": 10
   },
   "output":7
})


# test case 8. There is repeatative query in the list
cases.append({
   "inputs":{
      "cards":[10,9,9,9,9,7,5],
      "query": 9
   },
   "output":1
})


# test case 9. There is multiple repeatative element in the list and also multiple repeatative query in the list.
cases.append({
   "inputs":{
      "cards":[11,11,11,10,10,9,9,9,9,9,7,5,5,5,5],
      "query": 9
   },
   "output":5
})

# result = locate_card(cases[7]["inputs"]["cards"],cases[7]["inputs"]["query"])
# print(result)
# print(result == cases[7]["output"])

for index,val in enumerate(cases):
   result = locate_card(val["inputs"]["cards"],val["inputs"]["query"])
   fullTuple = (result, result==val['output'])
   print(fullTuple)

