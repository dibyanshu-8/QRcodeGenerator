import segno
#importing urlopen for retrieving url of gif from external website .

from urllib.request import urlopen
qr=segno.make_qr("https://youtu.be/Bs0f4QBzbek?si=Hxjsl1AWQCv05HH5")

carryurl=urlopen("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHltM2Z5NThpcXRjODA4dXdweGpmb2pvNnVhbnRpancxZmdhdmpmZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/8Y02mY0J2e49bh2BgB/giphy.gif")

#using to_artistic() method
qr.to_artistic(background=carryurl,target="animatedqr.gif",scale=10,quiet_zone="lightgreen",light="lightgreen")

