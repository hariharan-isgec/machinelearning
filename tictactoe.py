# Check the versions of libraries
import numpy, random, os

lr = 1 #learning rate
bias = 1 #value of bias
weights = [random.random(),random.random(),random.random()] #weights generated in a list (3 weights in total for 2 neurons and the bias)
print("Iteration No,Type,Input 1,Input 2,weight1,weight2,bias, Desired output, Predicted Output, Error")

def Perceptron(ctr,input1, input2, output) :
   outputP = input1*weights[0]+input2*weights[1]+bias*weights[2]
   print(ctr+1,",Pre Correction,",input1,",",input2,",",weights[0],",",weights[1],",",weights[2],",",output,",",outputP)
   if outputP > 0 : #activation function (here Heaviside)
      outputP = 1
   else :
      outputP = 0
   
   error = output-outputP
   weights[0] += error * input1 * lr
   weights[1] += error * input2 * lr
   weights[2] += error * bias * lr
   print(ctr+1,",Post Correction,",input1,",",input2,",",weights[0],",",weights[1],",",weights[2],",",output,",",outputP,",",error)
   
# Teaching the Neural Network so that it build the Weights  
for i in range(50) :
   Perceptron(i,1,1,1) #True or true
   Perceptron(i,1,0,0) #True or false
   Perceptron(i,0,1,0) #False or true
   Perceptron(i,0,0,0) #False or false

# Now see What it has learnt 

x = int(input())
y = int(input())
outputP = x*weights[0] + y*weights[1] + bias*weights[2]
if outputP > 0 : #activation function
   FinaloutputP = 1
else :
   FinaloutputP = 0
#print("Predicted Output for", x, "or", y, "is : ", outputP, " Final Corrected Output is", FinaloutputP)   

