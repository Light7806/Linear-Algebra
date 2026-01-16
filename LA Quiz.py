import streamlit as st
import numpy as np

def main():
    st.set_page_config(page_title="Math for ML - Season 2 Quiz", page_icon="🧮")
    
    st.title("🧠 Math for ML: The Gen Z Quiz")
    st.write("Did you actually watch the video or were you just scrolling comments? Let's find out.")
    st.markdown("---")

    # Quiz Data
    questions = [
        {
            "question": "1. In Machine Learning, what is the main difference between a Scalar and a Vector?",
            "options": [
                "Scalars are cooler than Vectors",
                "Scalar has Magnitude only, Vector has Magnitude + Direction",
                "Scalar is 2D, Vector is 3D",
                "Vector is just a list of random numbers with no meaning"
            ],
            "answer": "Scalar has Magnitude only, Vector has Magnitude + Direction",
            "explanation": "Correct! Speed is a Scalar (50km/h), Velocity is a Vector (50km/h North)."
        },
        {
            "question": "2. If I have a dataset with features: [Size, Rooms, Location, Age, Crime_Rate], what is the dimensionality of this vector?",
            "options": [
                "2D (X and Y)",
                "3D (Like PUBG)",
                "5D",
                "Infinite Dimensions"
            ],
            "answer": "5D",
            "explanation": "Bingo! 5 Features = 5 Dimensions. Our brain can't see it, but Python can."
        },
        {
            "question": "3. Which mathematical concept is used to calculate the 'Length' or Magnitude (L2 Norm) of a vector?",
            "options": [
                "The Quadratic Formula",
                "Pythagoras Theorem",
                "Newton's Third Law",
                "Einstein's Relativity"
            ],
            "answer": "Pythagoras Theorem",
            "explanation": "Yes! a² + b² = c². That's how we measure how 'strong' a vector is."
        },
        {
            "question": "4. How does a computer 'see' a Black and White image?",
            "options": [
                "As a Matrix of numbers (0-255)",
                "It uses eyes like humans",
                "It sees shapes and lines directly",
                "It sees hashtags"
            ],
            "answer": "As a Matrix of numbers (0-255)",
            "explanation": "Correct. It's just a grid. 0 is Black, 255 is White."
        },
        {
            "question": "5. What do we call a data structure that has 3 or more dimensions (like a Color RGB Image)?",
            "options": [
                "Mega-Matrix",
                "Tensor",
                "Cube",
                "Scalar"
            ],
            "answer": "Tensor",
            "explanation": "Right! Scalar(0D) -> Vector(1D) -> Matrix(2D) -> Tensor(3D+)."
        },
        {
            "question": "6. In the Netflix Recommendation example, what mathematical operation determines if you will like a movie?",
            "options": [
                "Addition (+)",
                "Division (/)",
                "The Dot Product",
                "Cross Product"
            ],
            "answer": "The Dot Product",
            "explanation": "Spot on. High Dot Product = High Similarity (You'll love the movie)."
        },
        {
            "question": "7. If the Dot Product of two vectors is ZERO, what does that mean?",
            "options": [
                "The vectors are the same",
                "The vectors are perpendicular (90 degrees) / Not similar",
                "The computer crashed",
                "The vectors are parallel"
            ],
            "answer": "The vectors are perpendicular (90 degrees) / Not similar",
            "explanation": "Exactly. Zero means no correlation. You like Horror, the movie is Comedy. No match."
        },
        {
            "question": "8. You have Matrix A with shape (3, 2) and Matrix B with shape (3, 2). Can you calculate the Dot Product (A dot B)?",
            "options": [
                "Yes, obviously",
                "No, Shape Mismatch Error",
                "Only if you use a GPU",
                "Yes, but the answer will be zero"
            ],
            "answer": "No, Shape Mismatch Error",
            "explanation": "Correct! Inner dimensions must match. (3,2) and (3,2) don't work. The '2' and '3' clash."
        },
        {
            {
                {
            "question": "9. To fix a Shape Mismatch error (e.g., turning rows into columns), which operation do we use?",
            "options": [
                "Rotate",
                "Transpose (.T)",
                "Inverse",
                "Delete the matrix"
            ],
            "answer": "Transpose (.T)",
            "explanation": "The Golden Rule! Flip it to fix it."
        },
        {
            "question": "10. In Python code, what is the specific rule for Matrix Multiplication shape alignment?",
            "options": [
                "(M, N) x (N, K) -> Columns of A must equal Rows of B",
                "(M, N) x (M, N) -> Shapes must be identical",
                "There are no rules, Python is magic",
                "Rows must always equal Rows"
            ],
            "answer": "(M, N) x (N, K) -> Columns of A must equal Rows of B",
            "explanation": "100%. The inner numbers (N and N) act like a password. They must match."
        }
    ]

    # Initialize Session State for Score
    if 'score' not in st.session_state:
        st.session_state.score = 0
    if 'submitted' not in st.session_state:
        st.session_state.submitted = False

    # Form to hold the quiz
    with st.form("quiz_form"):
        user_answers = []
        for i, q in enumerate(questions):
            st.subheader(q["question"])
            # Create a unique key for each radio button
            choice = st.radio("Choose one:", q["options"], key=f"q{i}", index=None)
            user_answers.append(choice)
            st.write("") # Spacer

        submit_button = st.form_submit_button("Submit Quiz")

    # Logic after submission
    if submit_button:
        score = 0
        for i, q in enumerate(questions):
            user_choice = user_answers[i]
            if user_choice == q["answer"]:
                score += 1
                st.success(f"✅ Q{i+1}: Correct! {q['explanation']}")
            else:
                st.error(f"❌ Q{i+1}: Wrong. The correct answer was: {q['answer']}")
        
        st.session_state.score = score
        st.session_state.submitted = True

    # Final Score Display
    if st.session_state.submitted:
        st.markdown("---")
        final_score = st.session_state.score
        st.header(f"Your Final Score: {final_score}/10")

        if final_score == 10:
            st.balloons()
            st.write("🏆 **GOD MODE.** You are ready to build the Matrix.")
        elif final_score >= 7:
            st.write("🔥 **Pretty Good.** You can survive an interview.")
        elif final_score >= 4:
            st.write("😐 **Meh.** Did you skip the ads? Go watch the video again.")
        else:
            st.write("💀 **Emotional Damage.** You need to re-watch Season 1 immediately.")

if __name__ == "__main__":
    main()
             
