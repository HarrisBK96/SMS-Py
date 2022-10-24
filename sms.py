from twilio.rest import Client 
 
account_sid = 'ACf05d50c7341869c4993052dcc29931db' 
auth_token = '716c86280b2c6b189ed5faf0fbce8a2c' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create(  
                              messaging_service_sid='MG7064846840ca806644ebe4d2332feb10', 
                              body='How you doin?',      
                              to='+923215036572' 
                          ) 
 
print(message.sid)