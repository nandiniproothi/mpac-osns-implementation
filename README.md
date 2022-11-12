# [Implementation] A Multi-party Approach to Policy Resolution of Shared Data and Preclude Collusion Attacks Using Strength of Interaction in Online Social Networks

This repository contains the code and supporting materials for the paper titled **A Multi-party Approach to Policy Resolution of Shared Data and Preclude Collusion Attacks Using Strength of Interaction in Online Social Networks** submitted to [IEEE Access](https://ieeeaccess.ieee.org/)

## Abstract

The number of users on Online Social Networks (OSNs) has grown tremendously over the past few years, with sites like Facebook amassing over a billion users. With the popularity of OSNs, the increase in privacy risk from the large volume of sensitive and private data is inevitable. While there are many features for access control for an individual user, most OSNs still need concrete mechanisms to preserve the privacy of data shared between multiple users. The proposed method uses metrics such as Identity Leakage and Strength of interaction to fine-tune the scenarios that use Privacy Risk and Sharing Loss to identify and resolve conflicts. In addition to conflict resolution, bot detection is also done to mitigate collusion attacks. The final decision to share the data item is then ascertained based on whether it passes the threshold condition for the above metrics.

## Demo

You can run the code locally or view it on the published streamlit application [here]().

### Prerequisites for running the code locally:
1. Install the latest version of Python from 

To run the code the locally, follow the steps mentioned below:

1. Clone this repository by using the `git clone` command OR download a copy of the repository and unzip the folder.
2. Once you've redirected to the directory containing the code, run the following command: `pip install -r requirements.txt` - this installs all the Python modules necessary to run the code.
3. After successfully installing all modules, run the following command: `streamlit run src/app.py` - this should open up the app in your browser. If it does not, head over to `http://localhost:8501/` and take a look at the demo.
