proyecto = input("Digita la descripción del proyecto: ")
horas_estimadas = input("Digita la cantidad de horas estimadas: ")
valor_hora = input("Digita el valor de la hora trabajada: ")
tiempo_estimado = input("Digita el plazo estimado: ")

valor_total = int(horas_estimadas) * int(valor_hora)

# Generando archivo pdf para el presupuesto
# ! pip install fpdf 

from fpdf import FPDF

pdf = FPDF() # Creamos el archivo pdf

pdf.add_page() # Agregamos una pagina la pdf
pdf.set_font("Arial") # Configuramos el tipo de letra

pdf.image("PROYECTO01/Template.png",x=0,y=0) #Cargamos el template en el origen 0,0

# Coordena en X, Coordenada en Y, Texto
# pdf.text(115,145,"el mejor proyecto con Python")

# INGRESNADO INFORMACION DIGITALIZADA
pdf.text(115,145,proyecto)
pdf.text(115,160,horas_estimadas)
pdf.text(115,175,valor_hora)
pdf.text(115,190,tiempo_estimado)
pdf.text(115,205,str(valor_total))


pdf.output("PROYECTO01/presupuesto.pdf") 

print("Presupuesto generado con exito")
