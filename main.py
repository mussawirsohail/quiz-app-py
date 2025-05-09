# import streamlit as st
# import random

# # Set page configuration
# st.set_page_config(
#     page_title="Quiz App",
#     page_icon="❓",
#     layout="centered"
# )

# # Custom CSS for styling
# st.markdown("""
# <style>
#     .main-title {
#         font-size: 2.5rem;
#         color: #FF4B4B;
#         text-align: center;
#         margin-bottom: 2rem;
#     }
#     .question {
#         font-size: 1.5rem;
#         font-weight: bold;
#         margin-bottom: 1rem;
#     }
#     .score-display {
#         font-size: 1.8rem;
#         font-weight: bold;
#         margin: 2rem 0;
#         text-align: center;
#     }
#     .correct-answer {
#         color: #00CC66;
#         font-weight: bold;
#     }
#     .wrong-answer {
#         color: #FF4B4B;
#         font-weight: bold;
#     }
#     .progress-text {
#         text-align: center;
#         margin-bottom: 1rem;
#     }
# </style>
# """, unsafe_allow_html=True)

# # Title
# st.markdown("<h1 class='main-title'>Quiz App by Measam Ali and Abbas Ali</h1>", unsafe_allow_html=True)

# # Quiz questions
# quiz_data = [
#     {
#         "question": "Which planet is known as the Red Planet?",
#         "options": ["Venus", "Mars", "Jupiter", "Saturn"],
#         "correct_answer": "Mars"
#     },
#     {
#         "question": "Who painted the Mona Lisa?",
#         "options": ["Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Michelangelo"],
#         "correct_answer": "Leonardo da Vinci"
#     },
#     {
#         "question": "What is the largest ocean on Earth?",
#         "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
#         "correct_answer": "Pacific Ocean"
#     },
#     {
#         "question": "Which country is home to the kangaroo?",
#         "options": ["New Zealand", "South Africa", "Australia", "Brazil"],
#         "correct_answer": "Australia"
#     },
#     {
#         "question": "What is the chemical symbol for gold?",
#         "options": ["Go", "Gd", "Au", "Ag"],
#         "correct_answer": "Au"
#     },
#     {
#         "question": "Who wrote 'Romeo and Juliet'?",
#         "options": ["Charles Dickens", "William Shakespeare", "Jane Austen", "Mark Twain"],
#         "correct_answer": "William Shakespeare"
#     },
#     {
#         "question": "What is the capital of Japan?",
#         "options": ["Beijing", "Seoul", "Tokyo", "Bangkok"],
#         "correct_answer": "Tokyo"
#     },
#     {
#         "question": "Which element has the chemical symbol 'O'?",
#         "options": ["Osmium", "Oxygen", "Oganesson", "Olivine"],
#         "correct_answer": "Oxygen"
#     },
#     {
#         "question": "What is the tallest mountain in the world?",
#         "options": ["K2", "Mount Everest", "Kangchenjunga", "Makalu"],
#         "correct_answer": "Mount Everest"
#     },
#     {
#         "question": "Which is the largest mammal in the world?",
#         "options": ["African Elephant", "Blue Whale", "Giraffe", "Polar Bear"],
#         "correct_answer": "Blue Whale"
#     },
#     {
#         "question": "In which year did World War II end?",
#         "options": ["1943", "1944", "1945", "1946"],
#         "correct_answer": "1945"
#     },
#     {
#         "question": "What is the smallest country in the world?",
#         "options": ["Monaco", "Nauru", "Vatican City", "San Marino"],
#         "correct_answer": "Vatican City"
#     },
#     {
#         "question": "Which famous scientist developed the theory of relativity?",
#         "options": ["Isaac Newton", "Albert Einstein", "Galileo Galilei", "Stephen Hawking"],
#         "correct_answer": "Albert Einstein"
#     },
#     {
#         "question": "What is the largest organ in the human body?",
#         "options": ["Liver", "Brain", "Skin", "Heart"],
#         "correct_answer": "Skin"
#     },
#     {
#         "question": "Which country is known as the Land of the Rising Sun?",
#         "options": ["China", "Thailand", "South Korea", "Japan"],
#         "correct_answer": "Japan"
#     },
#     {
#         "question": "Who is the author of 'Harry Potter' series?",
#         "options": ["J.R.R. Tolkien", "J.K. Rowling", "George R.R. Martin", "Stephen King"],
#         "correct_answer": "J.K. Rowling"
#     },
#     {
#         "question": "What is the currency of the United Kingdom?",
#         "options": ["Euro", "Dollar", "Pound Sterling", "Yen"],
#         "correct_answer": "Pound Sterling"
#     },
#     {
#         "question": "Which planet has the most moons?",
#         "options": ["Jupiter", "Saturn", "Uranus", "Neptune"],
#         "correct_answer": "Saturn"
#     },
#     {
#         "question": "What is the main component of the Sun?",
#         "options": ["Helium", "Oxygen", "Carbon", "Hydrogen"],
#         "correct_answer": "Hydrogen"
#     },
#     {
#         "question": "Who discovered penicillin?",
#         "options": ["Marie Curie", "Alexander Fleming", "Louis Pasteur", "Joseph Lister"],
#         "correct_answer": "Alexander Fleming"
#     }
# ]

