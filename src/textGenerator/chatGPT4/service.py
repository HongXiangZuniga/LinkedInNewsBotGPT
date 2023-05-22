import openai

class textGenerator :
    result = None
    key = ''

    def getSummaries(self,html,language):
        if (language=="es"):
            prompt="Crea un texto de 246 caracteres para compartir en linkedin el siguiente post:"+html
        elif(language=="en"):
            prompt="Create a text to share the following post on linkedin in english:"+html
        else:
            prompt="Crea un texto de 246 caracteres para compartir en linkedin el siguiente post:"+html
        summaries =[]
        openai.api_key=self.key
        result = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=2048,
            n=self.result
        )
        for i in range(self.result):
            summaries.append(result.choices[i].text)
        return summaries
    
    def __init__(self,result,key):
        self.result = result
        self.key = key