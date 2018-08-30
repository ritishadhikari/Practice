import matplotlib.pyplot as plt

#exp_vals = [1400,600,300,410,250]
#exp_labels = ["Home Rent","Food","Phone/Internet Bill","Car ","Other Utilities"]
plt.title("Consumption Diagram")
plt.axis("equal")
plt.pie(x=[1400,600,300,410,250],
        labels=["Home Rent","Food","Phone/Internet Bill","Car ","Other Utilities"],
        explode=[0,0,0,0,0],
        autopct="%0.0f%%",
        startangle=90,
        radius=1,
        colors=["g","B","magenta","yellow", "Red"],
        shadow=True)
plt.show()
