from pyPdf import PdfFileWriter, PdfFileReader

output = PdfFileWriter()
pdfOne = PdfFileReader(open("test.pdf", "r+b"))

#print "title = %s" % (input1.getDocumentInfo().title)

for i in range(0,28):
	output.addPage(pdfOne.getPage(i))

outputStream = file("output.doc", "wb")
output.write(outputStream)
outputStream.close()

	
