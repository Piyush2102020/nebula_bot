<h1><b>Nebula</b></h1>

<h3>Description</h3>
Nebula is a bot generator that creates user and generates random texts based on provided chat data. This tool is designed to generate a specified number of bot users and simulate their activity by providing random texts from a dataset (chat_data.txt). 
The generated data is presented in JSON format and can be used for scenarios like load testing, creating a user rush on sites or applications, testing environments, or showcasing demo users.

<br>
<br>
<h3>Files</h3>
<b>1:- nebula.py:</b> Python script responsible for generating bot users and providing random texts.<br>
<b>2:- chat_data.txt:</b> Text file containing chat data used by Nebula for generating random messages.<br>

<h3>Workflow</h3>

<b>Bot Generation:</b> Nebula generates a specified number of bot users (no_of_bots) with random data including names, genders, ages, etc.<br>
<b><i>NOTE</i></b>:- the names are generated with a api you can also add random names for your list or change the phrases by adding the in the chat_data.txt<br> 
<b>Text Generation:</b> For each bot user, Nebula provides random text messages based on the contents of chat_data.txt.<br>
<b>JSON User Data:</b> The generated user data is formatted in JSON and continuously provided in an infinite loop, offering randomness in the generated data.<br><br>
<h3>Usage</h3>
<br>
<b>Clone the repository.<br>
Ensure you have Python installed.<br>
Modify the no_of_bots and chat_data.txt according to your requirements.<br>
Run the nebula.py script to generate user data and random texts.<br>
<h4>Important Notes</h4><br>
Adjust no_of_bots and chat_data.txt to suit your testing or demonstration needs.<br>
Ensure that the generated data is used responsibly and in compliance with relevant policies and laws.</b>
