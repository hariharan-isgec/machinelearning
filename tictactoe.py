# Check the versions of libraries
import numpy, random, os

lr = 1 #learning rate
bias = 1 #value of bias
weights = [random.random(),random.random(),random.random()] #weights generated in a list (3 weights in total for 2 neurons and the bias)
#print("Iteration No,Type,Input 1,Input 2,weight1,weight2,bias, Desired output, Predicted Output, Error")

def ActivationFunction_2_nerons(input1, weights1, input2, weights2, bias, weights3) :
   outputP = input1*weights1+input2*weights2+bias*weights3

   if outputP > 0 : #activation function (here Heaviside)
      outputP = 1
   else :
      outputP = 0
	
   return outputP

def Perceptron_2_nerons(ctr,input1, input2, output) :
   outputP = ActivationFunction_2_nerons(input1,weights[0],input2,weights[1],bias,weights[2])
   
   error = output-outputP
   weights[0] += error * input1 * lr
   weights[1] += error * input2 * lr
   weights[2] += error * bias * lr
   #print(ctr+1,",Post Correction,",input1,",",input2,",",weights[0],",",weights[1],",",weights[2],",",output,",",outputP,",",error)
   
# Teaching the 2 Neuron Neural Network so that it learns to decide GameOver cominations   
for i in range(50) :
   Perceptron_2_nerons(i,1,1,0) #True or true
   Perceptron_2_nerons(i,1,0,0) #True or false
   Perceptron_2_nerons(i,0,1,0) #False or true
   Perceptron_2_nerons(i,0,0,1) #False or false

# Now see What it has learnt 
board_row1 = [1,1,2]
board_row2 = [2,1,2]
board_row3 = [1,2,1]
#x = int(input())
#y = int(input())
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
 
game_status_row1 = ActivationFunction_2_nerons(check_game_row1[0], weights[0], check_game_row1[1], weights[1], bias, weights[2])
game_status_row2 = ActivationFunction_2_nerons(check_game_row2[0], weights[0], check_game_row2[1], weights[1], bias, weights[2])
game_status_row3 = ActivationFunction_2_nerons(check_game_row3[0], weights[0], check_game_row3[1], weights[1], bias, weights[2])
game_status_across1 = ActivationFunction_2_nerons(check_game_across1[0], weights[0], check_game_across1[1], weights[1], bias, weights[2])
game_status_across2 = ActivationFunction_2_nerons(check_game_across2[0], weights[0], check_game_across2[1], weights[1], bias, weights[2])

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

   

