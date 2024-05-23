import segno
'''p=dir(segno)
print(p)'''
qr=segno.make_qr("https://www.linkedin.com/in/dibyanshukar/")
qr.save("linkqr.png",scale=10) #if we don't mention scale value it will be 1 by default and this 1 is called a module
'''border=0 ka matlab h qr code k side me jo white space ya quiet zone(border=4) by default segno ne create kiya h usko khatam karna'''

qr.save("linkbord0.png",scale=10,border=0)





