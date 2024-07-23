import os
from fpdf import FPDF

class Shirtificate(FPDF):
    def create_shirtificate(self, name):
        self.add_page()
        self.set_font('Times', 'B', 50)
        self.cell(0, 60, 'CS50 Shirtificate', new_x="LMARGIN", new_y="NEXT", align='C')

        shirt_image = 'shirtificate.png'
        self.image(shirt_image,  w=self.epw)
        self.set_font('helvetica', 'B', 30)

        self.set_text_color(255, 255, 255)
        self.text(x=48, y=140, text=f"{name} took CS50")

    def save(self,name):
        self.output(name)

def main():

    name = input('Name: ')
    pdf = Shirtificate(orientation='P', unit='mm', format='A4')
    pdf.create_shirtificate(name)
    pdf.save("shirtificate.pdf")

if __name__ == '__main__':
    main()
