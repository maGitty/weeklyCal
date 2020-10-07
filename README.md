weekly_cal
==========
__________

This project provides scripts to create a week planer via LaTeX for students. The year of the summer term and the first monday have to be specified respectively.

Additionally, a pdf document can be used to provide a graphical title page.

The document can be folded up accordingly to be printed as A5/A6 using the week\_cal\_1x2.tex and week\_cal\_2x2.tex respectively.
Therefore, the "signature" key of the \includepdf command has to be set to a value of the next multiple of 4 from the number of pages the previous document contains, so that the pages will be printed in the correct order(e.g. if the previous document has 39 pages, the signature has to be 40).
