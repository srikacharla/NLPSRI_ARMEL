import pickle
import numpy as np
import nltk
import matplotlib.pyplot as plt
nltk.download('stopwords')

'''
In this file, we plot the of each music genre vs. other genres per year 
Input: 5 similarity matrix | 1 per year group - build in extract_year_sim.py
Output: plot of each music genre vs. others
'''

# ------------------------------------------------------| Functions

# Function 1: Year change by genre
def changeByYears(all_sim,col):
    '''
    :param all_sim: Array with all similarity grouped by year
    :param col: Selected genre
    :return: Change sim by year
    '''
    vec = [0,1,2,3,4,5] # 0: pop, 1:rock, 2:rnb, 3:edm, 4:country, 5:gospel etc.
    x = np.zeros([5, 5])
    column = col
    vec.remove(column)
    k = 0
    for i in vec:
        x[k, :] = all_sim[:, column, i]
        k += 1
    return x
# ------------------------------------------------------| Loading data
# Downloading lyrics dates split by year range
sim_all_x1 = pickle.load( open( "similarity_analysis/sim_1", "rb" ) ) # < 2000
sim_all_x2 = pickle.load( open( "similarity_analysis/sim_2", "rb" ) ) # 2000 - 2005
sim_all_x3 = pickle.load( open( "similarity_analysis/sim_3", "rb" ) ) # 2005 - 2010
sim_all_x4 = pickle.load( open( "similarity_analysis/sim_4", "rb" ) ) # 2010 - 2015
sim_all_x5 = pickle.load( open( "similarity_analysis/sim_5", "rb" ) ) # > 2015

# ------------------------------------------------------ | Analysis
# --------------- | Similarity across time

# Putting all arrays together
all_sim = np.array([sim_all_x1,sim_all_x2,sim_all_x3,sim_all_x4,sim_all_x5])


# Change by years
pop  = changeByYears(all_sim,0) # Pop vs. others
rock = changeByYears(all_sim,1) # Rock vs. others
rnb  = changeByYears(all_sim,2) # RnB vs. others
edm  = changeByYears(all_sim,3) # EDM vs. others
ctry = changeByYears(all_sim,4) # Country vs. others
gspl = changeByYears(all_sim,5) # Gospel vs. others


# Plotting
# Pop vs. others
plt.figure(10)
x_axis = [0,1,2,3,4]
year_x = ['<2000', '2000-2005','2005-2010','2010-2015','>2015']
label_y = ['Rock','R&B/Hip Hop','EDM/Electro','Country','Christian/Gospel']
plt.xticks(x_axis, year_x)
plt.plot(x_axis,pop[0,:],'r',label= label_y[0])
plt.plot(x_axis,pop[1,:],'b',label= label_y[1])
plt.plot(x_axis,pop[2,:],'g',label= label_y[2])
plt.plot(x_axis,pop[3,:],'m',label= label_y[3])
plt.plot(x_axis,pop[4,:],'k',label= label_y[4])
plt.ylim(0, 1)
plt.legend()
plt.title('Pop vs. Others')
plt.xlabel('Year')
plt.ylabel('Similarity')
plt.show()

# Rock vs. others
plt.figure(11)
x_axis = [0,1,2,3,4]
year_x = ['<2000', '2000-2005','2005-2010','2010-2015','>2015']
label_y = ['Pop','R&B/Hip Hop','EDM/Electro','Country','Christian/Gospel']
plt.xticks(x_axis, year_x)
plt.plot(x_axis,rock[0,:],'r',label= label_y[0])
plt.plot(x_axis,rock[1,:],'b',label= label_y[1])
plt.plot(x_axis,rock[2,:],'g',label= label_y[2])
plt.plot(x_axis,rock[3,:],'m',label= label_y[3])
plt.plot(x_axis,rock[4,:],'k',label= label_y[4])
plt.ylim(0, 1)
plt.legend()
plt.title('Rock vs. Others')
plt.xlabel('Year')
plt.ylabel('Similarity')
plt.show()

# R&B/Hip Hop vs others
plt.figure(12)
x_axis = [0,1,2,3,4]
year_x = ['<2000', '2000-2005','2005-2010','2010-2015','>2015']
label_y = ['Pop','Rock','EDM/Electro','Country','Christian/Gospel']
plt.xticks(x_axis, year_x)
plt.plot(x_axis,rnb[0,:],'r',label= label_y[0])
plt.plot(x_axis,rnb[1,:],'b',label= label_y[1])
plt.plot(x_axis,rnb[2,:],'g',label= label_y[2])
plt.plot(x_axis,rnb[3,:],'m',label= label_y[3])
plt.plot(x_axis,rnb[4,:],'k',label= label_y[4])
plt.ylim(0, 1)
plt.legend()
plt.title('R&B/Hip Hop vs. Others')
plt.xlabel('Year')
plt.ylabel('Similarity')
plt.show()

# EDM/Electro vs others
plt.figure(13)
x_axis = [0,1,2,3,4]
year_x = ['<2000', '2000-2005','2005-2010','2010-2015','>2015']
label_y = ['Pop','Rock','R&B/Hip Hop','Country','Christian/Gospel']
plt.xticks(x_axis, year_x)
plt.plot(x_axis,edm[0,:],'r',label= label_y[0])
plt.plot(x_axis,edm[1,:],'b',label= label_y[1])
plt.plot(x_axis,edm[2,:],'g',label= label_y[2])
plt.plot(x_axis,edm[3,:],'m',label= label_y[3])
plt.plot(x_axis,edm[4,:],'k',label= label_y[4])
plt.ylim(0, 1)
plt.legend()
plt.title('EDM/Electro vs. Others')
plt.xlabel('Year')
plt.ylabel('Similarity')
plt.show()

# Country vs others
plt.figure(14)
x_axis = [0,1,2,3,4]
year_x = ['<2000', '2000-2005','2005-2010','2010-2015','>2015']
label_y = ['Pop','Rock','R&B/Hip Hop','EDM/Electro','Christian/Gospel']
plt.xticks(x_axis, year_x)
plt.plot(x_axis,ctry[0,:],'r',label= label_y[0])
plt.plot(x_axis,ctry[1,:],'b',label= label_y[1])
plt.plot(x_axis,ctry[2,:],'g',label= label_y[2])
plt.plot(x_axis,ctry[3,:],'m',label= label_y[3])
plt.plot(x_axis,ctry[4,:],'k',label= label_y[4])
plt.ylim(0, 1)
plt.legend()
plt.title('Country vs. Others')
plt.xlabel('Year')
plt.ylabel('Similarity')
plt.show()

# Christian/Gospel vs others
plt.figure(15)
x_axis = [0,1,2,3,4]
year_x = ['<2000', '2000-2005','2005-2010','2010-2015','>2015']
label_y = ['Pop','Rock','R&B/Hip Hop','EDM/Electro','Country']
plt.xticks(x_axis, year_x)
plt.plot(x_axis,gspl[0,:],'r',label= label_y[0])
plt.plot(x_axis,gspl[1,:],'b',label= label_y[1])
plt.plot(x_axis,gspl[2,:],'g',label= label_y[2])
plt.plot(x_axis,gspl[3,:],'m',label= label_y[3])
plt.plot(x_axis,gspl[4,:],'k',label= label_y[4])
plt.ylim(0, 1)
plt.legend()
plt.title('Christian/Gospel vs. Others')
plt.xlabel('Year')
plt.ylabel('Similarity')
plt.show()