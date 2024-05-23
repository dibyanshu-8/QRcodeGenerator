import segno
qr=segno.make_qr("https://www.linkedin.com/in/dibyanshukar/")

#making colorful qr code
#light="#" means we are changing the while module of the qr code
#dark="#" means we are changing the dark module of the qr code

qr.save("colinkqr.png",scale=10,light="lightgreen")


#changing color of quiet zone or white boarder area
qr.save("colquiet.png",scale=10,dark="red",quiet_zone="orange")

'''the data modules are black & white blocks where the data is actually stored
.now we will change the color of the data modules'''

#data_dark argument to change the black color of data block
#data_light argument to change the white color of data block
qr.save("chngdtcl.png",scale=10,light="lightgreen",dark="green",data_dark="blue",data_light="yellow")
