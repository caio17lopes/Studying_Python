wedding_invitation = ['juracy', 'tiago', 'arno']
message = wedding_invitation[0].title() + " Você esta convidada para o meu casamento dia 08/04/2016. "
message1 = wedding_invitation[1].title() + " Você esta convidada para o meu casamento dia 08/04/2016. "
message2 = wedding_invitation[2].title() + " Você esta convidada para o meu casamento dia 08/04/2016. "
print( message, message1, message2,sep="\n")
del wedding_invitation[0]
wedding_invitation.insert(0, 'alex')
print (wedding_invitation)
message = wedding_invitation[0].title() + " Você esta convidada para o meu casamento dia 08/04/2016. "
message1 = wedding_invitation[1].title() + " Você esta convidada para o meu casamento dia 08/04/2016. "
message2 = wedding_invitation[2].title() + " Você esta convidada para o meu casamento dia 08/04/2016. "
print ("Novo convidado, " + message, message1, message2,sep="\n")
wedding_invitation.insert(0, 'João')
wedding_invitation.insert(0, 'Ana')
wedding_invitation.insert(0, 'Saulo')
print(wedding_invitation)
message = wedding_invitation[0].title() + " Você esta convidada para o meu casamento dia 08/04/2016. "
message1 = wedding_invitation[1].title() + " Você esta convidada para o meu casamento dia 08/04/2016. "
message2 = wedding_invitation[2].title() + " Você esta convidada para o meu casamento dia 08/04/2016. "
message3 = wedding_invitation[3].title() + " Você esta convidada para o meu casamento dia 08/04/2016. "
message4 = wedding_invitation[4].title() + " Você esta convidada para o meu casamento dia 08/04/2016. "
message5 = wedding_invitation[5].title() + " Você esta convidada para o meu casamento dia 08/04/2016. "
print(message,message1,message2,message3,message4,message5, sep="\n")
wedding_invitation.pop()
print(wedding_invitation)
message = wedding_invitation[0].title() + " Você esta convidada para o meu casamento dia 08/04/2016. "
message1 = wedding_invitation[1].title() + " Você esta convidada para o meu casamento dia 08/04/2016. "
message2 = wedding_invitation[2].title() + " Você esta convidada para o meu casamento dia 08/04/2016. "
message3 = wedding_invitation[3].title() + " Você esta convidada para o meu casamento dia 08/04/2016. "
message4 = wedding_invitation[4].title() + " Você esta convidada para o meu casamento dia 08/04/2016. "
print(message,message1,message2,message3,message4, sep="\n")