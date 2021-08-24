#!/usr/bin/env python
# coding: utf-8

# In[1]:


############Import Libraries
import openai
import pandas as pd



# In[2]:
class Model:

    openai.api_key = "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"


    def usamodel(self,quest,mt,mr):
        document_list = pd.read_csv('Data/USA.csv').sample(n = 30)['Text'].tolist()
        response = openai.Answer.create(
        search_model="ada",
        model="curie",
        question=quest,
        documents=document_list,
        examples_context="In 2017, U.S. life expectancy was 78.6 years.",
        examples=[["What is human life expectancy in the United States?","78 years."]],
        max_tokens=mt,
        max_rerank=mr,
        stop=["\n", "<|endoftext|>"],
        )
        result=[]
        scores=[]
        count=0
        for ans in response["selected_documents"]:
            print("tyepe",ans)
            count=count+1
            result.append({count:ans['text']})
            scores.append({count:ans['score']})
        return result,scores

    def italymodel(self,quest,mt,mr):
        document_list = pd.read_csv('Data/ITALY.csv').sample(n = 30)['Text'].tolist()
        response = openai.Answer.create(
        search_model="ada",
        model="curie",
        question=quest,
        documents=document_list,
        examples_context="In 2017, U.S. life expectancy was 78.6 years.",
        examples=[["What is human life expectancy in the United States?","78 years."]],
        max_tokens=mt,
        max_rerank=mr,
        stop=["\n", "<|endoftext|>"],
        )
        result=[]
        scores=[]
        count=0
        for ans in response["selected_documents"]:
            print("tyepe",ans)
            count=count+1
            result.append({count:ans['text']})
            scores.append({count:ans['score']})
        return result,scores


    def russiamodel(self,quest,mt,mr):
        document_list = pd.read_csv('Data/RUSSIA.csv').sample(n = 30)['Text'].tolist()
        response = openai.Answer.create(
        search_model="ada",
        model="curie",
        question=quest,
        documents=document_list,
        examples_context="In 2017, U.S. life expectancy was 78.6 years.",
        examples=[["What is human life expectancy in the United States?","78 years."]],
        max_tokens=mt,
        max_rerank=mr,
        stop=["\n", "<|endoftext|>"],
        )
        result=[]
        scores=[]
        count=0
        for ans in response["selected_documents"]:
            print("tyepe",ans)
            count=count+1
            result.append({count:ans['text']})
            scores.append({count:ans['score']})
        return result,scores


    def chinamodel(self,quest,mt,mr):
        document_list = pd.read_csv('Data/CHINA.csv').sample(n = 30)['Text'].tolist()
        response = openai.Answer.create(
        search_model="ada",
        model="curie",
        question=quest,
        documents=document_list,
        examples_context="In 2017, U.S. life expectancy was 78.6 years.",
        examples=[["What is human life expectancy in the United States?","78 years."]],
        max_tokens=mt,
        max_rerank=mr,
        stop=["\n", "<|endoftext|>"],
        )
        result=[]
        scores=[]
        count=0
        for ans in response["selected_documents"]:
            print("tyepe",ans)
            count=count+1
            result.append({count:ans['text']})
            scores.append({count:ans['score']})
        return result,scores


    def nigeriamodel(self,quest,mt,mr):
        document_list = pd.read_csv('Data/NIGERIA.csv').sample(n = 30)['Text'].tolist()
        response = openai.Answer.create(
        search_model="ada",
        model="curie",
        question=quest,
        documents=document_list,
        examples_context="the csa said the current aim of reaching 85% of the population by 2007 was achievable",
        examples=[["What was the populations aim in 2007?","85% Population."]],
        max_tokens=mt,
        max_rerank=mr,
        stop=["\n", "<|endoftext|>"],
        )
        result=[]
        scores=[]
        count=0
        for ans in response["selected_documents"]:
            print("tyepe",ans)
            count=count+1
            result.append({count:ans['text']})
            scores.append({count:ans['score']})
        return result,scores

    def startwork(self,question,country,mt,mr):
        if country=='1' and question !="" :
    
            result,scores=self.usamodel(question,mt,mr)
            print("Question is =====>\n",question,"====>\nAnswer",result, "\nScores==========>\n",scores)
        
        if country=='2' and question !="" :
            
            result,scores=self.italymodel(question,mt,mr)
            return result,scores
            
            
        if country=='3' and question !="" :
            
            result,scores=self.russiamodel(question,mt,mr)
            print("Question is =====>\n",question,"====>\nAnswer",result, "\nScores==========>\n",scores)
            
        if country=='4' and question !="" :
            
            result,scores=self.chinamodel(question,mt,mr)
            print("Question is =====>\n",question,"====>\nAnswer",result, "\nScores==========>\n",scores)
            
        if country=='5' and question !="" :
            
            result,scores=self.nigeriamodel(question,mt,mr)
            print("Question is =====>\n",question,"====>\nAnswer",result, "\nScores==========>\n",scores)
            
        else:
            print("Wrong Input for Country or Question is Wrong")


    
    def __init__(self):
        print("Start Model")
    
    # In[ ]:
