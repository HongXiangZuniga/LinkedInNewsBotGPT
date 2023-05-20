import openai

class textGenerator :
    result = 5
    key = ''

    def getSummaries(self,html,language):
        if (language=="es"):
            prompt="Crea un texto para compartir en linkedin el siguiente post:"+html
        elif(language=="en"):
            prompt="Create a text to share the following post on linkedin in engliu:"+html
        else:
            prompt="Crea un texto para compartir en linkedin el siguiente post:"+html
        summaries =[]
        openai.api_key=self.key
        result = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=246,
            n=self.result
        )
        for i in range(self.result):
            summaries.append(result.choices[i].text)
        return summaries
    
    def __init__(self,result,key):
        self.result = result
        self.key = key