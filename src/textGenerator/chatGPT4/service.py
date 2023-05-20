import openai

class textGenerator :
    result = 5
    key = ''

    def getSummaries(self,html,lang):
        summaries =[]
        prompt="Crea un texto para compartir en linkedin el siguiente post:"+html
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