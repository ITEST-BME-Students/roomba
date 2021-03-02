from library import Microphone

microphone = Microphone.Microphone()

iid, lag = microphone.listen()
print('IID:', iid)
print('ITD:', lag)
