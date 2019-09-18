# Check the versions of libraries
import numpy, random, os

lr = 1 #learning rate part of NeuralNetwork Perceptron Algorithm
bias = 1 #value of bias part of NeuralNetwork Perceptron Algorithm
weights_2_neurons = [random.random(),random.random(),random.random()] #weight for 2 Neuron NeuralNetwork as per Perceptron Algorithm
weights_5_neurons = [random.random(),random.random(),random.random(),random.random(),random.random(),random.random()] #weight for 5 Neuron NeuralNetwork as per Perceptron Algorithm

##### Creating Neural Network Generic Functions ##### 
def ActivationFunction_2_nerons(input1, weights1, input2, weights2, bias, weights3) :
   outputP = input1*weights1+input2*weights2+bias*weights3

   if outputP > 0 : #activation function (here Heaviside)
      outputP = 1
   else :
      outputP = 0
	
   return outputP

def Perceptron_2_nerons(input1, input2, output) :
   outputP = ActivationFunction_2_nerons(input1,weights_2_neurons[0],input2,weights_2_neurons[1],bias,weights_2_neurons[2])
   
   error = output-outputP
   weights_2_neurons[0] += error * input1 * lr
   weights_2_neurons[1] += error * input2 * lr
   weights_2_neurons[2] += error * bias * lr
   
   
def ActivationFunction_5_neurons(input1, weights1, input2, weights2,input3, weights3, input4, weights4, input5, weights5, bias, weights6) :
   outputP = input1*weights1+input2*weights2+input3*weights3+input4*weights4+input5*weights5+bias*weights6

   if outputP > 0 : #activation function (here Heaviside)
      outputP = 1
   else :
      outputP = 0
	
   return outputP

def Perceptron_5_neurons(input1, input2, input3, input4, input5,output) :
   outputP = ActivationFunction_5_neurons(input1,weights_5_neurons[0],input2,weights_5_neurons[1],input3,weights_5_neurons[2],input4,weights_5_neurons[3],input5,weights_5_neurons[4],bias,weights_5_neurons[5])   
   
   error = output-outputP
   weights_5_neurons[0] += error * input1 * lr
   weights_5_neurons[1] += error * input2 * lr
   weights_5_neurons[2] += error * input3 * lr
   weights_5_neurons[3] += error * input4 * lr
   weights_5_neurons[4] += error * input5 * lr
   
   weights_5_neurons[5] += error * bias * lr
   #print("PostCorrection,",weights_5_neurons[0],",",weights_5_neurons[1],",",weights_5_neurons[2],",",weights_5_neurons[3],",",weights_5_neurons[4],",",weights_5_neurons[5],",",error)
   
def Teach_2_neurons():   
	# Teaching the 2 Neuron Neural Network so that it learns to decide Row wise GameOver cominations   
	for i in range(50) :
	   Perceptron_2_nerons(1,1,0)
	   Perceptron_2_nerons(1,0,0)
	   Perceptron_2_nerons(0,1,0)
	   Perceptron_2_nerons(0,0,1)
	   
def Teach_5_neurons():
	# Teaching the 5 Neuron Neural Network so that can judge GameOver  
	for i in range(50) :
	   Perceptron_5_neurons(1,0,0,0,0,1) 
	   Perceptron_5_neurons(0,1,0,0,0,1) 
	   Perceptron_5_neurons(0,0,1,0,0,1) 
	   Perceptron_5_neurons(0,0,0,1,0,1) 
	   Perceptron_5_neurons(0,0,0,0,1,1) 
	   Perceptron_5_neurons(0,0,0,0,0,0) 

##### End of Generic Neural Functions ########## End of Generic Neural Functions #####

##### Main Body ########## Main Body #####
# Speciifc Functions for Tic Tac Toe

# Game Related code Startes Here
	   
Teach_2_neurons()
Teach_5_neurons()
   
# Tic Tac Board Status 
board_row1 = [2,1,1]
board_row2 = [2,1,2]
board_row3 = [1,2,1]

# Check the Board Values to Pass it to Neural Network with 2 Neurons 
check_game_row1=[0,0]
check_game_row1[0]=abs(board_row1[0]-board_row1[1])
check_game_row1[1]=abs(board_row1[1]-board_row1[2])
check_game_row2=[0,0]
check_game_row2[0]=abs(board_row2[0]-board_row2[1])
check_game_row2[1]=abs(board_row2[1]-board_row2[2])
check_game_row3=[0,0]
check_game_row3[0]=abs(board_row3[0]-board_row3[1])
check_game_row3[1]=abs(board_row3[1]-board_row3[2])
check_game_across1=[0,0]
check_game_across1[0]=abs(board_row1[0]-board_row2[1])
check_game_across1[1]=abs(board_row2[1]-board_row3[2])
check_game_across2=[0,0]
check_game_across2[0]=abs(board_row3[0]-board_row2[1])
check_game_across2[1]=abs(board_row2[1]-board_row1[2])
 
game_status_row1 = ActivationFunction_2_nerons(check_game_row1[0], weights_2_neurons[0], check_game_row1[1], weights_2_neurons[1], bias, weights_2_neurons[2])
game_status_row2 = ActivationFunction_2_nerons(check_game_row2[0], weights_2_neurons[0], check_game_row2[1], weights_2_neurons[1], bias, weights_2_neurons[2])
game_status_row3 = ActivationFunction_2_nerons(check_game_row3[0], weights_2_neurons[0], check_game_row3[1], weights_2_neurons[1], bias, weights_2_neurons[2])
game_status_across1 = ActivationFunction_2_nerons(check_game_across1[0], weights_2_neurons[0], check_game_across1[1], weights_2_neurons[1], bias, weights_2_neurons[2])
game_status_across2 = ActivationFunction_2_nerons(check_game_across2[0], weights_2_neurons[0], check_game_across2[1], weights_2_neurons[1], bias, weights_2_neurons[2])

print("Tic Tac Toe Board:")
print("[", board_row1[0], "] [", board_row1[1], "] [", board_row1[2], "]")   
print("[", board_row2[0], "] [", board_row2[1], "] [", board_row2[2], "]")   
print("[", board_row3[0], "] [", board_row3[1], "] [", board_row3[2], "]")   
print("")
print("Game Over Status Row 1:-", game_status_row1)
print("Game Over Status Row 2:-", game_status_row2)
print("Game Over Status Row 3:-", game_status_row3)
print("Game Over Status Across 1:-", game_status_across1)
print("Game Over Status Across 2:-", game_status_across2)
print("")

# Pass the output of 2 Neuron Neural Network as Input to 5 Neurons Neural Network
FinalStatus = ActivationFunction_5_neurons(game_status_row1,weights_5_neurons[0],game_status_row2,weights_5_neurons[1],game_status_row3,weights_5_neurons[2],game_status_across1,weights_5_neurons[3],game_status_across2,weights_5_neurons[4],bias,weights_5_neurons[5])
print("Final Game Status:-", FinalStatus)   


   

