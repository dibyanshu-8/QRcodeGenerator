#for advanced graphical operations we have to install dependencies like qrcode-artistic & pillow

#to_pil() method to rotate the qr ->it will convert our qr code in to a pillow image instance
import segno
qr=segno.make_qr("https://www.linkedin.com/in/dibyanshukar/")

#here for size,color change wehave to give parameters inside .pil() as we r actually calling .save() on a PIL object & not a QR code object

rotate_qr=qr.to_pil(scale=10,light="darkblue",dark="orange",quiet_zone="lightgreen").rotate(45,expand=True)
rotate_qr.save("rotateqr.png",)#scale=20
