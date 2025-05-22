from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # Set font for the header
        self.set_font("Arial", "B", 14)
        self.set_text_color(0, 0, 128)  # Dark Blue
        # Title
        self.cell(0, 10, "Grade 7 - Mathematics Question Paper", ln=True, align="C")
        # Info line
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)  # Reset to black
        self.cell(0, 10, "Time: 1 Hour     Total Marks: 40", ln=True, align="C")
        self.cell(0, 10, "Topics: Fractions & One-Variable Algebraic Equations", ln=True, align="C")
        self.ln(10)

    def add_section(self, title, questions, color=(0, 128, 0)):
        # Set font and color for section heading
        self.set_font("Arial", "B", 12)
        self.set_text_color(*color)  # Set heading color
        self.cell(0, 10, title, ln=True)
        # Reset to default black color and normal font
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        
        # Add questions in this section
        for q in questions:
            # Simply add the question
            self.multi_cell(0, 10, q)
        self.ln(5)

# Create PDF instance
pdf = PDF()
pdf.add_page()

# Define questions for each section
section_a_questions = [
    "Q1. (3 marks) Simplify: 5/6 - (3/4 + 1/8)",
    "Q2. (3 marks) Evaluate: (2/3 * 9/10) / (4/5)",
    "Q3. (4 marks) A recipe requires 3/5 cup of sugar for one cake. How much sugar is needed for 3 cakes? If only 1 1/4 cups of sugar are available, is it enough? Show calculations.",
    "Q4. (5 marks - Word Problem) A tank was 2/3 full. After using 3/10 of the total capacity, it is now partially full. What fraction of the tank's capacity is left?",
    "Q5. (5 marks - Word Problem) Two friends, Neha and Anu, read 5/8 and 7/12 of the same book respectively. Who read more? What fraction of the book is still unread?"
]

section_b_questions = [
    "Q6. (3 marks) Solve: 2(3x - 4) + 5 = 3(x + 2)",
    "Q7. (3 marks) Solve and verify: (2x + 3)/4 = (x - 2)/2",
    "Q8. (4 marks) Solve for x: (5x - 7)/3 = (2x + 1)/2",
    "Q9. (5 marks - Word Problem) The length of a rectangle is 4 cm more than twice its width. If the perimeter is 44 cm, find the dimensions of the rectangle.",
    "Q10. (5 marks - Word Problem) A number is such that when 5 is subtracted from 3 times the number, the result is equal to twice the number plus 7. Find the number."
]

# Add Section A (Fractions)
pdf.add_section("Section A: Fractions (20 Marks)", section_a_questions, color=(0, 128, 0))

# Add Section B (Algebraic Equations)
pdf.add_section("Section B: Algebraic Equations – One Variable (30 Marks)", section_b_questions, color=(0, 0, 128))

# Save PDF
file_name = "Paper3.pdf"
pdf.output(file_name)

print(f"✅ PDF saved as: {file_name}")
