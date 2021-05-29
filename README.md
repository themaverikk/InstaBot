### This repository is no longer maintained, Open an issue to get support or feel free to contribute.

# InstaBot
Instagram Bot to automate commenting, liking and following other users.

While I was still learning Python, I was a bit skeptical whether writing code in Python is more efficient than in Java, as people always used to say. And the answer was yes!!

I started writing the code at 9 PM on the Sunday night, given I had no prior experience with Selenium (of course I learnt Selenium while writing this bot), I was able to get the bot properly working and finally slept at 1 AM :)

# Run
1. clone the Project and go to the cloned directory
    ```
    git clone <project_url_here>
    cd InstaBot
    ```

2. Create the virtual environment
    ```
    virtualenv -p python3 InstaBotVenv
    ```
3. Activate the virtual environment
    ```
    source InstaBotVenv/bin/activate
    ```
4. Install required dependencies
    ```
    pip install -r requirements.txt
    ```
5. Download appropriate selenium driver for your browser
    - chrome -> http://chromedriver.chromium.org/downloads

6. Extract the driver from zip file and copy it to `InstaBotVenv/bin` directory

7. Add your username and password in `InstaBot/src/instabot/main.py` file

8. Run the project
    ```
    python src/instabot/main.py
    ```
