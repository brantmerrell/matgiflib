"""
Visualizing an N-body gravitational simulation
with the matgiflib framework.
"""

import matgiflib as mgl
import matplotlib.pyplot as plt
import numpy as np


def gravity_simulation(N=20, timesteps=500, dt=0.01):
    """
    Simulates N point masses under the influence
    of Newtonian gravity.
    """
    
    num_particles = 20
    np.random.seed(seed=668)

    # Construct the Gif object. "stride" controls how often
    # a frame is actually created.
    gravity_gif = mgl.Gif("gravity.gif", 2.54*3, 2.54*3, stride=3)

    # Set initial conditions
    masses = np.random.uniform(5.0,8.0,N),
    coords = np.random.normal(0.0,4.0,[N,2])
    vels = np.random.normal(0.0,2.0,[N,2]),

    # We'll use this to store the positions of the particles
    # over the course of the simulation.
    history = [coords[:]]

    # Run the simulation
    for t in range(timesteps):

        if t % 20 == 0:
            print("timestep: {}".format(t))

        # Compute pairwise forces: G*m1*m2/r^2
        diffs = [[coords[i,:] - coords[j,:] for j in range(coords.shape[0])] for i in range(coords.shape[0]) ]
        diffs = np.array(diffs)
        mags = np.linalg.norm(diffs, axis=2)
        mags[np.diag_indices_from(mags)] = 1.0
        mags = mags.reshape(*mags.shape, 1)
        mprod = np.outer(masses,masses)
        mprod = mprod.reshape(*mprod.shape, 1)

        F = diffs * mprod / (0.1+mags)**3.0
                             # add 0.1 to the denominator---a cheap trick :)
        f = np.sum(F,axis=0) 

        vels = vels + f*dt
        coords = coords + vels*dt
        coords = coords[0]

        # Record the particles' current positions, 
        # and make a plot of the current state.
        history.insert(0, coords)
        plot_system(gravity_gif, history)

    # close the Gif
    gravity_gif.close()


    # End simulation
    return


def plot_system(gravity_gif, history):

    # Start a new frame!
    gravity_gif.start_frame()

    # Various stylistic elements
    plt.rc("text",usetex=True)
    plt.title("Newtonian Gravity", family="serif",fontsize=14)
    plt.xlim([-10,10])
    plt.ylim([-10,10])
    plt.xticks([])
    plt.yticks([])

    #print(history)
    #input("press enter")

    # Plot the tracks of the particles
    for r in range(history[0].shape[0]):
        xs = []
        ys = []
        for t in range(len(history)):
            xs.append(history[t][r][0])
            ys.append(history[t][r][1])
        plt.plot(np.array(xs),np.array(ys),"silver",linewidth=0.5)
    
    # Plot the particles themselves
    plt.scatter(history[0][:,0],
                history[0][:,1],
                color="k",
                zorder=500)

    plt.xlabel('$ \displaystyle F_{ij} = G \\frac{m_i m_j}{ \| x_i - x_j \|^2 } $',
            fontsize=16)
    plt.tight_layout()
 
    # End the frame!
    gravity_gif.end_frame()

    return


#################################################
if __name__=="__main__":

    gravity_simulation()



