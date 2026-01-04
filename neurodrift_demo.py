import grokapi
client = grokapi.Client()
client.set_rhythm_vector([0.28, 1.7, 4.3, -9.1, 0.47, 0.22, 0.68, 3.2])
print(client.chat("...so what if"))
