import subprocess

pdflatex = ["pdflatex", "-interaction=nonstopmode", "-file-line-error", "main"]
biber = ["biber", "main"]

print subprocess.Popen(pdflatex).communicate()   
print subprocess.Popen(biber).communicate()   
print subprocess.Popen(pdflatex).communicate()   