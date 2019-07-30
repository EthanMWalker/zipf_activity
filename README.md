# Zipf Coding Activity

This activity is based on something called "_Zipf's law_". [Zipf's law](https://en.wikipedia.org/wiki/Zipf%27s_law), is an emperical law that describes the occurace of many social and physical phenomena. It claims that many of these phenomena follow a Zipfian distribution, which is a descrete power law.

## Tools

In this activity we are using web scraping, html parsing, and data visualization to confirm Zipf's law.
We will write the code in python3 and we will use the following libraries:
- requestes
- BeautifulSoup from bs4
    - this usually doesn't come preinstalled with Anaconda so you will have to install it yourself
- pyplot from matplotlib
- numpy
- re
    - this is a python regex library, we are using it to help us parse the text and eliminate different text anomolies.

## Process

The idea behind the activity is to scrape some webpage that had a lot of plain text, I chose a webpage that has the Homeric hymn to Demeter. After scraping the page we will parse the text then count the occurances of unique words and finally display the occurance frequency in a bar chart. 
