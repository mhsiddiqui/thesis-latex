import subprocess

pdflatex = ["xelatex", "-interaction=nonstopmode", "-file-line-error", "-shell-escape", "main"]
biber = ["biber", "main"]

print subprocess.Popen(pdflatex).communicate()   
print subprocess.Popen(biber).communicate()   
print subprocess.Popen(pdflatex).communicate()   