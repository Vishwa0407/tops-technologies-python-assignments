# 3. Try to change the first element of your fav_apps tuple to 'YouTube' and observe the error message. Write a comment explaining why this happens based on tuple immutability.

fav_apps = ('Instagram', 'Zomato', 'Spotify', 'WhatsApp', 'Flipkart')

fav_apps[0] = 'YouTube'

print(fav_apps)


'''
Error: 

     fav_apps[0] = 'YouTube'
        ~~~~~~~~^^^
    TypeError: 'tuple' object does not support item assignment

    This gives a TypeError because tuples are immutable.
    Their elements cannot be changed after the tuple is created.
    
'''
   