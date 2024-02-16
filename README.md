# 🔐eCTFBot
This is a ChatGPT API integrated chatbot that's sole purpose is to help users with embedded systems capture the flag competitions. The first step to getting this running is by going to this link.
```
https://openai.com/blog/openai-api
```
Login or make an account if you don't have one already, then load atleast $5 dollars onto your account, and create an OpenAI API key (make sure you to keep the key a secret). After obtaining the API you will need to start setting up your Python environment. Open Visual Studio Code and a new terminal set to command prompt. In the command prompt terminal window run these commands one by one.
```
# Creates Python virtual environment 
python -m venv TestRun

# Activates and runs the environment for files
TestRun\Scripts\activate
```
Once active your terminal command line should look like this, ```(TestRun) C:\Users\username>```. Once you have done this download the ```./requirements.txt``` from this repo and run it with the follwing command in the TestRun terminal.
```
pip install -r "pathtothefile\reqirements.txt"
```
This file will download and install the latest versions of ```openai``` and ```streamlit```, which are used to make this application work. If for some reason the openai import is not working, in your TestRun terminal run this command ```pip install openai --upgrade```, this should fix the problem. Now navigate your file explorer to find your ```.streamlit``` file. The path to this file should look something like this.
```
C:\Users\username\.streamlit
```
If you do not have a ```.streamlit``` folder, simply make a new folder under your username and name it ```.streamlit```. Now inside of this existing/new folder you need to create a ```secrets.toml``` file. You can create one by simply creating a new file inside of Visual Studio Code and naming it ```secrets.toml```. In this file you need to add this variable and your OpenAI API key. (Make sure to save the file and drag it into the ```.streamlit``` folder.)
```
OPENAI_API_KEY = "yourapikeyfromOpenAI"
```
Next download the ```./eCTFBot.py``` file from this repo and open it in Visual Studio Code. After all of these steps have been done all you have to do is run this command in your TestRun command terminal.
```
python -m streamlit run "C:\pathtofile\eCTFBot.py"
```
This will create a Streamlit web application that is accessable via the internet at the network address provided in the terminal. If you wish to stop the application just click ```ctrl + c``` in the terminal.
<p align="center"><img src="https://github.com/ScottSnow13/eCTFBot/assets/117798417/5df87160-5f8d-465c-8a37-aea5960148c3)" /></p>
