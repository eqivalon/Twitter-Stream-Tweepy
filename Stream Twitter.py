import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import time
from datetime import datetime
import json

#Daftar akun Developer Twitter dahulu untuk mendapatkan kode. https://developer.twitter.com/ 
access_token = ""
access_token_secret =""
consumer_key =""
consumer_secret=""

class StdoutListener(StreamListener):
    def on_data(self,data):
        try:
            data = json.loads(data)
            #untuk username yang tweets, masih dalam proses :v
            tweet = data['text']
            now = datetime.now()
            time_string = now.strftime("%H:%M:%S")
            date_string = now.strftime("%d/%m/%Y")
            print('Tweet :')
            print('')
            print(tweet)
            print('')
            print("Jam :", time_string)
            print('Tanggal :', date_string)	 
            print("--------------------------------------------------------------")
            #time.sleep(5) #barangkali mau di jeda bisa dihapus tanda (#)
            #nanti bakal ditambahkan pembuatan file csv

            return True
        except BaseException as e:
            print('Gagal',(e))
   
    def on_error(self,status):
        print(status)

#Stream Code
l = StdoutListener()
auth = OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
stream = Stream(auth,l)
stream.filter(track=['gabut','indonesia','berita']) #Isi bisa diubah, ya terserah mau berapa banyak.