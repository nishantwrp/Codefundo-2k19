# CodeFunDo - LetsVote

>Project proposal for Microsoft's Codefundo++ 2019

---
### Team :- /data/study_material

* [Nishant Mittal](https://www.github.com/nishantwrp)
* [Mudit Bharadwaj](https://github.com/muditbhardwaj195)
* [Prakhar Dwivedi](https://github.com/meowmeow321)

## IDEA

The idea is to create an application that aims to incentivize voting. It will be an online portal which will keep track of the people who have voted and facilitate the government to reward them for their participation in the democracy. The application will also serve as a platform for the citizens of the country to apply for voters' ID, apply corrections in their ID, and make the voting process hassle-free for the general public.  


Inspiration for the idea was the relatively low participation of Indian citizens in the voting process. We tried to find the reasons behind it, and one of the primary reasons is the hassle-full process of obtaining voters' ID. 

We will sync our application with government records to easily keep track of the people who have voted. Since this application deals with sensitive data, security is the topmost priority. We will use Azure Blockchain to achieve this goal.

## App
We have made a web application using **django** a python web framework and used **azure blockchain services** to make our app secure.

## Deployment

[![Build Status](https://dev.azure.com/nishantwrp/lets-vote/_apis/build/status/lets-vote%20-%20CI?branchName=master)](https://dev.azure.com/nishantwrp/lets-vote/_build/latest?definitionId=1&branchName=master)

I have deployed the django application on azure app sevices itself.

- [https://lets-vote.azurewebsites.net/](https://lets-vote.azurewebsites.net/)

## Blockchain
The application uses azure blockchain services to make it secure. LetsVote application interacts with blockchain through rest api provided by azure blockchain services.

- [Github Repository With Blockchain Code](https://github.com/nishantwrp/Codefundo-2k19-Blockchain)
- [LetsVote Blockchain](https://codefundo-oz5vuz.azurewebsites.net/applications)
- [LetsVote Blockchain Rest Api](https://codefundo-oz5vuz-api.azurewebsites.net/swagger/ui/index.html)

## Technical Stack
- Django
- Requests Library
- Azure Blockchain Services
- Gmail SMTP

## Official Credentials
- username : admin
- passsword: nishantwrp

## Note
> The app may not work perfectly as shown in video because the azure credits limit have exceeded
