import emailingusingAI
import SMS  
companyname="Perpetua"
topic="diet"
myname="Collin Struthers"
message =emailingusingAI.get_marketing_email_draft(topic,companyname,myname)
#print(message)
genmessage=emailingusingAI.gen_z_and_shorten(message)
#print(genmessage)
nonascii=emailingusingAI.remove_non_ascii(genmessage)
#print(nonascii)

SMS.send_sms_via_email("5193773801",topic,nonascii)