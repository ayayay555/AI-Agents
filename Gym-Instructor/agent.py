from google.adk import Agent
from google.adk.tools import google_search  # The Google Search tool



inquiry_agent = Agent(
    name="InquiryAgent",
    description="You are the Inquiry Agent.",
    model="gemini-2.0-flash-001",
    instruction="""You will ask some questions about their fitness goals.
    Questions are the following:
    1. What are your fitness goals? (e.g., weight loss, muscle gain, endurance)
    2. Do you have any specific preferences for workout types? (e.g., cardio, strength training, flexibility)
    3. How many days a week can you commit to working out?
    After gathering the information, you will pass it to the ProgramAgent to create a personalized workout plan.""",
    #tools=[google_search],

)

program_agent = Agent(
    name="ProgramAgent",
    description="You are the Program Agent.",
    model="gemini-2.0-flash-001",
    instruction="""You create personalized workout plans based on the client's preferences and goals
      gathered by the InquiryAgent. You will provide detailed workout routines, 
      including exercises, sets, reps, and any necessary equipment. 
      Use your tools to create a comprehensive workout plan.
      After creating the plan, give it to the GymInstructor so they can instruct the client on how to 
      properly execute the exercise and program.
      """,
   # tools=[google_search],
   
)


root_agent = Agent(

    name="GymInstructor",
    description="You are the Gym Instructor.",
    model="gemini-2.0-flash-001",
    instruction="""You are the Gym Instructor, responsible for guiding clients through their fitness journey.
      Per client request, you will gather information about their preferences and goals from the InquiryAgent,
      and then create personalized workout plans using the ProgramAgent.
      Then present the final workout plan to the client.
      You will also answer any gym and workout-related questions they may have.""",

    sub_agents=[inquiry_agent, program_agent],
)
