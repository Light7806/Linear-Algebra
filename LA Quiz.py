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
