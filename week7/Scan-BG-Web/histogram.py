from classHistogram import Histogram
import matplotlib.pyplot as plt

h = Histogram()

# servers=["Appache", "nginx", "Oracle", "lighttpd", "Microsoft-IIS"]

with open("servers.txt", 'r') as f:
    data = f.read().split("\n")
for serv in data:
    for server in ["Apache", "nginx", "Oracle", "lighttpd", "Microsoft-IIS"]:
        if server in serv:
            h.add(server)

keys = list(h.get_dict().keys())
X = list(range(len(keys)))
values = list(h.get_dict().values())

plt.bar(X, list(values), width=1)
plt.xticks(X, keys)
plt.xlabel("Server")
plt.ylabel("Count")
ax = plt.subplot(111)
plt.title("Most used servers for BG sites")
plt.savefig("histogram.png")
