from spire.pdf.common import *
from spire.pdf import *

pdfs = ["resume1.pdf", "resume2.pdf", "resume3.pdf"]

mergeOptions = MergerOptions()

outputPdf = "resume.pdf"

PdfMerger.MergeByFile(pdfs, outputPdf, mergeOptions)

pdf_merged = PdfDocument()

pdf_merged.LoadFromFile(outputPdf)

pdf_merged.SaveToFile("resume.docx", FileFormat.DOCX)

pdf_merged.Close()