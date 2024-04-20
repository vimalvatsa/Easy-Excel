# Easy-Excel
 Introducing Easy-Excel: a groundbreaking project merging handwriting recognition and natural language processing. Effortlessly convert handwritten tables into Excel sheets, get prompt-specific insights, all on iOS and Android. Revolutionize data management, reclaim time, and empower productivity.

Easy excel is a LLM powered application that allows its users to convert handwritten tables that are in the form of an image or a PDF, convert it into an excel file that the user can download and perform query. 

This application uses a LLM model that extracts input using: 

OCR (Optical Character Recognition), the LLM parses through the input that has been obtained by the OCR model, processes it, and then converts it to JSON format. 

Excel to JSON, the LLM will read the excel, process it, and then convert it into JSON format. 

The obtained JSON file is processed into a Pandas Array. 

The user can use the application to convert handwritten images to Excel Directly. 
The query processing model that is being used is Google TAPAS-sqa. This is a LLM model that is trained to answers structured queries, the preferred input format for this LLM model is a Pandas array for the dataset and a query in the form of a string. 

The query response will be received in a truncated form that will be displayed one at a time on the UI. 

The LLM model will run on loop until the user exits. 

Important points: 

 1. Targeting more languages provides the directly implemented formatted output Excel and Business Report according to the industry standards which a normal chat-gpt like AI chatbot cannot provide directly, it cannot make changes in the excel sheets or format it, it can only provide normal analytical that is not accurate all the time.  
 
 2. To use file upload functionality, the user needs to buy open ai’s GP 4.0 license which costs 10$ per million tokens for input and 30$ per million tokens for output. 
 
 3. Gemini, which is free is still not capable enough to solve the issues and lacks the capability to process files, the same issue is with Microsoft copilot.


