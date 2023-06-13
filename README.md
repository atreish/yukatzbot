# yukatzbot
The official repository for Katz School's Internet Bot developed for the MS in Artificial Intelligence program

## Technologies
<div align="center">   

 ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
 ![Rasa](https://img.shields.io/badge/Rasa-3.5.10-blue?style=for-the-badge&logo=rasa&logoColor=white)
 ![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)

</div>

## Table of Contents
1. [Requirements](#requirements)
2. [Installation](#installation)
3. [GitHub Best Practices with an IDE](#github-best-practices-with-an-ide)
4. [Setup](#setup)
5. [Training](#training)
6. [Adding Data](#adding-data)
7. [Running the API](#running-the-api)
8. [Visualize the chat flow](#visualize-the-chat-flow)
9. [Goals](#goals)
   - [Phase 1](#phase-1)
   - [Phase 2](#phase-2)



## Requirements
Make sure you have the following requirements before running Rasa:
- Python 3.9
- Rasa

## Installation
To install Rasa, follow these steps:

1. Clone this GitHub repository to your local machine:
    ```
    git clone https://github.com/atreish/yukatzbot.git
    ```

2. Change into the cloned directory:
    ```
    cd yukatzbot
    ```

## GitHub Best Practices with an IDE
Follow these best practices when working with GitHub:

### Creating a Subbranch
To create a subbranch for your work, use the following commands:
  ```
  git checkout -b your-subbranch-name
  ```
 
  This will create a new branch based on the current branch you are on.
  
### Saving Changes in Your Subbranch
After making changes to your code, save the changes in your subbranch using the following commands:
   ```
  git add .
  git commit -m "Your commit message"
   ```
   This will stage and commit your changes to your subbranch.
  


### Pulling Changes from the Main Branch
Before pushing your changes, it's a good practice to pull the latest changes from the main branch. Use the following command:
  ```
  git pull origin main
   ```
  This will fetch and merge the latest changes from the main branch into your current branch.

### Pushing Changes to Remote Repository
Once you are ready to push your changes to the remote repository, use the following command:
   ```
   git push origin your-subbranch-name
   ```
  This will push your changes to the remote repository, making them available for review and collaboration.
  
## Setup
Before running Rasa, you need to perform the following setup steps:

1. Create a virtual environment (optional but recommended):
     Make sure you have Python version 3.9
     ```
     python -m venv myenv
     source myenv/bin/activate
     ```
     or
     ```
     conda create -n myenv python==3.9
     conda myenv activate
     ```

2. Install Rasa within the virtual environment:
    ```
    pip install rasa
    ```

## Training
To train your Rasa model, follow these steps:

1. Create and structure your training data by adding `.md` or `.yml` files in the `data` directory.

2. Train the model using the following command:
    ```
    rasa train
    ```
    Rasa will process your training data and train the model. The trained model will be saved in the `models` directory.

## Adding Data
To add more training data to your Rasa model, follow these steps:

1. Open the relevant `.md` or `.yml` file in the `data` directory.

2. Add your training examples, intents, entities, and responses in the specified format.

3. Save the file.

4. Train the model again to incorporate the newly added data.

## Running the API
To run the Rasa API and interact with your trained model, follow these steps:

1. Start the Rasa server using the following command:
    ```
    rasa run -m models --enable-api --cors "*"
    ```
    The API server will start, and you will see the endpoint information in the console.

2. You can now make HTTP requests to the API to send messages and receive responses from your trained Rasa model.

## Visualize the chat flow
If you want to visualize the flow of the context, use the following command:
   ```
   rasa visualize
   ```
  
## Interface
Open up a new terminal within the directory and start the HTML file with the following command:
   ```
   start index.html
   ```
   
![Chat Interface](https://github.com/atreish/yukatzbot/assets/37763863/20f7f270-64b7-47ad-b2c7-6c4f2855cc0f)

## Goals
The goals of this project are as follows:

- [ ] Phase 1:
  - [ ] Goal 1 for Phase 1
  - [ ] Goal 2 for Phase 1
  - [ ] Goal 3 for Phase 1

- [ ] Phase 2:
  - [ ] Goal 1 for Phase 2
  - [ ] Goal 2 for Phase 2
  - [ ] Goal 3 for Phase 2
    
