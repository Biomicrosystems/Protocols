##########################################
# MLX90640 Thermal Camera w Raspberry Pi
# -- 2fps with Interpolation and Blitting
##########################################
#
import time,board,busio
import numpy as np
import adafruit_mlx90640
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from datetime import datetime as dt
import matplotlib as mpl

textstr = "Mean temperature: \n" + "Temperature on click: " 

i2c = busio.I2C(board.SCL, board.SDA, frequency=400000) # setup I2C
mlx = adafruit_mlx90640.MLX90640(i2c) # begin MLX90640 with I2C comm
mlx.refresh_rate = adafruit_mlx90640.RefreshRate.REFRESH_2_HZ # set refresh rate
N=26
frame = np.zeros((24*32,)) # 768 pts
plt.ion()

fig =plt.figure()
ax=fig.add_subplot(111)


props = dict(boxstyle="round", facecolor = "wheat", alpha = 0.5)
t1 = ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize = 14, fontstyle =  "italic",verticalalignment = "top", bbox = props)
# t2 = ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize = 14, fontstyle =  "italic",verticalalignment = "top", bbox = props)
mlx_shape = (24,32) # mlx90640 shape

data_array = np.fliplr(np.reshape(frame,mlx_shape))

cmap=plt.get_cmap('jet',N)
therm1 = ax.imshow(data_array,interpolation='none',
                  cmap=cmap,vmin=10,vmax=60) # preemptive image

cbar = fig.colorbar(therm1, ticks=np.linspace(10, 260, N), label = "Temperature [°C]") # setup colorbar

plt.title(label="Thermal view",
          position=(0.5, 0.9),
          fontdict={'family': 'Dejavu Serif',
                    'color' : 'black',
                    'weight': 'bold',
                    'size': 16})

plt.xlabel("x-coordinate", size = 12)
plt.ylabel("y-coordinate", size = 12)

def on_move(event):

    try:
        NewText = "Temperature on click: "+ str(np.round((data_array[round(event.ydata), round(event.xdata)]), 2)) + " °C \n"
        t1.set_text(NewText)
    except:
        print("Fuera de los limites")
    # print("El valor aquí es: " , data_array[round(event.xdata), round(event.ydata)], "Acción: ", event.button)

def key_on_press(event):
    if (event.key=='f1'):
        fig.savefig("pictures/Thermal_view_"+str(dt.now().time())+".png")
        print ("Imagen guardada como Thermal_view_"+str(dt.now().time())+".png")

def plotea():
    mlx.getFrame(frame) # update plot
#     print('Average MLX90640 Temperature: {0:2.1f}C ([{1:2.1f}F)'.\
#          format (np.mean(frame),(((9.0/5.0)*np.mean(frame))+32.0)))
    data_array = np.fliplr(np.reshape(frame,mlx_shape))
#     print (data_array)
#     print (data_array.shape)
#     therm1= ax.imshow(data_array,interpolation='none',
#                    cmap=plt.cm.bwr,vmin=10,vmax=60) # preemptive image
    therm1.set_array(data_array) # set data
    mean = np.mean(frame)
    
    fig.canvas.mpl_connect('motion_notify_event', on_move)
    
    fig.canvas.mpl_connect('key_press_event', key_on_press)

    fig.canvas.draw()
    fig.canvas.flush_events() # show the new image
while True:
    try:
        plotea()
    except ValueError:
        continue




    

   

