###############################################################################
#
# Makefile for the photon note
#                              	
###############################################################################

NOTENAME=fcc_timing

all:#default target makes everything
	pdflatex $(NOTENAME).tex && bibtex $(NOTENAME) && pdflatex $(NOTENAME).tex && pdflatex $(NOTENAME).tex

dvi:
	latex $(NOTENAME).tex && bibtex $(NOTENAME) && latex $(NOTENAME).tex 

ps:
	latex $(NOTENAME).tex && bibtex $(NOTENAME) && latex $(NOTENAME).tex && latex $(NOTENAME).tex && dvips -P pdf $(NOTENAME).dvi 

pdf:
	latex $(NOTENAME).tex && bibtex $(NOTENAME) && latex $(NOTENAME).tex && latex $(NOTENAME).tex && dvips -P pdf $(NOTENAME).dvi && ps2pdf $(NOTENAME).ps $(NOTENAME).pdf

show:
	evince $(NOTENAME).pdf

.PHONY: clean
clean:
	rm -rf $(NOTENAME).aux $(NOTENAME).log $(NOTENAME).out $(NOTENAME).bbl $(NOTENAME).blg\
	$(NOTENAME).dvi $(NOTENAME).ps \
	$(NOTENAME).toc $(NOTENAME).tof thumb*.* *~ 