# # Initialize session state
# if 'current_question' not in st.session_state:
#     st.session_state.current_question = 0
#     st.session_state.score = 0
#     st.session_state.answered = False
#     st.session_state.selected_option = None
#     st.session_state.quiz_completed = False
#     # Shuffle questions for each new session
#     random.shuffle(quiz_data)

# # Display progress
# total_questions = len(quiz_data)
# progress_percentage = (st.session_state.current_question / total_questions) * 100

# if not st.session_state.quiz_completed:
#     st.markdown(f"<p class='progress-text'>Question {st.session_state.current_question + 1} of {total_questions}</p>", unsafe_allow_html=True)
#     st.progress(progress_percentage / 100)

#     # Display current question
#     current_q = quiz_data[st.session_state.current_question]
#     st.markdown(f"<div class='question'>{st.session_state.current_question + 1}. {current_q['question']}</div>", unsafe_allow_html=True)

#     # Display options
#     if not st.session_state.answered:
#         selected_option = st.radio("Select your answer:", current_q['options'], key=f"q{st.session_state.current_question}")
        
#         col1, col2 = st.columns([1, 4])
#         with col1:
#             if st.button("Submit Answer"):
#                 st.session_state.answered = True
#                 st.session_state.selected_option = selected_option
                
#                 # Check if answer is correct
#                 if selected_option == current_q['correct_answer']:
#                     st.session_state.score += 1
#                 st.experimental_rerun()
#     else:
#         # Show result of the answer
#         selected_option = st.session_state.selected_option
#         st.radio("Select your answer:", current_q['options'], key=f"q{st.session_state.current_question}", 
#                  index=current_q['options'].index(selected_option), disabled=True)
        
#         if selected_option == current_q['correct_answer']:
#             st.success("✅ Correct!")
#         else:
#             st.error(f"❌ Wrong! The correct answer is: {current_q['correct_answer']}")
        
#         # Next question button
#         col1, col2 = st.columns([1, 4])
#         with col1:
#             if st.button("Next Question"):
#                 st.session_state.current_question += 1
#                 st.session_state.answered = False
                
#                 # Check if quiz is completed
#                 if st.session_state.current_question >= total_questions:
#                     st.session_state.quiz_completed = True
                
#                 st.experimental_rerun()

# # Display final score when quiz is completed
# if st.session_state.quiz_completed:
#     final_score = st.session_state.score
#     percentage = (final_score / total_questions) * 100
    
#     st.markdown(f"<div class='score-display'>Quiz Completed!</div>", unsafe_allow_html=True)
#     st.markdown(f"<div class='score-display'>Your Score: {final_score}/{total_questions} ({percentage:.1f}%)</div>", unsafe_allow_html=True)
    
