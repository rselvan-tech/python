from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, "Mathematics Question Paper", ln=True, align="C")
        self.set_font("Arial", "", 12)
        self.cell(0, 10, "Grade: 7    Topics: One-Variable Algebraic Equations & Fractions", ln=True, align="C")
        self.ln(10)

    def section_title(self, title):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, title, ln=True)
        self.set_font("Arial", "", 12)

pdf = PDF()
pdf.add_page()

# Section A
pdf.section_title("Section A: One-Variable Algebraic Equations - [15 Marks]")
section_a = [
    "1. Solve: x + 9 = 16",
    "2. Solve: 4x = 28",
    "3. Solve: x - 7 = 11",
    "4. Solve: 3x + 5 = 20",
    "5. Solve: 5x - 10 = 15",
]
for q in section_a:
    pdf.multi_cell(0, 10, q)

# Section B
pdf.ln(5)
pdf.section_title("Section B: Word Problems (Equations) - [9 Marks]")
section_b = [
    "6. A number minus 4 equals 9. Find the number.",
    "7. The sum of a number and its triple is 40. Find the number.",
    "8. If you double a number and subtract 3, the result is 11. Find the number.",
]
for q in section_b:
    pdf.multi_cell(0, 10, q)

# Section C
pdf.ln(5)
pdf.section_title("Section C: Fractions (Add, Subtract, Multiply, Divide) - [10 Marks]")
section_c = [
    "9. Simplify: 3/4 + 2/5",
    "10. Simplify: 5/6 - 1/3",
    "11. Multiply: 2/3 × 4/7",
    "12. Divide: 5/8 ÷ 3/4",
    "13. Simplify: (1/2 + 3/4) - 2/5",
]
for q in section_c:
    pdf.multi_cell(0, 10, q)

# Section D
pdf.ln(5)
pdf.section_title("Section D: Word Problems (Fractions) - [6 Marks]")
section_d = [
    "14. Rani ate 2/5 of a cake. Her friend ate 1/4 of it. What fraction of the cake is left?",
    "15. A water tank is 3/4 full. After using 1/3 of the water, how much water remains?",
]
for q in section_d:
    pdf.multi_cell(0, 10, q)

# Instructions
pdf.ln(5)
pdf.set_font("Arial", "I", 11)
pdf.multi_cell(0, 10, "Instructions:\n- Show all steps clearly.\n- Use proper methods for fractions.\n- Write your final answers neatly.\n- Time: 1 Hour\n- Total Marks: 40")

# Save the PDF
pdf.output("Grade7_Math_Equations_and_Fractions.pdf")
