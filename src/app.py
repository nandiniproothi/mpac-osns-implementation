# import necessary modules
# to install with pip run `pip install -r requirements.txt`

from utils import *
import streamlit as st
import pandas as pd
import numpy as np
from math import e
from faker import Faker
from faker.providers import *
import random
import json
import matplotlib.pyplot as plt
from matplotlib_venn import venn3, venn3_circles, venn2
from mpl_toolkits.mplot3d import Axes3D
fake = Faker()  # initialise faker module
from utils import *

st.title('A Multi-party Approach to Policy Resolution of Shared Data and Preclude Collusion Attacks Using Strength of Interaction in Online Social Networks')
st.header('Abstract')
st.write("The number of users on Online Social Networks (OSNs) has grown tremendously over the past few years, with sites like Facebook amassing over a billion users. With the popularity of OSNs, the increase in privacy risk from the large volume of sensitive and private data is inevitable. While there are many features for access control for an individual user, most OSNs still need concrete mechanisms to preserve the privacy of data shared between multiple users. The proposed method uses metrics such as Identity Leakage and Strength of interaction to fine-tune the scenarios that use Privacy Risk and Sharing Loss to identify and resolve conflicts. In addition to conflict resolution, bot detection is also done to mitigate collusion attacks. The final decision to share the data item is then ascertained based on whether it passes the threshold condition for the above metrics.")


st.header('Demo')
st.write('Due to strict data governance laws and restrictions and the lack of accessibility of ethically obtained online social network data, we generated a dataset instead of scraping data from existing platforms. For testing our proposed approach, we made use of Trumania - a scenario-based random dataset generator [library in Python](https://github.com/RealImpactAnalytics/trumania). Trumania simulations are run as part of a circus along with a clock which maintains the virtual time during the execution of a [circus](https://realimpactanalytics.github.io/trumania/wiki.html#a-name-overview-of-circus-a-overview-of-circus-elements-and-runtimes). For the following examples, we generated interactions between three users - Matthew, Jennifer, and Nicholas. Trumania allows for defining relationships and attributes for persons in the simulation. By leveraging these features, friends and interaction types are relationships while messages and popularity of the user is an attribute. Interaction types are picked from the ones listed in table below. With some interaction types being more likely than others:')

data_prob_interaction = {'Type': ['Like', 'Comment', 'Share', 'Post'], 'Probability': [0.6, 0.15, 0.15, 0.10]}
df_prob_interaction = pd.DataFrame(data=data_prob_interaction)
st.write(df_prob_interaction)

st.write("Using Trumania, we generated a data set with 100 users having varying popularity. We ran their interactions on Microsoft's pre-built Sentiment Analysis model. Here's a preview of the generated dataset: ")
df_dataset_100 = pd.read_csv('data/dataset_100.csv').dropna(axis=1, how='all', inplace=False)
st.write(df_dataset_100)

st.write("For the following scenarios we'll be using a subset of the data, focusing on 3 users: Matthew, Nicholas, and Jennifer:")
df_dataset_short = pd.read_csv('data/dataset_short_sentiment.csv').dropna(axis=1, how='all', inplace=False)
st.write(df_dataset_short)

st.header('Example 1')
st.write('Data sharing between two users - proprietor and collaborator (with PR and SL).')
st.write('*Matthew posts a picture with Nicholas*')
df_example1 = return_pr_sl([0.66, 0.66], [0.33,0.33], 1, lambd=0.5)
st.write('PR, SL values: ', df_example1)
st.write('Using conflict resolution, the result is: ')
st.write(calculate_pr_sl([0.66, 0.66], [0.33,0.33], 1, lambd=0.5))

st.header('Example 2')
st.write('Sharing data with target users')
st.write('*Taking the same scenario as Example 1. We have now learned that Matthew and Nicholas are good friends, whereas Matthew and Jennifer don\'t have a great relationship.*')

st.header('Example 3')
st.write('Non-consensual sharing from a trusted user')
st.write('*Matthew shares a picture of Jennifer where Jennifer\'s Identity Leakage is low* (permit)')
st.write('*Matthew shares a picture of Jennifer where Jennifer\'s Identity Leakage is high* (deny)')
st.write('*Matthew shares a picture of Nicholas where Nicholas\'s Identity Leakage is low* (deny)')
st.write('*Matthew shares a picture of Nicholas where Nicholas\'s Identity Leakage is high* (deny)')

st.header('Example 4')

Ru = [0.5, 0.3, 0.7, 0.4, 0.1]
Np = [5, 2, 20, 40, 100]
L = 10
A = [50, 20, 200, 60, 5]
B = [70, 24, 100, 5, 0]

data = {'recommendation': Ru, 'number of posts': Np, 'number of followers': A, 'number of following': B}
df_data_rep = pd.DataFrame(data=data)
st.write('The following data is used to calculate reputation of 5 users: ')
st.write(df_data_rep)
st.write('We calculate reputation to be:')
df_data_rep['reputation'] = 2*df_data_rep['recommendation'] + df_data_rep['number of posts']  + L/(1+((L-1)*e**(-df_data_rep['number of followers'] - df_data_rep['number of following'] -1) ) ) 
st.write(df_data_rep)
st.write(e**(df_data_rep['number of followers'] - df_data_rep['number of following'] ))

st.write('Once we run [Björn et. al\'s model for bot detection](https://github.com/qmdnls/ADM19F-bot-detection), we assign reputation as zero for those users. Upon doing so, we ignore any attemps actions by these accounts while focusing on the privacy of other users.')