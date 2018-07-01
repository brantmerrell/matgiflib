# Try making a game of life visualization
# with the matgiflib framework.

import matgiflib as mgl
import matplotlib.pyplot as plt
import numpy as np


def game_of_life(board_len=200, p=0.2, timesteps=200, random_seed=666):
    
    # Set the game's initial condition (randomly)
    np.random.seed(random_seed)
    board = np.random.choice([0,1], p=[1.0-p, p], 
                             size=(board_len, board_len))

    # Construct the Gif object
    mygif = mgl.Gif("conway.gif", 4.0, 4.0, dpi=200)

    # Let the game run...
    for t in range(timesteps):

        print("Time step: {}".format(t))

        # Make a frame for the animation
        plot_state(board, mygif) 

        occupied = (board > 0)
       
        # Update each square of the board 
        for i in range(board.shape[0]):
            for j in range(board.shape[1]):

                # (periodic boundary)
                neighbor_count = np.sum([[occupied[ii%board.shape[0],
                                                   jj%board.shape[1]] for ii in [i-1,i,i+1]]\
                                                                       for jj in [j-1,j,j+1]])
                neighbor_count -= occupied[i,j]

                # Update according to the simple "biological" logic
                if occupied[i,j]:
                    if neighbor_count < 2 or neighbor_count > 3:
                        board[i,j] = 0
                else:
                    if neighbor_count == 3:
                        board[i,j] = 1


    # Plot the final state
    plot_state(board, mygif)

    # Close the Gif
    mygif.close()

    return



def plot_state(board, gif):

    # Begin the frame
    gif.start_frame()
    
    # From here on, it's just matplotlib...
    plt.title("Conway's Game of Life", family="serif",fontsize=10)
    
    plt.xticks(np.linspace(-0.5,board.shape[0]-0.5),[])
    plt.yticks(np.linspace(-0.5,board.shape[1]-0.5),[])
    plt.tick_params(length=0.0)
    plt.grid(linewidth=0.1,color="silver")

    plt.imshow(board,cmap="Greys")
    #plt.rc("text",usetex=True)
    plt.xlabel("Periodic Boundaries",family="serif",fontsize=10)
    plt.tight_layout()

    # End the frame
    gif.end_frame()

    return


#################################################
if __name__=="__main__":

    game_of_life(board_len=100, p=0.2, timesteps=100)