#     # Performance message
#     if percentage >= 80:
#         st.balloons()
#         st.success("🏆 Excellent! You're a quiz master!")
#     elif percentage >= 60:
#         st.success("👍 Good job! You have solid general knowledge!")
#     elif percentage >= 40:
#         st.info("🙂 Not bad! Keep learning!")
#     else:
#         st.warning("📚 Keep studying to improve your general knowledge!")
    
#     # Restart button
#     if st.button("Restart Quiz"):
#         st.session_state.current_question = 0
#         st.session_state.score = 0
#         st.session_state.answered = False
#         st.session_state.quiz_completed = False
#         random.shuffle(quiz_data)
#         st.experimental_rerun()

# # Footer
# st.markdown("---")
# st.markdown("© 2023 Quiz App by Measam Ali and Abbas Ali")


import streamlit as st
import random

# Set page configuration
st.set_page_config(
    page_title="Quiz App",
    page_icon="❓",
    layout="centered"
)

# Custom CSS for styling
st.markdown("""
<style>
    .main-title {
        font-size: 2.5rem;
        color: #FF4B4B;
        text-align: center;
        margin-bottom: 2rem;
    }
    .question {
        font-size: 1.5rem;
        font-weight: bold;
        margin-bottom: 1rem;
    }
    .score-display {
        font-size: 1.8rem;
        font-weight: bold;
        margin: 2rem 0;
        text-align: center;
    }
    .correct-answer {
        color: #00CC66;
        font-weight: bold;
    }
    .wrong-answer {
        color: #FF4B4B;
        font-weight: bold;
    }
    .progress-text {
        text-align: center;
        margin-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 class='main-title'>Quiz App by Measam Ali and Abbas Ali</h1>", unsafe_allow_html=True)

# Quiz questions
quiz_data = [
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Venus", "Mars", "Jupiter", "Saturn"],
        "correct_answer": "Mars"
    },
    {
        "question": "Who painted the Mona Lisa?",
        "options": ["Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Michelangelo"],
        "correct_answer": "Leonardo da Vinci"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
        "correct_answer": "Pacific Ocean"
    },
    {
        "question": "Which country is home to the kangaroo?",
        "options": ["New Zealand", "South Africa", "Australia", "Brazil"],
        "correct_answer": "Australia"
    },
    {
        "question": "What is the chemical symbol for gold?",
        "options": ["Go", "Gd", "Au", "Ag"],
        "correct_answer": "Au"
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "options": ["Charles Dickens", "William Shakespeare", "Jane Austen", "Mark Twain"],
        "correct_answer": "William Shakespeare"
    },
    {
        "question": "What is the capital of Japan?",
        "options": ["Beijing", "Seoul", "Tokyo", "Bangkok"],
        "correct_answer": "Tokyo"
    },
    {
        "question": "Which element has the chemical symbol 'O'?",
        "options": ["Osmium", "Oxygen", "Oganesson", "Olivine"],
        "correct_answer": "Oxygen"
    },
    {
        "question": "What is the tallest mountain in the world?",
        "options": ["K2", "Mount Everest", "Kangchenjunga", "Makalu"],
        "correct_answer": "Mount Everest"
    },
    {
        "question": "Which is the largest mammal in the world?",
        "options": ["African Elephant", "Blue Whale", "Giraffe", "Polar Bear"],
        "correct_answer": "Blue Whale"
    },
    {
        "question": "In which year did World War II end?",
        "options": ["1943", "1944", "1945", "1946"],
        "correct_answer": "1945"
    },
    {
        "question": "What is the smallest country in the world?",
        "options": ["Monaco", "Nauru", "Vatican City", "San Marino"],
        "correct_answer": "Vatican City"
    },
    {
        "question": "Which famous scientist developed the theory of relativity?",
        "options": ["Isaac Newton", "Albert Einstein", "Galileo Galilei", "Stephen Hawking"],
        "correct_answer": "Albert Einstein"
    },
    {
        "question": "What is the largest organ in the human body?",
        "options": ["Liver", "Brain", "Skin", "Heart"],
        "correct_answer": "Skin"
    },
    {
        "question": "Which country is known as the Land of the Rising Sun?",
        "options": ["China", "Thailand", "South Korea", "Japan"],
        "correct_answer": "Japan"
    },
    {
        "question": "Who is the author of 'Harry Potter' series?",
        "options": ["J.R.R. Tolkien", "J.K. Rowling", "George R.R. Martin", "Stephen King"],
        "correct_answer": "J.K. Rowling"
    },
    {
        "question": "What is the currency of the United Kingdom?",
        "options": ["Euro", "Dollar", "Pound Sterling", "Yen"],
        "correct_answer": "Pound Sterling"
    },
    {
        "question": "Which planet has the most moons?",
        "options": ["Jupiter", "Saturn", "Uranus", "Neptune"],
        "correct_answer": "Saturn"
    },
    {
        "question": "What is the main component of the Sun?",
        "options": ["Helium", "Oxygen", "Carbon", "Hydrogen"],
        "correct_answer": "Hydrogen"
    },
    {
        "question": "Who discovered penicillin?",
        "options": ["Marie Curie", "Alexander Fleming", "Louis Pasteur", "Joseph Lister"],
        "correct_answer": "Alexander Fleming"
    }
]

# Initialize session state
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
    st.session_state.score = 0
    st.session_state.answered = False
    st.session_state.selected_option = None
    st.session_state.quiz_completed = False
    random.shuffle(quiz_data)

# Display progress
total_questions = len(quiz_data)
progress_percentage = (st.session_state.current_question / total_questions) * 100

if not st.session_state.quiz_completed:
    st.markdown(f"<p class='progress-text'>Question {st.session_state.current_question + 1} of {total_questions}</p>", unsafe_allow_html=True)
    st.progress(progress_percentage / 100)

    current_q = quiz_data[st.session_state.current_question]
    st.markdown(f"<div class='question'>{st.session_state.current_question + 1}. {current_q['question']}</div>", unsafe_allow_html=True)

    if not st.session_state.answered:
        selected_option = st.radio("Select your answer:", current_q['options'], key=f"q{st.session_state.current_question}")

        col1, col2 = st.columns([1, 4])
        with col1:
            if st.button("Submit Answer"):
                st.session_state.answered = True
                st.session_state.selected_option = selected_option

                if selected_option == current_q['correct_answer']:
                    st.session_state.score += 1
                st.rerun()
    else:
        selected_option = st.session_state.selected_option
        st.radio("Select your answer:", current_q['options'],
                 index=current_q['options'].index(selected_option),
                 disabled=True, key=f"q{st.session_state.current_question}")

        if selected_option == current_q['correct_answer']:
            st.success("✅ Correct!")
        else:
            st.error(f"❌ Wrong! The correct answer is: {current_q['correct_answer']}")

        col1, col2 = st.columns([1, 4])
        with col1:
            if st.button("Next Question"):
                st.session_state.current_question += 1
                st.session_state.answered = False

                if st.session_state.current_question >= total_questions:
                    st.session_state.quiz_completed = True
                st.rerun()

# Final score
if st.session_state.quiz_completed:
    final_score = st.session_state.score
    percentage = (final_score / total_questions) * 100

    st.markdown(f"<div class='score-display'>Quiz Completed!</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='score-display'>Your Score: {final_score}/{total_questions} ({percentage:.1f}%)</div>", unsafe_allow_html=True)

    if percentage >= 80:
        st.balloons()
        st.success("🏆 Excellent! You're a quiz master!")
    elif percentage >= 60:
        st.success("👍 Good job! You have solid general knowledge!")
    elif percentage >= 40:
        st.info("🙂 Not bad! Keep learning!")
    else:
        st.warning("📚 Keep studying to improve your general knowledge!")

    if st.button("Restart Quiz"):
        st.session_state.current_question = 0
        st.session_state.score = 0
        st.session_state.answered = False
        st.session_state.quiz_completed = False
        random.shuffle(quiz_data)
        st.rerun()

# Footer
st.markdown("---")
st.markdown("© 2023 Quiz App by Measam Ali and Abbas Ali")
