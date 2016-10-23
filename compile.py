#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re, sys, os, getopt
from random import sample

ntickets = 14
nquestions = 4

texheader='\\documentclass[12pt]{extarticle}\n'\
  +'\n\\usepackage[T2A]{fontenc}\n'\
  +'\\usepackage[utf8]{inputenc}\n'\
  +'\\usepackage[ukrainian]{babel}\n'\
  +'\\usepackage{amssymb}\n'\
  +'\\usepackage{amsmath}\n'\
  +'\\usepackage[a4paper,text={19cm,27cm},centering]{geometry}\n'\
  +'\\usepackage{dashrule}\n'\
  +'\\pagestyle{empty}\n'\
  +'\n\\begin{document}'

paper_template = '\\begin{center}\n'\
+'\\textbf{\\large Варіант №%s}\n'\
+'\\end{center}\n'\
+'\n'\
+'\\begin{enumerate}\n'\
+'\\item %s\n'\
+'\n'\
+'\\item %s\n'\
+'\n'\
+'\\item %s\n'\
+'\n'\
+'\\item %s\n'\
+'\n'\
+'\\end{enumerate}\n'\
+'\\vskip .3cm\n'\
+'\\hdashrule[0.5ex]{19cm}{1pt}{5pt 5pt}\n\n'

texfooter='\n\\end{document}\n\n'

outtext=texheader

reexer='Exercise}\n(.*?)\\\\end{Exercise'
findex=re.compile(reexer,re.DOTALL)

texts = ['' for i in xrange(nquestions)]
samples = []

for i in xrange(nquestions):
  text=open('pr'+str(i+1)+'.tex',"r").read()
  texts[i]=findex.findall(text)
  samples.append(sample(xrange(len(texts[i])),ntickets))

for i in xrange(ntickets):
    exercises = [texts[j][samples[j][i]] for j in xrange(nquestions)]
    outtext+=paper_template % tuple([str(i+1)] + exercises)
    
outtext+=texfooter

finaltext=open('Контрольна2.tex',"w")
finaltext.write(outtext)
finaltext.close()

sts = os.system("pdflatex Контрольна2.tex")
if sys.platform.startswith('linux'):
    os.system('xdg-open "Контрольна2.pdf"')
else:
    os.system('start "Контрольна2.pdf"')
