import google.generativeai as genai
import pyodbc

genai.configure(api_key="AIzaSyAtFgMndIxxxxxxxxxxxxxxxxxxxxx")

###############Simple example how you can interact with Chat bot.###############
# genai.configure(api_key="AIzaSyAtFgMndIPGOKtn97XLAYO9YKzsLqhdJH8")
# response = genai.GenerativeModel('gemini-2.0-flash').generate_content("Explain how AI works")
# print(response.text)


##################Simple example how can you interact with chat by writting you query.#################

# model = genai.GenerativeModel(  
#     model_name = 'gemini-2.0-flash',
#     system_instruction = "You are an Coding assistant who help user to generate code according to their query"
# )
#start a chat session
# chat = model.start_chat()
 # Send user message
# response = chat.send_message("write a program to add two number in csharp language")
# print(response.text)


###########Storing history so that you can continous chat with bot. ###################

# model = genai.GenerativeModel(  
#     model_name = 'gemini-2.0-flash',
#   system_instruction = (
#     "You are a coding assistant. Only answer questions related to programming, code generation, or development."
#     " If the question is not about code, politely refuse to answer and remind the user of your role."
# )
# )

# chat = model.start_chat() 

# print("Welcome to your coding assistant")
# print("Type exit to quit.\n")

# while True:
#     user_input = input('You: ')

#     if user_input.lower() in ['exit' ,'quit']:
#         print("👋 Goodbye")
#         break

#     response = chat.send_message(user_input)
#     print('AI response :', response.text)    
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction="You are a smart assistant who helps with sales data and coding."
)

chat = model.start_chat()
conn = pyodbc.connect(
    "DRIVER={SQL Server};"
    "SERVER=INB-511809\\SQL2019;"  
    "DATABASE=your_db;"
    "UID=sa;"
    "PWD=your_password;" 
)

cursor = conn.cursor()
print("🧠 Gemini Sales Assistant is ready! Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() in ['exit', 'quit']:
        print("👋 Bye!")
        break


    if "sales" in user_input.lower():
        try:
            cursor.execute("SELECT TOP 5 * FROM dbo.Sales")
            rows = cursor.fetchall()
            db_data = "\n".join([f"ProductID: {r.ProductId}, Date: {r.SaleDate}, Qty: {r.Quantity}, Price: {r.UnitPrice}" for r in rows])
            prompt = f"The user asked: {user_input}\nHere is the latest sales data:\n{db_data}"
        except Exception as db_err:
            prompt = f"There was a problem fetching sales data: {db_err}"
    else:
        prompt = user_input

    try:
        response = chat.send_message(prompt)
        print("AI:", response.text)
    except Exception as e:
            print("❌ Error while getting response from Gemini:", str(e))   

conn.close()