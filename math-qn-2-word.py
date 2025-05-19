from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 14)
        self.set_text_color(0, 0, 128)  # Dark Blue
        self.cell(0, 10, "Grade 7 - Mathematics Question Paper", ln=True, align="C")
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)  # Reset to black
        self.cell(0, 10, "Time: 1 Hour     Total Marks: 40", ln=True, align="C")
        self.cell(0, 10, "Topics: Fractions & One-Variable Algebraic Equations", ln=True, align="C")
        self.ln(10)

    def add_section(self, title, questions, color=(0, 128, 0)):
        self.set_font("Arial", "B", 12)
        self.set_text_color(*color)  # Set heading color
        self.cell(0, 10, title, ln=True)
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)  # Reset to black
        for q in questions:
            self.multi_cell(0, 10, q)
        self.ln(5)

# Create PDF instance
pdf = PDF()
pdf.add_page()

# Section A: Fractions
section_a = [
    "1. Add: 3/5 + 2/7",
    "2. Subtract: 7/8 - 3/10",
    "3. Multiply: 2/3 x 4/9",
    "4. Divide: 5/6 ÷ 2/5",
    "5. Simplify: (1/2 + 3/4) - 2/5"
]
pdf.add_section("Section A: Fractions (Add, Subtract, Multiply, Divide) - [10 Marks]", section_a)

# Section B: Fraction Word Problems
section_b = [
    "6. A jug is filled with 5/6 liter of water. If 1/4 liter is poured out, how much water is left in the jug?",
    "7. Riya read 3/5 of a book on Monday and 2/7 of it on Tuesday. What fraction of the book is yet to be read?"
]
pdf.add_section("Section B: Word Problems (Fractions) - [6 Marks]", section_b)

# Section C: Algebraic Equations
section_c = [
    "8. Solve: 2x + 5 = 17",
    "9. Solve: x/4 - 3 = 5",
    "10. Solve: (3x - 2)/5 = 4",
    "11. Solve: -2x + 1/3 = 5/6"
]
pdf.add_section("Section C: Algebraic Equations (One Variable) - [12 Marks]", section_c)

# Section D: Equation Word Problems with Shapes
section_d = [
    "12. The perimeter of a triangle is 60 cm. If two sides are 18 cm and 22 cm, and the third side is x, write and solve the equation to find the value of x.",
    "13. The length of a rectangle is 3 cm more than its width. If the perimeter is 34 cm, find the length and width using an algebraic equation.",
    "14. The sum of three times a number and 5 is equal to 29. Find the number."
]
pdf.add_section("Section D: Word Problems (Algebraic Equations & Shapes) - [12 Marks]", section_d)

# Instructions
instructions = [
    "Instructions:",
    "- Write all steps clearly.",
    "- Simplify all answers where possible.",
    "- Draw diagrams for shape-related questions if needed."
]
pdf.add_section("Instructions", instructions, color=(128, 0, 0))  # Maroon for final section

# Save the PDF
pdf.output("Grade7_Math_Question_Paper.pdf")
