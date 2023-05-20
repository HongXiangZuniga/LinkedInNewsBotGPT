
from src.scrapping.service import scrappingService
from src.textGenerator.chatGPT4.service import textGenerator
from dotenv import load_dotenv
import os

def main():
    load_dotenv()
    totalPost = int(os.getenv('TOTAL_POST'))
    url = input("Enter the url\n")
    html = scrappingService.GetInfo(url)
    TextGenerator = textGenerator(totalPost,os.getenv('OPENAI_KEY'))
    result = TextGenerator.getSummaries(html,os.getenv('LANGUAGE'))
    for i in range(len(result)):
        print(result[i])
main()
